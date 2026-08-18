"""DuckDB SQL DDL schema definitions for staging and production warehouse."""

STAGING_SCHEMA_DDL = """
CREATE TABLE IF NOT EXISTS stg_raw_payloads (
    payload_id VARCHAR PRIMARY KEY,
    source_id VARCHAR NOT NULL,
    tournament_id VARCHAR NOT NULL,
    resource_name VARCHAR NOT NULL,
    source_url VARCHAR NOT NULL,
    retrieval_timestamp_utc VARCHAR NOT NULL,
    content_sha256 VARCHAR NOT NULL,
    parser_version VARCHAR NOT NULL,
    ingestion_run_id VARCHAR NOT NULL,
    http_status INTEGER NOT NULL,
    raw_payload_text VARCHAR
);

CREATE TABLE IF NOT EXISTS stg_boxscores (
    stg_boxscore_id VARCHAR PRIMARY KEY,
    source_id VARCHAR NOT NULL,
    tournament_id VARCHAR NOT NULL,
    game_date VARCHAR NOT NULL,
    stage_raw VARCHAR NOT NULL,
    team_name_raw VARCHAR NOT NULL,
    opp_team_name_raw VARCHAR NOT NULL,
    pts INTEGER,
    fgm INTEGER,
    fga INTEGER,
    fg2m INTEGER,
    fg2a INTEGER,
    fg3m INTEGER,
    fg3a INTEGER,
    ftm INTEGER,
    fta INTEGER,
    orb INTEGER,
    drb INTEGER,
    trb INTEGER,
    ast INTEGER,
    stl INTEGER,
    blk INTEGER,
    tov INTEGER,
    pf INTEGER,
    overtimes INTEGER DEFAULT 0,
    raw_content_hash VARCHAR NOT NULL
);
"""

