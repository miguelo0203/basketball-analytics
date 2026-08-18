"""Quality assurance engine coordinating validation gates and issue logging."""

import uuid
from typing import List, Tuple
from src.domain.enums import ValidationSeverity, ValidationStatus
from src.domain.models import ValidationIssue, TeamGame, PlayerGame
from src.validation.ball_math import validate_scoring_math, validate_field_goal_math, validate_rebound_math
from src.validation.minutes_validator import validate_team_minutes


class QAEngine:
    """Central automated quality assurance engine for basketball data."""

    def __init__(self, minute_tolerance_seconds: int = 60):
        self.minute_tolerance_seconds = minute_tolerance_seconds

    def validate_team_game(
        self,
        team_game: TeamGame,
        overtimes: int = 0,
    ) -> Tuple[ValidationStatus, List[ValidationIssue]]:
        """Validate a team game record against all critical accounting assertions."""
        issues: List[ValidationIssue] = []

        # 1. Scoring Ball-Math
        score_ok, score_msg = validate_scoring_math(
            pts=team_game.pts,
            fg2m=team_game.fg2m,
            fg3m=team_game.fg3m,
            ftm=team_game.ftm,
        )
        if not score_ok:
            issues.append(
                ValidationIssue(
                    issue_id=str(uuid.uuid4()),
                    entity_type="fact_team_game",
                    entity_id=team_game.team_game_id,
                    qa_flag="BALL_MATH_MISMATCH",
                    severity=ValidationSeverity.CRITICAL,
                    message=score_msg,
                )
            )

        # 2. Field Goal Component Math
        fg_ok, fg_errors = validate_field_goal_math(
            fgm=team_game.fgm,
            fga=team_game.fga,
            fg2m=team_game.fg2m,
            fg2a=team_game.fg2a,
            fg3m=team_game.fg3m,
            fg3a=team_game.fg3a,
        )
        if not fg_ok:
            for err in fg_errors:
                issues.append(
                    ValidationIssue(
                        issue_id=str(uuid.uuid4()),
                        entity_type="fact_team_game",
                        entity_id=team_game.team_game_id,
                        qa_flag="FGM_CONSISTENCY",
                        severity=ValidationSeverity.CRITICAL,
                        message=err,
                    )
                )

        # 3. Rebounds Math
        reb_ok, reb_msg = validate_rebound_math(
            orb=team_game.orb,
            drb=team_game.drb,
            trb=team_game.trb,
        )
        if not reb_ok:
            issues.append(
                ValidationIssue(
                    issue_id=str(uuid.uuid4()),
                    entity_type="fact_team_game",
                    entity_id=team_game.team_game_id,
                    qa_flag="REBOUND_CONSISTENCY",
                    severity=ValidationSeverity.ERROR,
                    message=reb_msg,
                )
            )

        # 4. Minute Accounting
        min_ok, min_msg = validate_team_minutes(
            accounted_seconds=team_game.team_player_seconds_accounted,
            overtimes=overtimes,
            tolerance_seconds=self.minute_tolerance_seconds,
        )
        if not min_ok:
            issues.append(
                ValidationIssue(
                    issue_id=str(uuid.uuid4()),
                    entity_type="fact_team_game",
                    entity_id=team_game.team_game_id,
                    qa_flag="MINUTES_ACCOUNTING_MISMATCH",
                    severity=ValidationSeverity.CRITICAL,
                    message=min_msg,
                )
            )

        # Determine overall promotion status
        has_critical = any(issue.severity == ValidationSeverity.CRITICAL for issue in issues)
        has_error = any(issue.severity == ValidationSeverity.ERROR for issue in issues)
        has_warning = any(issue.severity == ValidationSeverity.WARNING for issue in issues)

        if has_critical or has_error:
            status = ValidationStatus.QUARANTINED
        elif has_warning:
            status = ValidationStatus.WARNING
        else:
            status = ValidationStatus.VALIDATED

        return status, issues

    def reconcile_game_players(
        self,
        team_game: TeamGame,
        players: List[PlayerGame],
    ) -> Tuple[bool, List[ValidationIssue]]:
        """Reconcile sum of player boxscores against team totals."""
        issues: List[ValidationIssue] = []
        sum_pts = sum(p.pts for p in players)
        sum_fgm = sum(p.fgm for p in players)
        sum_fga = sum(p.fga for p in players)
        sum_seconds = sum(p.seconds_played for p in players)

        if sum_pts != team_game.pts:
            issues.append(
                ValidationIssue(
                    issue_id=str(uuid.uuid4()),
                    entity_type="fact_team_game",
                    entity_id=team_game.team_game_id,
                    qa_flag="SCORE_CONSISTENCY_MISMATCH",
                    severity=ValidationSeverity.CRITICAL,
                    message=f"Player sum PTS ({sum_pts}) != Team PTS ({team_game.pts})",
                )
            )

        if sum_fgm != team_game.fgm:
            issues.append(
                ValidationIssue(
                    issue_id=str(uuid.uuid4()),
                    entity_type="fact_team_game",
                    entity_id=team_game.team_game_id,
                    qa_flag="TEAM_TOTALS",
                    severity=ValidationSeverity.ERROR,
                    message=f"Player sum FGM ({sum_fgm}) != Team FGM ({team_game.fgm})",
                )
            )

        return (len(issues) == 0), issues
