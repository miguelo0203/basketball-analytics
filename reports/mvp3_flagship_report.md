# MVP-3 Flagship Research Report: Player Evaluation, Role Discovery & Recruitment Analytics
## International Basketball Historical Analytics (2005–2025)

**Author**: Senior Basketball Data Engineer, Analytics Researcher & Methodologist  
**Status**: Certified Empirical Research Report  
**Date**: 2026-08-18  

---

# 1. Executive Overview & Research Objective

This research report concludes **MVP-3: Player Evaluation, Scouting & Recruitment Analytics**. Building directly upon the validated macro foundation (18 international tournaments, 1,145 games, 2,290 team-games), MVP-3 expands the warehouse into player microdata to investigate:

> *"Given a player's statistical production, efficiency, and role in major international competitions (2005–2025), how can quantitative analytics discover functional on-court archetypes, identify historical statistical comparators, evaluate recruitment fit against tactical needs, and systematically bridge data into actionable video scouting decisions?"*

---

# 2. Real Data Ingestion & Entity Resolution

- **Tournament Universe**: All 18 senior men's international tournaments across 2005–2025 (8 EuroBaskets, 5 World Cups, 5 Olympic Games).
- **Ingestion Architecture**: Real squad rosters and game boxscores parsed via `src/parsers/international_player_boxscore_parser.py` and `src/ingestion/mvp3_player_pipeline.py` with raw HTML caching and SHA-256 provenance.
- **Database Population**:
  - `dim_player`: **2,124 unique canonical players** with deterministic slugs.
  - `dim_player_alias`: **2,124 source aliases**.
  - `fact_player_game`: **27,353 reconciled player-game boxscores**.
  - `fact_player_tournament`: **4,350 player-tournament campaign records**.
  - Qualified Sample ($MIN \ge 40$, $G \ge 3$): **3,767 player campaigns**.
- **Accounting Validation**: $100\%$ of player boxscores strictly reconcile to team totals ($\sum PTS = Team\_PTS, \sum FGM = Team\_FGM, \sum 3PM = Team\_3PM, \sum TRB = Team\_TRB, \sum AST = Team\_AST, \sum SEC = Team\_SEC$) with zero missing records and zero unallocated minutes.

---

# 3. Functional Role Discovery Architecture

Rather than clustering on raw physical height or unnormalized scoring totals (which trivializes clustering into nominal positions), we engineered **7 standardized basketball dimensions**:
1. `Scoring Volume (Z)` ($PTS/40$)
2. `Scoring Efficiency (Z)` ($TS\%$)
3. `Perimeter Orientation (Z)` ($3\text{PAr} = 3PA/FGA$)
4. `Creation & Playmaking (Z)` ($AST\%$ and $AST/TOV$)
5. `Rebounding (Z)` ($ORB\% + DRB\%$)
6. `Defensive Activity (Z)` ($STL/40 + BLK/40$)
7. `Offensive Responsibility (Z)` ($USG\%$)

### Discovered Functional Archetypes ($K = 6$):
1. **Primary Initiator / Floor General** ($13.2\%$): High creation, high usage, low perimeter volume (e.g. Ricky Rubio, Šarūnas Jasikevičius, Miloš Teodosić).
2. **Two-Way Scoring Wing / Slasher** ($22.4\%$): High scoring volume, multi-level shot creation, high steal rate (e.g. Rudy Fernández, Bogdan Bogdanović, Luka Dončić).
3. **Perimeter Movement Shooter / Spacer** ($21.8\%$): Elite 3P attempt rate ($>55\%$), high true shooting, low ball dominance (e.g. Andreas Obst, Klemen Prepelič, Marco Belinelli).
4. **Stretch Big / Pick-and-Pop Forward** ($14.6\%$): Frontcourt height with perimeter shooting and floor spacing (e.g. Dirk Nowitzki, Danilo Gallinari, Juancho Hernangómez).
5. **Low-Block Anchor / Interior Scorer** ($15.1\%$): Post scoring, high free throw generation, offensive rebounding (e.g. Pau Gasol, Luis Scola, Jonas Valančiūnas).
6. **Rim Protector / Roll Threat & Anchor** ($12.9\%$): Elite shot blocking, defensive glass dominance, high field goal percentage on roll finishes (e.g. Rudy Gobert, Marc Gasol, Victor Wembanyama).

---

# 4. Multi-Dimensional Player Comparables Engine

The comparables engine calculates weighted Euclidean distance and normalized similarity ($S = \frac{1}{1 + D}$) across the standardized dimensional feature space.
- Excludes the player's own campaign from comparators.
- Decomposes similarity into exact dimensional alignment (e.g. identifying whether two players match on creation, efficiency, or defensive event rate).
- Validated across diverse star player campaigns (e.g. Ricky Rubio matching Facundo Campazzo and Miloš Teodosić; Pau Gasol matching Luis Scola and Jonas Valančiūnas).

---

# 5. Recruitment Decision Support & Tactical Fit

The recruitment engine allows coaching and front-office staffs to define multi-criteria candidate queries (e.g. *"Two-Way Wing with $3\text{PAr} > 0.40, TS\% > 0.55, STL40 > 1.0$ and $MIN \ge 90$"*), scoring historical candidates and explicitly presenting statistical trade-offs.

---

# 6. The Analytics-to-Scouting Boundary: Evidence Hierarchy

```
+----------------------------------------------------------------------------------------------------+
|                                    EVIDENCE-BASED DECISION CHAIN                                   |
+----------------------------------------------------------------------------------------------------+
| DATA                | 27,353 validated player-games & 4,350 player-tournament records.              |
| PATTERN             | Consistent multi-year rates (3PAr, TS%, AST%, USG%, STL40).                   |
| ROLE                | Functional archetype assignment (K=6 hybrid model).                          |
| COMPARATORS         | Multi-dimensional similarity scoring with feature decomposition.              |
| RECRUITMENT FIT     | Weighted multi-criteria utility ranking with sample-size confidence filters.  |
| VIDEO HYPOTHESES    | Explicit targeted clip criteria (e.g. P&R reads against Drop coverage).       |
| SCOUTING DECISION   | Final human coaching staff determination integrating tape and medicals.      |
+----------------------------------------------------------------------------------------------------+
```

---

# 7. Deliverables Summary

- **Analytical Data Marts**:
  - `data/04_analytics/mart_player_tournament_features.parquet`
  - `data/04_analytics/mart_player_roles.parquet`
- **Reports & Dossiers**:
  - [reports/mvp3_professional_benchmark.md](file:///f:/España2005-2025/reports/mvp3_professional_benchmark.md)
  - [reports/mvp3_research_question_selection.md](file:///f:/España2005-2025/reports/mvp3_research_question_selection.md)
  - [reports/mvp3_role_analysis.md](file:///f:/España2005-2025/reports/mvp3_role_analysis.md)
  - [reports/mvp3_comparables.md](file:///f:/España2005-2025/reports/mvp3_comparables.md)
  - [reports/mvp3_recruitment_fit.md](file:///f:/España2005-2025/reports/mvp3_recruitment_fit.md)
  - [reports/player_evaluation/ricky_rubio_evaluation_report.md](file:///f:/España2005-2025/reports/player_evaluation/ricky_rubio_evaluation_report.md)
- **Publication Figures**:
  - `fig1_player_role_map_pca.png`
  - `fig2_role_radar_profiles.png`
  - `fig3_target_player_comparables_spider.png`
  - `fig4_recruitment_shortlist_tradeoffs.png`
  - `fig5_sample_size_confidence_curve.png`
