# International Basketball Analytics (2005–2024)
## Decision Support & Quantitative Scouting System for Professional Basketball

> **Author**: Miguel  
> **Role Target**: Basketball Data Analyst | Quantitative Scouting | Sports Analytics Engineer  
> **Repository**: [github.com/miguelo0203/basketball-analytics](https://github.com/miguelo0203/basketball-analytics)

---

## One-Line Value Proposition

An end-to-end basketball analytics pipeline and decision-support system that transforms 20 years of international tournament data into pace-neutral evidence, calibrated probabilities, and 1.5-page pre-game coaching briefs.

---

## The Problem

In high-stakes basketball competitions and short international tournaments (6–9 games over 15 days), coaching staffs and front offices face three critical challenges:
1. **Small-Sample Shooting Noise**: Unstabilized 3PT% and plus-minus over 7 games distort true player evaluation and risk poor tactical or recruitment decisions.
2. **Information Overload**: 30-page raw statistical packets overwhelm coaches who have less than 48 hours to prepare game plans.
3. **Hindsight Bias & Data Leakage**: Post-game rationalizations evaluate tactics solely on whether the final shot went in, while predictive models often contaminate training folds with future information.

---

## The Solution

I engineered a modular, reproducible sports analytics platform that bridges the gap between relational data warehousing, calibrated machine learning, non-parametric statistical inference, and court-level coaching decisions:
- **Data Engineering Layer**: Ingests and validates 1,145 official match boxscores into an embedded DuckDB OLAP warehouse with strict mathematical checks (200 min/game invariant).
- **Longitudinal Inference & Archetypes**: Discovers 6 functional player archetypes using K-Means++ and PCA across 3,767 qualified campaigns, applying Bayesian shrinkage ($\lambda = 0.75$) to stabilize short-sample shooting.
- **Calibrated Predictive Engine**: Trains LightGBM models over 17 expanding walk-forward temporal folds, achieving probability calibration certified by isotonic regression.
- **Decision-Support Interface**: Generates automated 1.5-page pre-game coaching briefs and powers an interactive Streamlit workspace with an anti-hindsight quarantine barrier.

---

## Technical Stack

| Component | Technologies Used |
|---|---|
| **Data Warehouse & Storage** | DuckDB (Embedded OLAP), Apache Parquet, SQL |
| **Analytics & Modeling (Python)** | Python 3.10+, LightGBM, Scikit-learn, Pandas, NumPy, Streamlit |
| **Statistical Inference (R)** | R 4.4+, Tidyverse (`dplyr`, `tidyr`), `ggplot2`, Quarto CLI |
| **Testing & Quality Assurance** | Pytest (227 automated tests, 100% pass rate) |
| **Presentation & Reporting** | ReportLab (PDF), `python-pptx`, Markdown, LaTeX |

---

## Verified Project Scale & Evidence

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              VERIFIED REPOSITORY METRICS                               │
├───────────────────────────────────┬────────────────────────────────────────────────────┤
│ Historical Coverage               │ 20 Years (2005–2024: EuroBasket, World Cup, OLY)   │
│ Official Matches Analyzed         │ 1,145 International games                          │
│ Player-Game Observations          │ 27,353 Clean individual records                    │
│ Canonical Players Tracked         │ 2,124 Unique athletes                              │
│ Qualified Player Campaigns        │ 3,767 Tournament campaigns (>= 40 min played)      │
│ Functional Player Archetypes      │ 6 Unsupervised clusters (K-Means++ & PCA)          │
│ Temporal ML Validation            │ 17 Expanding walk-forward folds (1,105 test games) │
│ Out-of-Sample Calibration         │ Brier Score: 0.1967 | ECE: 0.0314 | MAE: 11.74 pts │
│ Stochastic Tournament Projections │ 180,000 Monte Carlo bracket simulations            │
│ Automated Test Suite              │ 227 Unit/Integration tests in Pytest (100% pass)   │
└───────────────────────────────────┴────────────────────────────────────────────────────┘
```

---

## Basketball Output & Decision Flow

$$\text{RAW DATA (DuckDB)} \longrightarrow \text{EVIDENCE (Four Factors \& ML)} \longrightarrow \text{TACTICAL CONTEXT} \longrightarrow \text{COACHING BRIEF (1.5 Pages)}$$

1. **Dean Oliver Four Factors**: Pace-neutral evaluation of effective shooting ($eFG\%$), turnover control ($TOV\%$), offensive rebounding ($ORB\%$), and free throw rate ($FTR$).
2. **Tactical Coaching Briefs**: Executive 1.5-page summaries designed for 2.5-minute reads, highlighting opponent P&R defensive drop tendencies and pace thresholds.
3. **6 Functional Player Archetypes**: Objective roles (Primary Initiator, Floor Spacer, Interior Hub, Floor General, Defensive Anchor, Balanced Wing) replacing rigid 1–5 positions.
4. **Stochastic Tournament Bracket Engine**: Simulates entire tournament trees rather than fragile single-winner picks, accounting for matchup variance.
5. **Anti-Hindsight Workflow**: Isolates pre-game evidence ($T-30$, $T-7$, $T-1$) from ground-truth match outcomes to ensure unbiased decision auditing.

---

## Flagship Case Study: Beijing 2008 Final (Spain vs. USA)

- **The Challenge**: How to prepare Spain to compete against the dominant USA *Redeem Team* after suffering a 37-point blowout ($82\text{–}119$) in the group stage.
- **Quantitative Signal**: In half-court 5v5 sets, Spain held a $+4.2$ Net Rating advantage through Pau and Marc Gasol; defensive leakage occurred exclusively on live-ball transition ($1.25$ PPP allowed).
- **Tactical Contradiction**: US centers executed a deep drop in pick-and-roll coverage to protect the paint, conceding uncontested pick-and-pop perimeter attempts.
- **Actionable Game Plan**: Limit game pace to $\le 72$ possessions, implement a 2-3 zone defense immediately after made baskets, and exploit the deep drop with pick-and-pop 3-pointers from Pau Gasol, Marc Gasol, and Jorge Garbajosa.
- **Outcome**: Spain executed the game plan, cut the deficit to 4 points ($108\text{–}104$) with 2:20 remaining, and delivered one of the closest finals in Olympic history ($107\text{–}118$).

---

## Key Project Links

- 📁 **[Public GitHub Repository](https://github.com/miguelo0203/basketball-analytics)**
- 📑 **[Executive Presentation (PDF 16:9 Panorámico)](../presentation/International_Basketball_Analytics_Presentation.pdf)**
- 📊 **[Executive Presentation (.pptx)](../presentation/International_Basketball_Analytics_Presentation.pptx)**
- 🏀 **[Flagship Case Study (Beijing 2008)](case_studies/case_01_tactical_decision_support.md)**
- 📚 **[Portfolio Case Studies Hub](case_studies/README.md)**
- ⚙️ **[Reproducibility Guide](../REPRODUCIBILITY.md)**
