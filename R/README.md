# Capa Analítica en R: Exploratory Data Analysis & Validación Estadística
## International Basketball Analytics (2005–2024)

> [!IMPORTANT]
> Este módulo demuestra competencia práctica en **R para análisis estadístico, EDA, análisis longitudinal y visualización avanzada con `ggplot2`**, integrándose de forma directa y nativa con el almacén relacional DuckDB y los marts en Apache Parquet.

---

## 1. Arquitectura Profesional Dual-Stack (Python + R)

El proyecto separa responsabilidades con claridad para utilizar la mejor herramienta en cada etapa:

```text
                 ┌───────────────┐
                 │   Raw Data    │
                 │   (Boxscores) │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │ Python / ETL  │
                 │  (QA Engine)  │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │    DuckDB     │
                 │ (OLAP Store)  │
                 └───────┬───────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
        ┌───────────┐         ┌───────────┐
        │  Python   │         │     R     │
        │ ML / Sim. │         │ Stats/EDA │
        └─────┬─────┘         └─────┬─────┘
              │                     │
              └──────────┬──────────┘
                         ▼
                ┌──────────────────┐
                │ Decision Support │
                │ (Briefs & Video) │
                └──────────────────┘
```

- **Python**: Ingesta, pipelines de datos, motor de QA, DuckDB, Machine Learning (LightGBM), simulaciones Monte Carlo, testing automatizado (pytest) y aplicación interactiva (Streamlit).
- **R**: Exploratory Data Analysis (EDA), análisis longitudinal de trayectorias, análisis de distribuciones empíricas, validación estadística independiente (bootstrap e inferencia no paramétrica) y generación de gráficos publication-ready con `ggplot2`.

---

## 2. Estructura del Directorio `R/`

```text
R/
├── analysis/
│   ├── 01_eda_tournaments.R            # EDA de 18 torneos y evolución del tiro de 3 (regla 2010)
│   ├── 02_player_longitudinal_analysis.R # Trayectorias longitudinales (TS% y per-40 en carreras)
│   ├── 03_role_stability.R             # Distribución y estabilidad de los 6 arquetipos funcionales
│   ├── 04_team_four_factors.R          # Descomposición de Four Factors en 2.290 observaciones
│   ├── 05_player_distributions.R       # Distribuciones y percentiles de 3.767 campañas individuales
│   └── 06_statistical_validation.R     # Bootstrap (B=5k), permutación (P=10k) y Spearman
│
├── functions/
│   ├── metrics.R                       # Fórmulas vectorizadas: Four Factors, Pace, Net Rating, TS%
│   ├── visualization.R                 # Tema custom 'theme_basketball_analytics()' y paletas
│   └── validation.R                    # Funciones de bootstrap, permutación y test Kolmogorov-Smirnov
│
├── reports/
│   └── exploratory_analysis.qmd        # Informe reproducible en Quarto con gráficos y tablas
│
└── README.md                           # Guía técnica de la capa R
```

---

## 3. Paquetes de R Utilizados

Se priorizan librerías del ecosistema moderno y reproducible:
- **Manipulación de Datos**: `dplyr`, `tidyr`, `readr`, `purrr`
- **Visualización**: `ggplot2`
- **Bases de Datos & Columnar**: `DBI`, `duckdb`, `arrow`
- **Modelado & Estadística**: `broom`, `stats`
- **Documentación Reproducible**: `quarto` / `rmarkdown`

---

## 4. Cómo Ejecutar los Scripts en R

```r
# Instalar paquetes requeridos si no están disponibles
install.packages(c("dplyr", "tidyr", "ggplot2", "readr", "DBI", "duckdb", "arrow", "broom"))

# Ejecutar los análisis desde la raíz del proyecto:
source("R/analysis/01_eda_tournaments.R")
source("R/analysis/02_player_longitudinal_analysis.R")
source("R/analysis/03_role_stability.R")
source("R/analysis/04_team_four_factors.R")
source("R/analysis/05_player_distributions.R")
source("R/analysis/06_statistical_validation.R")
```

---

## 5. Validación Estadística Independiente

La capa R implementa comprobaciones estadísticas no paramétricas que confirman de manera independiente los resultados calculados en Python:
1. **Intervalos de Confianza Bootstrap ($B=5.000$)**: Verificación empírica de medias de eFG% y ritmo (Pace) a nivel torneo.
2. **Test de Permutación ($P=10.000$)**: Contraste de hipótesis sobre el incremento estadísticamente significativo en la tasa de tiro de 3 puntos tras el cambio reglamentario FIBA de 2010 ($p < 0.0001$).
3. **Estabilidad de Rankings**: Correlación de rangos de Spearman ($\rho \ge 0.85$) en la ordenación de características clave.
