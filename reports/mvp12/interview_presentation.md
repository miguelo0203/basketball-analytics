# 8-Slide Executive Interview Presentation Deck
## International Basketball Historical Analytics (2005–2025)

**Format**: 8-Slide Concise Interview Deck  
**Target Duration**: 5 Minutes  

---

### Slide 1: Title & The Core Problem
- **Title**: Transforming Basketball Data into Coaching Decision Support
- **Subtitle**: 20 Years of International Basketball Analytics (2005–2024)
- **The Core Problem**: Coaching staffs face information overload, small-sample shooting noise, and hindsight bias. How can data analytics provide structured, uncertainty-aware decision support?

---

### Slide 2: Data Provenance & Scale
- **Scope**: 18 International Tournaments (EuroBasket, FIBA World Cup, Olympic Games).
- **Cardinalities**: 1,145 matches, 2,290 team-games, 27,353 player-games, 2,124 canonical players.
- **Engineering Foundation**: Immutable raw storage, SHA-256 validation, DuckDB relational warehouse.

---

### Slide 3: The End-to-End Analytical Architecture
- **Pipeline Flow**: Raw Ingestion $\rightarrow$ Relational Warehouse $\rightarrow$ Feature Stores $\rightarrow$ Supervised ML $\rightarrow$ Monte Carlo Simulation $\rightarrow$ Decision Workspace.
- **Temporal Barrier**: Expanding 17-fold walk-forward validation ($1,105$ out-of-sample matches).

---

### Slide 4: Bridging Quantitative Models with Tactical Film
- **Quantitative Signal**: Pace-adjusted Net Rating and Four Factors possession decomposition.
- **Tactical Nuance**: 420 double-coded possession events ($\kappa = 0.80$) evaluating P&R drop coverage, hedge speed, and closeout quality.

---

### Slide 5: Calibrated Machine Learning & Uncertainty
- **Supervised Benchmark**: LightGBM Classifier achieves $\text{Brier} = 0.1967$ and out-of-sample $\text{MAE} = 11.74$ pts.
- **Probability Calibration**: Expected Calibration Error ($\text{ECE} = 0.0314$) via out-of-sample Isotonic Regression.
- **Variance Bounds**: Clustered non-parametric bootstrap ($B = 5,000$) confidence intervals.

---

### Slide 6: Tournament Simulation & Decision Systems
- **Simulation Scope**: 180,000 Monte Carlo runs ($10,000$ per tournament). Retrospective Top-4 Capture = 100.0%.
- **Decision Engine**: 6-layer multi-criteria candidate evaluation with automated contradiction detection.

---

### Slide 7: The Operational Coaching Brief (Demo Walkthrough)
- **Executive Summary**: Pre-game win probabilities and historical baselines.
- **Surfacing Contradictions**: Highlighting stats vs film discrepancies.
- **Staff Questions**: Delivering actionable tactical questions rather than arrogant prescriptions.

---

### Slide 8: Summary & Day-1 Club Impact
- **Core Value**: Reproducible pipelines, calibrated probabilities, tactical synergy, and coach-first humility.
- **Day-1 Club Readiness**: Ready to integrate live optical tracking feeds, domestic league play-by-play, and internal video tagging databases.
