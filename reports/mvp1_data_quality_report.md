# MVP-1 Data Quality & Validation Audit Report
## International Basketball Historical Analytics (2005–2025)

**Database**: `basketball_analytics.duckdb`  
**Audit Date**: 2026-08-19T00:07:01.142258  

---

## 1. Accounting Assertions Summary

| Rule Category | Assertion Formula / Rule | Evaluated Records | Failed Records | Status |
| :--- | :--- | :---: | :---: | :---: |
| **Ball Math** | $PTS = 2 \times 2PM + 3 \times 3PM + FTM$ | 2290 | 0 | **PASSED** |
| **Field Goals** | $FGM = 2PM + 3PM$ | 2290 | 0 | **PASSED** |
| **Minutes** | $(200 + 25 \times \text{OT}) \times 60$ s (Tolerance $\pm 60$s) | 2290 | 0 | **PASSED** |
| **Rebounds** | $TRB = ORB + DRB$ | 2290 | 0 | **PASSED** |
| **Four Factors Bounded** | $eFG\%, TOV\%, ORB\%, FTr \in [0.0, 1.0]$ | 2290 | 0 | **PASSED** |
| **Identity Resolution** | Canonical Player and Team Foreign Keys Valid | 2290 | 0 | **PASSED** |

---

## 2. Issues Distribution by Severity

- **CRITICAL (Blocks Ingestion)**: `0`
- **ERROR (Quarantine)**: `0`
- **WARNING (Flagged for Review)**: `0`
- **INFO**: `0`

---

## 3. Quarantine State

- Total Quarantined Records: `0`
- Unresolved Entities in Production: `0`
