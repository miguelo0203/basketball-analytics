# MVP-10 Analyst Decision Workspace Architecture & Design Specification
## International Basketball Historical Analytics (2005–2025)

**Status**: Certified Workspace Design  
**Interface Modes**: Interactive Streamlit Web UI & CLI Programmatic Engine  
**Evidence Architecture**: 8-Layer Multi-Modal Matrix  
**Anti-Hindsight Guarantee**: Strict Pre-Game / Post-Game Outcome Isolation  

---

# 1. System Objective & Operational Philosophy

The **MVP-10 Analyst Decision Workspace** operationalizes the entire 20-year research stack (MVP-0 through MVP-9) into a structured decision-support environment for basketball coaching staffs and sporting directors.

```
+----------------------------------------------------------------------------------------------------+
|                               MVP-10 WORKSPACE INFORMATION FLOW                                    |
+----------------------------------------------------------------------------------------------------+
| 1. RAW DATA           | Official FIBA boxscores, play-by-play events, possession counts            |
| 2. CONTEXT            | Pace adjustments, opponent quality, tournament stage, rest days            |
| 3. EVIDENCE MATRIX    | 8-Layer structured metrics (NetRtg, Four Factors, Roles, Film, ML, Sim, CIs)|
| 4. ANALYTICAL SIGNAL  | Calibrated win probabilities (ECE = 0.0314), Net Rating disparities        |
| 5. UNCERTAINTY        | Clustered Bootstrap 95% CIs, sample size tiering, variance bounds          |
| 6. CONTRADICTIONS     | Automated surfacing of stats vs film conflicts and form vs prior divergence|
| 7. COACHING BRIEF     | Actionable tactical brief: Executive summary, film notes, staff questions  |
| 8. DECISION AUTHORITY | Final tactical and roster decision exercised exclusively by the Head Coach |
+----------------------------------------------------------------------------------------------------+
```

---

# 2. The 8-Layer Evidence Matrix Specification

Every match or decision scenario evaluated in the workspace generates a machine-readable evidence matrix:

```
+----------------------------------------------------------------------------------------------------+
| LAYER # | EVIDENCE LAYER NAME        | SOURCE DATASET / MART              | OUTPUT METRICS / SIGNAL|
+----------------------------------------------------------------------------------------------------+
| **1**   | **Historical Performance** | `mart_team_game_analytics.parquet` | Prior 3-Tourney NetRtg |
| **2**   | **Tournament Form**        | `fact_game` group stage records    | In-Tournament Net Margin|
| **3**   | **Four Factors Efficiency**| `mart_team_game_analytics.parquet` | eFG%, TOV%, ORB%, FTR  |
| **4**   | **Functional Archetypes**  | `mart_player_roles.parquet`        | 6 K-Means++ Role Counts|
| **5**   | **Tactical Film Evidence** | `mvp5_video_observations.csv`      | P&R reads (κ = 0.80)   |
| **6**   | **Predictive ML Output**   | `mvp6_model_predictions.csv`       | Calibrated P(Win A)    |
| **7**   | **Tournament Simulation**  | `mvp7_tournament_simulations`      | 10,000 Monte Carlo Odds|
| **8**   | **Statistical Uncertainty**| `mvp6_bootstrap_results.csv`       | Bootstrap 95% CIs      |
+----------------------------------------------------------------------------------------------------+
```

---

# 3. Dedicated Contradiction Engine

The workspace incorporates dedicated heuristics to identify and surface contradictions rather than suppressing mixed evidence:
1. **Prior vs Form Conflict**: Triggered when a long-term model favorite ($P > 60\%$) exhibits deteriorating in-tournament group-stage point margins ($\Delta \text{Form} < -4.0$).
2. **Stats vs Film Mismatch**: Triggered when high boxscore scoring efficiency ($TS\% > 60\%$) masks poor defensive drop coverage containment on double-coded video film.
3. **Lineup Spacing Deficit**: Triggered when roster composition accumulates three ball-dominant primary creators without sufficient movement shooters.
