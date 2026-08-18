# Relational Data Model & Star Schema Specification
## International Basketball Historical Analytics (2005–2025)

---

## 1. Grain Definitions & Relational Entities

Every table in the production DuckDB data warehouse has an explicitly defined grain and strict key constraints.

```
+------------------------------------------------------------------------------------+
| TABLE GRAIN SUMMARY                                                                |
+-----------------------------+------------------------------------------------------+
| Table Name                  | Exact Grain Definition                               |
+-----------------------------+------------------------------------------------------+
| dim_source                  | 1 row = 1 data acquisition source / provider         |
| dim_rule_set                | 1 row = 1 regulatory FIBA ruleset era                |
| dim_competition             | 1 row = 1 competition type (EuroBasket, WC, Olympics)|
| dim_tournament              | 1 row = 1 tournament edition                         |
| dim_team                    | 1 row = 1 national federation / country              |
| dim_player                  | 1 row = 1 canonical physical human person            |
| dim_player_alias            | 1 row = 1 source-specific player identifier / name   |
| fact_game                   | 1 row = 1 basketball game played                     |
| fact_team_game              | 1 row = 1 team's boxscore in 1 game (2 rows / game)  |
| fact_player_game            | 1 row = 1 player's boxscore in 1 game                |
| fact_player_tournament      | 1 row = 1 player's aggregated stats in 1 tournament  |
| fact_validation_issue       | 1 row = 1 QA warning / error logged for an entity    |
| fact_shot_event (Optional)  | 1 row = 1 spatial shot attempt (2019-2025)           |
+-----------------------------+------------------------------------------------------+
```

---

## 2. Table Specifications

### 2.1 `dim_source`
- **Purpose**: Tracks acquisition providers and establishes fallback precedence.
- **Grain**: One row per data provider.
- **Primary Key**: `source_id` (VARCHAR)
- **Columns**:
  - `source_id` (VARCHAR, PK): e.g. `SRC_FIBA_ARCHIVE`, `SRC_BREF`, `SRC_FIBA_MODERN`.
  - `source_name` (VARCHAR, NOT NULL)
  - `base_url` (VARCHAR, NOT NULL)
  - `source_type` (VARCHAR, NOT NULL): `official_archive`, `official_api`, `secondary_structured`.
  - `precedence_rank` (INTEGER, NOT NULL): 1 (Primary) to 3 (Secondary).

### 2.2 `dim_rule_set`
- **Purpose**: Encodes regulatory eras to prevent inferring basketball rules from calendar year.
- **Grain**: One row per ruleset version.
- **Primary Key**: `rule_set_id` (VARCHAR)
- **Columns**:
  - `rule_set_id` (VARCHAR, PK): `fiba_2005_2010`, `fiba_2011_2013`, `fiba_2014_present`.
  - `effective_from` (DATE, NOT NULL)
  - `effective_to` (DATE, NOT NULL)
  - `rule_3pt_distance_m` (FLOAT, NOT NULL): 6.25 or 6.75.
  - `shot_clock_seconds` (INTEGER, NOT NULL): 24.
  - `shot_clock_orb_seconds` (INTEGER, NOT NULL): 24 or 14.
  - `lane_geometry` (VARCHAR, NOT NULL): `trapezoid` or `rectangle`.
  - `no_charge_semicircle` (BOOLEAN, NOT NULL): `false` or `true`.
  - `game_duration_minutes` (INTEGER, NOT NULL): 40.
  - `ot_duration_minutes` (INTEGER, NOT NULL): 5.

### 2.3 `dim_tournament`
- **Purpose**: Defines specific tournament editions.
- **Grain**: One row per tournament edition.
- **Primary Key**: `tournament_id` (VARCHAR)
- **Foreign Keys**: `competition_id` $\rightarrow$ `dim_competition`, `rule_set_id` $\rightarrow$ `dim_rule_set`.
- **Columns**:
  - `tournament_id` (VARCHAR, PK): e.g. `eurobasket_2011`, `worldcup_2019`.
  - `competition_id` (VARCHAR, FK, NOT NULL)
  - `rule_set_id` (VARCHAR, FK, NOT NULL)
  - `year` (INTEGER, NOT NULL)
  - `official_name` (VARCHAR, NOT NULL)
  - `host_countries` (VARCHAR, NOT NULL)
  - `num_teams` (INTEGER, NOT NULL)
  - `start_date` (DATE, NOT NULL)
  - `end_date` (DATE, NOT NULL)

