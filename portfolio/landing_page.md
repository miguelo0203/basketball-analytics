# Basketball Analytics — Decision Support for Coaching
### Turning basketball data into interpretable evidence for better decisions.

---

## The Problem

Coaching staffs and sporting directors face information overload, small-sample shooting noise, and hindsight bias. Raw statistics fluctuate rapidly, and naive machine learning models often act as opaque black boxes that claim to replace human decision-making. 

---

## The Approach

This project demonstrates a disciplined analytical philosophy:
$$\text{DATA} \longrightarrow \text{ANALYSIS} \longrightarrow \text{EVIDENCE} \longrightarrow \text{CONTEXT} \longrightarrow \text{DECISION SUPPORT}$$

The analyst's role is not making the decision or prescribing lineups. The analyst's role is organizing competing evidence, quantifying uncertainty, surfacing hidden contradictions between statistical models and video film, and formulating actionable questions for coaching staff discussion.

---

## What I Built

- **Relational Data Warehouse**: Certified DuckDB database spanning 18 international tournaments, 1,145 matches, and 27,353 player-games (2005–2024).
- **Player Role Discovery**: K-Means++ and PCA clustering 3,767 qualified player campaigns into 6 functional archetypes.
- **Tactical Video Coding**: 420 double-coded possession events ($\kappa = 0.80$) evaluating P&R drop depth and closeout contest speed.
- **Calibrated Machine Learning**: Expanding 17-fold chronological walk-forward validation ($1,105$ out-of-sample games, LightGBM $\text{Brier} = 0.1967$, $\text{ECE} = 0.0314$).
- **Monte Carlo Simulations**: 180,000 tournament iterations propagating probabilistic bracket uncertainty.
- **Analyst Decision Workspace**: Interactive Streamlit interface with a strict anti-hindsight barrier, contradiction engine, and automated pre-game coaching brief generator.

---

## Flagship Demonstration: Beijing 2008 Olympic Final (Spain vs. USA)

- **Pre-Game State**: Calibrated model assigned USA a $73.2\%$ win probability (Expected Margin: $-8.5$ pts).
- **Contradiction Surfaced**: USA transition scoring dominance vs. Spain's $+4.2$ half-court paint efficiency and USA's vulnerability in P&R drop coverage against pick-and-pop trailers.
- **Coaching Brief**: Actionable questions on deploying a 2-3 zone and pick-and-pop sets.
- **Outcome & Process Review**: USA won 118–107 (within 95% bootstrap CI). Spain deployed the 2-3 zone, exploited pick-and-pop pockets, and trailed by only 4 with 2:20 remaining.

---

## Technical Stack & Architecture

- **Core Analytics & Data Engineering**: Python, SQL, DuckDB, Parquet, Pandas.
- **Modeling & Inference**: Scikit-Learn, LightGBM, TreeSHAP, Clustered Bootstrap ($B=5,000$), Permutation Tests ($P=10,000$).
- **Interface & Operational UI**: Streamlit, Matplotlib.
- **Testing & Verification**: Pytest (195 automated tests passing with 100% pass rate).

---

## Limitations & Professional Boundaries

- **Historical Scope**: Covers 18 completed tournaments (2005–2024); does not simulate live transfer markets.
- **Sample Sizes**: International tournaments feature small samples (6–9 games); shooting metrics carry natural variance.
- **Tactical Video**: Video coding layer ($N=420$) is an exploratory qualitative sample, not an exhaustive census.
- **No Causal Claims**: Feature attributions describe historical conditional associations, not guaranteed causal levers.

---

## How to Explore This Repository

```bash
# Launch interactive Streamlit Analyst Decision Workspace
streamlit run src/analytics/mvp10_analyst_workspace.py -- streamlit

# Execute complete 195-test regression suite
python -m pytest tests -q
```

- **[Master Case Studies](file:///f:/España2005-2025/portfolio/index.md)**
- **[32-Question Interview Guide & Answers](file:///f:/España2005-2025/reports/mvp12/interview_answers.md)**
- **[Methodology Guide for Non-Technical Readers](file:///f:/España2005-2025/reports/mvp12/methodology_summary.md)**
- **[Claim Usage & Governance Guide](file:///f:/España2005-2025/reports/mvp12/claim_usage_guide.md)**
- **[40-Slide Master Presentation Deck](file:///f:/España2005-2025/reports/presentation/mvp9_analyst_portfolio_presentation.md)**

---

## Contact & Professional Profile
* **Role**: Basketball Data Analyst / Scouting Analytics / Sporting Decision Support  
* **GitHub**: `github.com/miguelo0203/basketball-analytics`  
* **Perfil**: Basketball Data Analyst | Quantitative Scouting | Sports Decision Support
