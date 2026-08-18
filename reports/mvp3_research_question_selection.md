# MVP-3 Research Question Selection & Analytical Framework
## International Basketball Historical Analytics (2005–2025)

**Framework**: Player Evaluation, Role Discovery, Comparables & Recruitment Analytics  
**Date**: 2026-08-18  

---

## 1. Candidate Research Questions Evaluated

| Research Question | Data Requirements | Analytical Method | Scouting & Front-Office Value | Methodological Feasibility | Ranking & Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Q1: Functional Role Discovery** | Rate-based player profiles ($USG\%, TS\%, 3PAr, AST\%, TOV\%, ORB\%, DRB\%, STL40, BLK40$) | Hybrid basketball-informed clustering & dimensional profiling | High (Replaces outdated 5 positions with operational roles) | **High (Certified)** | **Candidate A (Core Pillar 1)** |
| **Q2: Historical Player Comparables Engine** | Standardized multidimensional feature vectors across all international players | Cosine & Euclidean similarity with feature decomposition | Very High (Contextual benchmark for prospect/pro evaluation) | **High (Certified)** | **Candidate B (Core Pillar 2)** |
| **Q3: Recruitment Fit & Decision Support** | Role profiles, contextual usage, production rates, sample size indicators | Multi-criteria weighted fit scoring & trade-off analysis | Maximum (Direct decision-support for scouting staff) | **High (Certified)** | **Candidate C (Core Pillar 3)** |
| **Q4: Unadjusted Career Plus-Minus** | 5-man substitution stint timestamps across 2005–2025 | Stint-level linear regression (APM) | Low (Severe collinearity & noisy small samples) | **Infeasible (Missing sub-minute PBP before 2012)** | **REJECTED** |

---

## 2. Selected Primary Flagship Question for MVP-3

> **Selected Unified Research Architecture**:  
> **"Multi-Dimensional Player Role Discovery, Statistical Comparables, and Decision-Support Recruitment Analytics in International Basketball (2005–2025)"**

### Why Selected:
1. **Direct Practical Value for Basketball Operations**: Solves the central question faced by sports analysts and front offices: *"Given a player's statistical production, efficiency, and role in international competition, what functional archetype does he represent, who are his historical statistical comparators, and how does he fit against a team's tactical requirements?"*
2. **Rejects Naive One-Number Metrics**: Avoids collapsing basketball into a single black-box number (e.g. raw PIR or unadjusted +/-), constructing instead an interpretable multi-dimensional functional role profile.
3. **Bridge from Data to Scouting**: Connects quantitative data to qualitative decision-making by explicitly generating **"What the Data Says" vs. "What Still Requires Video Scouting"**.

---

## 3. Rejected Methodologies & Exclusions

1. **Rejected: Pure Raw Boxscore Clustering (Height/PTS Collinearity)**:
   - Clustering on raw height, raw PTS, and raw FGA produces trivial positional groupings (tall players vs short players).
   - *Resolution*: Height is strictly excluded from clustering and evaluated post-hoc. Features are normalized into rates, percentages, and per-40 possession shares.
2. **Rejected: Unregularized Stint Plus-Minus**:
   - Short international tournaments ($5\text{--}11$ games) generate severe multicollinearity when 5-man lineups play together for few possessions.
   - *Resolution*: Focus on validated boxscore rate distributions and contextual opportunity shares.
