# Professional Basketball Analyst Operational Workflow
## International Basketball Historical Analytics (2005–2025)

**Status**: Certified Operational Workflow Specification  
**Architecture**: 12-Step Analyst Protocol & 5-Point Operational Decision Horizon  

---

# 1. The 12-Step Systematic Analyst Protocol

```
+----------------------------------------------------------------------------------------------------+
| STEP # | PROTOCOL ACTION            | OPERATIONAL FOCUS & METHODOLOGY                              |
+----------------------------------------------------------------------------------------------------+
| **1**  | **Define the Question**    | Identify the exact tactical, rotational, or strategic decision|
| **2**  | **Establish Context**      | Verify tournament stage, opponent strength, rest days, venue |
| **3**  | **Audit Data Quality**     | Check boxscore provenance, possessions, and zero future leakage|
| **4**  | **Review Stats Signal**    | Analyze multi-tournament Net Ratings and Four Factors metrics|
| **5**  | **Review Tactical Film**   | Examine double-coded video film on P&R drop and recovery speed|
| **6**  | **Query Calibrated Model** | Inspect out-of-sample win probability (LightGBM ECE = 0.0314)|
| **7**  | **Check Uncertainty**      | Review Clustered Bootstrap 95% CIs and sample exposure tiers |
| **8**  | **Surface Contradictions** | Audit conflicts between quantitative models and video film   |
| **9**  | **Formulate Questions**    | Translate contradictions into actionable coaching inquiries  |
| **10** | **Deliver Coaching Brief** | Hand off concise pre-game brief prior to coaching walk-through|
| **11** | **Coach Makes Decision**   | Human coaching staff exercises tactical authority            |
| **12** | **Post-Game Process Review**| Audit outcome deviations and evaluate uncertainty calibration|
+----------------------------------------------------------------------------------------------------+
```

---

# 2. The 5-Point Operational Decision Timeline

```text
T-30 DAYS (Pre-Tournament)
  ├── Available Data: Multi-tournament historical Net Ratings & Four Factors baselines.
  ├── Model Output: Initial tournament simulations & medal round reach odds.
  └── Analyst Focus: Roster archetype coverage audit & positional depth assessment.

T-7 DAYS (Tournament Eve)
  ├── Available Data: Final 12-man roster confirmation & warm-up game stats.
  ├── Model Output: Refined calibrated pre-game win probabilities (ECE = 0.0314).
  └── Analyst Focus: Opponent scouting profile & creator gravity audit.

T-1 DAY (Match Eve)
  ├── Available Data: In-tournament group stage form, recent point margins & rest days.
  ├── Model Output: Matchup win probability ($P(\text{Win})$) & expected margin.
  └── Analyst Focus: Tactical film review on opponent P&R drop coverage & transition defense.

GAME DAY (Pre-Tipoff)
  ├── Available Data: Starting lineups, referee profiles & shooting variance bounds.
  ├── Model Output: Expected possession battle & key tactical mismatch alerts.
  └── Analyst Focus: Delivery of concise Coaching Staff Brief (Executive Summary + Questions).

POST-GAME (Review & Process Audit)
  ├── Available Data: Boxscore, possession efficiency, rotation deltas & actual outcome.
  ├── Model Output: Deviation audit against pre-game model expectation.
  └── Analyst Focus: Evaluating process quality, uncertainty calibration & film insights.
```

---

# 3. Demonstrated Capabilities vs Real-Club Requirements

```
+----------------------------------------------------------------------------------------------------+
| DEMONSTRATED IN THIS REPOSITORY             | WOULD REQUIRE LIVE CLUB ENVIRONMENT / APIS           |
+----------------------------------------------------------------------------------------------------+
| • Historical multi-tournament feature stores| • Live optical tracking telemetry (Second Spectrum)  |
| • Expanding walk-forward machine learning   | • Biometric and GPS wearable load-monitoring         |
| • Probability calibration & bootstrap CIs   | • Real-time in-game quarter-by-quarter adjustments   |
| • Structured qualitative film coding protocol| • Team internal video tagging database integration  |
| • Automated coaching brief generation       | • Live transfer contract and market pricing feeds    |
+----------------------------------------------------------------------------------------------------+
```
