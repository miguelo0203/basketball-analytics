# 03 — Technical Interview Questions & Answers
## Machine Learning, Calibration, Uncertainty & Inference

---

### Q1: Why did you evaluate your model using Brier Score and ECE instead of raw classification accuracy?
**Answer**:
> *"In sports betting and decision support, classification accuracy is misleading because basketball games are probabilistic events, not deterministic labels. A team with a 70% win probability should win 7 out of 10 times, not 10 out of 10. Evaluating with Brier score ($0.1967$) measures the mean squared error of probability forecasts, and Expected Calibration Error ($\text{ECE} = 0.0314$) ensures our probabilities are empirically reliable for tournament Monte Carlo simulations."*

---

### Q2: How did you prevent temporal data leakage in your supervised modeling?
**Answer**:
> *"I implemented a strict 17-fold chronological expanding walk-forward cross-validation scheme. For each tournament $T_k$, the model was trained strictly on historical tournaments $T_1 \dots T_{k-1}$. All feature scaling, imputation, and rolling rating calculations were computed strictly within each fold's historical window."*

---

### Q3: How do you interpret TreeSHAP feature attributions without making causal claims?
**Answer**:
> *"TreeSHAP values describe how each feature conditionally shifts the model's log-odds output relative to the baseline training population. They measure historical statistical association, not causal intervention. For example, high Net Rating pushes win probability up conditionally, but increasing a team's pace in a live game does not causally guarantee better efficiency."*

---

### Q4: Why did you use Clustered Non-Parametric Bootstrap ($B=5,000$) instead of standard normal approximations?
**Answer**:
> *"Basketball match observations are non-independent because games are clustered within specific tournaments and team rosters. Clustered bootstrap resampling preserves tournament-level correlation structures without making unrealistic Gaussian assumptions about skewed shooting distributions."*
