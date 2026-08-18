# MVP-0 Automated Data Quality & Accounting Audit Report
## International Basketball Historical Analytics (2005–2025)

**Total Games Audited**: 559  
**Total Team-Game Records**: 1118  
**Critical Accounting Violations**: 0  

---

## 1. Accounting Assertions & Validation Summary

| Accounting Assertion | Mathematical Invariant | Total Checked | Violations | Action Taken |
| :--- | :--- | :---: | :---: | :---: |
| **Scoring Ball-Math** | $PTS = 2 \times 2PM + 3 \times 3PM + FTM$ | 1118 | **0** | Verified |
| **Field Goal Sums** | $FGM = 2PM + 3PM \land FGA = 2PA + 3PA$ | 1118 | **0** | Verified |
| **Rebound Accounting** | $TRB = ORB + DRB$ | 1118 | **0** | Verified |
| **Single-Team Minutes** | $\text{Seconds} = (200 + 25 \times \text{OT}) \times 60$ | 1118 | **0** | Verified |
| **Game Overtime Pace** | $\text{Pace}_{40} = 40 \times \frac{\text{Poss}}{\text{Duration}/60}$ | 559 | **0** | Verified |
| **Four Factors Bounding** | $eFG\%, TOV\%, ORB\% \in [0, 1]$ | 1118 | **0** | Verified |

---

## 2. Issues Logged

Total logged issues in `fact_validation_issue`: **0**.
