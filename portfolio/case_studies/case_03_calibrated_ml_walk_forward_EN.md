[🇬🇧 English](case_03_calibrated_ml_walk_forward_EN.md) | [🇪🇸 Español](case_03_calibrated_ml_walk_forward.md)

# Case Study 03: Calibrated Machine Learning with Walk-Forward Validation

## 1. The Challenge
Predictive modeling in sports often suffers from future data leakage and overconfidence in probability estimates.

## 2. Methodology
- **Strict Walk-Forward Temporal Validation**: Training only on historical tournaments up to year $T-1$ to predict tournament $T$.
- **Probability Calibration**: Calibrating output probabilities to achieve reliable uncertainty estimates.
- **SHAP Feature Attribution**: Explaining individual prediction drivers through Four Factors feature importance.

## 3. Performance
Achieved an audited **Brier score of 0.1872** with robust probabilistic calibration.
