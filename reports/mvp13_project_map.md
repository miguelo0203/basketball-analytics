# Master Project Map: The Analytical Lifecycle from MVP-0 to MVP-13
## International Basketball Historical Analytics (2005–2025)

**Status**: Formally Certified Master Project Map  
**Structure**: 14 Progressive Stages from Data Engineering to Professional Deployment  

---

### MVP-0: Data Engineering Foundation & SHA-256 Provenance
- **Purpose & Output**: Ingested and typed raw EuroBasket boxscores into an immutable lake with SHA-256 validation and DuckDB staging tables.
- **Basketball Question**: *Can historical tournament boxscores be deterministically validated and mathematically reconciled with zero missing games?*
- **Professional Skill Demonstrated**: Robust data engineering, relational modeling, data contracts, and cryptographic auditability.

---

### MVP-0.1: Complete EuroBasket 2005–2022 Coverage Certification
- **Purpose & Output**: Closed coverage gaps across all 559 EuroBasket matches and resolved player name collisions across international rosters.
- **Basketball Question**: *How do we ensure 100% complete tournament game and player coverage across two decades of European basketball?*
- **Professional Skill Demonstrated**: Comprehensive data quality assurance, deterministic entity resolution, and historical data reconciliation.

---

### MVP-1: Global Competition Expansion (World Cups & Olympics)
- **Purpose & Output**: Expanded the DuckDB warehouse to 18 tournaments, 1,145 games, 2,290 team-games, and 27,353 player-game rows.
- **Basketball Question**: *How does international tournament competition scale when integrating FIBA World Cups and Olympic Games?*
- **Professional Skill Demonstrated**: Scalable data warehousing, multi-competition schema normalization, and database scaling.

---

### MVP-2: Longitudinal Econometrics & Interrupted Time Series
- **Purpose & Output**: Implemented an Interrupted Time Series (ITS) econometric study evaluating the 2010 FIBA 3-point line expansion ($6.25\text{m} \rightarrow 6.75\text{m}$).
- **Basketball Question**: *Did moving the 3-point line back structurally reduce shooting efficiency or accelerate tactical perimeter spacing?*
- **Professional Skill Demonstrated**: Econometric modeling, longitudinal time-series analysis, counterfactual estimation, and causal inference caveats.

---

### MVP-3: Player-Level Analytics & Functional Role Discovery
- **Purpose & Output**: Engineered $4,350$ player tournament feature vectors and discovered 6 functional player archetypes using K-Means++ and PCA on $3,767$ qualified campaigns.
- **Basketball Question**: *How can we classify players by their functional on-court usage, passing, and shooting roles rather than nominal positions (PG/SG/SF/PF/C)?*
- **Professional Skill Demonstrated**: Unsupervised machine learning, dimensionality reduction, feature engineering, and basketball taxonomy design.

---

### MVP-4: Recruitment-Oriented Decision Support & Reliability
- **Purpose & Output**: Built the Candidate Fit Index (CFI), player similarity comparables, sample size reliability tiers ($N \ge 150\text{m}$), and blind analyst validation.
- **Basketball Question**: *How can an analyst identify historical player comparables and evaluate positional fit while accounting for small-sample noise?*
- **Professional Skill Demonstrated**: Multi-criteria decision modeling, sample reliability weighting, blind evaluation protocols, and scouting handoffs.

---

### MVP-5: Tactical Video Validation & Inter-Rater Reliability
- **Purpose & Output**: Double-coded 420 possession events across 36 games on P&R drop coverage, hedge speed, and closeouts, achieving Cohen's $\kappa = 1.00 / 0.80$.
- **Basketball Question**: *Do quantitative boxscore metrics align with tactical execution on video film, or do they conceal defensive scheme vulnerabilities?*
- **Professional Skill Demonstrated**: Qualitative video coding protocols, inter-rater reliability measurement, and qualitative-quantitative evidence synthesis.

---

### MVP-6: Supervised Machine Learning & Statistical Inference
- **Purpose & Output**: Trained expanding 17-fold chronological walk-forward models ($1,105$ out-of-sample games, LightGBM $\text{Brier} = 0.1967$, $\text{ECE} = 0.0314$, $\text{MAE} = 11.74$) with Clustered Bootstrap CIs ($B=5,000$).
- **Basketball Question**: *Can pre-game features generate calibrated win probabilities without future data leakage, and what features drive those probabilities?*
- **Professional Skill Demonstrated**: Supervised learning, probability calibration, TreeSHAP feature attribution, and non-parametric statistical inference.

