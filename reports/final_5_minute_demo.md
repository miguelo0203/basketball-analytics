# Final 5-Minute Portfolio Demonstration Script
## Real-Time Walkthrough for Technical & Tactical Job Interviews

**Scenario**: Beijing 2008 Olympic Final (Spain vs. USA)  
**Target Duration**: 5:00 Minutes  
**Tool**: Streamlit Analyst Workspace (`src/analytics/mvp10_analyst_workspace.py`)  

---

### [0:00–0:30] Who I Am & The Core Problem
- **Verbal**: *"Good morning. I am a basketball data analyst. The fundamental problem I built this project to solve is that modern basketball coaching staffs face an overload of noisy data—boxscores fluctuate wildly due to short tournament samples, and models often act as opaque black boxes claiming to replace human decision-making. I built an end-to-end analytical pipeline to demonstrate how an analyst turns raw data into clean, uncertainty-aware evidence that actively supports coaching staff decisions."*

---

### [0:30–1:15] The Data & Analytical Architecture
- **Screen Action**: Point to architecture diagram and DuckDB database in workspace sidebar.
- **Verbal**: *"The system runs on an immutable DuckDB relational warehouse covering 20 years of international basketball—18 tournaments, 1,145 games, and over 27,000 player performances. Crucially, the entire workspace enforces a strict anti-hindsight barrier: all features, rolling ratings, and models reflect information available strictly before tip-off. Ground-truth scores remain quarantined."*

---

### [1:15–3:15] Flagship Case Walkthrough: Beijing 2008 (Spain vs. USA)
- **Screen Action**: Select **Beijing 2008 Spain vs USA** $\rightarrow$ Click **Tab 1: 8-Layer Evidence Matrix**.
- **Verbal**: *"Let's look at one of the highest-leverage games in international history: Beijing 2008. Spain had just lost by 37 points to the USA 'Redeem Team' in group play. Before tip-off, our expanding walk-forward model favored USA at 73.2% with an 8.5-point expected deficit.*
*However, looking at our Four Factors decomposition, we found that USA's dominance was concentrated entirely in fast-break transition off turnovers (1.42 pts/poss). In half-court sets, Spain actually held a +4.2 Net Rating advantage.*
*Now look at our Contradiction Alert: our tactical film layer (Cohen's Kappa = 0.80) revealed that USA's interior bigs dropped deep into the paint to protect the rim, conceding open 15-foot elbow pockets to pick-and-pop perimeter trailers—which happened to be Spain's greatest frontcourt weapon with Pau and Marc Gasol."*

---

### [3:15–4:15] The Coaching Brief & Tactical Questions
- **Screen Action**: Click on **Tab 2: Coaching Decision-Support Brief**.
- **Verbal**: *"Rather than dictating tactics, our Coaching Brief delivered actionable inquiries: (1) Can we deploy a 2-3 matchup zone to break USA's transition flow? and (2) Can our bigs consistently punish USA's drop coverage by popping to the 3-point line?*
*In reality, Spain executed those exact adjustments, cutting the deficit to 4 points with 2 minutes left in a historic 118–107 battle."*

---

### [4:15–5:00] Limitations, Uncertainty & Translating to a Real Club
- **Screen Action**: Click on **Tab 4: Post-Game Process Review** $\rightarrow$ Show Bootstrap Confidence Intervals.
- **Verbal**: *"The 11-point margin fell squarely within our pre-game uncertainty interval. I am completely transparent about what data cannot do: models show historical associations, not guaranteed causal levers. In your organization, I would connect this exact pipeline to your live Second Spectrum optical tracking and league play-by-play feeds, giving your coaching staff faster, cleaner, and more objective decision support before every game."*
