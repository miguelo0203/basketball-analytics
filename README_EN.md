[🇬🇧 English](README_EN.md) | [🇪🇸 Español](README.md)

# 🏀 International Basketball Analytics (2005–2024)
> **Comprehensive decision-support and quantitative analytics system covering 20 years of senior men's FIBA tournaments (18 official tournaments, 1,145 matches, 2,290 team performances, 27,353 player box scores).**

```text
WHO:         Miguel — Data Analyst | Basketball Analytics
WHAT:        Decision-Support & Quantitative Analytics System for International Basketball
WHY:         Grounded, interpretable, and calibrated evidence for coaching staffs and sporting directors
SCOPE:       18 Tournaments (2005–2024: EuroBasket, FIBA World Cup, Olympic Games — 1,145 games, 2,290 team games)
TECHNOLOGY:  Python, DuckDB, Polars, Scikit-Learn, Streamlit, R (tidyverse, ggplot2)
OUTPUT:      1.5-page pre-game coaching briefs and anti-hindsight interactive workspace
LIMITATION:  Statistical uncertainty reduction tool; does not replace coach basketball expertise
```

[![DuckDB](https://img.shields.io/badge/OLAP_Store-DuckDB-yellow.svg)](https://duckdb.org/)
[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-Tidyverse%20%7C%20ggplot2-276DC3.svg)](R/README_EN.md)
[![Machine Learning](https://img.shields.io/badge/ML-Calibrated_Walk--Forward_Validation-orange.svg)](https://scikit-learn.org/)
[![Pytest](https://img.shields.io/badge/pytest-227%20passed%20(100%25)-brightgreen.svg)](tests/)
[![Sports Analytics](https://img.shields.io/badge/Domain-Basketball%20Analytics-red.svg)](https://github.com/miguelo0203)

---

## 🚀 Start Here

*New to this project?*
1. 👔 **[Executive Case Studies (English)](portfolio/README_EN.md)** | **[Casos de Estudio Ejecutivos (Español)](portfolio/README.md)**: 4 core dossiers covering tactical decisions, OLAP data engineering, calibrated ML, and longitudinal shooting.
2. 📄 **[Sample Pre-Game Tactical Briefs (1.5 Pages)](reports/mvp5_player_briefs/andreas_obst_1996_worldcup_2023_scouting_brief.md)**: Editorial decision-support deliverable format designed for coaching staffs.
3. 📊 **[Executive Presentation Deck (PDF)](presentation/International_Basketball_Analytics_Presentation.pdf)**: Complete slide deck detailing system architecture and findings.
4. 🔬 **[DuckDB Architecture & Data Pipeline](#-technical-architecture--reproducibility)**: Embedded OLAP data mart, ML predictive models, and statistical inference.

---

## 📌 What is this? (The Professional Problem)

This repository contains an **end-to-end analytics and decision-support system for international basketball**, built upon two decades of senior men's FIBA official competitions (EuroBasket, FIBA World Cup, and Olympic Games between 2005 and 2024).

Analyzing **18 official tournaments, 1,145 games, 2,290 team performances, and 27,353 individual player performances**, the system converts raw box scores and play-by-play events into:
- **Concise 1.5-page pre-game coaching briefs** for national team staffs.
- **A high-performance embedded DuckDB OLAP analytical store**.
- **Supervised win probability models with strict walk-forward temporal validation** and probability calibration.
- **Monte Carlo full-tournament simulations** and counterfactual matchup scenario analysis.

---

## 🏆 Key Results (Audited Project Scale)

- ⚡ **OLAP Data Engineering & Performance**: Automated ingestion and deterministic validation of 27,353 player records, executing multi-table analytical aggregations in **<15 milliseconds on DuckDB**.
- 🔮 **Calibrated Predictive Modeling**: Supervised game outcome prediction using strict walk-forward temporal validation (zero future data leakage), achieving an audited **Brier score of 0.1872** and excellent probability calibration.
- 🧠 **Tactical Model Interpretability (SHAP Values)**: Quantitative breakdown of Four Factors feature contributions for individual game predictions.
- 🎲 **Monte Carlo Tournament Simulator**: 10,000-iteration bracket simulation engine projecting medal probabilities and counterfactual tactical scenarios.
- 🟢 **Comprehensive Test Suite**: **227 automated tests (100% passing in Pytest)** enforcing ball math consistency, temporal continuity, minute conservation, and schema integrity.

---

## 🛠️ What I Built (Technical Architecture)

1. **Modular Ingestion & Quality Pipeline**: Python architecture (`src/acquisition`, `src/parsers`, `src/validation`) featuring automated entity resolution for players and national teams.
2. **DuckDB Analytical Mart**: Dimensional schema (`src/storage/schema.py`) with analytical team and player aggregation views.
3. **Advanced Analytics & ML Modules**: Tactical archetype clustering, predictive match models, tournament simulation, and decision engines (`src/analytics/`).
4. **Interactive Streamlit Workspace**: Web interface for pre-game brief exploration and decision auditing (`src/analytics/mvp10_analyst_workspace.py`).
5. **Editorial Visualizations & R ggplot2**: Publication-quality analytical visualization pipeline in R (`R/analysis/`) and brief compilation.

---

## 🎯 Why It Matters (From Raw Data to Coaching Question)

International tournament basketball presents distinct analytical challenges: small sample sizes, brief preparation windows, and high game-to-game variance. This system demonstrates how to build a disciplined analytics framework that filters out statistical noise and provides coaching staffs with robust, actionable tactical signals.

---

## 🧭 Project Navigation

### 👔 Executive View (Coaches, Scouts & Sporting Directors)
- 📚 [Portfolio Hub & Case Studies (English)](portfolio/README_EN.md) | [Hub de Portfolio (Español)](portfolio/README.md)
- 📄 [Pre-Game Player Briefs (Scouting)](reports/mvp5_player_briefs/)
- 📊 [Executive Presentation Deck in PDF](presentation/International_Basketball_Analytics_Presentation.pdf)
- 📋 [Core Case Studies](portfolio/case_studies/)

### 🔬 Technical View (Data Scientists & Engineers)
- `src/`: Modular Python source code (ingestion, metrics, ML models, simulation).
- `data/`: Processed datasets and DuckDB database files.
- `R/`: Statistical analysis and visualization pipeline in R (`R/README_EN.md`).
- `tests/`: Complete 227-test automated Pytest suite.
- `reports/`: Comprehensive catalog of technical MVP reports and audits.

---

## 📂 Repository Structure

```text
basketball-analytics/
├── README.md                           # Project presentation (Spanish)
├── README_EN.md                        # Project presentation (English)
├── run_project.py                      # Full pipeline execution script
├── config/                             # Tournament manifests and FIBA rulesets
├── data/                               # DuckDB database and processed datasets
│
├── portfolio/                          # Presentation hub and case studies
│   ├── README.md                       # Portfolio index (Spanish)
│   ├── README_EN.md                    # Portfolio index (English)
│   ├── index.md                        # Portfolio case studies index
│   ├── case_studies/                   # 4 Executive case studies
│   ├── job_search/                     # Candidate profiles and skills matrices
│   └── presentation/                   # Slide decks and summaries
│
├── presentation/                       # Executive slide deck (PDF & PPTX)
│   ├── README.md                       # Presentation index (Spanish)
│   ├── README_EN.md                    # Presentation index (English)
│   └── International_Basketball_Analytics_Presentation.pdf
│
├── R/                                  # R analytical and visualization pipeline
│   ├── README.md                       # R module documentation (Spanish)
│   ├── README_EN.md                    # R module documentation (English)
│   ├── analysis/                       # Longitudinal & Four Factors analysis scripts
│   └── functions/                      # Auxiliary R functions
│
├── reports/                            # Technical reports, briefs, and audits
│   ├── README.md                       # Reports index (Spanish)
│   ├── README_EN.md                    # Reports index (English)
│   ├── figures/                        # Visual charts and plots
│   └── mvp5_player_briefs/             # Sample pre-game scouting briefs
│
├── src/                                # Python source code
│   ├── acquisition/                    # Scraping and rate limiting
│   ├── analytics/                      # ML, simulation, briefs & inference
│   ├── domain/                         # Data models and business rules
│   ├── ingestion/                      # ETL pipelines
│   ├── metrics/                        # Four Factors, Pace, Ratings
│   ├── normalization/                  # Entity resolution
│   ├── parsers/                        # Box-score parsers
│   ├── storage/                        # DuckDB schema and storage
│   └── validation/                     # Data quality and ball math
│
└── tests/                              # 227-test automated Pytest test suite
```

---

## 👤 Author & Contact

**Miguel** — Data Analyst | Basketball Analytics  
- **GitHub**: [@miguelo0203](https://github.com/miguelo0203)
- **LinkedIn**: [linkedin.com/in/miguelo0203](https://www.linkedin.com)

---
*Reproducible international basketball analytics system built with Python, DuckDB, R, and Streamlit.*
