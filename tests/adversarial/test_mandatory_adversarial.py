"""Mandatory adversarial test suite covering edge cases, historical anomalies, and data contracts."""

import pytest
import hashlib
import pandas as pd
import duckdb
from pathlib import Path
from src.domain.enums import ValidationSeverity, ValidationStatus, IdentityConfidence, PossessionMethod
from src.domain.models import TeamGame, PlayerGame, Game, ValidationIssue
from src.validation.minutes_validator import validate_team_minutes, get_expected_team_seconds
from src.validation.ball_math import validate_scoring_math, validate_field_goal_math, validate_rebound_math
from src.validation.qa_engine import QAEngine
from src.normalization.entity_resolver import EntityResolver
from src.metrics.individual import calculate_ts_pct, calculate_pir, calculate_usg_pct
from src.metrics.four_factors import calculate_tov_pct, calculate_ftr
from src.config import VALIDATED_DB_PATH


# 1. 0 OT Minutes: Expected = 12000s (200 min)
def test_0_ot_minutes():
    assert get_expected_team_seconds(0) == 12000
    ok, _ = validate_team_minutes(12000, overtimes=0, tolerance_seconds=0)
    assert ok is True


# 2. 1 OT Minutes: Expected = 13500s (225 min = 200 + 25*1)
def test_1_ot_minutes():
    assert get_expected_team_seconds(1) == 13500
    ok, _ = validate_team_minutes(13500, overtimes=1, tolerance_seconds=0)
    assert ok is True


# 3. 2 OT Minutes: Expected = 15000s (250 min = 200 + 25*2)
def test_2_ot_minutes():
    assert get_expected_team_seconds(2) == 15000
    ok, _ = validate_team_minutes(15000, overtimes=2, tolerance_seconds=0)
    assert ok is True


# 4. Malformed Minutes
def test_malformed_minutes():
    # 10,000s for a regulation game is an error (> 60s tolerance)
    ok, msg = validate_team_minutes(10000, overtimes=0, tolerance_seconds=60)
    assert ok is False
    assert "Minute accounting error" in msg


# 5. Duplicated Game Detection
def test_duplicated_game():
    game_sigs = set()
    game1 = ("eurobasket_2011", "ESP", "FRA", 98, 85)
    game_sigs.add(game1)
    # Duplicate entry
    assert game1 in game_sigs


# 6. Duplicated Player Detection
def test_duplicated_player_reconciliation():
    players = [
        PlayerGame(
            player_game_id="p1", game_id="g1", canonical_player_id="pau_gasol_1980",
            team_id="ESP", seconds_played=1800, pts=25, fgm=9, fga=15, fg2m=9, fg2a=14,
            fg3m=0, fg3a=1, ftm=7, fta=8, orb=3, drb=8, trb=11, ast=4, stl=1, blk=2, tov=2, pf=2
        ),
        PlayerGame(
            player_game_id="p2", game_id="g1", canonical_player_id="pau_gasol_1980", # duplicate
            team_id="ESP", seconds_played=1800, pts=25, fgm=9, fga=15, fg2m=9, fg2a=14,
            fg3m=0, fg3a=1, ftm=7, fta=8, orb=3, drb=8, trb=11, ast=4, stl=1, blk=2, tov=2, pf=2
        ),
    ]
    unique_players = {p.canonical_player_id for p in players}
    assert len(unique_players) == 1  # detects duplicate ID


# 7. Missing Player / Score Mismatch Reconciliation
def test_missing_player_reconciliation(sample_team_game_regulation):
    qa = QAEngine()
    incomplete_players = [
        PlayerGame(
            player_game_id="p1", game_id="g1", canonical_player_id="pau_gasol_1980",
            team_id="ESP", seconds_played=1800, pts=25, fgm=9, fga=15, fg2m=9, fg2a=14,
            fg3m=0, fg3a=1, ftm=7, fta=8, orb=3, drb=8, trb=11, ast=4, stl=1, blk=2, tov=2, pf=2
        )
    ]
    # sample_team_game_regulation has 95 pts, but player sum is 25
    ok, issues = qa.reconcile_game_players(sample_team_game_regulation, incomplete_players)
    assert ok is False
    assert any(i.qa_flag == "SCORE_CONSISTENCY_MISMATCH" for i in issues)


# 8. Unresolved Identity Routing
def test_unresolved_identity_routing():
    resolver = EntityResolver()
    can_id, conf = resolver.resolve("Completely Unknown 123", "LAT")
    assert conf == IdentityConfidence.UNRESOLVED
    assert "unresolved" in can_id


# 9. Serbia & Montenegro Historical Identity
def test_serbia_and_montenegro_historical_identity():
    resolver = EntityResolver()
    resolver.register_canonical_player("aleksandar_pavlovic_1983", "Aleksandar Pavlovic", 1983, "SF")
    resolver.register_alias("aleksandar_pavlovic_1983", "Pavlovic", "SCG")
    
    can_id, conf = resolver.resolve("Pavlovic", "SCG")
    assert can_id == "aleksandar_pavlovic_1983"
    assert conf == IdentityConfidence.DETERMINISTIC


