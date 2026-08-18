# 5–10 Minute Interactive Live Demonstration Script
## International Basketball Historical Analytics (2005–2025)

**Scenario**: Beijing 2008 Olympic Gold Medal Final: Spain vs. United States  
**Application**: Streamlit Analyst Decision Workspace (`src/analytics/mvp10_analyst_workspace.py`)  
**Target Duration**: 7–8 Minutes  

---

# 1. Demonstration Outline & Verbal Flow

```text
STEP 1: LAUNCH & ORIENTATION (Minute 0:00 - 1:00)
  ├── Command: streamlit run src/analytics/mvp10_analyst_workspace.py -- streamlit
  ├── Screen: Sidebar Match Selector -> Select "Beijing 2008 Olympic Final: Spain vs USA"
  └── Verbal: "Welcome. Today I will demonstrate how an analyst uses this workspace to prepare a coaching staff for a major tournament final without hindsight bias."

STEP 2: PRE-GAME CONTEXT & MODEL VIEW (Minute 1:00 - 2:30)
  ├── Screen: Top Header Cards & Calibrated Win Odds
  └── Verbal: "Notice that we are looking strictly at pre-game evidence. The LightGBM model, trained on previous tournaments, gives USA a 73.2% win probability (Expected Margin: -8.5 points). But let's look deeper into the 8-layer evidence matrix."

STEP 3: MULTI-LAYER EVIDENCE & CONTRADICTIONS (Minute 2:30 - 4:30)
  ├── Screen: Tab 1 (8-Layer Evidence Matrix) & Expand Contradiction Alerts
  └── Verbal: "Here the system surfaces a critical Tactical Contradiction: USA dominates overall transition scoring, but Spain holds a +4.2 Net Rating advantage in half-court paint efficiency. Our double-coded film confirms USA bigs struggle when trailing in drop coverage against pick-and-pop trailers (Pau and Marc Gasol)."

STEP 4: THE COACHING BRIEF (Minute 4:30 - 6:00)
  ├── Screen: Tab 2 (Coaching Brief)
  └── Verbal: "We don't tell the coach 'Play Pau Gasol 38 minutes.' We deliver structured questions: 'Can our secondary guards handle USA's aggressive hedge without live-ball turnovers?' and 'Are we prepared to deploy a 2-3 zone to break their transition pace?'"

STEP 5: OUTCOME REVEAL & POST-GAME PROCESS REVIEW (Minute 6:00 - 7:30)
  ├── Screen: Tab 4 (Post-Game Review) -> Click "Reveal Historical Outcome"
  └── Verbal: "Now we reveal the historical result: USA 118 - Spain 107. USA won by 11 points, precisely within our bootstrap uncertainty bounds. Spain deployed the 2-3 zone, punished USA's drop coverage, and had the ball within 4 points with 2 minutes remaining. The process successfully identified the critical inflection points before tip-off."
```
