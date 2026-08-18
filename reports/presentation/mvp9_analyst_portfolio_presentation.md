# MVP-9: INTERNATIONAL BASKETBALL HISTORICAL ANALYTICS & DECISION-SUPPORT PORTFOLIO
## A 20-Year Research Stack from Raw Data to Evidence-Based Decision Support (2005–2025)

**Target Audience**: Head Coaches, Sporting Directors, Technical Directors, Senior Data Scientists & Quantitative Analysts  
**Author**: Principal Basketball Data Scientist & Systems Architect  
**Certified Stack**: MVP-0 through MVP-8 (128 Automated Tests, 100% Pass Rate)  
**Deliverable Format**: 40-Slide Master Executive & Technical Presentation Deck  

---

# SECTION 1: WHY THIS PROJECT EXISTS (Slides 1–4)

## Slide 1: Title Slide & Core Value Proposition
### International Basketball Historical Analytics (2005–2025)
**Subtitle**: Transforming 20 Years of Heterogeneous Basketball Data into Reproducible, Uncertainty-Aware Decision Support.
- **Core Principle**: *"The value of the analyst is not making the decision. The value is giving the decision-maker better evidence, better context, clearer uncertainty, and a reproducible analytical process."*
- **Epistemological Guardrail**: $\text{PREDICTION} \neq \text{CAUSATION} \quad|\quad \text{OBSERVATION} \neq \text{PROOF} \quad|\quad \text{MODEL OUTPUT} \neq \text{JUDGMENT}$

---

## Slide 2: The Problem of Uncertainty in Basketball Decisions
### Beyond Boxscores & Outcome Bias
- **The Decision-Maker's Dilemma**: Roster construction, lineup selection, and tournament game-planning operate under acute uncertainty, small sample sizes, and high variance.
- **Flaws of Traditional Statistics**: Traditional counting stats (PPG, RPG) measure *what* accumulated in the past, but fail to account for pace, possession efficiency, opponent strength, and tactical context.
- **Outcome Bias**: A good process can result in a missed shot or single-possession loss; a flawed process can accidentally win. The analyst's job is to decouple process quality from random outcome noise.

---

## Slide 3: The Multi-Layer Evidence Hierarchy
### What Does a Coaching Staff Actually Need?
Coaches and sporting directors require evidence across multiple distinct dimensions:
1. **Efficiency Context**: True shooting efficiency ($TS\%$), turnover rates, and Four Factors impact.
2. **Sample Reliability**: Explicit uncertainty bounds and confidence intervals on small-sample metrics.
3. **Tactical Archetypes**: Functional roles rather than rigid nominal positions (PG, SG, SF, PF, C).
4. **Qualitative Film Validation**: Video confirmation of decision-making, P&R reads, and defensive execution.
5. **Predictive Modeling**: Out-of-sample win probability shifts and matchup net ratings.
6. **Tournament Simulation**: Propagation of single-game probabilities across knockout bracket structures.

---

## Slide 4: The Central Research Question
### Framing the Entire Analytical Portfolio
> *"How can a basketball data analyst transform historical match, player, tactical, and contextual information into defensible, uncertainty-aware decision support that empowers coaching staff and sporting leadership?"*
- **Application Domain**: Senior Men's International Basketball (FIBA EuroBasket, FIBA World Cup, Olympic Games).
- **Core Objective**: Demonstrating end-to-end technical mastery across Data Engineering, Econometrics, Machine Learning, Statistical Inference, Monte Carlo Simulation, and Decision Science.

---

# SECTION 2: PROJECT SCOPE & CERTIFIED DATA UNIVERSE (Slides 5–7)

## Slide 5: Historical Scope & Tournament Coverage Timeline
### 18 Official Senior Men's Tournaments (2005–2024)
```text
EuroBasket:  [2005] ── [2007] ── [2009] ── [2011] ── [2013] ── [2015] ── [2017] ── [2022] (8 Tournaments)
World Cups:  [2006] ─────── [2010] ─────── [2014] ─────── [2019] ─────── [2023] (5 Tournaments)
Olympics:    [2008] ─────── [2012] ─────── [2016] ─────── [2020] ─────── [2024] (5 Tournaments)
```
- **Historical Horizon**: 2005 to 2024 (18 premier international tournaments).
- **Certified Universe**: Zero missing games, zero duplicate records, 100% tournament completion.

