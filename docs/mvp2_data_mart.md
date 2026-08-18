# Analytical Data Mart Architecture & Data Dictionary
## International Basketball Historical Analytics (2005–2025)

**Location**: `data/04_analytics/`  
**Generated Date**: 2026-08-19T00:07:55.363517  
**Source Warehouse**: `data/03_validated/basketball_analytics.duckdb`  

---

## 1. Materialized Marts Overview

| Mart Name | Format | Rows | Columns | Primary Key | Description |
| :--- | :--- | :---: | :---: | :--- | :--- |
| `mart_team_game_analytics` | Parquet | 2290 | 52 | `team_game_id` | Core analytical feature table for game-level and team-level modeling |
| `mart_tournament_summary` | Parquet | 18 | 24 | `tournament_seq` | Longitudinal tournament time-series aggregates for ITS and macro trends |

---

## 2. Data Dictionary: `mart_team_game_analytics`

| Column Name | Type | Epistemology | Formula / Lineage | Description |
| :--- | :--- | :--- | :--- | :--- |
| `team_game_id` | String | OBSERVED | Source primary key | Unique team-game identifier |
| `game_id` | String | OBSERVED | `fact_game.game_id` | Foreign key to game record |
| `tournament_seq` | Integer | DERIVED | Dense rank (0 to 17) | Chronological tournament index |
| `year` | Integer | OBSERVED | `dim_tournament.year` | Tournament calendar year |
| `competition_id` | String | OBSERVED | `dim_tournament.competition_id` | Federation competition category |
| `rule_3pt_distance_m` | Float | OBSERVED | `dim_rule_set.rule_3pt_distance_m` | Official 3PT line distance (6.25m or 6.75m) |
| `post_2010_rule` | Integer | DERIVED | $1(\text{rule} \ge 6.75)$ | Indicator for post-2010 3PT distance era |
| `time_after_2010` | Integer | DERIVED | $\max(0, T - 6)$ | Relative time elapsed since 2010 rule change |
| `three_point_attempt_rate` | Float | DERIVED | $\text{FG3A} / \text{FGA}$ | 3-Point Attempt Rate ($3\text{PAr}$) |
| `three_point_pct` | Float | DERIVED | $\text{FG3M} / \text{FG3A}$ | 3-Point Accuracy ($3\text{P}\%$) |
| `two_point_pct` | Float | DERIVED | $\text{FG2M} / \text{FG2A}$ | 2-Point Accuracy ($2\text{P}\%$) |
| `free_throw_pct` | Float | DERIVED | $\text{FTM} / \text{FTA}$ | Free Throw Accuracy ($\text{FT}\%$) |
| `efg_pct` | Float | DERIVED | $(\text{FGM} + 0.5 \times \text{FG3M}) / \text{FGA}$ | Effective Field Goal Percentage |
| `tov_pct` | Float | ESTIMATED | $\text{TOV} / (\text{FGA} + 0.44 \cdot \text{FTA} + \text{TOV})$ | Turnover Rate |
| `orb_pct` | Float | ESTIMATED | $\text{ORB} / (\text{ORB} + \text{Opp\_DRB})$ | Offensive Rebound Rate |
| `ftr` | Float | DERIVED | $\text{FTA} / \text{FGA}$ | Free Throw Rate |
| `possessions_bilateral`| Float | ESTIMATED | Dean Oliver $0.44$ Possessions | Game pace denominator |
| `ortg` | Float | ESTIMATED | $100 \times \text{PTS} / \text{Poss}$ | Offensive Rating per 100 possessions |
| `drtg` | Float | ESTIMATED | $100 \times \text{Opp\_PTS} / \text{Poss}$ | Defensive Rating per 100 possessions |
| `net_rtg` | Float | ESTIMATED | $\text{ORtg} - \text{DRtg}$ | Net Rating per 100 possessions |

---

## 3. Provenance & Reproducibility
All transformations are 100% deterministic and execute directly against the immutable validated DuckDB warehouse.
