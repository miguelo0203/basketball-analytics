# MVP-4 Candidate Universe Audit & Eligibility Report
## International Basketball Historical Analytics (2005–2025)

**Warehouse Source**: `data/03_validated/basketball_analytics.duckdb`  
**Data Mart**: `data/04_analytics/mart_player_roles.parquet`  
**Audit Date**: 2026-08-18  

---

## 1. High-Level Universe Cardinality

| Category | Campaign Count | % of Total Database | Operational Status |
| :--- | :---: | :---: | :--- |
| **Total Ingested Campaigns** | **4,350** | 100.0% | Complete tournament roster universe (18 competitions) |
| **Eligible Qualified Universe** ($MIN \ge 40, G \ge 3$) | **3,767** | **86.6%** | **Admitted to Analytical Screening** |
| **Excluded Campaigns** ($MIN < 40$ or $G < 3$) | **583** | **13.4%** | **Excluded from Recruitment Pool** |

---

## 2. Breakdown of Excluded Campaigns

Exclusions are governed by strict, transparent sample-size rules to eliminate noisy statistical artifacts:

```
+---------------------------------------------------------------------------------------------------+
| EXCLUSION REASON                      | COUNT | REASON FOR EXCLUSION                              |
+---------------------------------------------------------------------------------------------------+
| Low Minutes (< 40.0 Total Minutes)   |   583 | Insufficient sample; rate metrics possess         |
|                                       |       | excessive sampling variance.                      |
| Low Games (< 3 Tournament Games)     |     0 | All players with >= 40 mins had at least 3 games. |
+---------------------------------------------------------------------------------------------------+
```

---

## 3. Reliability Distribution of the Eligible Pool ($N = 3,767$)

```
+---------------------------------------------------------------------------------------------------+
| RELIABILITY TIER        | CRITERIA                       | COUNT | % OF ELIGIBLE | SAMPLE POWER  |
+---------------------------------------------------------------------------------------------------+
| HIGH RELIABILITY        | MIN >= 150.0 AND Games >= 6    | 1,412 |         37.5% | Very High     |
| MODERATE RELIABILITY    | MIN >= 90.0 AND Games >= 4     | 1,498 |         39.8% | High          |
| LIMITED SAMPLE          | MIN >= 40.0 AND Games >= 3     |   857 |         22.7% | Moderate      |
+---------------------------------------------------------------------------------------------------+
```

> [!NOTE]
> 77.3% of the eligible pool ($2,910$ player campaigns) falls into High or Moderate Reliability tiers, providing high empirical power for scouting decision support.