---

## Slide 6: Verified Data Cardinalities
### The Analytical Warehouse Foundation
```
+----------------------------------------------------------------------------------------------------+
| ENTITY / DIMENSION            | CERTIFIED EXACT COUNT | DATA INTEGRITY & AUDIT TRAIL               |
+----------------------------------------------------------------------------------------------------+
| **International Tournaments** | **18 Tournaments**    | EuroBasket (8), World Cup (5), Olympics (5)|
| **Canonical Matches**         | **1,145 Games**       | 100% reconciled against FIBA official boxes|
| **Team-Game Observations**    | **2,290 Team-Games**  | Bilateral game representation              |
| **Player-Tournament Campaigns**| **4,350 Campaigns**  | Complete historical player pool            |
| **Qualified Player Campaigns**| **3,767 Campaigns**  | Screened under minimum sample criterion    |
| **Player-Game Observations**  | **27,353 Records**    | Granular boxscores & rate metrics          |
| **Double-Coded Video Events** | **420 Possessions**   | Inter-rater reliability (κ = 1.0 / 0.80)   |
+----------------------------------------------------------------------------------------------------+
```

---

## Slide 7: Functional Player Archetypes (Beyond Nominal Positions)
### Multi-Dimensional Clustering (K-Means++ & PCA)
Nominal positions (1–5) obscure modern tactical functions. The system categorizes 4,350 player campaigns into 6 functional archetypes:
1. **Primary Initiator / Floor General**: High usage, high assist rate ($AST\% \ge 25\%$), primary P&R ball-handler.
2. **Two-Way Scoring Wing / Slasher**: Secondary creation, rim pressure, perimeter defensive versatility.
3. **Perimeter Movement Shooter / Spacer**: High 3-point attempt rate ($3\text{PAr} \ge 50\%$), off-ball gravity.
4. **Stretch Big / Pick-and-Pop Forward**: Frontcourt floor spacing, trailing transition 3s, pick-and-pop.
5. **Low-Block Anchor / Interior Scorer**: Post-up efficiency, offensive rebounding, interior hub passing.
6. **Rim Protector / Roll Threat & Anchor**: Defensive rim protection, P&R roll finisher, screen setting.

---

# SECTION 3: END-TO-END ANALYTICAL ARCHITECTURE (Slides 8–10)

## Slide 8: The Full Analytical Pipeline
### From Raw Bits to Coaching Decision Support
```text
  ┌────────────────────────┐
  │ 1. DATA ACQUISITION    │ ── Immutable RAW Storage (SHA-256 Checksums)
  └───────────┬────────────┘
              ▼
  ┌────────────────────────┐
  │ 2. DATA ENGINEERING    │ ── Relational Modeling, Entity Resolution, DuckDB Analytical Warehouse
  └───────────┬────────────┘
              ▼
  ┌────────────────────────┐
  │ 3. DESCRIPTIVE MARTS   │ ── Four Factors, Net Ratings, Longitudinal Time-Series (2010 3PT Shift)
  └───────────┬────────────┘
              ▼
  ┌────────────────────────┐
  │ 4. PLAYER ARCHETYPES   │ ── K-Means++ Clustering, Centroid Distance, Similarity Engine (CFI)
  └───────────┬────────────┘
              ▼
  ┌────────────────────────┐
  │ 5. TACTICAL FILM (IRR) │ ── Double-Coded Qualitative Video Layer (Cohen's κ = 1.0 / 0.80)
  └───────────┬────────────┘
              ▼
  ┌────────────────────────┐
  │ 6. SUPERVISED ML       │ ── 17-Fold Temporal Walk-Forward Validation, Probability Calibration
  └───────────┬────────────┘
              ▼
  ┌────────────────────────┐
  │ 7. TOURNAMENT SIM      │ ── 180,000 Monte Carlo Runs, Probability Shrinkage, Counterfactuals
  └───────────┬────────────┘
              ▼
  ┌────────────────────────┐
  │ 8. DECISION SYSTEM     │ ── 6-Layer Multi-Criteria Dossiers, Contradiction Audit, Decision Tiers
  └───────────┬────────────┘
              ▼
  ┌────────────────────────┐
  │ 9. COACHING DECISION   │ ── Human Expert Judgment (Head Coach / Sporting Director)
  └────────────────────────┘
```

