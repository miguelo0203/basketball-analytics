# MANIFIESTO DE REPRODUCIBILIDAD Y HASHES CRIPTOGRÁFICOS SHA-256
## International Basketball Analytics (2005–2024)

> **Propósito**: Garantizar la trazabilidad, integridad e inmutabilidad de los artefactos canónicos, datasets procesados, marts analíticos y figuras del repositorio.

---

## 1. Almacén de Datos y Tablas Canónicas

| Archivo | SHA-256 | Generado por | Determinista |
|---|---|---|---|
| `data/03_validated/basketball_analytics.duckdb` | `5e0459d9a3c70b9ade36f9dec23794c8521e32f26df5f8acca754d2047a84f11` | `src/etl/pipeline.py` (QA Engine) | SÍ |
| `config/expected_tournament_manifest.yaml` | `3bc9c42d4f181a9930ef442d02821bcf87721baa4d950a6c7bf5a5a01b58d6fa` | Configuración Canónica | SÍ |
| `config/tournaments.csv` | `6e80dff81a139f135595fc6e46b7189efff049786500be86efbb4fc42e9274f7` | Catálogo de Torneos (18 torneos) | SÍ |
| `config/rule_sets.csv` | `95b3a13bb0c43294e4186c548d7794a3d9813ad48467da2270f2ffa99226007a` | Reglas FIBA / Distancia 3P | SÍ |
| `config/teams.csv` | `f5628fd959ee267548305be450658c36700efbc0db93f742393377a0ecc2b9f5` | Entidades de Equipos y Selecciones | SÍ |
| `config/sources.yaml` | `d487a4bc0c0ab58f8a1b6ffcc696a4f8e531ec296643e0c3dd3e002c105e2416` | Fuentes Oficiales FIBA | SÍ |
| `config/mvp5_video_observation_rubric.yaml` | `eb05576cca473ea1535d84f386eee5f8a2ecda54cf0b509fe4ee5ad86dee6857` | Rúbrica Cualitativa de Vídeo P&R | SÍ |

---

## 2. Marts Analíticos en Formato Parquet

| Archivo | SHA-256 | Generado por | Determinista |
|---|---|---|---|
| `data/04_analytics/mart_tournament_summary.parquet` | `96200e80d82cb0d902064a62f7a0514a71df359cea8abb1db56f835350951649` | `src/analytics/data_mart.py` | SÍ |
| `data/04_analytics/mart_team_game_analytics.parquet` | `463cddc2ceed1f433857911cf12dfa7ef03d0b9d903ef8a1384539deef29998c` | `src/analytics/data_mart.py` | SÍ |
| `data/04_analytics/mart_player_tournament_features.parquet` | `8ba4ec9ca8dc22ed4a9e363bf8354367d812e1f69d7f18db36c8904ce7c11221` | `src/analytics/player_data_mart.py` | SÍ |
| `data/04_analytics/mart_player_roles.parquet` | `08493fc57717d4cba980d51c0e640ec8f53172526a159f6d2848f04f4b259cc7` | `src/analytics/player_roles.py` | SÍ (Seed fija: 42) |
| `data/04_analytics/mvp6_pre_game_features.parquet` | `2bc4170bc4b60447530efc12013eebc2dc13b0bc2a36ef342947bc2b348f3924` | `src/analytics/mvp6_supervised_models.py` | SÍ |
| `data/04_analytics/mvp7_tournament_simulations.parquet` | `e8d4487d1820b56fe5c6e4bf945c8f0f4f35f31f547313aa5ae73c82dec51d59` | `src/analytics/mvp7_tournament_simulation.py` | SÍ (Seed fija: 42) |
| `data/04_analytics/mvp7_team_advancement_probabilities.parquet` | `e8d4487d1820b56fe5c6e4bf945c8f0f4f35f31f547313aa5ae73c82dec51d59` | `src/analytics/mvp7_tournament_simulation.py` | SÍ (Seed fija: 42) |
| `data/04_analytics/mvp8_decision_dossiers.parquet` | `61bf8d26ef2bec82181c2815c3b4438e0e8d5e9d13456d509d11ede95866e469` | `src/analytics/mvp8_decision_system.py` | SÍ |
| `data/04_analytics/mvp10_evidence_matrix.parquet` | `e167da46dd9c287dd3d76358adf18cc5558f575d322eab79883f864df232fc7d` | `src/analytics/mvp10_evidence_engine.py` | SÍ |
| `data/04_analytics/mvp10_coaching_briefs.parquet` | `d0ff4f6b06eb19d40b7ca564e38e44ee100d4b401fa4967c9812f3a65cb25b52` | `src/analytics/mvp10_brief_generator.py` | SÍ |
| `data/04_analytics/mvp10_workspace_records.parquet` | `5a431bbdb200e8d7556722bbfbbe4cac7ba007b9dfafb91fb9a1d0503fc41bea` | `src/analytics/mvp10_analyst_workspace.py` | SÍ |

---

## 3. Figuras y Visualizaciones Analíticas Regenerables

Las figuras se regeneran ejecutando los scripts correspondientes (`src/analytics/mvp*_visualizations.py` o `R/analysis/*.R`):

| Archivo | Formato | Generador | Determinismo Visual |
|---|---|---|---|
| `reports/figures_r/fig_01_tournament_trends.png` | PNG (300 DPI) | `R/analysis/01_eda_tournaments.R` | SÍ (basado en agregaciones DuckDB) |
| `reports/figures_r/fig_02_player_trajectories.png` | PNG (300 DPI) | `R/analysis/02_player_longitudinal_analysis.R` | SÍ |
| `reports/figures_r/fig_03_archetype_distribution.png` | PNG (300 DPI) | `R/analysis/03_role_stability.R` | SÍ |
| `reports/figures_r/fig_04_four_factors_correlation.png` | PNG (300 DPI) | `R/analysis/04_team_four_factors.R` | SÍ |
| `reports/figures_r/fig_05_ts_distribution.png` | PNG (300 DPI) | `R/analysis/05_player_distributions.R` | SÍ |
| `reports/figures/fig_01_tournament_pace_evolution.png` | PNG (300 DPI) | `src/analytics/mvp3_visualizations.py` | SÍ |
| `reports/figures/fig_02_four_factors_importance.png` | PNG (300 DPI) | `src/analytics/mvp6_visualizations.py` | SÍ |
| `reports/figures/fig_03_calibration_reliability_curve.png` | PNG (300 DPI) | `src/analytics/mvp6_visualizations.py` | SÍ |
| `reports/figures/fig_04_monte_carlo_distribution.png` | PNG (300 DPI) | `src/analytics/mvp7_visualizations.py` | SÍ |
| `reports/figures/fig_05_tactical_film_kappa.png` | PNG (300 DPI) | `src/analytics/mvp5_visualizations.py` | SÍ |
| `reports/figures/fig_06_analyst_decision_timeline.png` | PNG (300 DPI) | `src/analytics/mvp10_visualizations.py` | SÍ |

---

## 4. Política de Tolerancia y Variabilidad

- **Machine Learning**: Los modelos utilizan particiones cronológicas estrictas (walk-forward con 17 folds) y semillas fijas (`random_state=42`).
- **Simulaciones Monte Carlo**: $180.000$ iteraciones con `np.random.seed(42)` y contracción bayesiana ($\lambda = 0.75$).
- **Inferencia no paramétrica en R**: Bootstrap ($B=5.000$) y test de permutación ($P=10.000$) fijan `set.seed(42)`.
