# Prioritized Research Question Bank & Flagship Analyses
## International Basketball Historical Analytics (2005–2025)

---

## 1. Portfolio Prioritization Matrix

Rather than publishing 13 fragmented questions, the portfolio focuses on **4 Flagship Analyses (Tier 1)** that demonstrate end-to-end engineering, statistical rigor, and domain expertise, supported by strong secondary modules (Tier 2).

```
+-----------------------------------------------------------------------------+
| TIER 1: CORE FLAGSHIP ANALYSES (Mandatory Portfolio Assets)                 |
+-----------------------------------------------------------------------------+
| 1. Flagship A: Longitudinal Dominance & Generational Transition of Spain    |
| 2. Flagship B: Four Factors Decomposition of Championship Runs              |
| 3. Flagship C: Global Player Archetype Discovery via Unsupervised Learning  |
| 4. Flagship D: Quasi-Experimental Evaluation of the 2010 3-Point Arc Change |
+-----------------------------------------------------------------------------+
                                       |
+-----------------------------------------------------------------------------+
| TIER 2: STRONG OPTIONAL MODULES (Implemented as Feature Extensions)        |
+-----------------------------------------------------------------------------+
| - Pre-Game Scouting Engine & Automated Decision Support Reports             |
| - Leak-Free LOTO Predictive Win Probability & Margin Model                  |
| - Spatial Shot Charts & Expected Points per Shot (2019-2025 Sub-Dataset)    |
+-----------------------------------------------------------------------------+
                                       |
+-----------------------------------------------------------------------------+
| TIER 3: EXPLORATORY ANALYSES (Descriptive Context)                          |
+-----------------------------------------------------------------------------+
| - Stylistic Fingerprints by Coaching Era (Strictly Non-Causal)              |
| - 20-Year Evolution of Secular FIBA Pace and Spacing                        |
+-----------------------------------------------------------------------------+
                                       |
+-----------------------------------------------------------------------------+
| TIER 4: DEFERRED / EXCLUDED ANALYSES                                        |
+-----------------------------------------------------------------------------+
| - 5-Man Lineup Stint On/Off Analysis prior to 2012 (Lack of reliable PBP)   |
| - Difference-in-Differences Causal Claims on Rule Changes (No control group)|
+-----------------------------------------------------------------------------+
```

---

## 2. Flagship Analysis Specifications

### Flagship 1: Longitudinal Dominance & Generational Transition (Spain 2005–2025)
- **Research Question**: How did Spain maintain international dominance over 20 years, and at what specific tournament inflection points did usage and production transition across birth cohorts?
- **Unit of Analysis**: `fact_player_game` & `fact_team_game`.
- **Sample**: 145 games of Spain across 19 major tournaments.
- **Methodology**: Cohort aggregation (1980s Golden Generation vs. 1990s Transition vs. 2000s New Era), Herfindahl-Hirschman Usage Concentration Index, and Generalized Additive Models (GAM) modeling career $USG\%$ vs. $TS\%$ aging curves for Pau Gasol, Marc Gasol, Juan Carlos Navarro, and Ricky Rubio.
- **Key Output**: Cohort production streamgraphs and longitudinal aging curves with 95% bootstrap confidence bands.

### Flagship 2: Four Factors Decomposition of Championship Runs
- **Research Question**: What structural basketball dimensions explained the variance in Spain's Net Rating during Gold Medal tournaments (2006, 2009, 2011, 2015, 2019, 2022) compared to non-medal editions?
- **Unit of Analysis**: `fact_team_game` bilateral records.
- **Methodology**: Shapley value regression decomposition and dominance analysis partitioning Net Rating variance across $\Delta eFG\%$, $\Delta TOV\%$, $\Delta ORB\%$, and $\Delta FTr$.
- **Key Output**: Factor contribution waterfall charts demonstrating shifting team identities (e.g. interior scoring/rebounding in 2009/2011 vs. turnover creation/defensive discipline in 2019/2022).

### Flagship 3: Unsupervised Discovery of International Basketball Archetypes
- **Research Question**: What natural functional archetypes exist in international basketball across 2005–2025, and how did Spanish players project into this latent space over time?
- **Unit of Analysis**: `fact_player_tournament` for all international players ($N \approx 3,500$).
- **Methodology**: Gaussian Mixture Models & K-Means++ on 13 rate-based functional features (excluding raw height to avoid morphological bias), mathematical evaluation of $k \in [3, 10]$ via Silhouette, Calinski-Harabasz, Davies-Bouldin, and 100-iteration bootstrap stability.
- **Key Output**: Validated archetype profiles and longitudinal player trajectory maps in 2D latent space.

### Flagship 4: Interrupted Time Series Analysis of the 2010 3-Point Line Shift
- **Research Question**: Did the extension of the 3-point line from 6.25m to 6.75m in October 2010 create an immediate level drop in 3-point volume/efficiency or alter long-term tactical adoption rates?
- **Unit of Analysis**: `fact_team_game` for all 1,203 games across 19 tournaments.
- **Methodology**: Segmented linear regression (ITS) with team fixed effects, cluster-robust standard errors, and sensitivity checks excluding transition tournaments.
- **Key Output**: Quantified level and slope coefficients isolating regulatory impact from secular tactical evolution.
