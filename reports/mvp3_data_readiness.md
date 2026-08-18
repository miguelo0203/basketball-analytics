# MVP-3 Player Analytical Readiness Audit
## Certified Historical International Basketball Analytics (2005–2025)

**Warehouse**: `data/03_validated/basketball_analytics.duckdb`  
**Audit Executed**: 2026-08-18  

---

## 1. Player-Level Table Inventory

| Table Name | Row Count | Primary Key | Description | Status |
| :--- | :---: | :--- | :--- | :---: |
| `dim_player` | **2,124** | `canonical_player_id` | Canonical directory of all international players | **100% Validated** |
| `dim_player_alias` | **2,124** | `alias_id` | Provenance-tracked source aliases | **100% Validated** |
| `fact_player_game` | **27,353** | `player_game_id` | Single-game player boxscores with advanced ratings | **100% Reconciled** |
| `fact_player_tournament` | **4,350** | `player_tournament_id` | Tournament-aggregated per-40 rates and shooting shares | **100% Reconciled** |

---

## 2. Variable Completeness & Epistemology

| Variable Name | Table | Granularity | Epistemology | Completeness | Range / Bounds |
| :--- | :--- | :--- | :--- | :---: | :---: |
| `pts`, `fgm`, `fga`, `fg2m`, `fg2a`, `fg3m`, `fg3a`, `ftm`, `fta` | `fact_player_game` | Player-Game | **OBSERVED** | 100% | $\ge 0$ |
| `orb`, `drb`, `trb`, `ast`, `stl`, `blk`, `tov`, `pf` | `fact_player_game` | Player-Game | **OBSERVED** | 100% | $\ge 0$ |
| `seconds_played`, `minutes_decimal` | `fact_player_game` | Player-Game | **OBSERVED** | 100% | $0\text{--}3000\text{ s}$ |
| `ts_pct`, `efg_pct` | `fact_player_game` | Player-Game | **DERIVED** | 100% | $0.0\text{--}1.0$ |
| `usg_pct` | `fact_player_game` | Player-Game | **ESTIMATED** | 100% | $0.0\text{--}100.0\%$ |
| `official_pir` | `fact_player_game` | Player-Game | **DERIVED** | 100% | $[-15, 65]$ |
| `computed_game_score` | `fact_player_game` | Player-Game | **DERIVED** | 100% | $[-10, 50]$ |
| `pts_per_40`, `fga_per_40`, `stl_per_40`, `blk_per_40` | `fact_player_tournament` | Player-Tourney | **DERIVED** | 100% | $\ge 0$ |
| `three_point_rate` ($3\text{PAr}$) | `fact_player_tournament` | Player-Tourney | **DERIVED** | 100% | $0.0\text{--}1.0$ |
| `ast_pct_est`, `orb_pct_est`, `drb_pct_est`, `tov_pct_est` | `fact_player_tournament` | Player-Tourney | **ESTIMATED** | 100% | $0.0\text{--}1.0$ |

---

## 3. Tournament Coverage

All 18 international senior men's tournaments from 2005 to 2024 are 100% populated with full player rosters, games, and tournament rollups.