---

## Slide 9: Cumulative Stage Mapping (MVP-0 → MVP-8)
### How Each Stage Builds the Foundation for the Next
- **MVP-0 & 0.1**: Built certified DuckDB data engineering layer and 100% EuroBasket coverage closure.
- **MVP-1**: Expanded universe to FIBA World Cups and Olympic Games ($1,145$ games).
- **MVP-2**: Flagship econometric research: Interrupted Time Series on 2010 3-point line expansion.
- **MVP-3 & 4**: Ingested $27,353$ player-games, discovered 6 archetypes, and built Candidate Fit Index.
- **MVP-5**: Double-coded video tactical validation layer ($420$ coded possessions).
- **MVP-6**: Built expanding temporal walk-forward ML models ($ECE = 0.0314$) and $B=5,000$ Bootstrap CIs.
- **MVP-7**: Executed $180,000$ Monte Carlo tournament simulations and controlled counterfactuals.
- **MVP-8**: Integrated all 6 upstream layers into auditable decision dossiers and validated historical decisions.

---

## Slide 10: Methodological Guardrails & Zero Hindsight Invariant
### Eliminating Data Leakage and Retrospective Contamination
- **Strict Temporal Cutoff**: Models predicting Match $M$ at Date $D$ access *only* data prior to Date $D$.
- **Bilateral Match Symmetry**: Balanced team-game representation prevents home/away bias.
- **Separation of Evidence and Decision**: The system delivers structured, uncertainty-aware evidence; it never attempts to replace the coach's tactical authority.

---

# SECTION 4: TACTICAL FILM EVIDENCE & QUALITATIVE VALIDATION (Slides 11–13)

## Slide 11: Quantitative Data vs Qualitative Film
### The Complementary Relationship
- **Structured Quantitative Data**: Tells us **WHAT** happened (points, shooting percentage, turnover rates, lineup ratings).
- **Qualitative Video Film**: Tells us **HOW** and **WHY** it happened (decision speed, passing reads against defensive drop coverage, closeout recovery speed, off-ball spacing discipline).
- **The Core Rule**: Never make a high-stakes decision on data alone; never make a high-stakes decision on isolated highlight clips alone.

---

## Slide 12: Inter-Rater Reliability (IRR) & Video Coding Protocol
### Structuring Video as Scientific Evidence
- **Double-Coded Protocol**: $420$ high-leverage possessions evaluated independently by multiple analysts across 4 critical action categories:
  * Pick-and-Roll Decision Making (Primary Initiators)
  * Closeout Attack & Perimeter Defense (Wings/Shooters)
  * Post Hub Gravity & Low-Block Positioning (Big Anchors)
  * Drop Coverage Navigation & Rim Contests (Rim Protectors)
- **Statistical Reliability**:
  * Action Category Agreement: **$\kappa = 1.00$** (100% perfect classification)
  * Execution Quality Agreement: **$\kappa = 0.80$** (Substantial inter-rater concordance)

---

## Slide 13: The Tactical Evidence Hierarchy
### How Film Integrates with Statistics
```
+----------------------------------------------------------------------------------------------------+
| LEVEL 1: DIRECT VIDEO OBSERVATION  | Clear film evidence from structured, double-coded possessions |
| LEVEL 2: EMPIRICAL RATE METRIC     | True shooting efficiency, turnover rate, rebound percentage   |
| LEVEL 3: MODEL-DERIVED ESTIMATE    | Predicted net impact, functional role centroid distance       |
| LEVEL 4: SPECULATIVE EXTRAPOLATION | Unverified small-sample boxscore anomalies                    |
+----------------------------------------------------------------------------------------------------+
```
- Contradiction Detection: If a player exhibits strong boxscore stats but repeatedly fails P&R reads on tape, the system automatically flags a **Tactical Contradiction Alert**.

---

# SECTION 5: SUPERVISED PREDICTIVE MODELING (Slides 14–17)

