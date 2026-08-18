# MVP-9 Slide Data Dictionary & Quantitative Manifest
## Complete Traceable Data Sources for the 40-Slide Portfolio Deck

---

# Data Tables & Metric Source Mapping

### Slide 5–6: Historical Universe & Cardinalities
- **Source**: `data/03_validated/basketball_analytics.duckdb` & `reports/mvp8_repository_audit.md`
- **Tournaments ($18$)**:
  * EuroBasket: 2005, 2007, 2009, 2011, 2013, 2015, 2017, 2022 ($8$ tournaments)
  * FIBA World Cup: 2006, 2010, 2014, 2019, 2023 ($5$ tournaments)
  * Olympic Games: 2008, 2012, 2016, 2020, 2024 ($5$ tournaments)
- **Total Matches**: `1,145` canonical games
- **Team-Game Observations**: `2,290` rows
- **Player-Tournament Campaigns**: `4,350` rows (`3,767` qualified with $\ge 40$ minutes)
- **Player-Game Observations**: `27,353` rows

### Slide 7: Functional Archetypes
- **Source**: `data/04_analytics/mart_player_roles.parquet`
- **6 Archetypes**:
  1. Primary Initiator / Floor General ($N = 612$, Mean $AST\% = 28.4\%$)
  2. Two-Way Scoring Wing / Slasher ($N = 1,140$, Mean $PTS/40 = 18.2$)
  3. Perimeter Movement Shooter / Spacer ($N = 784$, Mean $3\text{PAr} = 54.2\%$)
  4. Stretch Big / Pick-and-Pop Forward ($N = 598$, Mean $3\text{PAr} = 36.5\%$)
  5. Low-Block Anchor / Interior Scorer ($N = 688$, Mean $ORB\% = 11.4\%$)
  6. Rim Protector / Roll Threat & Anchor ($N = 528$, Mean $BLK\% = 4.2\%$)

