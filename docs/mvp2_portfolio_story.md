# Project Portfolio Story: 20 Years of International Basketball Analytics
## Historical International Basketball Analytics (2005–2025)

--------------------------------------------------
1. THE CORE PROBLEM & VISION
--------------------------------------------------

Most public sports analytics portfolio projects suffer from three fatal flaws:
1. **Shallow Data Engineering**: Scraping a pre-packaged CSV without verifying ball-math accounting or historical provenance.
2. **Methodological Causal Overreach**: Claiming "X caused Y" using naive regressions or misapplying Difference-in-Differences to global policy shifts that lacked a control group.
3. **Lack of Domain Reality**: Treating basketball as an abstract table of numbers without accounting for regulatory shifts (court dimensions, shot clocks, overtime mechanics).

This project was built from the ground up to demonstrate how a **Senior Sports Data Engineer and Quantitative Analytics Researcher** constructs an enterprise-grade, publication-defensible sports data system from raw historical web archives to inferential econometric modeling.

--------------------------------------------------
2. THE ENGINEERING FOUNDATION (MVP-0 to MVP-1)
--------------------------------------------------

### A. Immutable RAW Provenance & Cryptographic Traceability
- Acquired and validated **18 major senior men's international tournaments** across 2005–2025:
  - 8 FIBA EuroBaskets
  - 5 FIBA Basketball World Cups
  - 5 Men's Olympic Basketball Tournaments
- Every raw match archive is stored immutably with a verified SHA-256 cryptographic hash.
- Run A vs Run B bitwise warehouse reproducibility was certified with identical checksum:  
  `0b73195cb357dd8db5b6fb5dc201ec73a7b4b7ccdd0591b052c58d4f8296ef07`.

### B. Relational Star Schema in DuckDB
- Modeled inside `data/03_validated/basketball_analytics.duckdb`:
  - **1,145 games** (`fact_game`)
  - **2,290 team-game boxscores** (`fact_team_game`)
  - **100.0% coverage with 0 missing games and 0 duplicate records**.

### C. Automated Data Quality Gatekeeper (`QAEngine`)
- **Ball-Math Verification**: $PTS = 2 \times 2PM + 3 \times 3PM + FTM$ enforced across all 2,290 team-games (0 violations).
- **Minute Accounting**: Exact match for regulation and overtime $(200 + 25 \times \text{OT}) \times 60$ seconds (0 violations).
- **Epistemology Isolation**: Explicit tracking of metrics as `OBSERVED`, `DERIVED`, `ESTIMATED` (Dean Oliver $0.44$ bilateral possessions), and `MODELED`.

--------------------------------------------------
3. FLAGSHIP RESEARCH: THE 2010 3-POINT ARC SHIFT
--------------------------------------------------

### A. The Analytical Challenge
On October 1, 2010, FIBA moved the international 3-point line back from 6.25m to 6.75m (+50 cm).  
Many commentators claimed this caused an irreversible drop in perimeter scoring.

### B. The Methodological Breakthrough
- **Why Difference-in-Differences Fails**: FIBA applied the rule globally across all federations simultaneously. There was no unexposed control group.
- **The Correct Design**: **Interrupted Time Series (ITS) with Segmented Linear Regression** and tournament-clustered Newey-West standard errors.

### C. The Empirical Finding
- **Immediate Level Shock**: Moving the line back caused a statistically significant immediate drop of **$-0.462$ percentage points** in 3-point attempt rate ($z = -7.21, p < 0.0001, 95\%\text{ CI } [-0.588\%, -0.337\%]$).
- **Secular Resilience**: Post-2010 tactical adoption resumed positive growth at **$+0.041\%$ per tournament**, proving that global analytics-driven spacing principles overwhelmed court geometry friction by 2019.
- **Sensitivity Confirmation**: The finding survived 7 alternative specifications (excluding overtimes, excluding blowouts, tournament-level aggregation, and robust covariance estimators).

--------------------------------------------------
4. TECHNICAL SUMMARY
--------------------------------------------------

- **Language & Tech Stack**: Python 3.14, DuckDB, Pydantic, Statsmodels, Scipy, Matplotlib, Pytest.
- **Automated Test Suite**: 60 certified tests covering unit config, domain schema, adversarial edge cases, QA minute rules, entity resolution, and coverage closure.
- **Reproducibility**: 100% deterministic end-to-end pipeline execution.
