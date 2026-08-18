# Portfolio Case Study: International Basketball Historical Analytics (2005–2025)

---

## 1. Executive Summary

This project builds an end-to-end historical data warehouse, validation pipeline, and analytical suite covering **20 years of international men's basketball** (19 major FIBA EuroBasket, World Cup, and Olympic tournaments; 1,203 games; 2,406 team boxscores; ~26,000 player performances).

Focused on the Spanish Men's National Team ("La Familia") across its golden era and generational transition, the project demonstrates technical excellence across data engineering, relational modeling (DuckDB), data quality assurance, metric epistemology, and rigorous statistical methodology.

---

## 2. Key Engineering & Analytical Highlights

1. **4-Tier Data Pipeline with Strict Lineage**:
   - `RAW` $\rightarrow$ `STAGING` $\rightarrow$ `VALIDATED` $\rightarrow$ `ANALYTICS`.
   - Immutable raw payloads with SHA-256 content hashes and parser version tracking.
2. **Domain-Specific Quality Assurance Engine**:
   - Automated accounting assertions for basketball ball-math ($PTS = 2 \times 2PM + 3 \times 3PM + FTM$).
   - Exact FIBA minute accounting in regulation and overtime ($200 + 25 \times \text{OT}$ player-minutes per team).
3. **Deterministic Entity Resolution**:
   - Resolved multi-affiliation edge cases (changing federations, naturalized players, transliterated names) through a deterministic-first pipeline with explicit confidence scoring (`EXACT`, `DETERMINISTIC`, `MANUAL`).
4. **Methodological Rigor**:
   - **No Causal Over-Claims**: Replaced invalid DiD proposals with Interrupted Time Series (ITS) regression for the 2010 3-point line expansion.
   - **Unbiased Player Clustering**: Excluded raw height and collinear volume features from unsupervised learning to discover true functional play styles, formally evaluating $k$ across Silhouette, Calinski-Harabasz, Davies-Bouldin, and bootstrap stability.
   - **Leak-Free Predictive Modeling**: Implemented `available_as_of` temporal filters and atomic Leave-One-Tournament-Out (LOTO) cross-validation evaluating Brier Score, calibration curves, and SHAP feature contributions.

---

## 3. Tech Stack

- **Storage & Query Engine**: DuckDB, SQL, Parquet, PyArrow
- **Data Engineering**: Python, Polars, Pandas, Pydantic v2
- **Statistical Modeling & ML**: Scikit-Learn, Statsmodels, Scipy
- **Testing & Quality Assurance**: Pytest (Offline deterministic test suite)
- **Reporting & Visualisation**: Quarto, Plotly, Seaborn / Matplotlib