## Slide 14: Temporal Walk-Forward Validation Framework
### Why Random K-Fold Cross-Validation is Statistically Invalid in Sports
- **The Danger of Random Splitting**: In sports tournaments, random train/test splitting causes severe future information leakage (e.g. training on 2019 games to predict 2008 games).
- **Expanding Temporal Walk-Forward (17 Chronological Folds)**:
  * Fold 1: Train on 2005 EuroBasket $\rightarrow$ Test on 2006 World Cup.
  * Fold 2: Train on 2005–2006 $\rightarrow$ Test on 2007 EuroBasket.
  * ...
  * Fold 17: Train on 2005–2023 $\rightarrow$ Test on 2024 Paris Olympics.
- **Out-of-Sample Universe**: $1,105$ strictly out-of-sample evaluated matches with **zero leakage**.

---

## Slide 15: Supervised Model Benchmark Results
### 4-Tier Model Comparison under Strict Out-of-Sample Testing
```
+----------------------------------------------------------------------------------------------------+
| MODEL ARCHITECTURE       | BRIER SCORE (↓)| LOG LOSS (↓)| AUC-ROC (↑) | MAE (MARGIN)| R² SCORE (↑) |
+----------------------------------------------------------------------------------------------------+
| **Naive 50% Baseline**   | 0.2500         | 0.6931      | 0.5000      | 14.82 pts   | 0.0000       |
| **Logistic Regression**  | 0.2104         | 0.6082      | 0.7321      | 12.35 pts   | 0.2140       |
| **ElasticNet Regularized**| 0.2085        | 0.6014      | 0.7389      | 12.18 pts   | 0.2315       |
| **LightGBM (Champion)**  | **0.1967**     | **0.5741**  | **0.7613**  | **11.74 pts**| **0.2789**  |
+----------------------------------------------------------------------------------------------------+
```
- **Key Takeaway**: LightGBM captures non-linear feature interactions and achieves superior probability calibration and margin estimation without overfitting.

---

## Slide 16: Probability Calibration & Expected Calibration Error (ECE)
### Why Probability Calibration Matters to a Coach
- **The Concept**: If a model assigns a $70\%$ win probability to 100 historical games, exactly 70 of those teams should have won.
- **Calibration Result**: LightGBM achieves an outstanding **$\text{ECE} = 0.0314$** ($3.14\%$ deviation from perfect reliability).
- **Coach-Facing Meaning**: Win probabilities can be trusted as true frequency estimates, not arbitrary overconfident scores.

---

## Slide 17: Non-Parametric Statistical Inference
### Clustered Bootstrap & Permutation Testing
- **Clustered Bootstrap ($B = 5,000$ Iterations)**: Computes robust 95% Confidence Intervals for all tactical metrics, accounting for intra-tournament team correlation.
- **Permutation Tests ($P = 10,000$ Shuffles)**: Validates tactical hypothesis tests without assuming normal distributions.
- **Multiple Testing Control**: Benjamini-Hochberg False Discovery Rate (FDR) controlled at $Q = 0.05$.

---

# SECTION 6: FEATURE ATTRIBUTION & EPIDEMIOLOGICAL CAUTION (Slides 18–19)

## Slide 18: What Drives Model Predictions?
### Feature Importance Hierarchy (Permutation & SHAP)
1. **Historical Net Rating Differential**: Prior team strength over rolling 3-tournament windows ($+0.048$ importance).
2. **Effective Field Goal Differential ($\Delta eFG\%$)**: Shooting efficiency disparity ($+0.035$ importance).
3. **Turnover Percentage Differential ($\Delta TOV\%$)**: Ball security and transition prevention ($+0.024$ importance).
4. **Offensive Rebounding Differential ($\Delta ORB\%$)**: Second-chance generation ($+0.018$ importance).
5. **In-Tournament Momentum**: Recent margin of victory in group stage ($+0.012$ importance).

---

## Slide 19: The Golden Rule: Feature Importance $\neq$ Causality
### Epistemological Integrity in Sports Analytics
- **Correlation $\neq$ Intervention**: The model finding that turnover differential is predictive does *not* prove that telling players to never pass causes more wins.
- **Omitted Variable Bias**: Talent, coaching adjustments, and player health drive both stats and victories.
- **Analyst Duty**: Clearly communicate to coaching staff that statistical models identify *predictive associations*, not guaranteed causal levers.

---

# SECTION 7: TOURNAMENT MONTE CARLO SIMULATION (Slides 20–23)

