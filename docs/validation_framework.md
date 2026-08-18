# Data Quality & Automated Validation Framework
## International Basketball Historical Analytics (2005–2025)

---

## 1. Quality Assurance Lifecycle

Every ingested record passes through a validation gate before promotion to `fact_*` production tables.

```
+---------------+      Pass Validation      +------------------+
| Staging Table | ------------------------> | Production Table |
+---------------+                           +------------------+
        |                                             |
        | Fail Critical / Error Checks                | Logged Issues
        v                                             v
+------------------+                        +-----------------------+
| Quarantine Table |                        | fact_validation_issue |
+------------------+                        +-----------------------+
```

---

## 2. QA Flags & Severity Matrix

| QA Flag Code | Severity | Accounting / Business Rule Description | Action on Failure |
| :--- | :---: | :--- | :--- |
| `BALL_MATH_MISMATCH` | **CRITICAL** | $PTS \ne 2 \times 2PM + 3 \times 3PM + FTM$ or $FGM \ne 2PM + 3PM$. | **Quarantine record**. Block production insertion. |
| `MINUTES_ACCOUNTING_MISMATCH` | **CRITICAL** | Team player-seconds $\ne (200 + 25 \times \text{OT}) \times 60 \pm 60$ seconds. | **Quarantine record**. |
| `SCORE_CONSISTENCY_MISMATCH` | **CRITICAL** | Sum of player points $\ne$ Team final points. | **Quarantine record**. |
| `IDENTITY_UNRESOLVED` | **ERROR** | Player name cannot be mapped to a canonical person record. | Route to `player_identity_review.csv`. |
| `SOURCE_CONFLICT` | **WARNING** | Primary and secondary sources disagree on an observable metric. | Retain primary; log discrepancy in `fact_validation_issue`. |
| `REBOUND_LEAK` | **WARNING** | $DRB_{\text{Team A}} + ORB_{\text{Team B}} > TRB_{\text{Game}}$. | Retain record; flag potential uncredited team rebound. |
| `PIR_DISCREPANCY` | **INFO** | Calculated PIR differs from Official FIBA PIR due to missing Fouls Drawn. | Store both `official_pir` and `computed_game_score`. |
| `POSSESSION_FALLBACK` | **INFO** | Bilateral possession estimate used due to absence of PBP tracking. | Record `possession_method = 'EST_BILATERAL'`. |

---

## 3. Minute & Overtime Validation Rules

- **Single Team Regulation (40 min)**:
  $$\text{Expected Seconds} = 200 \times 60 = 12,000 \text{ seconds}$$
- **Single Team with $N$ Overtimes (5 min each)**:
  $$\text{Expected Seconds} = (200 + 25 \times N) \times 60 \text{ seconds}$$
  - 1 OT (45 min game): $225 \times 60 = 13,500$ seconds.
  - 2 OT (50 min game): $250 \times 60 = 15,000$ seconds.
- **Tolerances**:
  - Exact mm:ss data (2011–2025): $\pm 0$ seconds.
  - Legacy integer-rounded data (2005–2010): $\pm 60$ seconds tolerance permitted.
