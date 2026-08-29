[🇬🇧 English](README_EN.md) | [🇪🇸 Español](README.md)

# 📊 R Analytics & Visualization Module

This directory contains the reproducible quantitative analytics and publication-grade visualization suite supporting the International Basketball Analytics system.

---

## 🏗️ Dual Architecture: Python + R on DuckDB

The pipeline leverages a hybrid analytical architecture:
1. **Data Layer & OLAP in DuckDB**: Ingestion, cleaning, entity resolution, and high-performance embedded storage in DuckDB.
2. **Machine Learning & Modeling in Python**: Supervised ML models (Scikit-Learn, LightGBM), SHAP interpretability, and Monte Carlo tournament simulations.
3. **Statistical Modeling & Visuals in R (`tidyverse`, `ggplot2`)**: Native connection to DuckDB via `DBI` and `duckdb` for multi-tournament longitudinal trends, Dean Oliver's Four Factors, and editorial graphics.

---

## 📂 File Structure

- `analysis/01_eda_tournaments.R`: Exploratory data analysis across 18 FIBA tournaments.
- `analysis/02_player_longitudinal_analysis.R`: Two-decade longitudinal player trajectories and percentiles.
- `analysis/03_role_stability.R`: Tactical archetype stability and rotation balance.
- `analysis/04_team_four_factors.R`: Dean Oliver's Four Factors and win correlation analysis.
- `analysis/05_player_distributions.R`: True Shooting ($TS\%$) and usage distributions.
- `analysis/06_statistical_validation.R`: Hypothesis testing and bootstrap confidence intervals.
- `functions/metrics.R`: Standardized Four Factors, Pace, and Rating formulas.
- `functions/validation.R`: Mathematical validation and minute conservation checks.
- `functions/visualization.R`: Editorial ggplot2 theme `theme_fiba_analytics()`.