### 2.4 `dim_player`
- **Purpose**: Canonical physical person registry. Excludes tournament-specific nationalities.
- **Grain**: One row per human athlete.
- **Primary Key**: `canonical_player_id` (VARCHAR)
- **Columns**:
  - `canonical_player_id` (VARCHAR, PK): e.g. `pau_gasol_1980`.
  - `full_canonical_name` (VARCHAR, NOT NULL)
  - `birth_date` (DATE, NULLABLE)
  - `birth_year` (INTEGER, NOT NULL)
  - `primary_position` (VARCHAR, NOT NULL): `G`, `F`, `C`, `G-F`, `F-C`.
  - `identity_confidence` (VARCHAR, NOT NULL): `EXACT`, `DETERMINISTIC`, `MANUAL`, `PROBABILISTIC`.

### 2.5 `dim_player_alias`
- **Purpose**: Maps raw source identifiers to canonical person records.
- **Grain**: One row per source string/ID mapping.
- **Primary Key**: `alias_id` (VARCHAR)
- **Columns**:
  - `alias_id` (VARCHAR, PK)
  - `canonical_player_id` (VARCHAR, FK, NOT NULL)
  - `source_id` (VARCHAR, FK, NOT NULL)
  - `source_player_id` (VARCHAR, NULLABLE)
  - `raw_name_string` (VARCHAR, NOT NULL)

### 2.6 `fact_game`
- **Purpose**: Core game event registry with pace and possessions.
- **Grain**: One row per game played.
- **Primary Key**: `game_id` (VARCHAR)
- **Columns**:
  - `game_id` (VARCHAR, PK): e.g. `wc2019_final_esp_arg`.
  - `tournament_id` (VARCHAR, FK, NOT NULL)
  - `game_date` (DATE, NOT NULL)
  - `stage` (VARCHAR, NOT NULL): `Group Phase`, `Second Round`, `Quarter-Finals`, `Semi-Finals`, `Bronze Game`, `Final`.
  - `home_team_id` (VARCHAR(3), FK, NOT NULL)
  - `away_team_id` (VARCHAR(3), FK, NOT NULL)
  - `home_score` (INTEGER, NOT NULL)
  - `away_score` (INTEGER, NOT NULL)
  - `overtimes` (INTEGER, NOT NULL, DEFAULT 0)
  - `game_duration_seconds` (INTEGER, NOT NULL): $(40 + 5 \times \text{overtimes}) \times 60$.
  - `pace_40m` (FLOAT, NOT NULL)
  - `possessions_bilateral` (FLOAT, NOT NULL)
  - `possession_method` (VARCHAR, NOT NULL): `EST_BILATERAL`, `PBP_EXACT`.
  - `pbp_coverage_level` (INTEGER, NOT NULL): 0 to 5.
  - `shot_data_available` (BOOLEAN, NOT NULL DEFAULT FALSE)
  - `validation_status` (VARCHAR, NOT NULL): `VALIDATED`, `WARNING`, `QUARANTINED`.