### Slide 12–13: Video Tactical Evidence & IRR
- **Source**: `data/04_analytics/mvp5_video_observations.csv` & `reports/mvp5_final_report.md`
- **Total Coded Possessions**: `420` possessions
- **Inter-Rater Reliability (Cohen's Kappa)**:
  * Action Category Agreement: $\kappa = 1.00$
  * Execution Quality Score Agreement: $\kappa = 0.80$

### Slide 14–16: Supervised Model Benchmark & Calibration
- **Source**: `data/04_analytics/mvp6_model_benchmark.csv` & `reports/mvp6_supervised_benchmark_report.md`
- **Validation Scheme**: 17 expanding temporal walk-forward folds ($1,105$ out-of-sample matches)
- **Classification Benchmark**:
  * Naive 50%: Brier $= 0.2500$, LogLoss $= 0.6931$, AUC $= 0.5000$
  * Logistic Regression: Brier $= 0.2104$, LogLoss $= 0.6082$, AUC $= 0.7321$
  * ElasticNet: Brier $= 0.2085$, LogLoss $= 0.6014$, AUC $= 0.7389$
  * LightGBM (Champion): **Brier $= 0.1967$**, **LogLoss $= 0.5741$**, **AUC $= 0.7613$**
- **Regression Benchmark (Margin)**:
  * Naive Margin: MAE $= 14.82$ pts, RMSE $= 18.12$ pts, $R^2 = 0.0000$
  * Ridge: MAE $= 12.35$ pts, RMSE $= 15.94$ pts, $R^2 = 0.2140$
  * ElasticNet: MAE $= 12.18$ pts, RMSE $= 15.78$ pts, $R^2 = 0.2315$
  * LightGBM (Champion): **MAE $= 11.74$ pts**, **RMSE $= 15.35$ pts**, **$R^2 = 0.2789$**
- **Calibration**:
  * Expected Calibration Error (ECE): **$\text{ECE} = 0.0314$**

### Slide 17: Non-Parametric Statistical Inference
- **Source**: `data/04_analytics/mvp6_bootstrap_results.csv` & `mvp6_permutation_results.csv`
- **Bootstrap Iterations**: $B = 5,000$ clustered by tournament
- **Permutation Tests**: $P = 10,000$ random shuffles
- **False Discovery Rate**: Benjamini-Hochberg $Q = 0.05$

### Slide 20–23: Tournament Monte Carlo Simulations
- **Source**: `data/04_analytics/mvp7_tournament_simulations.parquet` & `reports/mvp7_simulation_report.md`
- **Scale**: $18$ Tournaments $\times 10,000$ Iterations $= 180,000$ Tournament Runs (Seed $= 42$)
- **Retrospective Validation**:
  * Champion Rank #1 Hit Rate: **$72.2\%$ (13 / 18)**
  * Champion Top-2 Hit Rate: **$77.8\%$ (14 / 18)**
  * Champion Top-4 Hit Rate: **$100.0\%$ (18 / 18)**
  * Mean Rank of Champion: **$1.50$**
  * Mean Title Probability of Champion: **$55.05\%$**
- **Shrinkage Invariance**:
  * $\lambda = 1.00 \rightarrow$ Top-1: $72.2\%$, Mean Rank: $1.50$, Mean Prob: $55.05\%$
  * $\lambda = 0.75 \rightarrow$ Top-1: $72.2\%$, Mean Rank: $1.50$, Mean Prob: $51.17\%$
  * $\lambda = 0.50 \rightarrow$ Top-1: $72.2\%$, Mean Rank: $1.50$, Mean Prob: $47.11\%$
- **Counterfactuals**:
  * CF1 (Beijing 2008 Spain vs USA): Spain Win Pct $= 26.84\%$ (USA $73.16\%$)
  * CF2 (EuroBasket 2015 Spain Path): Spain Model-Implied Title Prob $= 67.60\%$
  * CF3 (EuroBasket 2022 Spain Sensitivity): Baseline $72.04\% \rightarrow$ Shrunk $66.16\%$

### Slide 24–30: Decision System & Historical Validation
- **Source**: `data/04_analytics/mvp8_decision_dossiers.parquet` & `mvp8_decision_evaluations.csv`
- **Multi-Criteria Equation**:
  $$S_{\text{rec}} = 0.25 \cdot S_{\text{role}} + 0.25 \cdot \min(100, TS\% \cdot 140) + 0.20 \cdot S_{\text{rel}} + 0.15 \cdot S_{\text{pred}} + 0.15 \cdot S_{\text{film}}$$
- **Candidate Dossier Scores**:
  * Lorenzo Brown (EB 2022): $S_{\text{rec}} = 84.9$ (Tier B, RECOMMENDED) $\rightarrow$ Real: All-Tournament Team & Gold Medal
  * Pau Gasol (EB 2015): $S_{\text{rec}} = 80.8$ (Tier A, RECOMMENDED) $\rightarrow$ Real: Tournament MVP & Gold Medal
  * Willy Hernangómez (EB 2022): $S_{\text{rec}} = 78.8$ (Tier B, RECOMMENDED) $\rightarrow$ Real: Tournament MVP
  * Rudy Fernández (WC 2019): $S_{\text{rec}} = 76.3$ (Tier B, RECOMMENDED) $\rightarrow$ Real: Captain & Gold Medal
  * Alberto Díaz (EB 2022): $S_{\text{rec}} = 75.8$ (Tier B, RECOMMENDED) $\rightarrow$ Real: Defensive Anchor & Gold Medal
  * José Manuel Calderón (EB 2011): $S_{\text{rec}} = 74.8$ (Tier B, RECOMMENDED) $\rightarrow$ Real: Starting PG & Gold Medal
  * Ricky Rubio (WC 2019): $S_{\text{rec}} = 72.2$ (Tier B, RECOMMENDED) $\rightarrow$ Real: World Cup MVP & Gold Medal
  * Juan Carlos Navarro (EB 2011): $S_{\text{rec}} = 71.9$ (Tier B, RECOMMENDED) $\rightarrow$ Real: Tournament MVP & Gold Medal
- **Historical Decision Concordance**:
  * MVP-8 Multi-Layer System: **$80.0\%$ (4 / 5 Decisions)**
  * Baseline Rule A (Naive PPG): **$60.0\%$ (3 / 5 Decisions)**
  * Baseline Rule B (Experience): **$60.0\%$ (3 / 5 Decisions)**

### Slide 34: Test Suite & Code Quality
- **Automated Tests**: `128` passing tests in `31.80` seconds (100% pass rate).
- **Test Modules ($14$)**: Covering ETL, relational schema, features, archetypes, video IRR, supervised ML, statistical inference, tournament simulations, scenario analysis, and decision dossiers.
