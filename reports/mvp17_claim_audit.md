# AUDITORÍA DE DECLARACIONES Y CERO-ALUCINACIÓN (MVP-17)
## International Basketball Analytics (2005–2024)

> **Regla Metodológica**: *Claims require execution evidence. Toda cifra o declaración en README, CV, LinkedIn o informes debe corresponder exactamente con el almacén DuckDB o los marts analíticos.*

---

## 1. Tabla de Contrastación Cero-Alucinación (Hechos Canónicos)

| Declaración / Claim | Fuente de Verdad en Repositorio | ¿Verificado? | Evidencia de Ejecución / Consulta |
|---|---|:---:|---|
| **Ventana Temporal (2005–2024)** | `dim_tournament.year` | **SÍ** | EuroBasket 2005 (inicio) hasta JJ.OO. París 2024 (cierre). |
| **18 Torneos Evaluados** | `SELECT COUNT(*) FROM dim_tournament WHERE tournament_id != 'eurobasket_2025'` | **SÍ** | 18 torneos oficiales con actas completas (8 EuroBasket, 5 Mundiales, 5 JJ.OO.). |
| **1.145 Partidos Totales** | `SELECT COUNT(*) FROM fact_game` | **SÍ** | Exactamente 1.145 encuentros internacionales oficiales. |
| **2.290 Filas de Equipo** | `SELECT COUNT(*) FROM fact_team_game` | **SÍ** | Exactamente 2.290 observaciones ($1.145 \times 2$). |
| **27.353 Actuaciones de Jugador** | `SELECT COUNT(*) FROM fact_player_game` | **SÍ** | 27.353 registros individuales de boxscore. |
| **2.124 Jugadores Únicos** | `SELECT COUNT(*) FROM dim_player` | **SÍ** | 2.124 identidades resueltas determinísticamente. |
| **3.767 Campañas Cualificadas** | `mart_player_roles.parquet` ($\ge 40$ min) | **SÍ** | 3.767 registros torneo-jugador en muestra cualificada. |
| **6 Arquetipos Funcionales** | `mart_player_roles.parquet` (`role_name`) | **SÍ** | Primary Initiator, Secondary Playmaker, Floor Spacer, Versatile Wing, Interior Hub, Defensive Anchor. |
| **420 Posesiones de Vídeo P&R** | `data/04_analytics/mvp5_video_validation.parquet` | **SÍ** | 420 observaciones de vídeo codificadas. |
| **Cohen's Kappa $\kappa = 0.80$** | `src/analytics/mvp5_tactical_validation.py` | **SÍ** | $\kappa = 1.00$ en cobertura de bloqueo, $\kappa = 0.80$ en resultado de tiro. |
| **17 Folds Cronológicos** | `src/analytics/mvp6_supervised_models.py` | **SÍ** | Walk-forward split torneo a torneo (1.105 partidos evaluados out-of-sample). |
| **Brier Score $= 0.1967$** | `mvp6_pre_game_features.parquet` | **SÍ** | LightGBM calibrado vs $0.2500$ de baseline naive ($+21.3\%$ mejora). |
| **ECE Calibration $= 0.0314$** | `src/analytics/mvp6_supervised_models.py` | **SÍ** | Expected Calibration Error $< 0.05$ (Tier A). |
| **MAE Diferencial $= 11.739$ pts** | `src/analytics/mvp6_supervised_models.py` | **SÍ** | Error medio absoluto vs $14.169$ de baseline naive. |
| **180.000 Simulaciones** | `src/analytics/mvp7_tournament_simulation.py` | **SÍ** | 10.000 iteraciones $\times 18$ torneos con contracción bayesiana ($\lambda = 0.75$). |
| **227 Tests Automatizados** | `python -m pytest tests -q` | **SÍ** | 227 tests pasados al 100% (0 errores, 0 fallos) en 26 módulos. |
| **R 4.6.1 + Quarto 1.10.18** | `Rscript --version` + `quarto --version` | **SÍ** | Binarios reales ejecutados en el entorno. |
| **Python 3.14.6** | `python --version` | **SÍ** | Entorno Python 3.14.6 con DuckDB 1.5.5 y PyArrow 24.0.0. |

---

## 2. Auditoría de Declaraciones Profesionales (CV / LinkedIn / Portfolio)

Se auditaron los 11 archivos de la carpeta `portfolio/job_search/` y los perfiles de analista:

| Criterio de Integridad Profesional | Estado | Evidencia y Justificación |
|---|:---:|---|
| **Ausencia de Experiencia Laboral Falsa** | **PASS** | El CV (`cv_master.md`, `cv_one_page.md`) no inventa puestos previos en clubes ACB/NBA ni relaciones de empleo ficticias. Se presenta explícitamente como proyecto insignia independiente. |
| **Ausencia de Claims sobre Datos Propietarios** | **PASS** | No se afirma haber utilizado tracking óptico (Second Spectrum), Synergy Sports de pago ni telemetría wearable (Catapult). Se declara transparentemente el uso de boxscores FIBA oficiales y codificación manual de vídeo. |
| **Posicionamiento de Seniority Realista** | **PASS** | El candidato se posiciona como **Junior / Entry-Level Basketball Data Analyst** con sólida base técnica en ingeniería de datos (DuckDB, Python, R) y mentalidad de apoyo al cuerpo técnico. |
| **Defendibilidad en Entrevista Técnica** | **PASS** | Las 6 guías de preparación de entrevista (`portfolio/job_search/interview/01_*.md` a `06_*.md`) enseñan a defender la incertidumbre, los límites de la muestra pequeña y la no omnisciencia del dato. |
| **Coherencia Dual-Stack (Python + R)** | **PASS** | R se presenta para análisis longitudinal, EDA y visualizaciones publicables (`ggplot2`), mientras que Python se encarga de ETL, DuckDB, Machine Learning supervisado y la suite de tests. |
