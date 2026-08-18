# Public Claim Usage & Communication Governance Guide
## International Basketball Historical Analytics (2005–2025)

**Status**: Formally Certified Governance Guide  
**Application**: LinkedIn, Resume/CV, GitHub Documentation, Technical Presentations, and Job Interviews  

---

# 1. Claim-by-Claim Governance Matrix

```
+----------------------------------------------------------------------------------------------------+
| CATEGORY          | PHRASE / METRIC                 | GOVERNANCE CLASSIFICATION & COMPLIANT PHRASING|
+----------------------------------------------------------------------------------------------------+
| **Data Scope**    | "1,145 matches, 18 tournaments" | **SAFE TO SAY**: Exact verified count in      |
|                   |                                 | DuckDB relational warehouse (2005–2024).      |
+----------------------------------------------------------------------------------------------------+
| **Data Scope**    | "2005–2025 completed data"      | **DO NOT SAY**: 2025 is the current forward   |
|                   |                                 | cycle. Say "2005–2024 completed tournaments". |
+----------------------------------------------------------------------------------------------------+
| **Validation**    | "17-fold walk-forward ML"       | **SAFE TO SAY**: Evaluated 1,105 out-of-sample|
|                   |                                 | matches using expanding chronological folds.  |
+----------------------------------------------------------------------------------------------------+
| **Calibration**   | "Calibrated LightGBM ML"        | **SAFE TO SAY**: Brier = 0.1967, ECE = 0.0314 |
|                   |                                 | evaluated strictly out-of-sample.             |
+----------------------------------------------------------------------------------------------------+
| **Prediction**    | "Predicts games reliably"       | **DO NOT SAY**: Overclaims live certainty.    |
|                   |                                 | Say "Generates calibrated pre-game win odds". |
+----------------------------------------------------------------------------------------------------+
| **Simulations**   | "100% Top-4 Champion Hit Rate"  | **QUALIFY**: "Retrospectively placed the      |
|                   |                                 | champion in top 4 in 18/18 tourneys (N=18)".  |
+----------------------------------------------------------------------------------------------------+
| **Simulations**   | "72.2% Top-1 Champion Hit Rate" | **QUALIFY**: "13 of 18 historical tournaments |
|                   |                                 | saw the actual champion enter as simulated #1"|
+----------------------------------------------------------------------------------------------------+
| **Decisions**     | "80% vs 60% naive baseline"     | **QUALIFY**: "In an illustrative case series of|
|                   |                                 | 5 historical decisions, agreed with 4 of 5".  |
+----------------------------------------------------------------------------------------------------+
| **Decisions**     | "Proves superior decisions"     | **DO NOT SAY**: N=5 lacks statistical power.  |
|                   |                                 | Say "Demonstrates structured decision dossiers"|
+----------------------------------------------------------------------------------------------------+
| **Video Film**    | "Double-coded video reliability"| **SAFE TO SAY**: Evaluated 420 possessions,   |
|                   |                                 | achieving Cohen's Kappa = 0.80.               |
+----------------------------------------------------------------------------------------------------+
| **AI / Coaching** | "AI system that replaces coach" | **STRICTLY FORBIDDEN**: System provides       |
|                   |                                 | evidence to support human coaching decisions. |
+----------------------------------------------------------------------------------------------------+
| **Testing**       | "160 automated tests passing"   | **SAFE TO SAY**: 160 pytest tests passing     |
|                   |                                 | with 100% pass rate in ~117s.                 |
+----------------------------------------------------------------------------------------------------+
```
