# AUDITORÍA DE PRESENTACIÓN DEL GITHUB (MVP-19)
## International Basketball Analytics (2005–2024)

> **Objetivo**: Evaluar cómo percibe el repositorio un visitante externo según su perfil técnico y optimizar su visibilidad y facilidad de navegación sin añadir complejidad innecesaria.

---

## 1. Evaluación por Tipo de Visitante Externo

### 👤 Perfil 1: Analista de Baloncesto Profesional
- **Lo que busca en los primeros 30s**: ¿Entiende el autor el juego real o solo aplica algoritmos genéricos? ¿Usa Four Factors, posesiones y ritmo?
- **Experiencia en el repositorio**: Encuentra de inmediato las métricas de Dean Oliver, los mapas de tiro, los arquetipos funcionales y la codificación de vídeo de pick-and-roll con $\kappa = 0.80$.
- **Tiempo de comprensión**: $\approx 45$ segundos.
- **Veredicto**: **EXCELENTE (GREEN)**.

---

### 👤 Perfil 2: Hiring Manager / Lead Data Engineer
- **Lo que busca en los primeros 30s**: ¿El código es limpio y modular? ¿Hay tests automatizados? ¿El pipeline es determinista? ¿Hay data leakage?
- **Experiencia en el repositorio**: Observa la arquitectura DuckDB/Parquet, los 227 tests en pytest pasando al 100%, la validación walk-forward en 17 folds y los hashes criptográficos SHA-256 en el manifiesto.
- **Tiempo de comprensión**: $\approx 30$ segundos.
- **Veredicto**: **EXCELENTE (GREEN)**.

---

### 👤 Perfil 3: Entrenador de Baloncesto (Sin conocimientos de Python)
- **Lo que busca en los primeros 30s**: ¿Esto me ayuda a preparar el partido del domingo o es una pérdida de tiempo llena de fórmulas?
- **Experiencia en el repositorio**: El [Portfolio Hub](portfolio/README.md) y los briefs prepartido de 1.5 páginas le muestran preguntas tácticas directas (*"¿Cómo defender el bloqueo directo si el rival tiene un tirador por encima del 40% en pull-up?"*).
- **Tiempo de comprensión**: $\approx 60$ segundos.
- **Veredicto**: **MUY BUENO (GREEN)**.

---

## 2. Recomendaciones de Optimización de GitHub (Topics, Release & Metadata)

Para maximizar la descubribilidad orgánica en GitHub, se recomienda configurar los siguientes metadatos públicos:

### 🏷️ GitHub Topics Recomendados:
```text
basketball-analytics, sports-analytics, duckdb, python, rstats, quarto, 
sports-data, machine-learning, lightgbm, sports-engineering, fiba-basketball, 
walk-forward-validation, monte-carlo, streamlit, dean-oliver-four-factors
```

### 📝 Descripción Oficial del Repositorio (About Box):
> *End-to-End International Basketball Analytics System (2005–2024). 1,145 games, DuckDB OLAP warehouse, calibrated Machine Learning (17-fold walk-forward), non-parametric R statistics, and tactical decision support for coaching staffs. 227 tests (100% pass).*

### 📦 GitHub Release v1.0.0:
- **Tag**: `v1.0.0-release`
- **Título**: *International Basketball Analytics (2005–2024) — Production Release*
- **Contenido**: Manifiesto SHA-256 congelado, informe Quarto compilado en HTML (`exploratory_analysis.html`) y paquete completo de 227 tests automatizados.
