# MVP-12 Master Repository Inventory & Technical Asset Audit
## International Basketball Historical Analytics (2005–2025)

**Status**: Formally Certified Repository Inventory  
**Scope**: Complete Audit of Analytical, Engineering, Visualization, and Testing Assets (MVP-0 to MVP-11)  
**Date**: 2026-08-18  

---

# 1. Verified Architecture & Directory Layout

The repository is structured into modular layers spanning data engineering, feature stores, analytics marts, supervised machine learning, tournament simulation, decision support, and presentation:

```text
España2005-2025/
├── data/
│   ├── 01_raw/                  # Immutable raw tournament source data
│   ├── 02_staged/               # Parsed and typed intermediate staging tables
│   ├── 03_validated/            # Certified DuckDB relational warehouse (basketball_analytics.duckdb)
│   └── 04_analytics/            # Analytical Parquet feature marts & CSV benchmark outputs
│       ├── mart_team_game_analytics.parquet
│       ├── mart_player_tournament_features.parquet
│       ├── mart_player_roles.parquet
│       ├── mvp5_video_observations.csv
│       ├── mvp6_pre_game_features.parquet
│       ├── mvp6_model_predictions.csv
│       ├── mvp6_model_benchmark.csv
│       ├── mvp6_bootstrap_results.csv
│       ├── mvp7_tournament_simulations.parquet
│       ├── mvp7_scenario_results.csv
│       ├── mvp7_counterfactual_results.csv
│       ├── mvp8_decision_dossiers.parquet
│       ├── mvp8_decision_evaluations.csv
│       ├── mvp10_evidence_matrix.parquet
│       ├── mvp10_coaching_briefs.parquet
│       └── mvp10_workspace_records.parquet
├── src/
│   ├── config.py                # Global paths, constants, and database configurations
│   ├── data_engineering/        # Ingestion, staging, and DuckDB validation pipelines
│   └── analytics/               # Core analytical, ML, simulation, and decision engines
│       ├── mvp2_historical_research.py
│       ├── mvp3_player_analytics.py
│       ├── mvp4_recruitment_scouting.py
│       ├── mvp5_tactical_validation.py
│       ├── mvp6_supervised_analytics.py
│       ├── mvp6_visualizations.py
│       ├── mvp7_tournament_simulation.py
│       ├── mvp7_scenario_analysis.py
│       ├── mvp7_visualizations.py
│       ├── mvp8_decision_system.py
│       ├── mvp8_historical_validation.py
│       ├── mvp8_visualizations.py
│       ├── mvp9_generate_pptx.py
│       ├── mvp10_evidence_engine.py
│       ├── mvp10_brief_generator.py
│       ├── mvp10_analyst_workspace.py
│       └── mvp10_visualizations.py
├── reports/                     # Formal technical reports and markdown synthesis deliverables
│   ├── figures/                 # Publication-quality figures across MVP-6, MVP-7, MVP-8, MVP-10
│   ├── presentation/            # 40-slide master portfolio deck (.md, .pptx, slide data, notes)
│   ├── mvp0_*.md to mvp11_*.md  # 35+ comprehensive technical reports
│   └── mvp12/                   # Portfolio strategy, story, workflow, guides, interview pack
├── tests/                       # 17 Automated pytest test modules (160 passing tests)
└── portfolio/                   # Public portfolio assets, case studies, and demo resources
```

---

# 2. Verified Data Assets & Cardinalities

```
+----------------------------------------------------------------------------------------------------+
| DATA ASSET                   | FILE FORMAT & LOCATION             | VERIFIED CARDINALITY / SCOPE   |
+----------------------------------------------------------------------------------------------------+
| **Core Relational DB**       | `basketball_analytics.duckdb`      | 12 Tables, 1,145 matches       |
| **Team Analytics Mart**      | `mart_team_game_analytics.parquet` | 2,290 Rows, 52 Columns         |
| **Player Feature Mart**      | `mart_player_tournament_features`  | 4,350 Campaigns, 43 Columns    |
| **Player Role Mart**         | `mart_player_roles.parquet`        | 4,350 Campaigns, 6 Archetypes  |
| **Video Coding Dataset**     | `mvp5_video_observations.csv`      | 420 Double-Coded Possessions   |
| **Supervised Features**      | `mvp6_pre_game_features.parquet`   | 1,145 Pre-Game Feature Vectors |
| **Out-of-Sample Predictions**| `mvp6_model_predictions.csv`       | 1,105 Matches, 17 Folds        |
| **Tournament Simulations**   | `mvp7_tournament_simulations`      | 364 Campaigns, 180,000 Runs    |
| **Decision Dossiers**        | `mvp8_decision_dossiers.parquet`   | 14 Flagship Player Dossiers    |
| **Evidence Matrix**          | `mvp10_evidence_matrix.parquet`    | 1,145 Match Evidence Matrices  |
| **Coaching Briefs**          | `mvp10_coaching_briefs.parquet`    | Flagship Tactical Briefs       |
| **Workspace Records**        | `mvp10_workspace_records.parquet`  | Flagship Demonstration Records |
+----------------------------------------------------------------------------------------------------+
```

---

# 3. Existing Visual Assets & Figures

- `reports/figures/mvp6/`: 5 publication figures (model benchmark, calibration curves, SHAP summary, bootstrap CIs, learning curves).
- `reports/figures/mvp7/`: 5 publication figures (tournament champion probabilities, round distributions, bracket trees, shrinkage sensitivity, counterfactual replays).
- `reports/figures/mvp8/`: 5 publication figures (decision matrix, radar profiles, historical validation, contradiction alerts, workflow pipeline).
- `reports/figures/mvp10/`: 5 publication figures (evidence pipeline, coaching brief layout, signal vs uncertainty, contradiction matrix, 5-point decision timeline).
- `reports/presentation/`: `mvp9_analyst_portfolio.pptx` (40-slide widescreen presentation deck).

---

# 4. Current Execution Commands & Testing

- **Run Full Automated Test Suite**:
  ```bash
  python -m pytest tests -q
  ```
  *(Result: 160 passed in ~117s across 17 test modules)*.
- **Launch Interactive Streamlit Analyst Workspace**:
  ```bash
  streamlit run src/analytics/mvp10_analyst_workspace.py -- streamlit
  ```
- **Generate PowerPoint Deck**:
  ```bash
  python -m src.analytics.mvp9_generate_pptx
  ```

---

# 5. Public Boundaries & Items NOT to Expose as Current/Operational

1. **No Live Club / Transfer Data**: Historical Spanish national team data (2005–2024) must never be presented as live recruitment or current market pricing.
2. **No Claim of Autonomous Decision-Making**: The system supports human coaching staffs with structured evidence; it does not replace coaches.
3. **Strict Epistemological Boundaries**: Models describe historical conditional associations; they do not claim causal proof or infallible future forecasting.
