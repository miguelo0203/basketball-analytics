[🇪🇸 Español](README.md) | [🇬🇧 English](README_EN.md)

# 🏀 International Basketball Analytics (2005–2024)
> **Sistema integral de soporte a decisiones y analítica cuantitativa para 20 años de torneos FIBA de selecciones masculinas absolutas (18 torneos oficiales, 1,145 partidos, 2,290 actuaciones de equipo y 27,353 actuaciones de jugador).**

```text
WHO:         Miguel — Data Analyst | Basketball Analytics
WHAT:        Sistema de Análisis y Soporte a Decisiones para Baloncesto Internacional
WHY:         Evidencia cuantitativa, interpretable y calibrada para cuerpos técnicos y directores deportivos
SCOPE:       18 Torneos (2005–2024: EuroBasket, Copa del Mundo FIBA, Juegos Olímpicos — 1,145 partidos, 2,290 actuaciones de equipo)
TECHNOLOGY:  Python, DuckDB, Polars, Scikit-Learn, Streamlit, R (tidyverse, ggplot2)
OUTPUT:      Briefs prepartido de 1.5 páginas y Workspace interactivo anti-hindsight
LIMITATION:  Herramienta de reducción de incertidumbre estadística; no sustituye el juicio del entrenador
```

[![DuckDB](https://img.shields.io/badge/OLAP_Store-DuckDB-yellow.svg)](https://duckdb.org/)
[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-Tidyverse%20%7C%20ggplot2-276DC3.svg)](R/README.md)
[![Machine Learning](https://img.shields.io/badge/ML-Calibrated_Walk--Forward_Validation-orange.svg)](https://scikit-learn.org/)
[![Pytest](https://img.shields.io/badge/pytest-227%20passed%20(100%25)-brightgreen.svg)](tests/)
[![Sports Analytics](https://img.shields.io/badge/Domain-Basketball%20Analytics-red.svg)](https://github.com/miguelo0203)

---

## 🚀 Empieza Aquí — El proyecto en 30 segundos (Executive Summary)

*Si es tu primera vez en este proyecto:*
1. 👔 **[Casos de Estudio Ejecutivos (Español)](portfolio/README.md)** | **[Executive Case Studies (English)](portfolio/README_EN.md)**: 4 dossiers clave sobre decisiones tácticas, ingeniería de datos OLAP, machine learning calibrado y análisis longitudinal.
2. 📄 **[Briefs Prepartido de Ejemplo (1.5 Páginas)](reports/mvp5_player_briefs/andreas_obst_1996_worldcup_2023_scouting_brief.md)**: Formato editorial de entrega de información para cuerpos técnicos.
3. 📊 **[Presentación Ejecutiva en PDF (English)](presentation/International_Basketball_Analytics_Presentation.pdf)**: Slide deck completo de arquitectura y resultados del sistema.
4. 🔬 **[Arquitectura DuckDB & Data Pipeline](#-arquitectura-técnica-y-reproducibilidad)**: Almacén analítico OLAP, modelos de Machine Learning e inferencia estadística.

---

## 📌 ¿Qué hace el sistema? (The Professional Problem)

Este repositorio contiene un **sistema integral de análisis y soporte a decisiones para baloncesto internacional**, desarrollado sobre dos décadas de competiciones oficiales de selecciones masculinas absolutas de la FIBA (EuroBasket, Copa del Mundo y Juegos Olímpicos entre 2005 y 2024).

El sistema procesa **18 torneos oficiales, 1,145 partidos, 2,290 actuaciones de equipo y 27,353 actuaciones individuales de jugador**, transformando datos crudos de actas y eventos en:
- **Briefs tácticos prepartido concisos de 1.5 páginas** para cuerpos técnicos.
- **Un almacén analítico OLAP embebido en DuckDB** de alta velocidad.
- **Modelos predictivos supervisados con validación temporal estricta (*Walk-Forward*)** y calibración de probabilidades.
- **Simulaciones Monte Carlo de torneos completos** y análisis contrafáctico de escenarios competitivos.

---

## 🏆 El proyecto en cifras — Resultados Clave (Audited Project Scale)

- ⚡ **Ingeniería de Datos & Rendimiento OLAP**: Ingesta automatizada y validación determinista de 27,353 registros individuales, con consultas agregadas complejas ejecutadas en **<15 milisegundos sobre DuckDB**.
- 🔮 **Modelado Predictivo Calibrado**: Modelo supervisado de predicción de encuentros con validación temporal *Walk-Forward* (sin fuga de información hacia el futuro), alcanzando un **Brier score de 0.1872** y calibración probabilística auditada.
- 🧠 **Interpretabilidad Táctica (SHAP Values)**: Desglose cuantitativo del peso de cada variable de Four Factors en la probabilidad de victoria de cada partido.
- 🎲 **Simulador Monte Carlo de Torneos**: Motor de 10,000 simulaciones de cuadro de competición para calcular probabilidades de medalla y escenarios contrafácticos.
- 🟢 **Batería de Tests Exhaustiva**: Suite de **227 tests automáticos (100% de éxito en Pytest)** que validan ball math, continuidad temporal, conservación de minutos y consistencia de esquemas.

---

## 🛠️ Qué he construido — Arquitectura Visual (Technical Architecture)

1. **Pipeline de Ingesta & Data Quality**: Módulos en Python (`src/acquisition`, `src/parsers`, `src/validation`) con resolución de entidades de jugadores y países.
2. **Almacén Analítico DuckDB**: Esquema dimensional optimizado (`src/storage/schema.py`) con vistas analíticas de equipo y jugador.
3. **Módulo de Analítica Avanzada & ML**: Clasificación de arquetipos tácticos, modelos predictivos, simulación de torneos y soporte a decisiones (`src/analytics/`).
4. **Workspace Interactivo Streamlit**: Entorno visual para consulta de briefs prepartido y auditoría de decisiones (`src/analytics/mvp10_analyst_workspace.py`).
5. **Entregables Editoriales & R ggplot2**: Scripts de visualización de alta calidad en R (`R/analysis/`) y generación de briefs prepartido.

---

## 🎯 Por qué es relevante — Caso Flagship (From Raw Data to Coaching Question)

El baloncesto de selecciones nacionales presenta retos analíticos únicos: muestras reducidas, ventanas cortas de preparación y alta varianza. Este sistema demuestra cómo estructurar un flujo de trabajo analítico riguroso que minimice la sobreinterpretación del ruido estadístico y entregue a los entrenadores únicamente señales tácticas procesables y robustas.

---

## 🧭 Navegación del Proyecto (Project Navigation)

### 👔 Vista Ejecutiva (Coaches, Scouts & Directores Deportivos)
- 📚 [Hub de Portfolio y Casos de Estudio](portfolio/README.md)
- 📄 [Briefs Tácticos de Jugador (Scouting)](reports/mvp5_player_briefs/)
- 📊 [Presentación Ejecutiva en PDF](presentation/International_Basketball_Analytics_Presentation.pdf)
- 📋 [Estudios de Caso Clave](portfolio/case_studies/)

### 🔬 Vista Técnica (Data Scientists & Engineers)
- `src/`: Código fuente modular en Python (ingesta, métricas, modelos ML, simulación).
- `data/`: Datasets procesados y base de datos DuckDB.
- `R/`: Scripts de visualización y modelado estadístico en R (`R/README.md`).
- `tests/`: Suite completa de 227 tests unitarios y de integración en Pytest.
- `reports/`: Catálogo exhaustivo de auditorías técnicas (MVP0 a MVP36).

---

## 📂 Estructura del Repositorio

```text
basketball-analytics/
├── README.md                           # Presentación del proyecto (Español)
├── README_EN.md                        # Project presentation (English)
├── run_project.py                      # Launcher de ejecución del pipeline completo
├── config/                             # Configuraciones de torneos y reglas FIBA
├── data/                               # Almacén DuckDB y datasets procesados
│
├── portfolio/                          # Hub de presentación y casos de estudio
│   ├── README.md                       # Índice de portfolio (Español)
│   ├── README_EN.md                    # Portfolio index (English)
│   ├── index.md                        # Índice de casos de estudio
│   ├── case_studies/                   # 4 Casos de estudio ejecutivos
│   ├── job_search/                     # Perfiles de candidatura y competencias
│   └── presentation/                   # Decks y resúmenes ejecutivos
│
├── presentation/                       # Presentación ejecutiva oficial (PDF & PPTX)
│   ├── README.md                       # Índice de presentación (Español)
│   ├── README_EN.md                    # Presentation index (English)
│   └── International_Basketball_Analytics_Presentation.pdf
│
├── R/                                  # Pipeline de visualización y analítica en R
│   ├── README.md                       # Documentación del módulo R (Español)
│   ├── README_EN.md                    # R module documentation (English)
│   ├── analysis/                       # Scripts R de análisis longitudinal y Four Factors
│   └── functions/                      # Funciones auxiliares R
│
├── reports/                            # Informes técnicos, briefs prepartido y auditorías
│   ├── README.md                       # Índice de informes y auditorías
│   ├── README_EN.md                    # Reports index (English)
│   ├── figures/                        # Visualizaciones generadas
│   └── mvp5_player_briefs/             # Briefs prepartido de ejemplo
│
├── src/                                # Código fuente en Python
│   ├── acquisition/                    # Extracción y web scraping
│   ├── analytics/                      # ML, simulación, briefs e inferencia
│   ├── domain/                         # Modelos de datos y reglas
│   ├── ingestion/                      # Pipelines ETL
│   ├── metrics/                        # Four Factors, Pace, Ratings
│   ├── normalization/                  # Resolución de entidades
│   ├── parsers/                        # Box-score parsers
│   ├── storage/                        # Schema DuckDB y conexiones
│   └── validation/                     # Control de calidad y ball math
│
└── tests/                              # Suite de 227 tests automatizados en Pytest
```

---

## 👤 Autor y Contacto

**Miguel** — Data Analyst | Basketball Analytics  
- **GitHub**: [@miguelo0203](https://github.com/miguelo0203)
- **LinkedIn**: [linkedin.com/in/miguelo0203](https://www.linkedin.com)

---
*Sistema analítico reproducible para baloncesto internacional. Desarrollado con Python, DuckDB, R y Streamlit.*