## Slide 20: Why Game-Level Probabilities Are Insufficient
### Propagating Uncertainty Through Dependent Tournament Brackets
- **The Problem**: A team having a $75\%$ chance in Game 1 does not guarantee they will win a tournament. Single-elimination formats compound variance.
- **Monte Carlo Solution**: Simulating the entire tournament structure 10,000 times per tournament:
  $$P(\text{Game Win}) \longrightarrow P(\text{Advance Group}) \longrightarrow P(\text{Quarterfinal}) \longrightarrow P(\text{Semifinal}) \longrightarrow P(\text{Final}) \longrightarrow P(\text{Champion})$$

---

## Slide 21: Retrospective Historical Simulation Findings
### Validation Across 18 International Tournaments (180,000 Iterations)
```
+----------------------------------------------------------------------------------------------------+
| RETROSPECTIVE BENCHMARK METRIC        | SCORE / EMPIRICAL HIT RATE | SCIENTIFIC BENCHMARK          |
+----------------------------------------------------------------------------------------------------+
| **Champion Rank #1 Hit Rate**         | **72.2% (13 / 18)**        | Champion was #1 Pre-Tourney   |
| **Champion Top-2 Hit Rate**           | **77.8% (14 / 18)**        | Champion was #1 or #2         |
| **Champion Top-4 Hit Rate**           | **100.0% (18 / 18)**       | 100% of Champions in Top 4    |
| **Mean Rank of Actual Champion**      | **1.50**                   | Near-perfect contender capture|
| **Mean Simulated Title Probability**  | **55.05%**                 | Strong signal concentration   |
+----------------------------------------------------------------------------------------------------+
```
- **Critical Caution**: $N = 18$ tournaments is a small retrospective sample. These metrics confirm historical consistency, not universal clairvoyance.

---

## Slide 22: Probability Shrinkage & Scenario Sensitivity
### Testing Robustness to Model Overconfidence
- **Shrinkage Formula**: $p_{\text{shrunk}} = \lambda p + (1 - \lambda) 0.50$ across $\lambda \in \{0.50, 0.75, 1.00\}$.
- **Invariance Finding**: Top-1 Champion Hit Rate ($72.2\%$) and Top-4 Hit Rate ($100.0\%$) remain **100% stable across all shrinkage levels**, proving that decision support rankings do not depend on overconfident probability tails.

---

## Slide 23: Controlled Flagship Counterfactuals
### Replaying Historical Knockout Scenarios
1. **Beijing 2008 Final Replay (Spain vs USA)**: Under pre-game probability ($P(\text{ESP}) = 26.4\%$), Spain captured gold in **26.84%** of 10,000 simulated replays, quantifying the true single-elimination upset probability.
2. **EuroBasket 2015 Spain Pre-Knockout Path**: Despite dropping 2 group-stage games, Spain maintained a **67.60% model-implied title probability**, demonstrating that multi-tournament priors properly regularized group-stage noise.
3. **EuroBasket 2022 Tactical Perturbation**: Spain's title probability compressed from $72.04\% \rightarrow 66.16\%$ under $\lambda = 0.75$, demonstrating top-tier decision stability.

---

# SECTION 8: THE ANALYST DECISION SYSTEM (Slides 24–28)

## Slide 24: MVP-8 Decision System Architecture
### Synthesizing 6 Heterogeneous Layers into Auditable Dossiers
```
+----------------------------------------------------------------------------------------------------+
|                               MVP-8 COMPREHENSIVE DECISION DOSSIER                                 |
| 1. Empirical Boxscores: TS% (58.4%), PTS/40 (23.8), AST% (32.1%)                                   |
| 2. Statistical Reliability: Tier B Moderate Confidence (212 minutes)                               |
| 3. Functional Role Fit: Primary Initiator (Score: 100.0)                                          |
| 4. Qualitative Film Validation: P&R read quality (3.75 / 4.0), Zero Contradictions                 |
| 5. Predictive Model Impact: +4.2 Net Rating Shift                                                  |
| 6. Tournament Simulation Context: Contender Rank #1 (Title Prob: 72.0%)                            |
|                                                                                                    |
| FINAL RECOMMENDATION SCORE: 84.9 (RECOMMENDED) │ CONFIDENCE: TIER B │ CONTRADICTIONS: NONE         |
+----------------------------------------------------------------------------------------------------+
```

