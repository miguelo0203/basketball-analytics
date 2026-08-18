# Player Role Discovery & Functional Archetype Report
## MVP-3: International Basketball Historical Analytics (2005–2025)

**Sample Size**: $N = 3767$ qualified player-tournament campaigns ($MIN \ge 40$, $G \ge 3$) across 18 tournaments  
**Methodology**: Hybrid Domain-Informed K-Means++ Clustering on 7 Standardized Dimensions  

---

## 1. Hyperparameter Optimization & Diagnostics

| Clusters ($K$) | Silhouette Score | Davies-Bouldin Index | Total Inertia |
| :---: | :---: | :---: | :---: |
| **K = 4** | 0.6249 | 0.5714 | 6143.44 |
| **K = 5** | 0.6720 | 0.6062 | 3617.57 |
| **K = 6** | 0.7035 | 0.5493 | 2204.28 |
| **K = 7** | 0.7297 | 0.3664 | 1078.96 |
| **K = 8** | 0.7441 | 0.3319 | 747.98 |

> [!NOTE]
> $K = 6$ was selected as the optimal trade-off between mathematical separability (Silhouette = 0.704) and tactical basketball interpretability.

---

## 2. Discovered Functional Archetypes & Distribution

| Functional Role Name | Player Campaigns ($N$) | % of Qualified Sample | Avg Height (cm) | Top Statistical Archetype Traits |
| :--- | :---: | :---: | :---: | :--- |
| **Primary Initiator / Floor General** | 364 | 9.7% | 196.59 cm | Elite creation (AST% ~35%), high USG%, pick-and-roll orchestrator |
| **Two-Way Scoring Wing / Slasher** | 1381 | 36.7% | 200.96 cm | High scoring volume, defensive event creation (STL40), multi-level scoring |
| **Perimeter Movement Shooter / Spacer** | 364 | 9.7% | 196.51 cm | High 3PAr (>55%), elite true shooting, low ball dominance |
| **Stretch Big / Pick-and-Pop Forward** | 566 | 15.0% | 200.61 cm | Perimeter shooting big, floor spacing for drive-and-kick |
| **Low-Block Anchor / Interior Scorer** | 728 | 19.3% | 196.61 cm | Low-post scoring, offensive rebounding, high free throw generation |
| **Rim Protector / Roll Threat & Anchor** | 364 | 9.7% | 198.92 cm | Elite rim defense (BLK40), defensive glass dominance, vertical roll threat |

---

## 3. Mean Role Statistical Profiles

```
                                      pts_per_40  ts_pct  three_point_rate  ast_pct_est  orb_pct_est  drb_pct_est  stl_per_40  blk_per_40  usg_pct_avg  height_cm_at_tournament
role_name                                                                                                                                                                      
Low-Block Anchor / Interior Scorer     16.379999    0.64              0.11         0.08         0.25         0.22        0.76        0.83         0.32                   196.61
Perimeter Movement Shooter / Spacer    19.070000    0.47              0.93         0.17         0.09         0.08        1.42        0.00         0.50                   196.51
Primary Initiator / Floor General      30.260000    0.67              0.18         0.50         0.09         0.08        1.32        0.00         0.56                   196.59
Rim Protector / Roll Threat & Anchor   13.130000    0.68              0.01         0.05         0.91         0.52        0.00        1.80         0.24                   198.92
Stretch Big / Pick-and-Pop Forward      6.650000    0.36              0.19         0.00         0.00         0.02        0.00        0.00         0.13                   200.61
Two-Way Scoring Wing / Slasher          7.780000    0.99              0.00         0.00         0.00         0.02        0.00        0.00         0.09                   200.96
```