---

### MVP-7: Monte Carlo Tournament Simulation & Scenario Analysis
- **Purpose & Output**: Executed 180,000 Monte Carlo tournament simulations with probability shrinkage ($\lambda \in \{0.50, 0.75, 1.00\}$) and counterfactual bracket replays.
- **Basketball Question**: *How does single-game uncertainty propagate through a multi-round knockout tournament bracket?*
- **Professional Skill Demonstrated**: Probabilistic simulation, bracket propagation, scenario sensitivity analysis, and counterfactual testing.

---

### MVP-8: End-to-End Decision System & Historical Validation
- **Purpose & Output**: Engineered 6-layer candidate decision dossiers, contradiction auditing heuristics, and reconstructed 5 historical tournament decisions ($80\%$ exact agreement).
- **Basketball Question**: *Can the entire analytical stack transform historical data into an auditable, uncertainty-aware decision dossier for sporting leadership?*
- **Professional Skill Demonstrated**: Decision science, multi-criteria evidence aggregation, contradiction surfacing, and historical validation.

---

### MVP-9: Executive Presentation & Portfolio Deck
- **Purpose & Output**: Compiled a dual-layer 40-slide master portfolio presentation deck in markdown and automated PowerPoint (`.pptx`) with a full data dictionary and speaker notes.
- **Basketball Question**: *How do we present 20 years of technical basketball analytics to both a Head Coach and a Chief Data Scientist effectively?*
- **Professional Skill Demonstrated**: Technical communication, executive data storytelling, presentation design, and slide automation.

---

### MVP-10: Analyst Decision Workspace & Brief Generator
- **Purpose & Output**: Built an operational Streamlit decision workspace with an anti-hindsight historical replay barrier, 8-layer evidence matrices, and automated Coaching Briefs.
- **Basketball Question**: *What does an analyst actually deliver to a coaching staff on match eve, and how do we evaluate analytical quality post-game without outcome bias?*
- **Professional Skill Demonstrated**: Full-stack interactive tool development (Streamlit), anti-hindsight workflow isolation, and coaching decision support.

---

### MVP-11: Adversarial Portfolio Audit & Quality Verification
- **Purpose & Output**: Executed an independent 15-item claim registry audit, verifying temporal boundaries, statistical validity, and removing unsupported claims.
- **Basketball Question**: *Where could an experienced basketball analyst or data science lead challenge the methodology or conclusions of this project?*
- **Professional Skill Demonstrated**: Adversarial critical thinking, scientific integrity, bias detection, and rigorous self-auditing.

---

### MVP-12: Public Portfolio Deployment & Interview Master Package
- **Purpose & Output**: Deployed a polished public README, portfolio hub, 3 flagship case studies, 60-second pitch, 5-minute live demo script, and 32-question interview guide.
- **Basketball Question**: *How is this analytical system packaged and presented to demonstrate professional readiness for front-office analytics roles?*
- **Professional Skill Demonstrated**: Portfolio engineering, public technical writing, live software demonstration, and structured interview preparation.

---

### MVP-13: Final Professionalization & Operational Sanity Pass
- **Purpose & Output**: Executed a final professionalization pass: separated demonstrated vs. simulated experience, drafted 30-day club integration roadmap, created standardized coaching/director report templates, and refined Streamlit UX.
- **Basketball Question**: *How does this analyst operate within a professional basketball organization to support coaching decisions with humility and rigor?*
- **Professional Skill Demonstrated**: Operational integration planning, humble decision-support framing, and front-office realism.

---

### MVP-14: Real-World Analyst Demonstration & Interview Simulation
- **Purpose & Output**: Completed an adversarial gap analysis, realistic generational task study, 10-minute live demonstration script, raw analyst working note, coach pushback simulation, 20–30 minute live coding exercise, capability matrix, and final 5-minute pitch.
- **Basketball Question**: *Can this analyst investigate an open-ended coaching question, defend methodology against coaching staff pushback, and communicate uncertainty without overstepping tactical authority?*
- **Professional Skill Demonstrated**: Practical front-office communication, live technical problem solving, investigative critical thinking, and interview execution.
