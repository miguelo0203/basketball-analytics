🏀 International Basketball Analytics (2005–2024)
Decision Support & Quantitative Scouting System for Professional Basketball

How can analytics support coaching and front-office decisions in high-stakes basketball without creating information overload?

I developed an end-to-end sports analytics platform spanning 20 years of international competitions (18 FIBA tournaments, 1,145 games, 27,353 player boxscores). The objective is not to replace coaching intuition, but to provide actionable, evidence-based decision support:

🔹 Data Engineering: Validated 1,145 official match boxscores into an embedded DuckDB relational warehouse with strict mathematical checks (200 min/game invariant).
🔹 Statistical Inference: Discovered 6 functional player archetypes across 3,767 campaigns using K-Means++ & PCA, applying Bayesian shrinkage (λ=0.75) to stabilize tournament shooting noise.
🔹 Calibrated Machine Learning: Evaluated LightGBM models across 17 expanding walk-forward folds without data leakage (Brier Score: 0.1967 | ECE: 0.0314 | 180,000 Monte Carlo simulations).
🔹 Tactical Decision Support: Generated 1.5-page pre-game coaching briefs and an interactive Streamlit workspace with strict anti-hindsight outcome quarantine.

Backed by 227 automated tests in Pytest (100% pass rate) and full local reproducibility.

🔗 Repository: https://github.com/miguelo0203/basketball-analytics