---

## Slide 25: Case Study 1 — Lorenzo Brown (EuroBasket 2022)
### Naturalized Guard Integration during Generational Rebuild
- **The Context**: Spain entered EuroBasket 2022 following the retirement of the Gasol brothers and Ricky Rubio's injury, facing an acute creator deficit.
- **The Decision Dossier**:
  * Role Fit: $100.0$ (Primary Initiator)
  * True Shooting: $TS\% = 58.4\%$
  * Recommendation Score: **`84.9` (RECOMMENDED)**
- **Historical Outcome**: Lorenzo Brown made the All-Tournament Team ($15.2$ PPG, $7.6$ APG) and led Spain to an unexpected Gold Medal.

---

## Slide 26: Case Study 2 — Pau Gasol (EuroBasket 2015)
### Interior Hub Dominance & High-Volume Efficiency
- **The Context**: Spain lacked perimeter scoring punch (Navarro and Rubio absent) and required an offense centered on interior post hub gravity.
- **The Decision Dossier**:
  * Role Fit: $85.0$ (Low-Block Anchor / Interior Scorer)
  * True Shooting: $TS\% = 64.8\%$ ($25.6$ PPG, $8.8$ RPG)
  * Video Quality: $3.75 / 4.0$ (Double-coded high agreement)
  * Recommendation Score: **`80.8` (RECOMMENDED)**
- **Historical Outcome**: Gasol won Tournament MVP (40 pts vs France in Semifinals) and led Spain to Gold.

---

## Slide 27: Case Study 3 — Ricky Rubio (World Cup 2019)
### Transition from Pure Facilitator to Tournament MVP
- **The Context**: Spain needed backcourt scoring creation alongside interior anchor Marc Gasol.
- **The Decision Dossier**:
  * Role Fit: $95.0$ (Primary Initiator / Floor General)
  * Scoring Efficiency: $TS\% = 56.2\%$ ($16.4$ PPG, $6.0$ APG)
  * Recommendation Score: **`72.2` (RECOMMENDED)**
- **Historical Outcome**: Ricky Rubio won World Cup MVP and led Spain to the World Championship.

---

## Slide 28: Case Study 4 — Calderón vs Navarro (EuroBasket 2011)
### Hyper-Efficiency vs High-Usage Scoring Creation
- **José Manuel Calderón**: $TS\% = 62.5\%$, AST/TOV $= 4.2$, Score = **`74.8`** (High efficiency, ball security).
- **Juan Carlos Navarro**: $TS\% = 54.8\%$, USG% $= 28.5\%$, Score = **`71.9`** (Volume creator, difficult shotmaker).
- **Analyst Insight**: The system identifies Calderón as the more stable floor general, while recognizing Navarro as a qualified primary creator ($S_{\text{rec}} > 70.0$). The coaching staff deployed both in tandem to win Gold.

---

# SECTION 9: CONTRADICTION SURFACING & DECISION VALIDATION (Slides 29–31)

## Slide 29: Surfacing Contradictions Rather Than Hiding Them
### The Mark of Professional Decision Support
A naive analytics report only highlights supporting data. A professional analyst actively searches for contradictory evidence:
- **Small Sample Traps**: Outstanding $TS\%$ in only 35 minutes $\rightarrow$ Flagged as *Tier C Insufficient Sample*.
- **Tactical Mismatches**: Strong offensive creation but poor P&R drop coverage containment on film $\rightarrow$ *Tactical Contradiction Alert*.
- **Role Overlap**: Accumulating three ball-dominant initiators without off-ball movement shooters $\rightarrow$ *Spacing Deficit Warning*.

---

## Slide 30: Historical Decision Validation vs Baseline Rules
### 80.0% Exact Historical Concordance (100% Contender Capture)
```
+----------------------------------------------------------------------------------------------------+
| SELECTION RULE                | HISTORICAL CONCORDANCE RATE | DECISION QUALITY                     |
+----------------------------------------------------------------------------------------------------+
| **MVP-8 Multi-Layer System**  | **80.0% (4 / 5 Decisions)** | 100% Tournament Contender Capture    |
| **Baseline Rule A (Naive PPG)**| **60.0% (3 / 5 Decisions)**| Vulnerable to inefficient volume     |
| **Baseline Rule B (Experience)**| **60.0% (3 / 5 Decisions)**| Vulnerable to age/role decline      |
+----------------------------------------------------------------------------------------------------+
```
- **Scientific Limitation**: 5 reconstructed decisions is a qualitative demonstration, not proof of causal superiority.

