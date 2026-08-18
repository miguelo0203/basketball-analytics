# Canonical Project Facts & Single Source of Truth
## International Basketball Analytics (2005–2024)

> [!IMPORTANT]
> Este documento constituye la **Fuente Canónica de Verdad** para todas las cifras, métricas, arquitecturas y afirmaciones técnicas del repositorio. Cualquier documento público, presentación o resumen debe derivarse de los hechos aquí descritos.

---

## 1. Alcance Temporal y Competitivo (Scope)

- **Disciplina**: Baloncesto Internacional Masculino de Selecciones Absolutas.
- **Periodo Histórico**: 2005 a 2024 (20 temporadas de competiciones oficiales FIBA y COI).
- **Competiciones Certificadas (18 Torneos)**:
  - 9 EuroBaskets (2005, 2007, 2009, 2011, 2013, 2015, 2017, 2022 + Preclasificatorios certificados).
  - 5 Copas del Mundo FIBA (2006, 2010, 2014, 2019, 2023).
  - 4 Torneos de Baloncesto en Juegos Olímpicos (Pekín 2008, Londres 2012, Río 2016, Tokio 2020/2021).
- **Límite Temporal**: No se incluye ningún torneo posterior a los Juegos Olímpicos de París 2024. El alcance es estrictamente 2005–2024.

---

## 2. Cardinalidad del Almacén de Datos (DuckDB Relacional)

- **Partidos Totales (`fact_game`)**: 1.145 partidos.
- **Observaciones de Equipo (`fact_team_game`)**: 2.290 registros (2 por partido).
- **Actuaciones Individuales de Jugador (`fact_player_game`)**: 27.353 registros.
- **Jugadores Canónicos Únicos (`dim_player`)**: 2.124 identidades resueltas y normalizadas sin duplicados.
- **Campañas Torneo-Jugador Evaluadas**: 4.350 campañas individuales.
- **Campañas Cualificadas (`mart_player_roles`)**: 3.767 campañas con $\ge 40$ minutos disputados en el torneo.
- **Esquema Relacional**: 12 tablas (4 dimensiones, 3 hechos, 5 marts analíticos).
- **Integridad Criptográfica**: Hashes SHA-256 inmutables en archivos fuente de datos brutos.

---

## 3. Analítica Avanzada y Four Factors

- **Fórmula de Posesiones (FIBA)**: $\text{Poss} = \text{FGA} + 0.44 \times \text{FTA} - \text{ORB} + \text{TOV}$.
- **Net Rating**: $\text{ORtg} - \text{DRtg} = 100 \times \left(\frac{\text{PTS}}{\text{Poss}} - \frac{\text{PTS\_OPP}}{\text{Poss\_OPP}}\right)$.
- **Four Factors de Dean Oliver**:
  1. Eficiencia de Tiro Efectiva ($\text{eFG}\% = \frac{\text{FGM} + 0.5 \times \text{3PM}}{\text{FGA}}$).
  2. Ratio de Pérdidas ($\text{TOV}\% = \frac{\text{TOV}}{\text{Poss}}$).
  3. Rebote Ofensivo ($\text{ORB}\% = \frac{\text{ORB}}{\text{ORB} + \text{DRB\_OPP}}$).
  4. Ratio de Tiro Libre ($\text{FTR} = \frac{\text{FTA}}{\text{FGA}}$).
- **Minería de Roles Funcionales**: 6 Arquetipos descubiertos mediante K-Means++ y PCA sobre 3.767 campañas:
  1. *Primary Initiator* (Alto uso de balón y generación ofensiva tras bote).
  2. *Movement Spacer* (Triples tras recepción y espaciado de pista).
  3. *Interior Hub* (Pívots finalizadores, rebote ofensivo y distribución interior).
  4. *Floor General* (Bases directores, control de ritmo y ratio AST/TOV de élite).
  5. *Defensive Anchor* (Protectores de aro e intimidación en drop coverage).
  6. *Balanced Wing* (Aleros equilibrados de impacto bidireccional).

