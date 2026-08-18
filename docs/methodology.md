# Statistical & Analytical Methodology Guide
## International Basketball Historical Analytics (2005–2025)

---

## 1. Multiple Comparisons & Inference Controls

To avoid p-value fishing across exploratory questions, analyses are strictly stratified:
- **Primary Analyses**: Pre-registered hypotheses with Family-Wise Error Rate (FWER) control via Holm-Bonferroni.
- **Secondary / Exploratory Analyses**: False Discovery Rate (FDR) control via Benjamini-Hochberg ($\alpha = 0.05$).
- **Reporting Standard**: All estimates report **effect size**, **standard error**, and **95% bootstrap confidence intervals** alongside p-values.

---

## 2. 2010 Three-Point Rule Evaluation (Interrupted Time Series)

### Methodological Justification: Why DiD Fails
A Difference-in-Differences (DiD) design requires an unexposed parallel control group. Because FIBA implemented the 6.75m line change globally for all member federations simultaneously in October 2010, no unexposed international control group exists. Comparing FIBA to the NBA is invalid due to divergent court dimensions (7.24m), 48-minute durations, and non-overlapping player populations.

### Interrupted Time Series (ITS) Specification
We estimate a segmented quasi-experimental time-series model on team-game observations across 19 tournaments:

$$3\text{PAr}_{it} = \beta_0 + \beta_1 \cdot \text{TournamentTime}_t + \beta_2 \cdot \text{Rule2010}_t + \beta_3 \cdot (\text{TournamentTime}_t \times \text{Rule2010}_t) + \mathbf{\Gamma} \mathbf{X}_{it} + \epsilon_{it}$$

- $\beta_1$: Baseline secular trend in 3-point attempt rate prior to 2010.
- $\beta_2$: Immediate structural level change (jump/drop) at the transition boundary (EuroBasket 2011).
- $\beta_3$: Change in slope (post-intervention secular acceleration).
- $\mathbf{X}_{it}$: Covariates (Team talent tier, opponent defensive rating, tournament stage).
- Standard Errors: Cluster-robust at the team and tournament levels with Newey-West autocorrelation correction.

---

## 3. Unsupervised Player Archetype Discovery (Clustering)

### 3.1 Feature Space Engineering & Collinearity Elimination
To prevent trivial positional clustering (Bigs vs Guards) and compositional redundancy:
1. **Exclude raw physical/demographic attributes**: `height_cm`, `age`, `nationality`, `position_label` are excluded from the clustering space. They are evaluated *post-clustering* to describe discovered archetypes.
2. **Eliminate volume collinearity**: $PTS/40$, $FGA/40$, and $USG\%$ measure overlapping volume phenomena. We retain a clean vector of normalized behavioral and rate metrics:
   $$\vec{x} = [USG\%, TS\%, 3PAr, 3P\%, 2P\%, FTr, ORB\%_{\text{est}}, DRB\%_{\text{est}}, AST\%_{\text{est}}, TOV\%_{\text{est}}, STL_{40}, BLK_{40}, PF_{40}]$$

### 3.2 Filtering & Exposure Thresholds
- Baseline threshold: $Poss_{\text{on\_court}} \ge 50$ and $MIN \ge 40$ in tournament.
- Sensitivity audit: Stability evaluated against $MIN \ge 60$ and $MIN \ge 80$ thresholds.

### 3.3 Mathematical Evaluation of $k$
Cluster count $k \in [3, 10]$ is determined using:
- **Silhouette Coefficient**: Maximizing intra-cluster cohesion and inter-cluster separation.
- **Calinski-Harabasz Index**: Maximizing between-cluster variance relative to within-cluster variance.
- **Davies-Bouldin Index**: Minimizing cluster similarity ratios.
- **Gaussian Mixture Model (GMM) BIC**: Minimizing Bayesian Information Criterion.
- **Bootstrap Stability**: 100 bootstrap resamples evaluating cluster assignment consistency via Adjusted Rand Index (ARI).
- **UMAP Disclosure**: UMAP is strictly used for 2D visualization with fixed random seeds; cluster validity is never inferred from UMAP geometry.

---

## 4. Longitudinal Player Careers & Aging Curves

For high-volume players (Pau Gasol, Marc Gasol, Juan Carlos Navarro, Ricky Rubio):
- We separate **calendar age** from **international career phase** (Early, Peak, Veteran).
- We fit Generalized Additive Models (GAM) and cubic splines with shrinkage to model $USG\%$ vs. $TS\%$ trade-offs over time.
- All curves display 95% bootstrap confidence bands to reflect small tournament sample sizes ($N = 5 \dots 11$ games/year).

---

## 5. Team Style & Coaching Era Analysis

- Coaching tenures (Pepu Hernández, Aíto García Reneses, Sergio Scariolo, Juan Antonio Orenga) are analyzed as **descriptive stylistic fingerprints** (Pace, 3PAr, Turnover creation, Rotation depth).
- **No Causal Claims**: We explicitly forbid attributing team success directly to the coach without controlling for player talent and roster composition.

---

## 6. Predictive Modeling & Leakage Prevention

### 6.1 Temporal Isolation `available_as_of`
To predict game $G$, all feature transformations, imputation, scaling, and rolling aggregations must use data strictly timestamped prior to game $G$'s tip-off:

$$\mathbf{X}_{G} = f(\{g \in \text{Games} \mid \text{timestamp}(g) < \text{timestamp}(G)\})$$

### 6.2 Leave-One-Tournament-Out (LOTO) Cross-Validation
- Full tournament editions are held out as atomic test sets.
- Feature scaling and model tuning are executed inside the training folds.

### 6.3 Evaluation & Targets
- **Win Probability**: Calibrated Logistic Regression, GBDT evaluated with **Brier Score**, **Log-Loss**, and calibration curves.
- **Point Margin**: Ridge Regression and LightGBM evaluated with **MAE** and **RMSE**.
- **Baselines**: Compared against 50/50 coin-flip, Higher-Ranked baseline, and Simple Elo baseline.
- **SHAP Interpretation**: SHAP values are presented as model feature contributions, never as causal mechanisms.
