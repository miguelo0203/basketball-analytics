# MVP-6 Adversarial Repository Audit & Technical Feasibility Report
## International Basketball Historical Analytics (2005–2025)

**Author**: Principal Data Scientist & Lead Software Engineer  
**Status**: Certified Pre-Implementation Audit  
**Date**: 2026-08-18  

---

# 1. Verified Repository Facts & Ground Truth

An empirical audit of the certified repository infrastructure was executed to establish ground truth:

```
+----------------------------------------------------------------------------------------------------+
| REPOSITORY ASSET              | VERIFIED LOCATION & SCHEMA         | CARDINALITY / PROPERTIES      |
+----------------------------------------------------------------------------------------------------+
| **DuckDB Master Warehouse**   | `data/03_validated/`               | 12 tables, 100% foreign key   |
|                               | `basketball_analytics.duckdb`      | integrity, 0 QA violations.   |
| **Team-Game Analytics Mart**  | `data/04_analytics/`               | 2,290 rows (2 rows per match) |
|                               | `mart_team_game_analytics.parquet` | Four Factors, Pace, NetRtg.   |
| **Player Feature Mart**       | `data/04_analytics/`               | 4,350 rows (3,767 qualified)  |
|                               | `mart_player_tournament_features`  | 7 standardized Z-dimensions.  |
| **Player Roles Mart**         | `data/04_analytics/`               | 4,350 rows, 6 functional      |
|                               | `mart_player_roles.parquet`        | archetypes with confidence.   |
| **Video Observation Dataset** | `data/04_analytics/`               | 398 possession actions        |
|                               | `mvp5_video_observations.csv`      | (90 double-coded, κ=1.0/0.80) |
| **Existing Automated Suite**  | `tests/` (11 test files)           | 88 tests passing (88 / 88)    |
+----------------------------------------------------------------------------------------------------+
```

### Verified Tournament & Match Scope:
- **Total Certified Tournaments**: **18 official senior men's tournaments** (8 EuroBaskets, 5 World Cups, 5 Olympic Tournaments from 2005 to 2024).
- **Total Certified Matches**: **1,145 matches** (2,290 team-game observations).
- **Chronological Sequence**:
  - `eurobasket_2005` (40 games), `worldcup_2006` (80 games), `eurobasket_2007` (54 games), `olympics_2008` (38 games), `eurobasket_2009` (54 games), `worldcup_2010` (80 games), `eurobasket_2011` (90 games), `olympics_2012` (38 games), `eurobasket_2013` (90 games), `worldcup_2014` (76 games), `eurobasket_2015` (79 games), `olympics_2016` (38 games), `eurobasket_2017` (76 games), `worldcup_2019` (92 games), `olympics_2020` (26 games), `eurobasket_2022` (76 games), `worldcup_2023` (92 games), `olympics_2024` (26 games).
- **Expanding Temporal Folds**: **17 distinct out-of-sample folds** ($1,105$ evaluated games).

---

# 2. Dependency Audit & Platform Compatibility

```
+----------------------------------------------------------------------------------------------------+
| PACKAGE            | INSTALLED VERSION | RUNTIME STATUS                    | ACTION / RESOLUTION   |
+----------------------------------------------------------------------------------------------------+
| **Python**         | `3.14.6`          | Active 64-bit AMD64 runtime       | Verified              |
| **DuckDB**         | `1.4.4`           | High-performance analytical SQL   | Verified              |
| **Scikit-Learn**   | `1.9.0`           | Regressors, Classifiers, Metrics  | Verified              |
| **LightGBM**       | `4.7.0`           | High-speed GBDT ensembles         | Verified              |
| **SciPy**          | `1.18.0`          | Statistical inference & tests     | Verified              |
| **Statsmodels**    | `0.14.4`          | Multiple testing (multipletests)  | Verified              |
| **SHAP / Numba**   | `0.52.0`          | Numba C-extension DLL blocked by  | **RESOLVED**: Use     |
|                    |                   | Windows AppControl policy on host | model-agnostic feature|
|                    |                   | system.                           | attribution & exact   |
|                    |                   |                                   | TreeSHAP Python engine|
+----------------------------------------------------------------------------------------------------+
```

---

# 3. Methodological Risks & Corrective Decisions

### Risk 1: "Home Team" Semantic Bias in Neutral Tournaments
- *Finding*: International tournament basketball matches are held almost exclusively at neutral host arenas (except for specific host nation matches). Modeling a `home_team_win` target risks introducing artificial home-court priors.
- *Corrective Gate*: Construct a canonical match-level dataset with `game_team_a_win` ($1 = \text{Team A wins}, 0 = \text{Team B wins}$) where Team A and Team B are assigned canonically or randomly with explicit feature differentials $\Delta X = X_A - X_B$.

### Risk 2: Bilateral Duplication in Train/Test Folds
- *Finding*: `mart_team_game_analytics.parquet` contains 2,290 rows (2 per match). If team rows are split naively, Team A could appear in training while Team B (same game) appears in testing, leaking the target.
- *Corrective Gate*: Construct `mvp6_pre_game_features.parquet` with strictly **1 row per match ($N = 1,145$ rows)**.

### Risk 3: In-Tournament Cumulative Feature Leakage
- *Finding*: Calculating a team's tournament average $ORtg$ using all games of that tournament introduces direct look-ahead leakage into early group-stage games.
- *Corrective Gate*: Dynamic in-tournament form features (`diff_in_tourney_form_net`) must strictly aggregate games $1 \dots k-1$ prior to match $k$, excluding game $k$ and all future games.

### Risk 4: Calibration Overfitting
- *Finding*: Fitting Platt scaling or Isotonic regression on out-of-sample test folds causes data leakage.
- *Corrective Gate*: Calibration mappers must be fitted strictly on inner validation folds or expanding training folds.

---

# 4. Implementation Readiness Verdict

The repository infrastructure is **100% verified and ready for MVP-6 implementation**. All data dependencies, mathematical constraints, temporal boundaries, and test suites are defined.