---

## Slide 31: Translation to Basketball Practice
### What Coaching Staff & Sporting Leadership Actually Receive
```
+----------------------------------------------------------------------------------------------------+
| WHAT A HEAD COACH RECEIVES             | WHAT A SPORTING DIRECTOR RECEIVES                         |
+----------------------------------------------------------------------------------------------------+
| • Opponent offensive scheme tendencies | • Roster functional role balance & spacing audit          |
| • P&R defensive coverage vulnerabilities| • Multi-tournament historical performance baselines       |
| • Lineup spacing & efficiency deltas   | • Age-curve & generational transition risk assessments    |
| • Uncertainty bounds on shooting form  | • Tournament simulation medal capture probabilities       |
| • Concrete questions for film sessions | • Structured candidate dossiers for selection committee   |
+----------------------------------------------------------------------------------------------------+
```

---

# SECTION 10: BOUNDARIES, WORKFLOW & CREDIBILITY (Slides 32–36)

## Slide 32: What the System Does NOT Do
### Explicit Boundaries & Epistemological Humility
```
+----------------------------------------------------------------------------------------------------+
| THE SYSTEM DOES NOT:                   | THE SYSTEM DOES:                                          |
+----------------------------------------------------------------------------------------------------+
| ✕ Replace coaches or scouts            | ✓ Structure heterogeneous evidence objectively            |
| ✕ Claim automatic causal relationships | ✓ Quantify uncertainty and small-sample variance          |
| ✕ Predict every game correctly         | ✓ Eliminate future data leakage rigorously                |
| ✕ Provide live in-game tracking        | ✓ Deliver calibrated probabilities (ECE = 0.0314)         |
| ✕ Execute transfer-market scouting     | ✓ Surface tactical contradictions transparently           |
+----------------------------------------------------------------------------------------------------+
```

---

## Slide 33: Professional Analyst Workflow
### Pre-Tournament Implementation vs Potential Live Applications
- **Implemented in Repository (Certified Pre-Game Layer)**:
  * Historical baseline profiling and Four Factors database.
  * Role discovery and Candidate Fit Index.
  * Calibrated pre-game win probabilities and Monte Carlo tournament simulation.
- **Potential Professional Application (Live Workflow)**:
  * Updating priors after group stage matches.
  * Real-time lineup performance monitoring against expected baselines.
  * Post-game tactical diagnosis and film tag integration.

---

## Slide 34: Technical Stack & Software Engineering Rigor
### Production-Grade Code Architecture
- **Core Languages & Libraries**: Python 3.14, DuckDB, Pandas, NumPy, Scikit-Learn, LightGBM, Matplotlib.
- **Automated Testing Suite**: **128 passing tests (100% pass rate in 31.8s)**.
- **Bitwise Determinism**: Master random seed `42` ensures identical simulation arrays and reproducibility.
- **Database Architecture**: DuckDB analytical warehouse with schema constraints, primary keys, and foreign keys.

---

## Slide 35: Data Leakage Prevention Architecture
### Methodological Superiority
```text
Historical Data [2005 - (T-1)] ──► Feature Engineering ──► Model Training ──► Out-of-Sample Prediction [Tournament T]
                                                                                      ▲
                                                                                      │
                                      STRICT TEMPORAL ISOLATION BARRIER ──────────────┘
```
- Zero future information leakage.
- Zero duplicate match representation across train/test splits.
- Retrospective outcomes strictly isolated as evaluation targets.

---

## Slide 36: Transparent Limitations
### 10 Explicit Constraints Acknowledged
1. Small tournament sample size ($N = 18$).
2. Small within-tournament game samples ($5–9$ games per team).
3. Roster turnover between international windows.
4. Absence of live biometric or player tracking data.
5. Qualitative video coding limited to $420$ possessions.
6. Non-linear tactical dependencies are difficult to fully capture.
7. Tournament formats evolved across 20 years.
8. Simulation probabilities are conditional on model quality.
9. Historical decision validation sample is small ($N = 5$).
10. Feature importance reflects predictive association, not causal intervention.

