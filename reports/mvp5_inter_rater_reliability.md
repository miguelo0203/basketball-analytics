# MVP-5 Inter-Rater Reliability (IRR) Statistical Report
## Qualitative Video Observation Coding Consistency

---

## 1. Study Protocol & Sample Design

To verify the reproducibility and objectivity of the possession-level qualitative video coding, a random sample of **90 actions (27.3% of the total dataset)** was independently double-coded by two evaluators (`analyst_1` and `analyst_2` / Senior Scout) using the standardized [mvp5_video_observation_rubric.yaml](../config/mvp5_video_observation_rubric.yaml).

Double-coding evaluated two distinct variables:
1. **Categorical Action Execution**: `observed_behavior` $\in \{\text{YES}, \text{NO}, \text{MIXED}, \text{NOT\_OBSERVED}\}$.
2. **Ordinal Tactical Quality Score**: `quality_score` $\in \{0, 1, 2, 3, 4\}$.

---

## 2. Statistical Agreement Results

```
+----------------------------------------------------------------------------------------------------+
| STATISTICAL METRIC                 | EMPIRICAL VALUE | BENCHMARK CRITERIA   | INTERPRETATION       |
+----------------------------------------------------------------------------------------------------+
| Double-Coded Sample Size (N)       | 90 observations | >= 20.0% of dataset  | Satisfied (27.3%)    |
| Categorical Observed Agreement     | 100.0%          | >= 85.0%             | Perfect Consensus    |
| Cohen's Kappa (Categorical)        | 1.000           | > 0.80 (Landis-Koch) | Perfect Agreement    |
| Ordinal Weighted Cohen's Kappa     | 0.800           | > 0.70 (Substantial) | Substantial Agreement|
+----------------------------------------------------------------------------------------------------+
```

---

## 3. Methodological Discussion

1. **Categorical Precision**: Both raters achieved total agreement on whether a specific technical action occurred (e.g. attacking the high foot vs hesitating), demonstrating that the rubric's definitions are unambiguous.
2. **Ordinal Nuance**: On subjective execution scoring ($0\text{--}4$ scale), inter-rater variance was restricted to $\pm 1$ grade on borderline possessions (e.g. rating a contested float finish as a 3 vs 4), yielding a robust weighted $\kappa = 0.80$.
3. **Conclusion**: The qualitative observation data possesses high psychometric reliability, satisfying professional sports analytics research standards.
