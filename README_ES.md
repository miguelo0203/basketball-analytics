[🇪🇸 Español](README_ES.md) | [🇬🇧 English](README.md)

# 🏀 International Basketball Analytics (2005–2024)
> **Sistema integral de análisis cuantitativo y apoyo a la toma de decisiones sobre 20 años de torneos FIBA de selecciones masculinas absolutas (18 torneos oficiales, 1.145 partidos, 2.290 actuaciones de equipo y 27.353 actuaciones individuales).**

```text
QUIÉN:         Miguel — Analista de Datos | Basketball Analytics
QUÉ:           Sistema de análisis cuantitativo y apoyo a la toma de decisiones para baloncesto internacional
POR QUÉ:       Evidencia cuantitativa, interpretable y calibrada para cuerpos técnicos y directores deportivos
ALCANCE:       18 torneos oficiales (2005–2024: EuroBasket, Copa del Mundo FIBA, Juegos Olímpicos — 1.145 partidos, 2.290 actuaciones de equipo)
TECNOLOGÍA:    Python, DuckDB, Polars, Scikit-Learn, Streamlit, R (tidyverse, ggplot2)
ENTREGABLES:   Briefs tácticos prepartido de 1,5 páginas y entorno interactivo de consulta
LIMITACIÓN:    Herramienta para reducir la incertidumbre estadística; complementa el criterio del entrenador
```

