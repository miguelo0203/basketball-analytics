# DISTRIBUCIÓN DEL PROYECTO A TRAVÉS DE COMUNIDADES DE CONOCIMIENTO (MVP-20)
## International Basketball Analytics (2005–2024)

> **Principio de Difusión**: *El repositorio de GitHub es la fuente única de verdad; las comunidades son puertas de entrada contextualizadas que muestran la parte exacta del proyecto que interesa a cada audiencia.*

---

## 1. Matriz de Adaptación de Contenidos por Comunidad

| Comunidad / Ecosistema | Qué Componente del Proyecto Enseñar | Formato y Enfoque Recomendado | Qué NO Enseñar / Evitar |
|---|---|---|---|
| **Basketball Analytics** (`r/NBAanalytics`, SportsDataverse) | Dean Oliver Four Factors, 6 Arquetipos funcionales, análisis longitudinal de True Shooting %. | Hilo explicativo con gráficos limpios de `reports/figures_r/` y mapas de tiro. | Evitar aburrir con detalles internos de ingeniería SQL si lo que interesa es el impacto táctico. |
| **Comunidades R / RStats** (`Madrid RUG`, Posit Community) | Conexión nativa R $\leftrightarrow$ DuckDB vía `DBI`, análisis longitudinal con `tidyverse` e informes Quarto. | Snippet de código R reproducible + enlace al `.qmd` compilado en HTML. | Evitar hablar de Machine Learning en Python si la audiencia busca buenas prácticas en R y Quarto. |
| **Comunidades DuckDB / Data Eng.** (`DuckDB Discord`, PyData Madrid) | Almacén relacional OLAP de 12 tablas, compresión Snappy en Parquet, integridad criptográfica SHA-256 y QA determinista. | Diagrama de arquitectura de datos (`docs/arquitectura.md`) y consultas de ventana en SQL. | Evitar centrarse en opiniones deportivas sobre jugadores; centrarse en throughput y tiempos de consulta. |
| **Comunidades de Machine Learning** (`r/sportsanalytics`, Kaggle) | Esquema Walk-Forward en 17 particiones cronológicas, Brier Score ($0.1967$), ECE ($0.0314$) y calibración de probabilidades. | Curvas de calibración y análisis de feature importance out-of-sample. | Evitar presentar métricas clásicas no calibradas (como accuracy simple) que ocultan el desbalance de clases. |
| **Comunidades de Entrenadores** (`AEEB`, Escuela FBM) | Brief Prepartido de 1.5 páginas, alertas de vulnerabilidad en pick-and-roll drop y preguntas para la sesión de vídeo. | Ejemplo de informe de 1 página listo para imprimir o leer en tablet antes de entrenar. | Prohibido enseñar código, fórmulas matemáticas complejas o tecnicismos de algoritmos. |

---

## 2. El Repositorio de GitHub como Eje Central

```text
                               ┌────────────────────────┐
                               │   PySport Community    │
                               └───────────┬────────────┘
                                           │
┌─────────────────────────┐                ▼                ┌─────────────────────────┐
│  Reddit r/sportsanalytics│ ────►  REPOSITORIO GITHUB   ◄────│   DuckDB Discord &      │
│  (Validación & ML)      │       [CENTRO INMUTABLE]        │   Data Engineering Hub  │
└─────────────────────────┘                ▲                └─────────────────────────┘
                                           │
                               ┌───────────┴────────────┐
                               │    AEEB & Entrenadores │
                               │    (Briefs y Táctica)  │
                               └────────────────────────┘
```

El visitante que llega desde cualquier comunidad encuentra un README modular que le permite:
1. Validar la seriedad del proyecto en 30 segundos.
2. Explorar directamente el componente de su interés (Quarto, DuckDB, ML o Briefs).
3. Comprobar la reproducibilidad en un solo comando (`python scripts/run_project.py`).
