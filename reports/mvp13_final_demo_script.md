# Master 5-Minute Live Demonstration Script
## International Basketball Historical Analytics (2005–2025)

**Scenario**: Beijing 2008 Olympic Gold Medal Game: Spain vs. USA  
**Target Duration**: Exactly 5 Minutes  
**Tool**: Streamlit Analyst Decision Workspace (`src/analytics/mvp10_analyst_workspace.py`)  

---

### [0:00–0:30] Introduction & The Real-World Problem
- **Verbal**: *"Good morning. The fundamental problem in basketball analytics is not generating numbers; it is turning complex, noisy match data into clean, uncertainty-aware evidence that helps a coaching staff make better tactical decisions before tip-off. Today I will demonstrate our operational analyst workspace using one of the highest-leverage matchups in international basketball history: the Beijing 2008 Olympic Final between Spain and the USA 'Redeem Team'."*

---

### [0:30–1:15] Technical Data Architecture
- **Screen Action**: Point to architecture and data provenance in sidebar.
- **Verbal**: *"The entire system is powered by an immutable DuckDB relational warehouse spanning 18 international tournaments, 1,145 games, and over 27,000 player performances. Crucially, the workspace enforces a strict anti-hindsight barrier: all features, rolling ratings, and models reflect information available strictly before tip-off. Ground-truth scores and post-game statistics are completely quarantined."*

---

### [1:15–2:15] Multi-Layer Team Evidence Profile
- **Screen Action**: Click on **Tab 1: 8-Layer Evidence Matrix**.
- **Verbal**: *"Before tip-off, our expanding walk-forward LightGBM model, calibrated to an Expected Calibration Error of 0.0314, assigns USA a 73.2% win probability with an expected margin of -8.5 points. Looking at the Four Factors, USA dominates fast-break transition scoring off turnovers. However, Spain holds a +4.2 Net Rating advantage in half-court paint scoring and offensive rebounding."*

---

### [2:15–3:15] Tactical Contradiction Detection
- **Screen Action**: Expand the red **Tactical Contradiction Alert** banner.
- **Verbal**: *"Rather than hiding discrepancies, our Contradiction Engine highlights a vital conflict: USA's overall margin suggests heavy superiority, but our double-coded video film (Cohen's Kappa = 0.80) reveals that USA's interior bigs struggle when trailing in drop coverage against pick-and-pop perimeter trailers—which happens to be Spain's greatest frontcourt strength with Pau and Marc Gasol."*

---

### [3:15–4:15] The Coaching Decision-Support Brief
- **Screen Action**: Click on **Tab 2: Coaching Decision-Support Brief**.
- **Verbal**: *"As an analyst, I don't tell the coach 'Play 2-3 zone.' I hand off a structured 2-page brief with actionable inquiries: (1) Can our secondary ball-handlers attack USA's aggressive hedge without committing live-ball turnovers? and (2) Are we prepared to deploy a 2-3 zone to break their fast-break rhythm? This respects the coach's tactical authority while providing clean evidence."*

---

### [4:15–5:00] Anti-Hindsight Outcome Reveal & Process Review
- **Screen Action**: Click on **Tab 4: Post-Game Process Review** $\rightarrow$ Click **"Reveal Historical Match Outcome"**.
- **Verbal**: *"Now we reveal the actual outcome: USA 118 - Spain 107. USA won by 11 points, precisely within our bootstrap 95% uncertainty interval. Spain deployed the 2-3 matchup zone, punished USA's drop coverage with pick-and-pop trailers, and had the ball within 4 points with 2 minutes left. The value of the analysis was not predicting the winner—it was identifying the exact tactical levers and risks before the game was played."*
