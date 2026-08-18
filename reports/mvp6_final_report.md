# MVP-6 Final Synthesis Report: Supervised Analytics, Statistical Inference & Model Validation
## International Basketball Historical Analytics (2005–2025)

**Status**: Certified & Automated  
**Pipeline Coverage**: MVP-0 through MVP-6  
**Total Automated Tests**: 98 Passing (98 / 98, 100% Pass Rate)  
**Bitwise Reproducibility**: Confirmed across Run A and Run B  
**Master Random Seed**: 42  

---

# 1. Research Questions & Scientific Objectives

MVP-6 bridges econometric research (MVP-2) and decision-support systems (MVP-4/5) by delivering a rigorous supervised learning and statistical validation framework. It answers three formal research questions:

1. **Question A (Supervised Predictive Modeling)**: With what out-of-sample probabilistic accuracy and calibration can pre-game team baselines and Four Factors predict international match outcomes (Win/Loss) and point margins across 20 years of tournaments?
2. **Question B (Non-Parametric Statistical Inference)**: How wide are the empirical uncertainty bounds around player and team rate metrics, and do observed differences between functional archetypes survive exact permutation testing under False Discovery Rate (FDR) control?
3. **Question C (Model Interpretability & Stability)**: Which tactical features drive out-of-sample predictions, and does the feature hierarchy remain stable across disparate tournament eras?

---

# 2. Dataset & Verified Cardinalities

All features and targets are derived from the certified relational DuckDB warehouse:
- **Certified Tournaments**: 18 senior men's tournaments (8 EuroBaskets, 5 World Cups, 5 Olympic Tournaments from 2005 to 2024).
- **Match-Level Pre-Game Modeling Set**: Exactly **1,145 matches** (21 columns, strictly 1 canonical row per match).
- **Out-of-Sample Evaluated Games**: **1,105 games** across 17 expanding temporal walk-forward validation folds.
- **Player-Tournament Campaigns**: **4,350 campaigns** (3,767 qualified $\ge 40$ mins) used for non-parametric inference.

---

# 3. Feature Provenance & Leakage Invariants

Every feature in `mvp6_pre_game_features.parquet` satisfies the strict temporal invariant:
$$\text{feature\_information\_timestamp} < \text{game\_timestamp}$$

```
+----------------------------------------------------------------------------------------------------+
| FEATURE NAME                 | CATEGORY    | SOURCE / TEMPORAL WINDOW              | LEAKAGE STATUS|
+----------------------------------------------------------------------------------------------------+
| `diff_hist_net_rating`       | Historical  | Strictly prior tournaments (seq < t)  | SAFE          |
| `diff_hist_efg_pct`          | Historical  | Strictly prior tournaments (seq < t)  | SAFE          |
| `diff_hist_tov_pct`          | Historical  | Strictly prior tournaments (seq < t)  | SAFE          |
| `diff_hist_orb_pct`          | Historical  | Strictly prior tournaments (seq < t)  | SAFE          |
| `diff_hist_ftr`              | Historical  | Strictly prior tournaments (seq < t)  | SAFE          |
| `diff_in_tourney_form_net`   | Dynamic     | Cumulative games 1..k-1 in tourney    | SAFE (k excluded)|
| `diff_rest_days`             | Context     | Days since last game in same tourney  | SAFE          |
| `is_knockout_stage`          | Context     | Bracket stage prior to match tip-off  | SAFE          |
| `post_2010_rule_era`         | Context     | Regulatory distance standard (6.75m)  | SAFE          |
| `diff_experience_caps`       | Context     | Prior tournament games played         | SAFE          |
+----------------------------------------------------------------------------------------------------+
```

---

# 4. Expanding Temporal Walk-Forward Validation

To prevent future leakage and respect the temporal clustering of sports tournaments, the dataset was split into **17 expanding temporal folds**:
- **Fold 01**: Train 2005 ($N=40$) $\rightarrow$ Test 2006 ($N=80$)
- **Fold 02**: Train 2005–2006 ($N=120$) $\rightarrow$ Test 2007 ($N=54$)
- $\dots$
- **Fold 17**: Train 2005–2023 ($N=1,119$) $\rightarrow$ Test 2024 ($N=26$)

---

# 5. Out-of-Sample Model Benchmark

```
+----------------------------------------------------------------------------------------------------+
| MODEL ARCHITECTURE           | TASK           | PRIMARY SCORE | SECONDARY METRICS                  |
+----------------------------------------------------------------------------------------------------+
| **Naive 50% Baseline**       | Classification | Brier: 0.2500 | LogLoss: 0.6931, AUC: 0.5000       |
| **Logistic Regression L2**   | Classification | Brier: 0.2073 | LogLoss: 0.6085, AUC: 0.7440       |
| **ElasticNet Classifier**    | Classification | Brier: 0.2047 | LogLoss: 0.6004, AUC: 0.7514       |
| **LightGBM Classifier**      | Classification | **Brier: 0.1967**| **LogLoss: 0.5741, AUC: 0.7613**  |
+----------------------------------------------------------------------------------------------------+
| **Naive Margin Baseline**    | Regression     | MAE: 14.169 pts| RMSE: 18.116 pts, R²: -0.0038      |
| **Ridge Regressor**          | Regression     | MAE: 12.099 pts| RMSE: 15.692 pts, R²: +0.2469      |
| **ElasticNet Regressor**     | Regression     | MAE: 11.945 pts| RMSE: 15.502 pts, R²: +0.2651      |
| **LightGBM Regressor**       | Regression     | **MAE: 11.739 pts**| **RMSE: 15.355 pts, R²: +0.2789**  |
+----------------------------------------------------------------------------------------------------+
```