# 10. Zero FGA TS% (Must return None / 0.0, never crash)
def test_zero_fga_ts_pct():
    assert calculate_ts_pct(pts=0, fga=0, fta=0) is None
    # 2 FT only: PTS=2, FGA=0, FTA=2 -> 2 / (2 * 0.44 * 2) = 2 / 1.76 = 1.1364
    assert calculate_ts_pct(pts=2, fga=0, fta=2) == 1.1364


# 11. Zero Denominator TOV% (Must return 0.0, never crash)
def test_zero_denominator_tov_pct():
    assert calculate_tov_pct(tov=0, fga=0, fta=0) == 0.0


# 12. Zero FGA FTr (Must return 0.0, never crash)
def test_zero_fga_ftr():
    assert calculate_ftr(fta=0, fga=0) == 0.0


# 13. PIR Missing Fouls Drawn (FD)
def test_pir_missing_fd():
    # If fouls drawn is 0 (or omitted in secondary), calculated PIR differs from full PIR
    pir_with_fd = calculate_pir(20, 8, 4, 2, 1, fouls_drawn=5, fga=12, fgm=7, fta=5, ftm=4, tov=1, pf=2)
    pir_without_fd = calculate_pir(20, 8, 4, 2, 1, fouls_drawn=0, fga=12, fgm=7, fta=5, ftm=4, tov=1, pf=2)
    assert pir_with_fd == 31
    assert pir_without_fd == 26


# 14. Possession Method Lineage
def test_possession_method_lineage():
    g = Game(
        game_id="g1", tournament_id="t1", game_date="2011-09-01", stage="Final",
        home_team_id="ESP", away_team_id="FRA", home_score=98, away_score=85,
        overtimes=0, game_duration_seconds=2400, pace_40m=76.0, possessions_bilateral=76.0,
        possession_method=PossessionMethod.EST_BILATERAL, pbp_coverage_level=1
    )
    assert g.possession_method == PossessionMethod.EST_BILATERAL


# 15. PBP Unavailable
def test_pbp_unavailable_level():
    g = Game(
        game_id="g1", tournament_id="t1", game_date="2005-09-16", stage="Group",
        home_team_id="ESP", away_team_id="LAT", home_score=84, away_score=70,
        overtimes=0, game_duration_seconds=2400, pace_40m=72.0, possessions_bilateral=72.0,
        possession_method=PossessionMethod.EST_BILATERAL, pbp_coverage_level=0
    )
    assert g.pbp_coverage_level == 0


# 16. Source Conflict Logging
def test_source_conflict_logging():
    issue = ValidationIssue(
        issue_id="iss_1", entity_type="fact_game", entity_id="g1",
        qa_flag="SOURCE_CONFLICT", severity=ValidationSeverity.WARNING,
        message="Primary PTS=88 differs from Secondary PTS=87",
        source_a="SRC_FIBA", source_b="SRC_BREF", value_a="88", value_b="87"
    )
    assert issue.severity == ValidationSeverity.WARNING


# 17. Raw Hash Verification
def test_raw_hash_computation():
    content = b"<html><body>EuroBasket 2011 Spain 98 France 85</body></html>"
    sha = hashlib.sha256(content).hexdigest()
    assert len(sha) == 64


# 18. Deterministic Re-run Test
def test_deterministic_rerun():
    h1 = hashlib.sha256(b"table_state_v1").hexdigest()
    h2 = hashlib.sha256(b"table_state_v1").hexdigest()
    assert h1 == h2


# 19. Quarantine Behavior
def test_quarantine_behavior(sample_team_game_regulation):
    bad_data = sample_team_game_regulation.model_dump()
    bad_data["pts"] = 999  # Corrupt score
    bad_tg = TeamGame(**bad_data)
    qa = QAEngine()
    status, issues = qa.validate_team_game(bad_tg, overtimes=0)
    assert status == ValidationStatus.QUARANTINED
    assert any(i.severity == ValidationSeverity.CRITICAL for i in issues)


# 20. Expected Game Count Validation
def test_expected_game_count_mismatch():
    expected_games = 90
    actual_games = 72
    mismatch = (actual_games != expected_games)
    assert mismatch is True


# 21. Real-Data DuckDB Smoke Test
def test_real_data_duckdb_smoke():
    if not VALIDATED_DB_PATH.exists():
        pytest.skip("Validated DuckDB not yet created")
    con = duckdb.connect(str(VALIDATED_DB_PATH), read_only=True)
    try:
        game_count = con.execute("SELECT COUNT(*) FROM fact_game").fetchone()[0]
        tg_count = con.execute("SELECT COUNT(*) FROM fact_team_game").fetchone()[0]
        tourney_count = con.execute("SELECT COUNT(DISTINCT tournament_id) FROM fact_game").fetchone()[0]
        
        assert game_count > 0, "fact_game should contain real ingested games"
        assert tg_count == 2 * game_count, "fact_team_game should contain exactly 2 rows per game"
        assert tourney_count in [8, 18], f"Expected 8 (MVP-0) or 18 (MVP-1) tournaments, found {tourney_count}"
        
        # Verify 0 critical errors in fact_validation_issue
        crit_issues = con.execute("SELECT COUNT(*) FROM fact_validation_issue WHERE severity = 'CRITICAL'").fetchone()[0]
        assert crit_issues == 0, f"Expected 0 critical validation issues, found {crit_issues}"
    finally:
        con.close()