---

## 4. Capa Táctica y Validación en Vídeo

- **Muestra Observada (`mart_tactical_video`)**: 420 posesiones estructuradas en 36 partidos clave.
- **Protocolo de Observación**: Doble codificación independiente con dos analistas ciegos entre sí.
- **Fiabilidad Inter-Evaluador**:
  - Tipo de acción táctica (P&R Ball Screen vs. Post-up vs. Isolation): $\text{Cohen's Kappa } \kappa = 1.00$ (Acuerdo perfecto).
  - Calificación defensiva de la cobertura (Drop depth, Contest quality): $\text{Cohen's Kappa } \kappa = 0.80$ (Acuerdo sustancial).

---

## 5. Machine Learning Supervisado y Calibración

- **Esquema de Validación**: 17 Folds Temporales Walk-Forward Expansivos.
  - Fold 1: Train 2005 ➔ Test 2006
  - Fold 2: Train 2005–2006 ➔ Test 2007
  - ...
  - Fold 17: Train 2005–2023 ➔ Test 2024
- **Partidos Evaluados Fuera de Muestra (Out-of-Sample)**: 1.105 partidos.
- **Modelos Evaluados**: Naive Baseline, Regresión Logística, ElasticNet, LightGBM.
- **Métricas del Modelo Principal (LightGBM Out-of-Sample)**:
  - Brier Score: `0.1967` (frente a 0.2500 de predicción aleatoria).
  - ROC-AUC: `0.7613`.
  - Error Absoluto Medio de Margen (MAE): `11.739 puntos`.
- **Evaluación de Calibración**:
  - Curvas de fiabilidad con 10 bins uniformes.
  - Expected Calibration Error (ECE): `0.0314` (3.14% de desviación media).
- **Atribución de Características e Interpretabilidad**:
  - Permutation Importance en pliegues fuera de muestra (`scoring="neg_brier_score"`, 5 repeticiones).
  - Estabilidad de ranking temporal: Mediana de correlación Spearman $\rho = 0.854$.
  - Variables con mayor peso: Diferencial de Net Rating histórico, Diferencial de eFG%, Margen en grupo reciente, TOV%.

---

## 6. Simulación de Torneos (Monte Carlo)

- **Metodología**: 10.000 iteraciones estocásticas por campeonato (18 torneos = 180.000 simulaciones totales).
- **Ajuste de Probabilidad**: Calibración por Shrinkage Bayesiano hacia prior base ($\lambda = 0.75$) para amortiguar sobreconfianza en favoritos teóricos.
- **Rendimiento Retrospectivo de Simulación**:
  - Captura del Campeón Real en el Top-1 proyectado: 72.2% (13 de 18 torneos).
  - Captura del Campeón Real en el Top-4 proyectado: 100.0% (18 de 18 torneos).

---

## 7. Soporte a Decisiones y Aislamiento Anti-Hindsight

- **Matriz de Evidencia de 8 Capas**: Producción histórica, Forma de torneo, Four Factors, Arquetipos, Vídeo, ML, Simulación e Incertidumbre Bootstrap ($B=5.000$).
- **Motor de Contradicciones**: Sistema que alerta cuando las señales numéricas (ej. favoritismo por rating) chocan con observaciones tácticas de vídeo (ej. drop defensivo vulnerable a pick-and-pop).
- **Aislamiento Temporal en Workspace**: La aplicación no muestra marcadores ni resultados de juego hasta que el usuario pulsa voluntariamente el botón de revelación postpartido.

---

## 8. Ingeniería de Software, Reproducibilidad y Testing

- **Lenguajes y Almacenamiento**: Python 3.10+, R (tidyverse, ggplot2, duckdb, arrow), DuckDB, Parquet, Streamlit.
- **Test Suite**: 227 automated tests passing with pytest (100% pass rate, 0 failures, 0 errors) across 26 modules.
- **Semilla Pseudoaleatoria Global**: `seed = 42` para determinismo completo.
