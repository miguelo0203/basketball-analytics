# MVP-3 Player Analytics & Metric Architecture
## Certified Multi-Dimensional Feature Specifications

--------------------------------------------------
1. DIMENSIONAL FEATURE DEFINITIONS
--------------------------------------------------

| Dimension Name | Underlying Formula / Component | Standardization (Z-Score) | Tactical Purpose |
| :--- | :--- | :--- | :--- |
| `dim_scoring_volume` | $PTS/40 = \frac{PTS \times 2400}{Seconds}$ | $\mu=0, \sigma=1$ | Measures scoring load per 40 minutes of game time |
| `dim_scoring_efficiency` | $TS\% = \frac{PTS}{2 \cdot (FGA + 0.44 \cdot FTA)}$ | $\mu=0, \sigma=1$ | Measures true shooting efficiency including free throws |
| `dim_perimeter_orientation` | $3\text{PAr} = \frac{3PA}{FGA}$ | $\mu=0, \sigma=1$ | Quantifies perimeter shot selection share |
| `dim_creation` | $AST\%_{\text{est}} = \frac{AST}{Games \times 18}$ | $\mu=0, \sigma=1$ | Measures playmaking frequency and shot creation |
| `dim_rebounding` | $ORB\%_{\text{est}} + DRB\%_{\text{est}}$ | $\mu=0, \sigma=1$ | Measures two-way glass dominance |
| `dim_defense` | $STL/40 + BLK/40$ | $\mu=0, \sigma=1$ | Quantifies defensive event disruption per 40 minutes |
| `dim_usage` | $USG\%_{\text{avg}}$ | $\mu=0, \sigma=1$ | Measures offensive possession termination responsibility |

--------------------------------------------------
2. ROLE HYPERPARAMETER EVALUATION
--------------------------------------------------

- **Model**: Hybrid K-Means++ with $K=6$.
- **Distance Metric**: Euclidean distance in 7-dimensional standardized feature space.
- **Silhouette Separability**: $0.248$ (optimal balance between mathematical compactness and tactical interpretability).
- **Inertia**: $14,120.4$.

--------------------------------------------------
3. COMPARABLES FORMULATION
--------------------------------------------------

$$\text{Distance}(p_i, p_j) = \sqrt{\sum_{d=1}^7 w_d \cdot (z_{id} - z_{jd})^2}$$

$$\text{Similarity}(p_i, p_j) = \frac{1}{1 + \frac{\text{Distance}(p_i, p_j)}{\sqrt{\sum w_d}}}$$

Weights: Scoring Volume ($1.2$), Creation ($1.2$), Perimeter Orientation ($1.0$), True Shooting ($1.0$), Rebounding ($1.0$), Defensive Activity ($1.0$), Usage ($1.0$).
