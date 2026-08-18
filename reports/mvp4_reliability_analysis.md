# MVP-4 Uncertainty & Sample-Size Reliability Framework
## International Basketball Historical Analytics (2005–2025)

---

## 1. The Uncertainty Principle in Tournament Analytics

In short international competitions ($5\text{--}11$ games), sampling variance is the single largest threat to valid player evaluation. A player who converts $10\text{ of }18$ three-pointers ($55.6\%$) over 4 games possesses a $95\%$ confidence interval spanning $[33\%, 78\%]$.

To prevent front offices from chasing short-sample variance, MVP-4 enforces an explicit **Sample-Size Reliability Architecture**.

---

## 2. Reliability Tier Definitions & Governing Criteria

```
+---------------------------------------------------------------------------------------------------+
| TIER                    | GOVERNING CRITERIA               | STATISTICAL UNCERTAINTY              |
+---------------------------------------------------------------------------------------------------+
| **HIGH RELIABILITY**    | Total Minutes >= 150.0           | Standard error of rate estimates < 8%|
|                         | Games Played >= 6                | Profile is structurally representative|
|                         |                                  | of rotation capability.              |
+---------------------------------------------------------------------------------------------------+
| **MODERATE RELIABILITY**| Total Minutes >= 90.0            | Standard error of rate estimates <15%|
|                         | Games Played >= 4                | High tactical signal; requires       |
|                         |                                  | moderate sample caution.             |
+---------------------------------------------------------------------------------------------------+
| **LIMITED SAMPLE**      | Total Minutes >= 40.0            | Standard error > 20%                 |
|                         | Games Played >= 3                | Rate metrics possess elevated noise; |
|                         |                                  | shortlisted with explicit warning.   |
+---------------------------------------------------------------------------------------------------+
| **INSUFFICIENT SAMPLE** | Total Minutes < 40.0             | Excessive noise                      |
|                         | OR Games Played < 3              | Disqualified from recruitment pool.  |
+---------------------------------------------------------------------------------------------------+
```

---

## 3. Integration into Shortlisting Multiplier

Rather than hard-filtering out players with $MIN = 70$, our multi-stage workflow applies a **Reliability Scaling Multiplier** to the Tactical Fit Index:
- `HIGH RELIABILITY`: Multiplier = `1.05` (Rewarded for high-sample tournament consistency)
- `MODERATE RELIABILITY`: Multiplier = `1.00` (Neutral baseline)
- `LIMITED SAMPLE`: Multiplier = `0.92` (Penalized for estimation variance)

This guarantees that a candidate with $200\text{ minutes}$ of consistent $58\%\text{ TS}$ outranks a candidate with $45\text{ minutes}$ of noisy $65\%\text{ TS}$.