---

# 6. Probability Calibration & Reliability

- **Expected Calibration Error ($ECE$)**: LightGBM achieves $ECE = 0.0314$ (a $-47.6\%$ calibration error reduction over standard Logistic Regression at $0.0599$).
- **Reliability Diagram**: Probability estimates closely track empirical win fractions across all 10 probability deciles.

---

# 7. Feature Ablation Findings

```
Spec 1 (Macro NetRtg)          -> Brier: 0.2102 | ROC-AUC: 0.7261 | MAE: 12.207 pts
Spec 2 (+ Four Factors)        -> Brier: 0.1980 | ROC-AUC: 0.7590 | MAE: 11.724 pts  <-- Major Leap (-5.8% Brier)
Spec 3 (+ In-Tourney Form)     -> Brier: 0.1974 | ROC-AUC: 0.7622 | MAE: 11.731 pts  <-- Minor Signal (+0.003 AUC)
Spec 4 (+ Rest, Stage, Era)    -> Brier: 0.1967 | ROC-AUC: 0.7613 | MAE: 11.739 pts  <-- Stabilizes Long-Tail
```

---

# 8. Feature Attribution & Model Interpretability

> [!NOTE]
> Feature attributions represent **predictive game-theoretic associations**, not causal econometric effects.

1. **Top Predictive Drivers**:
   - 1. Historical Net Rating Differential (`0.0245` Brier loss drop)
   - 2. Effective Field Goal Percentage Differential (`0.0182` Brier loss drop)
   - 3. In-Tournament Form Differential (`0.0141` Brier loss drop)
   - 4. Turnover Rate Differential (`0.0118` Brier loss drop)
2. **Temporal Fold Stability**: Spearman rank correlation $\mathbf{\rho = 0.850}$ across all 17 temporal folds, confirming tactical invariance over 20 years.

---

# 9. Non-Parametric Statistical Inference & Hypothesis Testing

1. **Clustered Bootstrap ($B = 5,000$)**:
   - $TS\%$: Mean $63.65\%$ [95% CI: $62.64\%, 64.66\%$], $SE = 0.518\%$.
   - $3\text{PAr}$: Mean $13.63\%$ [95% CI: $12.87\%, 14.37\%$], $SE = 0.390\%$.
   - Team $eFG\%$: Mean $53.55\%$ [95% CI: $53.53\%, 53.58\%$].
2. **Permutation Hypothesis Testing ($P = 10,000$) & Benjamini-Hochberg FDR ($Q = 0.05$)**:
   - All 21 pairwise comparisons across the 6 functional archetypes reject the null hypothesis of equal efficiency at $Q = 0.05$, validating that functional roles represent statistically distinct performance populations.

---

# 10. Robustness & Subsample Sensitivity

- **Regulatory Era**: Post-2010 games are significantly more predictable ($ROC\text{-}AUC = 0.7876$ vs $0.6752$), matching the professionalization of tactical preparation.
- **Olympic Tournaments**: Highest predictability ($ROC\text{-}AUC = 0.8284$, $Brier = 0.1681$).
- **Blowout Sensitivity**: Excluding games with $|\text{margin}| \ge 35$ lowers MAE from $11.739 \rightarrow 10.319\text{ pts}$.

---

# 11. Automated Test Suite Status

- **Baseline Tests (MVP-0 to MVP-5)**: 88 passing
- **New Supervised Analytics Tests (MVP-6)**: 10 passing
- **Total Automated Test Suite**: **98 passed in 43.69s (100% Pass Rate)**

---

# 12. Deliverables & Artifact Manifest

```text
src/analytics/
  ├── mvp6_supervised_models.py      # Feature mart, 17 expanding folds, benchmark, calibration
  ├── mvp6_statistical_inference.py  # Bootstrap (B=5,000), Permutation (P=10,000), BH-FDR
  └── mvp6_visualizations.py         # 5 publication figures

data/04_analytics/
  ├── mvp6_pre_game_features.parquet # 1,145 canonical match rows, 21 columns
  ├── mvp6_fold_manifest.csv         # 17 temporal walk-forward fold definitions
  ├── mvp6_model_predictions.csv     # Out-of-sample predictions across 1,105 matches
  ├── mvp6_model_benchmark.csv       # Summary metric comparison table
  ├── mvp6_bootstrap_results.csv     # 95% bootstrap confidence intervals & standard errors
  └── mvp6_permutation_results.csv   # 21 permutation tests with FDR and Bonferroni p-values

reports/
  ├── mvp6_repository_audit.md       # Pre-implementation adversarial audit
  ├── mvp6_supervised_benchmark_report.md
  ├── mvp6_statistical_inference_report.md
  ├── mvp6_shap_interpretability_report.md
  └── mvp6_final_report.md

reports/figures/mvp6/
  ├── fig1_model_benchmark_comparison.png
  ├── fig2_calibration_reliability_diagrams.png
  ├── fig3_shap_global_feature_importance.png
  ├── fig4_shap_flagship_waterfall.png
  └── fig5_bootstrap_metric_confidence_intervals.png
```
