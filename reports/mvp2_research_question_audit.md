# Research Question Feasibility & Methodological Audit
## International Basketball Historical Analytics (2005–2025)

**Database**: `data/03_validated/basketball_analytics.duckdb`  
**Certified Scope**: 18 Senior Men's Tournaments (1,145 games, 2,290 team-game observations)  
**Date**: 2026-08-18  

---

## 1. Evaluation Matrix of the Four Tier-1 Flagship Questions

Every Tier-1 research question proposed in `docs/research_questions.md` was audited against the certified warehouse data availability, statistical power, and methodological validity:

| Evaluation Dimension | Flagship 1: Spain Generational Aging Curves | Flagship 2: Four Factors Championship Runs | Flagship 3: Unsupervised Player Archetypes | Flagship 4: 2010 3-Point Arc Shift (ITS) |
| :--- | :--- | :--- | :--- | :--- |
| **Unit of Analysis** | `fact_player_game` | `fact_team_game` | `fact_player_tournament` | `fact_team_game` |
| **Required Variables** | Individual MIN, PTS, USG%, TS% | Team eFG%, TOV%, ORB%, FTr, NetRtg | 13 normalized rate features per player | 3PAr, 3P%, FGA, Pace, Rule Set ID |
| **Available Variables** | 0% in production DuckDB | **100.0% Complete** | 0% in production DuckDB | **100.0% Complete** |
| **Effective Sample Size** | $N = 0$ player games | $N = 2,290$ team-games ($N=152$ ESP) | $N = 0$ player-tournaments | **$N = 2,290$ team-games (18 tourneys)** |
| **Historical Range** | Infeasible | 2005–2025 (18 tournaments) | Infeasible | **2005–2025 (18 tournaments)** |
| **Methodological Rigor** | GAM Splines (Deferred) | Shapley Variance Decomposition | K-Means++ / GMM (Deferred) | **Segmented Linear Regression (ITS)** |
| **Statistical Confounders** | Small sample per tournament | Blowout garbage time, pace shift | Morphological height bias | Secular tactical trend, 2014 rule change |
| **Causal Discipline** | Descriptive aging curves | Descriptive variance attribution | Purely exploratory clustering | **Quasi-experimental ITS (Non-DiD)** |
| **Portfolio Value** | High (Visual/Narrative) | High (Tactical) | High (Machine Learning) | **Very High (Econometric/Analytics)** |
| **Feasibility Verdict** | **BLOCKED (MVP-3)** | **FEASIBLE (Secondary)** | **BLOCKED (MVP-3)** | **SELECTED (PRIMARY FLAGSHIP)** |

---

## 2. In-Depth Methodological Assessment

### Flagship 1 & 3 (Individual Player Level): Diagnosis
- **Audit Finding**: While the relational schemas (`dim_player`, `dim_player_alias`, `fact_player_game`, `fact_player_tournament`) are fully defined, individual player boxscores were prioritized as secondary behind certified team-game and tournament coverage in MVP-0 and MVP-1.
- **Decision**: In strict compliance with the **Non-Negotiable Rule** ("Do not fabricate missing observations; do not alter validated data"), Flagships 1 and 3 are formally deferred to MVP-3 when player boxscore scraping pipelines are certified.

### Flagship 2 (Four Factors Decomposition): Secondary Asset
- **Audit Finding**: Highly feasible ($N = 2,290$ team-game observations). Team-level Four Factors are 100% populated with 0 missing values and validated ball-math consistency.
- **Decision**: Integrated as a supporting descriptive and decomposition module within the analytical data mart.

### Flagship 4 (2010 3-Point Arc Shift via ITS): Selected Primary Flagship
- **Audit Finding**: Optimal statistical properties. The 2010 regulatory change (6.25m to 6.75m) spans 6 pre-intervention tournaments (684 team-game observations) and 12 post-intervention tournaments (1,606 team-game observations).
- **Methodological Advantages**:
  1. Utilizes certified Interrupted Time Series (ITS) with Newey-West standard errors.
  2. Adheres to causal discipline by explicitly rejecting invalid Difference-in-Differences claims (no unexposed international control group).
  3. Tests both immediate level changes ($\beta_2$) and post-intervention slope changes ($\beta_3$).
  4. Answers a profound basketball question: Did moving the arc back 50cm suppress 3-point volume, or did secular global analytics trends dominate regulatory friction?

---

## 3. Final Ranking & Selection

1. **Rank 1 (Selected Primary Flagship)**: **Flagship 4 — Quasi-Experimental Evaluation of the 2010 3-Point Arc Change via Interrupted Time Series (ITS)**.
2. **Rank 2 (Supporting Module)**: **Flagship 2 — Four Factors Decomposition of International Performance**.
3. **Rank 3 (Deferred to MVP-3)**: **Flagship 3 — Unsupervised Player Archetype Discovery**.
4. **Rank 4 (Deferred to MVP-3)**: **Flagship 1 — Spain Generational Aging Curves**.
