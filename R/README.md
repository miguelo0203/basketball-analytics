[🇪🇸 Español](README.md) | [🇬🇧 English](README_EN.md)

# 📊 Módulo de Analítica y Visualización en R

Este directorio contiene la suite reproducible de análisis cuantitativo y generación de gráficos de alta fidelidad para el sistema de International Basketball Analytics.

---

## 🏗️ Arquitectura Dual: Python + R sobre DuckDB

El pipeline utiliza una arquitectura de procesamiento híbrido:
1. **Capa de Datos y OLAP en DuckDB**: Ingesta, limpieza, normalización y almacenamiento relacional de alta velocidad en DuckDB.
2. **Capa Analítica y de Modelado en Python**: Modelos de Machine Learning supervisados (Scikit-Learn, LightGBM), inferencia SHAP y simulaciones Monte Carlo.
3. **Capa Estadística y Visual en R (`tidyverse`, `ggplot2`)**: Conexión nativa a DuckDB mediante `DBI` y `duckdb` para análisis longitudinal de tendencias, Four Factors de Dean Oliver, curvas de densidad y visualizaciones editoriales.

---

## 📂 Estructura de Archivos

- `analysis/01_eda_tournaments.R`: Análisis exploratorio de 18 torneos FIBA.
- `analysis/02_player_longitudinal_analysis.R`: Trayectorias y percentiles de jugadores a lo largo de 20 años.
- `analysis/03_role_stability.R`: Evaluación de estabilidad de arquetipos tácticos.
- `analysis/04_team_four_factors.R`: Cuatro Factores de Dean Oliver y correlación con victorias.
- `analysis/05_player_distributions.R`: Distribuciones de True Shooting ($TS\%$) y volumen.
- `analysis/06_statistical_validation.R`: Pruebas de hipótesis e intervalos de confianza bootstrap.
- `functions/metrics.R`: Fórmulas estandarizadas de Four Factors, Pace y Ratings.
- `functions/validation.R`: Comprobaciones de integridad matemática y conservación de minutos.
- `functions/visualization.R`: Tema gráfico corporativo `theme_fiba_analytics()`.
