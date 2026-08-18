# 10-Minute Live Analyst Demonstration Guide
## Real-Time Analytical Walkthrough for Technical & Tactical Interviews

**Format**: Interactive Live Screen-Share & Code / Dashboard Walkthrough  
**Target Duration**: 10:00 Minutes  
**Demonstrator Stance**: Team Data Analyst briefing Head Coach & Sporting Director  

---

### [0:00–1:00] The Tactical Question & Context
- **Verbal**: *"Good morning, Coach. Today I am going to investigate a tactical question relevant to our tournament preparation: How has our offensive creation profile evolved over the past decade, what happens when we face high-pressure perimeter drop coverage, and how can we use our multi-layer evidence pipeline to prepare for tonight's game?"*
- **Visual**: Open terminal / Streamlit Analyst Workspace header.

---

### [1:00–3:00] Data Architecture & What We Are Measuring
- **Verbal**: *"To answer this without small-sample bias, our system pulls from a certified DuckDB relational warehouse covering 1,145 international matches. We don't just look at points per game; we decompose performance into Dean Oliver's Four Factors—Effective Field Goal %, Turnover %, Offensive Rebound %, and Free Throw Rate—adjusted for possession pace across 4,350 player campaigns."*
- **Visual**: Show DuckDB schema table relationships and Parquet feature store.

---

### [3:00–6:00] Executing the Analysis & Surfacing Contradictions
- **Verbal**: *"Let's examine our feature store. Notice that in our modern era, our 3-point attempt rate climbed to 38.6%, while our free throw rate dropped by 8.4%. When we look at our 6 functional archetypes via K-Means++, we see our creation has centralized around Primary Initiators (Lorenzo Brown, Ricky Rubio) who carry a 48.2% assist share.*
*Now look at our Contradiction Engine: Our calibrated machine learning model assigns a strong statistical prior, but our double-coded film layer (Cohen's Kappa = 0.80) reveals a hidden vulnerability: when opponents play aggressive hedge against our initiator, our secondary wings turn the ball over on middle kick-outs."*
- **Visual**: Navigate through **Tab 1: 8-Layer Evidence Matrix** and expand **Tactical Contradiction Alert**.

---

### [6:00–8:00] Translating Numbers into Basketball Meaning
- **Verbal**: *"What does this mean on the court? It means our offense is no longer an inside-out post-up machine that guarantees 25 free throws a night like in the Gasol era. We are a perimeter spacing team that relies on high pick-and-roll creation. If the opponent center plays deep drop, our bigs must pick-and-pop to create driving lanes. If they switch, our creator must attack the mismatch downhill."*
- **Visual**: Display shot chart distribution and P&R drop coverage film notes in **Tab 2: Coaching Brief**.

---

### [8:00–9:00] Addressing Uncertainty & Alternative Explanations
- **Verbal**: *"We must be honest about our limitations. Our modern sample is 66 tournament games. In a 9-game tournament, a cold shooting night (e.g. 5-for-26 from three) can drop our eFG% by 12 points without any change in our underlying shot quality. Furthermore, our model describes historical conditional correlations—it does not prove causality. The coaching staff's in-game adjustments remain paramount."*
- **Visual**: Show non-parametric bootstrap confidence intervals and calibration curves.

---

### [9:00–10:00] Final 60-Second Coaching Takeaway
- **Verbal**: *"To summarize for tonight's pre-game meeting:*
*1. Expect opponent to drop their center deep to protect the rim and bait our mid-range pullups.*
*2. Our tactical key is having our bigs pop to the 3-point arc to force their rim protector to vacate the paint.*
*3. When our 3-point shots aren't falling, our secondary guards must drive directly into the body of their dropping big to draw contact and recover our free throw volume.*
*Questions for the staff: (1) Who is our designated secondary driver when their primary defender denies our lead guard? and (2) Are we comfortable letting their big shoot uncontested elbow jumpers to protect our transition retreat?"*
- **Visual**: Hand off finalized 2-page Pre-Game Coaching Brief.