VALIDATED_SCHEMA_DDL = """
-- Dimension Tables
CREATE TABLE IF NOT EXISTS dim_source (
    source_id VARCHAR PRIMARY KEY,
    source_name VARCHAR NOT NULL,
    base_url VARCHAR NOT NULL,
    source_type VARCHAR NOT NULL,
    precedence_rank INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_rule_set (
    rule_set_id VARCHAR PRIMARY KEY,
    effective_from DATE NOT NULL,
    effective_to DATE NOT NULL,
    rule_3pt_distance_m FLOAT NOT NULL,
    shot_clock_seconds INTEGER NOT NULL,
    shot_clock_orb_seconds INTEGER NOT NULL,
    lane_geometry VARCHAR NOT NULL,
    no_charge_semicircle BOOLEAN NOT NULL,
    game_duration_minutes INTEGER NOT NULL,
    ot_duration_minutes INTEGER NOT NULL,
    description VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_competition (
    competition_id VARCHAR PRIMARY KEY,
    competition_name VARCHAR NOT NULL,
    governing_body VARCHAR NOT NULL,
    cycle_years INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_tournament (
    tournament_id VARCHAR PRIMARY KEY,
    competition_id VARCHAR NOT NULL REFERENCES dim_competition(competition_id),
    rule_set_id VARCHAR NOT NULL REFERENCES dim_rule_set(rule_set_id),
    year INTEGER NOT NULL,
    official_name VARCHAR NOT NULL,
    host_countries VARCHAR NOT NULL,
    number_of_teams INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_team (
    canonical_team_id VARCHAR(3) PRIMARY KEY,
    fiba_code VARCHAR(3) NOT NULL,
    iso_code VARCHAR(3) NOT NULL,
    canonical_name VARCHAR NOT NULL,
    fiba_zone VARCHAR NOT NULL,
    is_historical_entity BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS dim_player (
    canonical_player_id VARCHAR PRIMARY KEY,
    full_canonical_name VARCHAR NOT NULL,
    birth_date DATE,
    birth_year INTEGER NOT NULL,
    primary_position VARCHAR(5) NOT NULL,
    identity_confidence VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_player_alias (
    alias_id VARCHAR PRIMARY KEY,
    canonical_player_id VARCHAR NOT NULL REFERENCES dim_player(canonical_player_id),
    source_id VARCHAR NOT NULL REFERENCES dim_source(source_id),
    source_player_id VARCHAR,
    raw_name_string VARCHAR NOT NULL
);

-- Fact Tables
CREATE TABLE IF NOT EXISTS fact_game (
    game_id VARCHAR PRIMARY KEY,
    tournament_id VARCHAR NOT NULL REFERENCES dim_tournament(tournament_id),
    game_date DATE NOT NULL,
    stage VARCHAR NOT NULL,
    home_team_id VARCHAR(3) NOT NULL REFERENCES dim_team(canonical_team_id),
    away_team_id VARCHAR(3) NOT NULL REFERENCES dim_team(canonical_team_id),
    home_score INTEGER NOT NULL,
    away_score INTEGER NOT NULL,
    overtimes INTEGER NOT NULL DEFAULT 0,
    game_duration_seconds INTEGER NOT NULL,
    pace_40m FLOAT NOT NULL,
    possessions_bilateral FLOAT NOT NULL,
    possession_method VARCHAR NOT NULL,
    pbp_coverage_level INTEGER NOT NULL,
    shot_data_available BOOLEAN NOT NULL DEFAULT FALSE,
    validation_status VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_team_game (
    team_game_id VARCHAR PRIMARY KEY,
    game_id VARCHAR NOT NULL REFERENCES fact_game(game_id),
    team_id VARCHAR(3) NOT NULL REFERENCES dim_team(canonical_team_id),
    opponent_id VARCHAR(3) NOT NULL REFERENCES dim_team(canonical_team_id),
    is_spain BOOLEAN NOT NULL,
    is_winner BOOLEAN NOT NULL,
    team_player_minutes_expected INTEGER NOT NULL,
    team_player_seconds_accounted INTEGER NOT NULL,
    pts INTEGER NOT NULL,
    fgm INTEGER NOT NULL,
    fga INTEGER NOT NULL,
    fg2m INTEGER NOT NULL,
    fg2a INTEGER NOT NULL,
    fg3m INTEGER NOT NULL,
    fg3a INTEGER NOT NULL,
    ftm INTEGER NOT NULL,
    fta INTEGER NOT NULL,
    orb INTEGER NOT NULL,
    drb INTEGER NOT NULL,
    trb INTEGER NOT NULL,
    ast INTEGER NOT NULL,
    stl INTEGER NOT NULL,
    blk INTEGER NOT NULL,
    tov INTEGER NOT NULL,
    pf INTEGER NOT NULL,
    fouls_drawn INTEGER,
    possessions_simple FLOAT NOT NULL,
    possessions_bilateral FLOAT NOT NULL,
    ortg FLOAT NOT NULL,
    drtg FLOAT NOT NULL,
    net_rtg FLOAT NOT NULL,
    efg_pct FLOAT NOT NULL,
    tov_pct FLOAT NOT NULL,
    orb_pct FLOAT NOT NULL,
    ftr FLOAT NOT NULL,
    opp_efg_pct FLOAT NOT NULL,
    opp_tov_pct FLOAT NOT NULL,
    opp_orb_pct FLOAT NOT NULL,
    opp_ftr FLOAT NOT NULL,
    data_source_id VARCHAR NOT NULL,
    raw_content_hash VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_player_game (
    player_game_id VARCHAR PRIMARY KEY,
    game_id VARCHAR NOT NULL REFERENCES fact_game(game_id),
    canonical_player_id VARCHAR NOT NULL REFERENCES dim_player(canonical_player_id),
    team_id VARCHAR(3) NOT NULL REFERENCES dim_team(canonical_team_id),
    is_spain BOOLEAN NOT NULL,
    is_starter BOOLEAN NOT NULL,
    seconds_played INTEGER NOT NULL,
    minutes_decimal FLOAT NOT NULL,
    pts INTEGER NOT NULL,
    fgm INTEGER NOT NULL,
    fga INTEGER NOT NULL,
    fg2m INTEGER NOT NULL,
    fg2a INTEGER NOT NULL,
    fg3m INTEGER NOT NULL,
    fg3a INTEGER NOT NULL,
    ftm INTEGER NOT NULL,
    fta INTEGER NOT NULL,
    orb INTEGER NOT NULL,
    drb INTEGER NOT NULL,
    trb INTEGER NOT NULL,
    ast INTEGER NOT NULL,
    stl INTEGER NOT NULL,
    blk INTEGER NOT NULL,
    tov INTEGER NOT NULL,
    pf INTEGER NOT NULL,
    fouls_drawn INTEGER,
    plus_minus INTEGER,
    official_pir INTEGER,
    computed_game_score FLOAT NOT NULL,
    ts_pct FLOAT,
    efg_pct FLOAT,
    usg_pct FLOAT,
    data_source_id VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_player_tournament (
    player_tournament_id VARCHAR PRIMARY KEY,
    tournament_id VARCHAR NOT NULL REFERENCES dim_tournament(tournament_id),
    canonical_player_id VARCHAR NOT NULL REFERENCES dim_player(canonical_player_id),
    team_id VARCHAR(3) NOT NULL REFERENCES dim_team(canonical_team_id),
    games_played INTEGER NOT NULL,
    total_seconds INTEGER NOT NULL,
    total_minutes FLOAT NOT NULL,
    pts_per_40 FLOAT NOT NULL,
    fga_per_40 FLOAT NOT NULL,
    fg3a_per_40 FLOAT NOT NULL,
    fta_per_40 FLOAT NOT NULL,
    fg2_pct FLOAT,
    fg3_pct FLOAT,
    ft_pct FLOAT,
    efg_pct FLOAT,
    ts_pct FLOAT,
    three_point_rate FLOAT,
    free_throw_rate FLOAT,
    orb_pct_est FLOAT,
    drb_pct_est FLOAT,
    ast_pct_est FLOAT,
    tov_pct_est FLOAT,
    stl_per_40 FLOAT NOT NULL,
    blk_per_40 FLOAT NOT NULL,
    pf_per_40 FLOAT NOT NULL,
    usg_pct_avg FLOAT,
    avg_game_score FLOAT NOT NULL,
    pir_per_40 FLOAT,
    height_cm_at_tournament INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_validation_issue (
    issue_id VARCHAR PRIMARY KEY,
    entity_type VARCHAR NOT NULL,
    entity_id VARCHAR NOT NULL,
    qa_flag VARCHAR NOT NULL,
    severity VARCHAR NOT NULL,
    message VARCHAR NOT NULL,
    source_a VARCHAR,
    source_b VARCHAR,
    value_a VARCHAR,
    value_b VARCHAR
);
"""