### 2.7 `fact_team_game`
- **Purpose**: Team-level boxscore, ratings, and four factors for each team in each game.
- **Grain**: One row per team per game (exactly 2 rows per `game_id`).
- **Primary Key**: `team_game_id` (VARCHAR)
- **Columns**:
  - `team_game_id` (VARCHAR, PK): `{game_id}_{team_id}`.
  - `game_id` (VARCHAR, FK, NOT NULL)
  - `team_id` (VARCHAR(3), FK, NOT NULL)
  - `opponent_id` (VARCHAR(3), FK, NOT NULL)
  - `is_spain` (BOOLEAN, NOT NULL)
  - `is_winner` (BOOLEAN, NOT NULL)
  - `team_player_minutes_expected` (INTEGER, NOT NULL): $200 + 25 \times \text{overtimes}$.
  - `team_player_seconds_accounted` (INTEGER, NOT NULL)
  - `pts, fgm, fga, fg2m, fg2a, fg3m, fg3a, ftm, fta` (INTEGER, NOT NULL)
  - `orb, drb, trb, ast, stl, blk, tov, pf` (INTEGER, NOT NULL)
  - `fouls_drawn` (INTEGER, NULLABLE)
  - `possessions_simple` (FLOAT, NOT NULL)
  - `possessions_bilateral` (FLOAT, NOT NULL)
  - `ortg` (FLOAT, NOT NULL): $100 \times (\text{pts} / \text{possessions\_bilateral})$.
  - `drtg` (FLOAT, NOT NULL): $100 \times (\text{opp\_pts} / \text{possessions\_bilateral})$.
  - `net_rtg` (FLOAT, NOT NULL): $\text{ortg} - \text{drtg}$.
  - `efg_pct, tov_pct, orb_pct, ftr` (FLOAT, NOT NULL)
  - `opp_efg_pct, opp_tov_pct, opp_orb_pct, opp_ftr` (FLOAT, NOT NULL)
  - `data_source_id` (VARCHAR, FK, NOT NULL)
  - `raw_content_hash` (VARCHAR, NOT NULL)

### 2.8 `fact_player_game`
- **Purpose**: Individual player performance per game.
- **Grain**: One row per player in a game for a team.
- **Primary Key**: `player_game_id` (VARCHAR)
- **Columns**:
  - `player_game_id` (VARCHAR, PK): `{game_id}_{canonical_player_id}`.
  - `game_id` (VARCHAR, FK, NOT NULL)
  - `canonical_player_id` (VARCHAR, FK, NOT NULL)
  - `team_id` (VARCHAR(3), FK, NOT NULL)
  - `is_spain` (BOOLEAN, NOT NULL)
  - `is_starter` (BOOLEAN, NOT NULL)
  - `seconds_played` (INTEGER, NOT NULL)
  - `minutes_decimal` (FLOAT, NOT NULL): `seconds_played / 60.0`.
  - `pts, fgm, fga, fg2m, fg2a, fg3m, fg3a, ftm, fta` (INTEGER, NOT NULL)
  - `orb, drb, trb, ast, stl, blk, tov, pf` (INTEGER, NOT NULL)
  - `fouls_drawn` (INTEGER, NULLABLE)
  - `plus_minus` (INTEGER, NULLABLE)
  - `official_pir` (INTEGER, NULLABLE)
  - `computed_game_score` (FLOAT, NOT NULL)
  - `ts_pct` (FLOAT, NULLABLE)
  - `efg_pct` (FLOAT, NULLABLE)
  - `usg_pct` (FLOAT, NULLABLE)
  - `data_source_id` (VARCHAR, FK, NOT NULL)

### 2.9 `fact_player_tournament`
- **Purpose**: Normalised per-40 rates and usage metrics for unsupervised learning across all tournaments.
- **Grain**: One row per player per tournament edition.
- **Primary Key**: `player_tournament_id` (VARCHAR)
- **Columns**:
  - `player_tournament_id` (VARCHAR, PK): `{tournament_id}_{canonical_player_id}`.
  - `tournament_id` (VARCHAR, FK, NOT NULL)
  - `canonical_player_id` (VARCHAR, FK, NOT NULL)
  - `team_id` (VARCHAR(3), FK, NOT NULL)
  - `games_played` (INTEGER, NOT NULL)
  - `total_seconds` (INTEGER, NOT NULL)
  - `total_minutes` (FLOAT, NOT NULL)
  - `pts_per_40, fga_per_40, fg3a_per_40, fta_per_40` (FLOAT, NOT NULL)
  - `fg2_pct, fg3_pct, ft_pct, efg_pct, ts_pct` (FLOAT, NULLABLE)
  - `three_point_rate, free_throw_rate` (FLOAT, NULLABLE)
  - `orb_pct_est, drb_pct_est, ast_pct_est, tov_pct_est` (FLOAT, NULLABLE)
  - `stl_per_40, blk_per_40, pf_per_40` (FLOAT, NOT NULL)
  - `usg_pct_avg` (FLOAT, NULLABLE)
  - `avg_game_score` (FLOAT, NOT NULL)
  - `pir_per_40` (FLOAT, NULLABLE)
  - `height_cm_at_tournament` (INTEGER, NOT NULL)
