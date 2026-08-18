# CATÁLOGO DE MICRO-CASOS DE ESTUDIO DEL PROYECTO (MVP-21)
## International Basketball Analytics (2005–2024)

> **Propósito**: 8 casos de estudio técnicos y tácticos autónomos listos para ser compartidos en comunidades especializadas para generar debate y feedback metodológico.

---

### 📦 Caso 1: "Construyendo un Almacén Relacional OLAP con DuckDB y Parquet para 20 Años de Baloncesto"
- **Comunidades Adecuadas**: *DuckDB Discord, PyData Madrid, r/dataengineering*.
- **Contenido Técnico**: Esquema de 12 tablas, consultas analíticas con funciones de ventana en SQL, compresión Snappy/Zstd y lectura concurrente desde Python y R.
- **Gráfico a Mostrar**: Diagrama de linaje y arquitectura de `docs/arquitectura.md`.
- **Pregunta a la Comunidad**: *"¿Qué estrategia de particionado utilizáis en DuckDB cuando el dataset tiene una granularidad torneo-partido-jugador?"*

---

### 📉 Caso 2: "El Peligro del Data Leakage en Deportes: Walk-Forward en 17 Particiones Temporales"
- **Comunidades Adecuadas**: *Reddit `r/sportsanalytics`, Kaggle, Twitter/X*.
- **Contenido Técnico**: Por qué el k-fold estándar sobreestima el rendimiento en series temporales deportivas y cómo el esquema expansivo torneo a torneo evaluó 1.105 partidos out-of-sample.
- **Gráfico a Mostrar**: Curvas de calibración y Brier score (`reports/figures/mvp6/fig_02_calibration_curves.png`).
- **Pregunta a la Comunidad**: *"¿Aplicáis reentrenamiento por torneo o ventanas móviles deslizantes en ligas con cambios de ciclo olímpico/generacional?"*

---

### 🎯 Caso 3: "Calibración de Probabilidades Prepartido: Brier Score (0.1967) vs Expected Calibration Error (0.0314)"
- **Comunidades Adecuadas**: *Reddit `r/sportsanalytics`, PySport*.
- **Contenido Técnico**: Por qué la exactitud simple (accuracy) oculta el desbalance de clases en torneos y cómo la calibración con regularización L2 en LightGBM reduce el error cuadrático un $+21.3\%$.
- **Gráfico a Mostrar**: Reliability Diagram con bandas de confianza empíricas.
- **Pregunta a la Comunidad**: *"¿Preferís isotonic regression o Platt scaling para calibrar modelos de gradient boosting en muestras deportivas moderadas ($N \approx 1.000$)?"*

---

### 🎲 Caso 4: "Muestras Pequeñas en Torneos Cortos (6–9 partidos): Contracción Bayesiana ($\lambda = 0.75$) en Simulación Monte Carlo"
- **Comunidades Adecuadas**: *Reddit `r/NBAanalytics`, SportsDataverse*.
- **Contenido Técnico**: Varianza extrema en porcentajes de triple durante fases de grupos y cómo la contracción bayesiana evita que rachas cortas sobreestimen las probabilidades de campeonato en $180.000$ iteraciones estocásticas.
- **Gráfico a Mostrar**: Distribución de ranking de campeón simulado (`reports/figures/mvp7/fig_02_tournament_simulation.png`).
- **Pregunta a la Comunidad**: *"¿Cómo ponderáis la forma reciente de un equipo frente a su calidad estructural histórica antes de unos playoffs o torneo corto?"*

---

### 🔄 Caso 5: "Arquitectura Dual: Conexión Nativa DuckDB $\leftrightarrow$ R sin Duplicación de Datos"
- **Comunidades Adecuadas**: *Madrid R Users Group, Posit Community, RStats*.
- **Contenido Técnico**: Uso de `DBI::dbConnect(duckdb::duckdb(read_only=TRUE))` para consultar tablas y marts Parquet generados por Python, con verificación de 0 discrepancias numéricas en 9 métricas clave.
- **Gráfico a Mostrar**: Gráficos longitudinales generados con `ggplot2` y `theme_basketball_analytics()`.
- **Pregunta a la Comunidad**: *"¿Qué experiencia tenéis integrando DuckDB directamente en pipelines reproducibles con Quarto CLI?"*

---

### 🏀 Caso 6: "Del Algoritmo a la Pizarra: El Brief Prepartido Ejecutivo de 1.5 Páginas"
- **Comunidades Adecuadas**: *AEEB, Escuela Entrenadores FBM, LinkedIn*.
- **Contenido Técnico**: Cómo traducir modelos numéricos complejos a 3 preguntas tácticas procesables para el cuerpo técnico antes de la sesión de vídeo, incorporando alertas de vulnerabilidad en pick-and-roll.
- **Gráfico a Mostrar**: Ejemplo anonimizado de Brief Prepartido (`reports/mvp10/`).
- **Pregunta a la Comunidad**: *"Entrenadores y analistas: ¿Qué información consideráis imprescindible en una sola página dos días antes del partido?"*

---

### 👥 Caso 7: "Más Allá del 1 al 5: Minería de 6 Arquetipos Funcionales con K-Means++ y PCA"
- **Comunidades Adecuadas**: *Reddit `r/NBAanalytics`, SportsDataverse*.
- **Contenido Técnico**: Agrupamiento no supervisado sobre 3.767 campañas cualificadas ($\ge 40$ min), validando interpretabilidad de baloncesto (Primary Initiator, Floor Spacer, Interior Hub, etc.) con $>60\%$ de varianza explicada.
- **Gráfico a Mostrar**: Proyección en el espacio de componentes principales de `reports/figures/mvp3/`.
- **Pregunta a la Comunidad**: *"¿Utilizáis arquetipos basados en datos para evaluar el equilibrio de quintetos en pista en vuestros análisis?"*

---

### 🔍 Caso 8: "Resolución Determinista de Entidades: Desduplicando 2.124 Jugadores FIBA sin Servicios de Pago"
- **Comunidades Adecuadas**: *PySport, SportsDataverse (`hoopR`), r/dataengineering*.
- **Contenido Técnico**: Pipeline determinista de resolución de identidades a través de 18 torneos oficiales, generando identificadores canónicos inmutables (`pau_gasol_1980`) con control de calidad estricto de 200 minutos por encuentro.
- **Gráfico a Mostrar**: Esquema del motor de QA y reglas de validación relacional.
- **Pregunta a la Comunidad**: *"¿Cómo abordáis la desduplicación de nombres de atletas internacionales con caracteres diacríticos o transcripciones fonéticas variables?"*
