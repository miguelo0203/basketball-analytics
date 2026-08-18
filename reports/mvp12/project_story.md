# The Project Story: 20 Years of International Basketball to Decision Support
## International Basketball Historical Analytics (2005–2025)

**Status**: Certified Narrative & Project Evolution  

---

# 1. The Genesis: The Problem of Noise and Hindsight

International basketball represents one of the most demanding environments in professional sports analytics:
- Tournaments are ultra-compressed (6 to 9 games over 15 days).
- Sample sizes are fragile, causing raw 3-point shooting percentages and boxscore averages to fluctuate wildly.
- High roster turnover between tournament cycles renders naive multi-year averages misleading.
- Most public basketball analytics suffer from severe **hindsight bias**—using end-of-tournament or full-career statistics to evaluate past games.

The mission of this project was to answer one fundamental question:

> *"How can a basketball data analyst build an end-to-end system that takes 20 years of international tournament data, cleans and validates it with deterministic engineering, generates rigorous statistical and tactical evidence, isolates pre-game information states, and delivers actionable, uncertainty-aware decision support to a coaching staff?"*

---

# 2. The Analytical Journey: From Raw Provenance to Coaching Briefs

```text
STAGE 1: ENGINEERING FOUNDATION (MVP-0 to MVP-1)
  └── Built immutable RAW lake with SHA-256 validation.
  └── Engineered certified DuckDB relational warehouse (18 tournaments, 1,145 games, 27,353 player-games).

STAGE 2: DESCRIPTIVE & LONGITUDINAL RESEARCH (MVP-2)
  └── Conducted Interrupted Time Series (ITS) econometrics on the 2010 FIBA 3-point line expansion.

STAGE 3: PLAYER ROLE & SCOUTING TAXONOMY (MVP-3 to MVP-4)
  └── Discovered 6 functional player archetypes across 3,767 qualified campaigns using K-Means++ and PCA.
  └── Engineered Candidate Fit Index (CFI) and reliability tiering.

STAGE 4: TACTICAL VIDEO INTEGRATION (MVP-5)
  └── Double-coded 420 possession events across 36 games, proving substantial inter-rater reliability (κ = 0.80).

STAGE 5: SUPERVISED ML & STATISTICAL INFERENCE (MVP-6)
  └── Implemented expanding 17-fold chronological walk-forward validation (1,105 out-of-sample matches).
  └── Calibrated LightGBM classifier (Brier = 0.1967, ECE = 0.0314) and computed Bootstrap 95% CIs.

STAGE 6: TOURNAMENT SIMULATION & SCENARIOS (MVP-7)
  └── Ran 180,000 Monte Carlo tournament simulations with probability shrinkage and counterfactual replays.

STAGE 7: MULTI-CRITERIA DECISION SYSTEM (MVP-8 to MVP-9)
  └── Synthesized 6-layer decision dossiers and compiled 40-slide executive presentation portfolio.

STAGE 8: OPERATIONAL WORKSPACE & INTERACTIVE REPLAY (MVP-10 to MVP-12)
  └── Built Streamlit Analyst Decision Workspace with strict anti-hindsight barrier, contradiction engine,
      automated coaching briefs, and comprehensive interview package.
```

---

# 3. The Professional Takeaway

This project proves that modern sports analytics is not about building black-box models that claim to replace coaches. It is about building an **auditable, reproducible evidence pipeline** that empowers decision-makers with clarity, context, and calibrated uncertainty.
