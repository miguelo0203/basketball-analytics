"""Pydantic domain models for entities, games, boxscores, and validation."""

from typing import Optional, List
from datetime import date
from pydantic import BaseModel, Field, ConfigDict
from src.domain.enums import (
    ValidationSeverity,
    ValidationStatus,
    IdentityConfidence,
    PossessionMethod,
)


class Tournament(BaseModel):
    """Tournament edition domain model."""
    model_config = ConfigDict(frozen=True)

    tournament_id: str
    competition: str
    official_name: str
    year: int
    actual_start_date: str
    actual_end_date: str
    host: str
    number_of_teams: int
    expected_games: int
    official_game_count: int
    rule_set_id: str
    source: str
    verification_status: str


class Team(BaseModel):
    """National federation domain model."""
    model_config = ConfigDict(frozen=True)

    canonical_team_id: str
    fiba_code: str
    iso_code: str
    canonical_name: str
    fiba_zone: str
    is_historical_entity: bool = False


class Player(BaseModel):
    """Canonical person domain model."""
    model_config = ConfigDict(frozen=True)

    canonical_player_id: str
    full_canonical_name: str
    birth_date: Optional[str] = None
    birth_year: int
    primary_position: str
    identity_confidence: IdentityConfidence = IdentityConfidence.DETERMINISTIC


class PlayerAlias(BaseModel):
    """Source-specific alias mapping model."""
    model_config = ConfigDict(frozen=True)

    alias_id: str
    canonical_player_id: str
    source_id: str
    source_player_id: Optional[str] = None
    raw_name_string: str


class ValidationIssue(BaseModel):
    """QA issue logged for an entity or record."""
    model_config = ConfigDict(frozen=True)

    issue_id: str
    entity_type: str
    entity_id: str
    qa_flag: str
    severity: ValidationSeverity
    message: str
    source_a: Optional[str] = None
    source_b: Optional[str] = None
    value_a: Optional[str] = None
    value_b: Optional[str] = None


class PlayerGame(BaseModel):
    """Individual player game boxscore."""
    model_config = ConfigDict(frozen=True)

    player_game_id: str
    game_id: str
    canonical_player_id: str
    team_id: str
    is_spain: bool = False
    is_starter: bool = False
    seconds_played: int = Field(ge=0)
    pts: int = Field(ge=0)
    fgm: int = Field(ge=0)
    fga: int = Field(ge=0)
    fg2m: int = Field(ge=0)
    fg2a: int = Field(ge=0)
    fg3m: int = Field(ge=0)
    fg3a: int = Field(ge=0)
    ftm: int = Field(ge=0)
    fta: int = Field(ge=0)
    orb: int = Field(ge=0)
    drb: int = Field(ge=0)
    trb: int = Field(ge=0)
    ast: int = Field(ge=0)
    stl: int = Field(ge=0)
    blk: int = Field(ge=0)
    tov: int = Field(ge=0)
    pf: int = Field(ge=0)
    fouls_drawn: Optional[int] = None
    plus_minus: Optional[int] = None
    official_pir: Optional[int] = None
    computed_game_score: float = 0.0
    ts_pct: Optional[float] = None
    efg_pct: Optional[float] = None
    usg_pct: Optional[float] = None
    data_source_id: str = "SRC_DEFAULT"


class TeamGame(BaseModel):
    """Team-level game boxscore and ratings."""
    model_config = ConfigDict(frozen=True)

    team_game_id: str
    game_id: str
    team_id: str
    opponent_id: str
    is_spain: bool = False
    is_winner: bool = False
    team_player_minutes_expected: int = 200
    team_player_seconds_accounted: int = 12000
    pts: int = Field(ge=0)
    fgm: int = Field(ge=0)
    fga: int = Field(ge=0)
    fg2m: int = Field(ge=0)
    fg2a: int = Field(ge=0)
    fg3m: int = Field(ge=0)
    fg3a: int = Field(ge=0)
    ftm: int = Field(ge=0)
    fta: int = Field(ge=0)
    orb: int = Field(ge=0)
    drb: int = Field(ge=0)
    trb: int = Field(ge=0)
    ast: int = Field(ge=0)
    stl: int = Field(ge=0)
    blk: int = Field(ge=0)
    tov: int = Field(ge=0)
    pf: int = Field(ge=0)
    fouls_drawn: Optional[int] = None
    possessions_simple: float = 0.0
    possessions_bilateral: float = 0.0
    ortg: float = 0.0
    drtg: float = 0.0
    net_rtg: float = 0.0
    efg_pct: float = 0.0
    tov_pct: float = 0.0
    orb_pct: float = 0.0
    ftr: float = 0.0
    opp_efg_pct: float = 0.0
    opp_tov_pct: float = 0.0
    opp_orb_pct: float = 0.0
    opp_ftr: float = 0.0
    data_source_id: str = "SRC_DEFAULT"
    raw_content_hash: str = ""


class Game(BaseModel):
    """Basketball game domain model."""
    model_config = ConfigDict(frozen=True)

    game_id: str
    tournament_id: str
    game_date: str
    stage: str
    home_team_id: str
    away_team_id: str
    home_score: int
    away_score: int
    overtimes: int = 0
    game_duration_seconds: int = 2400
    pace_40m: float = 0.0
    possessions_bilateral: float = 0.0
    possession_method: PossessionMethod = PossessionMethod.EST_BILATERAL
    pbp_coverage_level: int = 0
    shot_data_available: bool = False
    validation_status: ValidationStatus = ValidationStatus.VALIDATED
