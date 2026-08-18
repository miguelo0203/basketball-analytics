# Professional Boundary Specification: Demonstrated vs. Simulated vs. Not Yet Demonstrated
## International Basketball Historical Analytics (2005–2025)

**Status**: Formally Certified Professional Boundary Document  
**Ethical Principle**: Transparently distinguishing portfolio capabilities from claimed professional club employment.  

---

# 1. Demonstrated Capabilities (Implemented & Reproducible)

These elements are **physically implemented, tested, and deterministically reproducible** in this repository:

1. **Relational Data Warehouse & Provenance**:
   - Certified DuckDB database ($12$ tables, $1,145$ matches, $27,353$ player-games) backed by immutable raw FIBA source files with SHA-256 validation.
2. **Longitudinal Econometrics & Interrupted Time Series**:
   - Econometric analysis evaluating the 2010 FIBA 3-point line expansion on shooting efficiency and spacing.
3. **Statistical Player Role Clustering**:
   - K-Means++ and PCA dimensionality reduction clustering $3,767$ qualified campaigns into 6 functional archetypes.
4. **Expanding Temporal Walk-Forward Machine Learning**:
   - 17-fold chronological walk-forward cross-validation ($1,105$ out-of-sample matches) preventing future leakage.
5. **Probability Calibration & Non-Parametric Inference**:
   - Out-of-sample Isotonic Regression probability calibration ($\text{ECE} = 0.0314$, $\text{Brier} = 0.1967$) and clustered bootstrap resampling ($B = 5,000$).
6. **Monte Carlo Tournament Simulation**:
   - $180,000$ tournament simulations with probability shrinkage ($\lambda \in \{0.50, 0.75, 1.00\}$) and counterfactual replays.
7. **Automated Quality Gate Testing**:
   - 169 automated pytest regression tests passing with 100% pass rate.

---

# 2. Simulated Operational Workflow (Using Historical Data)

These elements demonstrate **how an analyst operates in a professional environment** using the historical dataset:

1. **Pre-Game Coaching Staff Brief Generator**:
   - Automatically generates structured 1-to-2 page tactical pre-game briefs (Executive Summary, Strongest Evidence, Film Notes, Staff Questions).
2. **Anti-Hindsight Historical Match Replay Workspace**:
   - An interactive Streamlit interface that isolates pre-game information states ($T-30$, $T-7$, $T-1$, Game Day) and hides final scores until user reveal.
3. **Contradiction Detection Engine**:
   - Automated detection of discrepancies between statistical model favorites and qualitative video film vulnerabilities.
4. **Post-Game Process Review Protocol**:
   - Evaluates pre-game evidence quality and uncertainty calibration rather than relying on outcome bias.
5. **Structured Qualitative Video Coding Protocol**:
   - Double-coded film analysis on 420 possession events across 36 games proving substantial inter-rater reliability ($\kappa = 0.80$).

---

# 3. Not Yet Demonstrated (Requiring Real Club Access / Operational Employment)

The project **explicitly does NOT claim** experience in the following areas:

- **Live Optical Tracking (Second Spectrum / Synergy Telemetry)**: Processing real-time high-frequency XYZ player coordinate streams.
- **Wearable Biometric / GPS Load-Monitoring**: Physical fatigue, Catapult GPS, and heart-rate telemetry.
- **Live In-Game Bench Decision Support**: Real-time tactical communication between quarters during an active match.
- **Actual Club Roster Construction & Contract Negotiations**: Salary caps, buyout clauses, agent negotiations, and domestic transfer markets.
- **Proprietary Internal Club Video Databases**: Integration with internal team-specific video tagging workflows (Sportscode/Hudl).
- **Claim of Autonomous Coaching Decisions**: The system provides decision-support evidence; human coaches make basketball decisions.
