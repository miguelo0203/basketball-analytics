# CV Project Entries — International Basketball Analytics

This document provides ready-to-use, tailored CV bullet points for applications in Sports Analytics, Data Science, and Basketball Operations.

---

## Version A — Technical CV (Data Science & Analytics Engineering)

**International Basketball Analytics Platform | Python, R, DuckDB, Parquet, ML, Pytest**  
*Lead Developer & Analytics Engineer* | [github.com/miguelo0203/basketball-analytics](https://github.com/miguelo0203/basketball-analytics)

- **Data Engineering & Lakehouse Architecture**: Architected a medallion relational warehouse in DuckDB and Apache Parquet covering 20 years of international basketball (1,145 games, 27,353 player-game records, 2,124 unique players), enforcing 200 min/game mathematical invariant checks and SHA-256 raw data provenance.
- **Leakage-Free Predictive Modeling**: Built an out-of-sample prediction pipeline evaluated across 17 expanding walk-forward temporal folds (1,105 test games); trained and calibrated LightGBM models with isotonic regression, achieving a Brier Score of `0.1967`, Expected Calibration Error (ECE) of `0.0314` (3.14%), and spread MAE of `11.74 pts`.
- **Statistical Inference & Simulation**: Implemented cluster bootstrap confidence intervals ($B = 5,000$) in R and developed a 180,000-iteration Monte Carlo tournament engine with Bayesian probability shrinkage ($\lambda = 0.75$) to simulate full conditional bracket advancement distributions.
- **Testing, CI/CD & Reproducibility**: Engineered a comprehensive test suite of 227 automated tests in Pytest (100% pass rate) and a unified zero-overhead CLI runner executing data verification, R statistical reporting, and model validation in under 2 minutes.

---

## Version B — Basketball Analytics CV (Scouting & Decision Support)

**International Basketball Analytics Platform | Tactical Support & Quantitative Scouting**  
*Basketball Data Analyst* | [github.com/miguelo0203/basketball-analytics](https://github.com/miguelo0203/basketball-analytics)

- **Tactical Decision Support & Pre-Game Briefs**: Designed an automated 1.5-page executive pre-game briefing system translating Dean Oliver Four Factors, opponent pick-and-roll defensive drop coverage alerts, and pace targets ($\le 72$ possessions) into actionable game-plan questions for coaching staffs.
- **Quantitative Scouting & Role Discovery**: Uncovered 6 objective functional player archetypes (Primary Initiator, Floor Spacer, Interior Hub, Floor General, Defensive Anchor, Balanced Wing) via K-Means++ and PCA across 3,767 qualified campaigns ($\ge 40$ min), replacing rigid 1–5 positions with true skill profiles.
- **Small-Sample Shooting Stabilization**: Applied empirical Bayesian shrinkage ($\lambda = 0.75$) to short tournament shooting samples (6–9 games) to separate true shooting talent from short-term hot streaks, eliminating recruitment risk and overpayment on tournament variance.
- **Anti-Hindsight Interactive Workspace**: Built an operational Streamlit analyst workspace featuring a strict temporal barrier that quarantines post-game boxscores and outcomes, ensuring all tactical evaluations and probabilities reflect information available strictly prior to tip-off.
