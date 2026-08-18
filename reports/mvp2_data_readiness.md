# Analytical Data Readiness & Variable Availability Audit
## International Basketball Historical Analytics (2005–2025)

**Database**: `data/03_validated/basketball_analytics.duckdb`  
**Execution Timestamp**: 2026-08-18T04:42:25.177224  
**Status**: **CERTIFIED READINESS AUDIT**

---

## 1. Executive Summary & Warehouse Inventory

The analytical readiness audit evaluated all tables, relations, and variables in the certified DuckDB analytics warehouse across **18 senior men's international tournaments** (2005–2025).

| Table Name | Row Count | Completeness | Analytical Role | Readiness Status |
| :--- | :---: | :---: | :--- | :--- |
| `dim_competition` | 3 | 100.0% | Competition metadata | **READY** |
| `dim_rule_set` | 3 | 100.0% | Regulatory rule-era parameters | **READY** |
| `dim_tournament` | 19 | 100.0% | Tournament master dimension | **READY** |
| `dim_team` | 151 | 100.0% | Federation master dimension | **READY** |
| `dim_source` | 7 | 100.0% | Provenance & lineage registry | **READY** |
| `fact_game` | **1145** | **100.0%** | Game-level outcomes & possessions | **READY (Primary)** |
| `fact_team_game` | **2290** | **100.0%** | Team-game boxscores & Four Factors | **READY (Primary)** |
| `fact_player_game` | **0** | 0.0% | Individual player boxscores | **DEFERRED (MVP-3)** |
| `fact_player_tournament` | **0** | 0.0% | Player tournament rollups | **DEFERRED (MVP-3)** |
| `fact_validation_issue` | 0 | 100.0% | Data quality exception log | **READY (0 Critical)** |

> [!IMPORTANT]
> **Key Finding on Analytical Scope**:  
> Team-game and game-level analytical dimensions are **100% complete** across all 18 historical tournaments ($N = 1,145$ games, $N = 2,290$ team-game observations).  
> Individual player boxscores (`fact_player_game`) are not populated in the certified production warehouse and are scheduled for MVP-3.  
> Therefore, research questions requiring individual player micro-data are formally diagnosed as **unsuitable for MVP-2**, while team-level and game-level research questions possess **maximum statistical power and empirical completeness**.

---

## 2. Epistemological Classification of Variables

To prevent methodological conflation, every available analytical variable is classified into its exact epistemological origin:

| Epistemological Level | Definition | Available Variables in Certified Warehouse |
| :--- | :--- | :--- |
| **OBSERVED** | Direct empirical measurements from source boxscores | `pts`, `fgm`, `fga`, `fg2m`, `fg2a`, `fg3m`, `fg3a`, `ftm`, `fta`, `orb`, `drb`, `trb`, `ast`, `stl`, `blk`, `tov`, `pf`, `overtimes`, `home_score`, `away_score`, `game_date`, `stage` |
| **DERIVED** | Exact algebraic functions of observed variables | `point_differential`, `is_winner`, `is_spain`, `game_duration_seconds`, `pace_40m`, `3PAr` (3PA/FGA), `2P%`, `3P%`, `FT%`, `eFG%` ((FGM + 0.5*3PM)/FGA), `FTr` (FTA/FGA) |
| **ESTIMATED** | Statistical approximations accounting for missing play-by-play | `possessions_bilateral` (Dean Oliver $0.44$ coefficient), `ortg` ($100 	imes PTS / Poss$), `drtg` ($100 	imes Opp\_PTS / Poss$), `net_rtg` ($ORtg - DRtg$), `tov_pct`, `orb_pct` |
| **MODELED** | Outputs of downstream inferential or machine learning models | Segmented regression ITS coefficients ($eta_1, eta_2, eta_3$), Win Probability models, counterfactual predictions |

---

## 3. Tournament-by-Tournament Completeness Matrix

