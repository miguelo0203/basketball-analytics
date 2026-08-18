# 02 — Preguntas Técnicas de Entrevista (Technical Defense)
## Arquitectura, Datos, Machine Learning y Calibración

---

### 1. ¿Por qué utilizaste DuckDB en lugar de Pandas puro o PostgreSQL?
> **Respuesta**: DuckDB es un motor OLAP columnar en proceso (*in-process*) optimizado para análisis vectorizados masivos. Frente a Pandas, procesa consultas analíticas complejas con ejecución en memoria multinúcleo y soporte nativo de SQL estándar. Frente a PostgreSQL, no requiere mantener un servidor externo, simplificando el despliegue local y garantizando la inmutabilidad y reproducibilidad del entorno.

---

### 2. ¿Por qué exportar los marts analíticos en formato Parquet?
> **Respuesta**: Apache Parquet es un formato binario columnar comprimido (Snappy) que permite leer únicamente las columnas requeridas (*column pruning*) y saltar bloques de datos mediante metadatos (*predicate pushdown*). Esto acelera drásticamente la carga de datos en scripts de Python y aplicaciones interactivas en Streamlit.

---

### 3. ¿Cómo garantizaste la ausencia de fuga de datos (*data leakage*)?
> **Respuesta**: En series temporales deportivas, los partidos futuros no son independientes de los pasados. Un K-Fold aleatorio convencional mezcla información futura en el conjunto de entrenamiento. Para evitarlo:
> 1. Implementé **17 folds temporales walk-forward expansivos**, donde el conjunto de entrenamiento solo contiene datos anteriores al torneo evaluado.
> 2. Todas las variables prepartido (*features*) se calculan utilizando únicamente información disponible antes del salto inicial ($< \text{game\_date}$).

---

### 4. ¿Por qué elegiste LightGBM en lugar de redes neuronales profundas (Deep Learning)?
> **Respuesta**: En datos tabulares con muestras moderadas (1.145 partidos), los modelos basados en árboles de decisión potenciados por gradiente (GBDT) como LightGBM superan sistemáticamente a las redes neuronales profundas. LightGBM es insensible a escalas heterogéneas, maneja correlaciones multilineales y permite regularizar fuertemente (`max_depth=3`, `num_leaves=7`, `min_child_samples=15`) para evitar memorizar el ruido.

---

### 5. ¿Qué representa el Brier Score y por qué es superior al Accuracy en este contexto?
> **Respuesta**: El Brier Score es una regla de puntuación estrictamente adecuada (*strictly proper scoring rule*) que calcula el error cuadrático medio de las probabilidades: $\text{BS} = \frac{1}{N}\sum (p_i - y_i)^2$. La precisión binaria (Accuracy) descarta la incertidumbre (trata un 51% igual que un 99%). El Brier Score castiga la sobreconfianza errónea. Nuestro modelo obtuvo `0.1967`, batiendo ampliamente el baseline de `0.2500`.

---

### 6. ¿Qué es el Expected Calibration Error (ECE) y qué significa que sea 0.0314?
> **Respuesta**: El ECE mide la desviación absoluta media ponderada entre la probabilidad pronosticada y la frecuencia real de victoria observada en 10 intervalos uniformes. Un ECE de `0.0314` (3.14%) certifica que cuando el modelo estima un 70% de probabilidad de victoria, empíricamente el equipo gana aproximadamente 7 de cada 10 veces, lo que valida su uso para simulación estocástica.

---

### 7. ¿Por qué la atribución de características no implica causalidad?
> **Respuesta**: Evaluamos la importancia mediante Permutation Importance out-of-sample (midiendo la caída en Brier Score al permutar cada variable). Los valores de importancia describen la relevancia condicional de la variable dentro de la función matemática del algoritmo; no constituyen una prueba causal ni garantizan que forzar un cambio en esa métrica en la pista produzca una victoria.
