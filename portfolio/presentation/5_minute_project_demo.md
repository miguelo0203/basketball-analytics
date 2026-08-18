# Demostración del Proyecto en 5 Minutos (Live Demo Script)
## Guión Cronometrado para Demostración Práctica en Entrevistas Técnicas

**Duración**: Exactamente 5:00 Minutos  
**Objetivo**: Demostrar madurez analítica, rigor metodológico y fluidez baloncestística.

---

### 0:00–0:30 | Quién Soy y Qué Problema Aborda el Proyecto
> "Hola. Soy analista de datos de baloncesto. Construí este proyecto para resolver un problema recurrente en cuerpos técnicos: la sobrecarga de estadísticas descontextualizadas y la dificultad para separar la señal del ruido en muestras cortas de torneo. Mi objetivo fue crear un sistema integral y reproducible que cubriera toda la cadena: desde la ingesta de datos brutos hasta la entrega de briefs prepartido ejecutivos para el entrenador."

---

### 0:30–1:30 | Datos, Almacén DuckDB y Calidad Inmutable
> "Trabajé con 20 años de torneos internacionales oficiales (18 campeonatos entre 2005 y 2024, 1.145 partidos y más de 27.000 registros individuales). 
> 
> En lugar de trabajar sobre hojas de cálculo dispersas, diseñé un almacén relacional de 12 tablas en **DuckDB y Parquet**. Para garantizar la calidad, implementé firmas SHA-256 y reglas automáticas de QA que verifican matemáticamente que cada partido sume exactamente 200 minutos por quinteto y que la suma de puntos individuales cuadre al 100% con el marcador oficial."

---

### 1:30–2:30 | Flujo Analítico: Four Factors y Arquetipos Funcionales
> "En la capa de analítica de baloncesto, normalizamos el juego por posesión mediante los **Four Factors de Dean Oliver**. 
> 
> Para evaluar jugadores sin caer en el sesgo de los puntos por partido (PPG), analicé 3.767 campañas cualificadas utilizando **K-Means++ y PCA**, descubriendo 6 arquetipos funcionales objetivos (Iniciadores, Espaciadores, Ejes Interiores, Directores, Anclas Defensivas y Aleros Equilibrados). Además, validamos la cinta de vídeo con doble codificación independiente en 420 posesiones de pick-and-roll, alcanzando una fiabilidad inter-evaluador de $\kappa = 0.80$."

---

### 2:30–3:30 | Machine Learning sin Fuga Temporal y Calibración
> "Para el modelado predictivo, evité los K-Folds aleatorios que contaminan los datos con información del futuro. Diseñé **17 folds temporales walk-forward expansivos**, evaluando 1.105 partidos estrictamente fuera de muestra.
> 
> Con **LightGBM** obtuvimos un Brier Score de `0.1967`, un ROC-AUC de `0.7613` y un Expected Calibration Error (ECE) de solo `0.0314` (3.14%), lo que certifica que las probabilidades estimadas son estadísticamente fiables para propagar a nuestras 180.000 simulaciones Monte Carlo con shrinkage ($\lambda = 0.75$)."

---

### 3:30–4:30 | De los Datos al Soporte a Decisiones en Pizarra
> "Todo este procesamiento cuantitativo se traduce en **Briefs Prepartido de 1.5 páginas** (lectura en 2.5 minutos) y un Workspace interactivo en Streamlit con aislamiento anti-hindsight.
> 
> Por ejemplo, en la final olímpica de Pekín 2008 entre España y EE. UU., el sistema detectó la contradicción entre el favoritismo numérico de EE. UU. (+31 pts de margen) y su vulnerabilidad táctica en vídeo (su pívot jugaba drop muy profundo concediendo tiros liberados en pick-and-pop). El brief recomendó castigar ese espacio con pívots exteriores y aplicar zona 2-3 para frenar la transición, ajustes con los que España compitió hasta el minuto final."

---

### 4:30–5:00 | Qué Haría con Datos Reales de Club
> "Este proyecto demuestra mi método sobre datos históricos. En un club profesional de ACB o Euroliga, aplicaría esta misma arquitectura conectándola a feeds de tracking 25Hz de Second Spectrum, play-by-play de Synergy, métricas físicas de Catapult GPS y al ritmo de trabajo semanal del equipo para apoyar las decisiones del cuerpo técnico desde el primer día."