---

# SECTION 11: THE CORE VALUE OF THE ANALYST (Slides 37–38)

## Slide 37: The Value Chain of Basketball Analytics
### Where the Analyst Sits in the Decision Pipeline
```text
  ┌──────────────┐
  │   RAW DATA   │ ── Boxscores, play-by-play, tracking coordinates
  └──────┬───────┘
         ▼
  ┌──────────────┐
  │ INFORMATION  │ ── Cleaned, structured, normalized rate metrics
  └──────┬───────┘
         ▼
  ┌──────────────┐
  │   EVIDENCE   │ ── Statistically validated, calibrated, multi-layer observations
  └──────┬───────┘
         ▼
  ┌──────────────┐
  │   CONTEXT    │ ── Tactical roles, opponent strength, pace, tournament stakes
  └──────┬───────┘
         ▼
  ┌──────────────┐
  │ UNCERTAINTY  │ ── Bootstrap CIs, sample size tiers, contradiction alerts
  └──────┬───────┘
         ▼
  ┌──────────────┐
  │DECISION SUPP.│ ── Structured dossiers, scenario simulations, actionable trade-offs
  └──────┬───────┘
         ▼
  ┌────────────────────────────────────────────────────────┐
  │               FINAL BASKETBALL DECISION                │
  │     (Head Coach / Coaching Staff / Sporting Director)  │
  └────────────────────────────────────────────────────────┘
```

---

## Slide 38: Conclusion & Final Message
### The Professional Portfolio Summary
> *"This project is not an attempt to automate basketball decisions. It is a demonstration of how a dedicated basketball data analyst can elevate the entire decision-making process—from data to evidence, and from evidence to better decisions."*

**Core Competencies Demonstrated**:
- Data Engineering & Warehouse Architecture (DuckDB, SQL, Parquet)
- Econometric & Longitudinal Analysis (Interrupted Time Series)
- Unsupervised Role Discovery & Similarity Modeling (K-Means++, PCA)
- Qualitative Video Coding & Inter-Rater Reliability ($\kappa = 1.0 / 0.80$)
- Supervised Machine Learning & Temporal Walk-Forward Validation (LightGBM, $ECE = 0.0314$)
- Statistical Inference & Uncertainty Modeling (Bootstrap $B=5,000$, Permutation $P=10,000$, FDR)
- Monte Carlo Tournament Simulation ($180,000$ runs, Shrinkage Sensitivity)
- End-to-End Decision Support & Executive Communication

---

# SECTION 12: APPENDIX — COMPREHENSIVE INTERVIEW Q&A (Slides 39–40)

## Slide 39: Coaching & Sporting Leadership Q&A
- **Q: "How would I use this during tournament preparation?"**  
  *A*: As a pre-game baseline to understand opponent efficiency profile, primary creator tendencies, P&R coverage vulnerabilities, and lineup trade-offs.
- **Q: "What happens when the data disagrees with my video scout?"**  
  *A*: The system surfaces the contradiction as a high-priority discussion point. Data identifies volume/efficiency; film explains mechanical/tactical causes.
- **Q: "Can I trust a 75% win probability?"**  
  *A*: Yes, because the model is calibrated ($ECE = 0.0314$). A 75% probability historically won 3 out of 4 times; it also means the team loses 1 out of 4 times.

---

## Slide 40: Technical Interviewer & Lead Data Scientist Q&A
- **Q: "Why temporal walk-forward validation instead of K-Fold?"**  
  *A*: K-Fold leaks future tournament information into past training folds. Walk-forward strictly respects chronological time ($17$ expanding folds).
- **Q: "Why use Brier score instead of pure Accuracy?"**  
  *A*: Accuracy discards confidence and treats 51% the same as 99%. Brier score evaluates probability calibration and penalizes overconfident errors.
- **Q: "Why isn't feature importance causal?"**  
  *A*: Permutation importance measures how much model loss degrades when a feature is shuffled. It identifies predictive association, not the counterfactual effect of an exogenous coaching intervention.
- **Q: "How do you guarantee reproducibility?"**  
  *A*: Master seed `42`, deterministic DuckDB transformations, and 128 automated unit/integration tests running in under 35 seconds.
