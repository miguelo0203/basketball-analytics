# MAPA DE LINAJE DE DATOS Y EJECUCIÓN (DATA LINEAGE)
## International Basketball Analytics (2005–2024)

> **Propósito**: Detallar el flujo de transformación de datos paso a paso, desde las fuentes brutas FIBA hasta los informes de soporte a decisiones y aplicaciones interactivas.

---

## 1. Diagrama de Flujo de Transformación

```text
┌────────────────────────┐
│     1. RAW DATA        │  Actas oficiales FIBA y boxscores históricos (2005–2024)
│  (data/01_raw/...)     │
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│     2. INGESTION       │  Ingesta estructurada, validación de esquemas y hashing
│ (src/ingestion/...)    │
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│      3. DUCKDB         │  Almacén relacional OLAP con QA Engine determinista
│ (basketball_analytics) │  (12 tablas relacionales normalizadas)
└───────────┬────────────┘
            │
            ▼
┌────────────────────────┐
│   4. PARQUET MARTS     │  Marts dimensionales precalculados y particionados
│  (data/04_analytics/)  │
└─────┬────────────┬─────┘
      │            │
      ▼            ▼
┌───────────┐ ┌───────────┐
│ 5. PYTHON │ │   6. R    │  Python: Machine Learning, Monte Carlo, Workspaces
│ ML / Sim  │ │ Stats/EDA │  R: Inferencia estadística, trayectorias, Quarto
└─────┬─────┘ └─────┬─────┘
      │             │
      ├─────────────┴────────────────┐
      ▼                              ▼
┌────────────────────────┐ ┌────────────────────────┐
│    7. VISUALIZATIONS   │ │     8. REPORTS & UI    │
│   (figures & R plots)  │ │ (Briefs, Quarto, App)  │
└────────────────────────┘ └────────────────────────┘
```

---

## 2. Matriz Detallada de Trazabilidad por Etapas

| Etapa | Input Principal | Script Responsable | Output Generado | Formato | Dependencias Clave |
|---|---|---|---|---|---|
| **1. Ingesta** | Actas FIBA, Boxscores | `src/ingestion/pipeline.py` | `data/02_staging/staging.duckdb` | DuckDB Table | `duckdb`, `pandas` |
| **2. Control de Calidad (QA)** | Tablas staging | `src/data_quality/qa_engine.py` | `fact_validation_issue` | DuckDB Table | `duckdb`, `pytest` |
| **3. Resolución de Entidades** | Nombres y aliases | `src/entity_resolution/resolver.py` | `dim_player`, `dim_player_alias` | DuckDB Table | `rapidfuzz`, `duckdb` |
| **4. Almacén Canónico** | Tablas procesadas | `src/etl/pipeline.py` | `data/03_validated/basketball_analytics.duckdb` | DuckDB File | `duckdb` |
| **5. Marts de Torneo y Equipo** | `fact_game`, `fact_team_game` | `src/analytics/data_mart.py` | `mart_tournament_summary.parquet`, `mart_team_game_analytics.parquet` | Apache Parquet | `pyarrow`, `duckdb` |
| **6. Marts de Jugador y Roles** | `fact_player_game` | `src/analytics/player_data_mart.py`, `player_roles.py` | `mart_player_tournament_features.parquet`, `mart_player_roles.parquet` | Apache Parquet | `scikit-learn`, `pyarrow` |
| **7. Machine Learning (17 Folds)** | Marts de equipo | `src/analytics/mvp6_supervised_models.py` | `mvp6_pre_game_features.parquet`, métricas Brier/ECE/MAE | Parquet + Logs | `lightgbm`, `scikit-learn` |
| **8. Simulación Monte Carlo** | Matriz de rating prepartido | `src/analytics/mvp7_tournament_simulation.py` | `mvp7_tournament_simulations.parquet`, `mvp7_team_advancement_probabilities.parquet` | Apache Parquet | `numpy`, `scipy` |
| **9. Auditoría de Decisión** | Prepartido + Replay | `src/analytics/mvp8_decision_system.py`, `mvp10_analyst_workspace.py` | `mvp8_decision_dossiers.parquet`, `mvp10_workspace_records.parquet` | Apache Parquet | `pandas`, `duckdb` |
| **10. Análisis Exploratorio en R** | DuckDB + Parquet | `R/analysis/01_eda_tournaments.R` ... `06_statistical_validation.R` | Figuras `reports/figures_r/*.png` | PNG (300 DPI) | `R`, `ggplot2`, `dplyr` |
| **11. Informe Quarto** | Warehouse + R | `R/reports/exploratory_analysis.qmd` | `R/reports/exploratory_analysis.html` | HTML Standalone | `quarto`, `pandoc`, `R` |
| **12. Workspace Interactivo** | Marts analíticos | `src/analytics/mvp10_analyst_workspace.py` | App web interactiva | Streamlit UI | `streamlit`, `pandas` |

---

## 3. Garantía de Aislamiento Temporal y No Fuga de Datos (Anti-Hindsight)

- **Capa Prepartido**: Los scripts analíticos de modelado supervisado (`mvp6`), simulación (`mvp7`) y briefing táctico (`mvp10`) consumen variables filtradas con la condición:
  $$\text{game\_date} < \text{target\_game\_date}$$
- **Aislamiento de Marcadores**: El marcador final real solo se procesa en el módulo de auditoría de proceso post-partido (`reveal_match_outcome()`), previniendo cualquier contaminación retrospectiva en las evaluaciones.