| Tournament ID | Official Name | Year | Comp Type | 3PT Distance | Games | Team-Games | Avg Pace | Avg PTS | 3PAr | 3P% | Status |
| :--- | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `eurobasket_2005` | FIBA EuroBasket 2005 | 2005 | fiba_eurobasket | 6.25m | **40** | 80 | 72.53 | 74.53 | 0.313 | 0.371 | **COMPLETE** |
| `worldcup_2006` | FIBA World Championship 2006 | 2006 | fiba_world_cup | 6.25m | **80** | 160 | 76.18 | 78.24 | 0.314 | 0.370 | **COMPLETE** |
| `eurobasket_2007` | FIBA EuroBasket 2007 | 2007 | fiba_eurobasket | 6.25m | **54** | 108 | 71.71 | 73.52 | 0.314 | 0.371 | **COMPLETE** |
| `olympics_2008` | Beijing 2008 Men's Olympic Basketball Tournament | 2008 | olympics_basketball | 6.25m | **38** | 76 | 79.3 | 81.3 | 0.320 | 0.368 | **COMPLETE** |
| `eurobasket_2009` | FIBA EuroBasket 2009 | 2009 | fiba_eurobasket | 6.25m | **54** | 108 | 71.63 | 73.48 | 0.316 | 0.372 | **COMPLETE** |
| `worldcup_2010` | FIBA World Championship 2010 | 2010 | fiba_world_cup | 6.25m | **80** | 160 | 75.19 | 77.11 | 0.317 | 0.370 | **COMPLETE** |
| `eurobasket_2011` | FIBA EuroBasket 2011 | 2011 | fiba_eurobasket | 6.75m | **90** | 180 | 72.46 | 74.32 | 0.315 | 0.371 | **COMPLETE** |
| `olympics_2012` | London 2012 Men's Olympic Basketball Tournament | 2012 | olympics_basketball | 6.75m | **38** | 76 | 78.49 | 80.45 | 0.316 | 0.370 | **COMPLETE** |
| `eurobasket_2013` | FIBA EuroBasket 2013 | 2013 | fiba_eurobasket | 6.75m | **90** | 180 | 71.19 | 73.04 | 0.315 | 0.371 | **COMPLETE** |
| `worldcup_2014` | FIBA Basketball World Cup 2014 | 2014 | fiba_world_cup | 6.75m | **76** | 152 | 74.73 | 76.62 | 0.315 | 0.370 | **COMPLETE** |
| `eurobasket_2015` | FIBA EuroBasket 2015 | 2015 | fiba_eurobasket | 6.75m | **79** | 158 | 73.22 | 75.2 | 0.315 | 0.371 | **COMPLETE** |
| `olympics_2016` | Rio 2016 Men's Olympic Basketball Tournament | 2016 | olympics_basketball | 6.75m | **38** | 76 | 79.77 | 81.95 | 0.320 | 0.368 | **COMPLETE** |
| `eurobasket_2017` | FIBA EuroBasket 2017 | 2017 | fiba_eurobasket | 6.75m | **76** | 152 | 76.15 | 78.14 | 0.316 | 0.369 | **COMPLETE** |
| `worldcup_2019` | FIBA Basketball World Cup 2019 | 2019 | fiba_world_cup | 6.75m | **92** | 184 | 77.49 | 79.52 | 0.317 | 0.369 | **COMPLETE** |
| `olympics_2020` | Tokyo 2020 Men's Olympic Basketball Tournament | 2021 | olympics_basketball | 6.75m | **26** | 52 | 84.28 | 86.38 | 0.322 | 0.367 | **COMPLETE** |
| `eurobasket_2022` | FIBA EuroBasket 2022 | 2022 | fiba_eurobasket | 6.75m | **76** | 152 | 80.6 | 82.84 | 0.317 | 0.367 | **COMPLETE** |
| `worldcup_2023` | FIBA Basketball World Cup 2023 | 2023 | fiba_world_cup | 6.75m | **92** | 184 | 82.32 | 84.49 | 0.319 | 0.368 | **COMPLETE** |
| `olympics_2024` | Paris 2024 Men's Olympic Basketball Tournament | 2024 | olympics_basketball | 6.75m | **26** | 52 | 83.67 | 85.92 | 0.318 | 0.366 | **COMPLETE** |

---

## 4. Historical Comparability & Structural Shifts

### A. The 2010 FIBA Rule Change (October 1, 2010)
- **Pre-2010 Era (`fiba_2005_2010`)**: 3-point distance was **6.25 meters**; trapezoidal paint area.
- **Post-2010 Era (`fiba_2011_2013` & `fiba_2014_present`)**: 3-point distance extended to **6.75 meters** (+50 cm); rectangular paint area; no-charge semicircle introduced.
- **Analytical Implication**: The 2010 boundary represents a formal quasi-experimental intervention point for Interrupted Time Series (ITS) modeling.

### B. The 2014 Shot Clock Rule Update (October 1, 2014)
- Offensive rebound shot clock reset reduced from 24 seconds to 14 seconds.
- **Analytical Implication**: Creates a secondary acceleration in pace from 2014 onward.

### C. Variables Unsuitable for Longitudinal Comparison
- **Coordinate-based spatial shooting metrics**: Shot chart coordinates are unavailable before 2019.
- **5-man lineup on/off ratings**: Sub-minute substitution timestamps are incomplete before 2012.

### D. Variables Certified for Flagship Research
- `3PAr` (3-Point Attempt Rate): 100% complete across all 2,290 team-game observations.
- `3P%` (3-Point Accuracy): 100% complete across all 2,290 team-game observations.
- `eFG%` (Effective Field Goal Percentage): 100% complete.
- `Pace (40m)` and `Possessions (Bilateral)`: 100% complete.
- `Four Factors` ($eFG\%, TOV\%, ORB\%, FTr$): 100% complete.
- `Ratings` ($ORtg, DRtg, NetRtg$): 100% complete.

---

## 5. Audit Verdict

**ANALYTICAL READINESS: CERTIFIED GREEN FOR TEAM-GAME & TOURNAMENT RESEARCH**

The dataset provides a complete, 20-year longitudinal sample of **2,290 team-game observations** perfectly suited for evaluating macro-tactical evolution, rule-change impacts, and championship Four Factors dynamics.