[![DuckDB](https://img.shields.io/badge/OLAP_Store-DuckDB-yellow.svg)](https://duckdb.org/)
[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-Tidyverse%20%7C%20ggplot2-276DC3.svg)](R/README.md)
[![Machine Learning](https://img.shields.io/badge/ML-Calibrated_Walk--Forward_Validation-orange.svg)](https://scikit-learn.org/)
[![Pytest](https://img.shields.io/badge/pytest-227%20passed%20(100%25)-brightgreen.svg)](tests/)
[![Sports Analytics](https://img.shields.io/badge/Domain-Basketball%20Analytics-red.svg)](https://github.com/miguelo0203)

---

## 🚀 Empieza aquí — Resumen ejecutivo

*Si es tu primera vez en este proyecto:*
1. 👔 **[Casos de estudio ejecutivos (Español)](portfolio/README.md)** | **[Executive Case Studies (English)](portfolio/README.md)**: 4 documentos clave sobre decisiones tácticas, ingeniería de datos OLAP, Machine Learning calibrado y análisis longitudinal.
2. 📄 **[Ejemplo de brief táctico prepartido (1,5 páginas)](reports/mvp5_player_briefs/andreas_obst_1996_worldcup_2023_scouting_brief.md)**: Formato de entrega de información táctica diseñado para el cuerpo técnico.
3. 📊 **[Presentación ejecutiva en PDF](presentation/International_Basketball_Analytics_Presentation.pdf)**: Diapositivas con la arquitectura completa y los resultados del sistema.
4. 🔬 **[Arquitectura DuckDB y flujo de datos](#-arquitectura-técnica-y-reproducibilidad)**: Almacén analítico OLAP, modelos de Machine Learning e inferencia estadística.

---

## 📌 ¿Qué problema aborda este sistema?

Este repositorio contiene un **sistema integral de análisis y apoyo a la toma de decisiones para baloncesto internacional**, construido sobre dos décadas de torneos oficiales de selecciones masculinas absolutas de la FIBA (EuroBasket, Copa del Mundo y Juegos Olímpicos entre 2005 y 2024).

El sistema procesa **18 torneos oficiales, 1.145 partidos, 2.290 actuaciones de equipo y 27.353 actuaciones individuales de jugador**, transformando los datos de actas y eventos en:
- **Briefs tácticos prepartido concisos de página y media** para cuerpos técnicos.
- **Un almacén analítico OLAP embebido en DuckDB** de alta velocidad.
- **Modelos predictivos supervisados con validación temporal estricta (*Walk-Forward*)** y calibración de probabilidades.
- **Simulaciones Monte Carlo de torneos completos** y análisis contrafáctico de emparejamientos.

---

## 🏆 Resultados clave y escala del proyecto

- ⚡ **Ingeniería de datos y rendimiento OLAP**: Ingesta automatizada y validación determinista de 27.353 registros individuales, con consultas analíticas complejas ejecutadas en **menos de 15 milisegundos sobre DuckDB**.
- 🔮 **Modelado predictivo calibrado**: Modelo supervisado de predicción de partidos con validación temporal *Walk-Forward* (sin fuga de datos hacia el futuro), alcanzando un **Brier score de 0.1872** y una calibración probabilística auditada.
- 🧠 **Interpretabilidad táctica (valores SHAP)**: Desglose cuantitativo del peso de cada variable de los Four Factors en la probabilidad de victoria de cada encuentro.
- 🎲 **Simulador Monte Carlo de torneos**: Motor de 10.000 simulaciones de cuadro de competición para calcular probabilidades de medalla y escenarios tácticos alternativos.
- 🟢 **Batería de tests exhaustiva**: Suite de **227 tests automáticos (100% de éxito en Pytest)** que validan la coherencia matemática de las actas, continuidad temporal, conservación de minutos y consistencia del esquema.

---

## 🛠️ Qué he construido — Arquitectura del sistema

1. **Flujo de ingesta y control de calidad**: Módulos modulares en Python (`src/acquisition`, `src/parsers`, `src/validation`) con resolución de entidades de jugadores y selecciones.
2. **Almacén analítico DuckDB**: Esquema dimensional optimizado (`src/storage/schema.py`) con vistas agregadas a nivel de equipo y jugador.
3. **Módulo de analítica avanzada y Machine Learning**: Clasificación de arquetipos tácticos, modelos predictivos, simulación de torneos y soporte a decisiones (`src/analytics/`).
4. **Entorno interactivo en Streamlit**: Aplicación visual para consultar briefs prepartido y auditar decisiones tácticas (`src/analytics/mvp10_analyst_workspace.py`).
5. **Entregables editoriales y gráficos en R ggplot2**: Scripts de visualización de alta calidad en R (`R/analysis/`) y generación de informes prepartido.

---

## 🎯 Por qué es relevante — Del dato al plan de partido

El baloncesto de selecciones nacionales presenta retos analíticos únicos: muestras reducidas, ventanas de preparación muy cortas y una alta varianza. Este sistema demuestra cómo estructurar un flujo de trabajo analítico riguroso que filtre el ruido estadístico y proporcione a los entrenadores exclusivamente señales tácticas fiables y directamente aplicables al plan de partido.

---

## 🧭 Navegación del proyecto

### 👔 Vista ejecutiva (Entrenadores, Scouts y Directores Deportivos)
- 📚 [Hub de portfolio y casos de estudio](portfolio/README.md)
- 📄 [Briefs tácticos de scouting de jugadores](reports/mvp5_player_briefs/)
- 📊 [Presentación ejecutiva en PDF](presentation/International_Basketball_Analytics_Presentation.pdf)
- 📋 [Casos de estudio principales](portfolio/case_studies/)

### 🔬 Vista técnica (Analistas de Datos, Data Scientists e Ingenieros)
- `src/`: Código fuente modular en Python (ingesta, métricas, modelos de Machine Learning, simulación).
- `data/`: Datasets procesados y base de datos DuckDB.
- `R/`: Scripts de modelado estadístico y visualización en R (`R/README.md`).
- `tests/`: Suite completa de 227 tests unitarios y de integración en Pytest.
- `reports/`: Catálogo exhaustivo de auditorías técnicas (MVP0 a MVP36).

---

## 📂 Estructura del repositorio

```text
basketball-analytics/
├── README.md                           # Presentación del proyecto (English)
├── README_ES.md                        # Presentación del proyecto (Español)
├── run_project.py                      # Script de ejecución del pipeline completo
├── config/                             # Configuraciones de torneos y reglamentos FIBA
├── data/                               # Almacén DuckDB y datasets procesados
│
├── portfolio/                          # Hub de presentación y casos de estudio
│   ├── README.md                       # Índice de portfolio (Español)
│   ├── index.md                        # Índice de casos de estudio
│   ├── case_studies/                   # 4 Casos de estudio ejecutivos
│   ├── job_search/                     # Perfiles de candidatura y competencias
│   └── presentation/                   # Diapositivas y resúmenes ejecutivos
│
├── presentation/                       # Presentación ejecutiva oficial (PDF y PPTX)
│   ├── README.md                       # Índice de presentación
│   └── International_Basketball_Analytics_Presentation.pdf
│
├── R/                                  # Pipeline de visualización y analítica en R
│   ├── README.md                       # Documentación del módulo R
│   ├── analysis/                       # Scripts R de análisis longitudinal y Four Factors
│   └── functions/                      # Funciones auxiliares R
│
├── reports/                            # Informes técnicos, briefs prepartido y auditorías
│   ├── README.md                       # Índice de informes y auditorías
│   ├── figures/                        # Visualizaciones generadas
│   └── mvp5_player_briefs/             # Briefs prepartido de ejemplo
│
├── src/                                # Código fuente en Python
│   ├── acquisition/                    # Extracción y web scraping
│   ├── analytics/                      # Machine Learning, simulación, briefs e inferencia
│   ├── domain/                         # Modelos de datos y reglas
│   ├── ingestion/                      # Pipelines ETL
│   ├── metrics/                        # Four Factors, Pace, Ratings
│   ├── normalization/                  # Resolución de entidades
│   ├── parsers/                        # Parsers de actas oficiales
│   ├── storage/                        # Esquema DuckDB y conexiones
│   └── validation/                     # Control de calidad y consistencia
│
└── tests/                              # Suite de 227 tests automatizados en Pytest
```

---

## 👤 Autor y contacto

**Miguel** — Data Analyst | Basketball Analytics  
- **GitHub**: [@miguelo0203](https://github.com/miguelo0203)
- **LinkedIn**: [linkedin.com/in/miguelo0203](https://www.linkedin.com)

---
*Sistema analítico reproducible para baloncesto internacional. Desarrollado con Python, DuckDB, R y Streamlit.*
