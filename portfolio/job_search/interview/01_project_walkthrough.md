# 01 — Guía de Recorrido del Proyecto en Entrevistas (Project Walkthrough)
## Estructura para Explicar el Portfolio en 5 a 10 Minutos

---

### Paso 1: Introducción y Propósito (1 Minuto)
- **Mensaje**: *"Construí este proyecto para demostrar cómo cubro todo el ciclo de valor de un analista de datos de baloncesto: desde la ingeniería de datos en DuckDB y la analítica de Four Factors, hasta el modelado supervisado sin data leakage y la entrega de briefs de 1.5 páginas para entrenadores."*
- **Datos de Escala**: 20 años (2005–2024), 18 torneos oficiales, 1.145 partidos y 27.353 actuaciones de jugador.

---

### Paso 2: Datos y Control de Calidad (2 Minutos)
- **Mensaje**: *"La base de todo análisis es la integridad de los datos. En lugar de trabajar sobre CSVs sueltos, diseñé un almacén relacional de 12 tablas en DuckDB y Parquet. Implementé un pipeline determinista con firmas SHA-256 y reglas estrictas de QA que validan que cada partido sume exactamente 200 minutos y que los puntos individuales cuadren al 100% con el marcador oficial."*

---

### Paso 3: Analítica Táctica y Roles Funcionales (2 Minutos)
- **Mensaje**: *"En baloncesto, los puntos por partido (PPG) engañan si no se normalizan por posesión y rol. Analicé 3.767 campañas cualificadas mediante K-Means++ y PCA, identificando 6 arquetipos funcionales objetivos (Iniciadores, Espaciadores, Ejes Interiores, Directores, Anclas Defensivas y Aleros Equilibrados). Además, validé la capa de vídeo con doble codificación independiente en 420 posesiones de pick-and-roll, alcanzando una fiabilidad inter-evaluador de $\kappa = 0.80$."*

---

### Paso 4: Machine Learning sin Fuga Temporal y Calibración (2 Minutos)
- **Mensaje**: *"Para evitar el data leakage de los K-Folds aleatorios, diseñé 17 folds walk-forward expansivos. El modelo de 2008 jamás vio datos posteriores a 2007. Con LightGBM obtuvimos un Brier Score de `0.1967`, un ROC-AUC de `0.7613` y un Expected Calibration Error (ECE) de `0.0314` (3.14%), lo que asegura que las probabilidades estimadas son seguras para propagar a 180.000 simulaciones Monte Carlo con shrinkage ($\lambda = 0.75$)."*

---

### Paso 5: Soporte a Decisiones y Cierre (2 Minutos)
- **Mensaje**: *"Todo esto culmina en un generador de briefs prepartido de 1.5 páginas y un workspace en Streamlit con aislamiento anti-hindsight. Mi objetivo no es decirle al entrenador cómo jugar, sino ahorrarle tiempo, filtrar el ruido estadístico y formular preguntas concretas para la pizarra técnica."*
