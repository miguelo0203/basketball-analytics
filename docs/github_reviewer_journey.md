# Guía de Exploración para el Revisor de GitHub
## Itinerarios de Lectura Optimizados según el Tiempo Disponible

---

### Si tienes 2 Minutos (Primer Vistazo Rápido)
- **Objetivo**: Comprender qué es el proyecto, su escala y qué problema aborda.
- **Acciones**:
  1. Lee la sección *El proyecto en 30 segundos* en el [README.md](../README.md).
  2. Revisa la tabla de cifras clave ($1.145$ partidos, 18 torneos, DuckDB, Python 3.14).
  3. Comprueba el badge de 195 tests pasando al $100\%$.

---

### Si tienes 5 Minutos (Evaluación de Dominio de Baloncesto)
- **Objetivo**: Evaluar la capacidad del candidato para estructurar decisiones tácticas.
- **Acciones**:
  1. Lee el [Caso Flagship: Pekín 2008 (España vs. EE. UU.)](../portfolio/flagship_case.md).
  2. Observa la contradicción táctica entre el drop defensivo y el pick-and-pop de los Gasol.
  3. Revisa la [Guía de Figuras Públicas](../portfolio/figure_guide.md).

---

### Si tienes 15 Minutos (Evaluación Metodológica)
- **Objetivo**: Verificar el rigor analítico, la calibración y la prevención de fugas de datos.
- **Acciones**:
  1. Consulta [docs/machine_learning.md](machine_learning.md) para ver la validación walk-forward en 17 folds.
  2. Consulta [docs/analisis_tactico.md](analisis_tactico.md) para revisar la fiabilidad Cohen's Kappa ($\kappa = 0.80$).
  3. Lee [docs/limitaciones.md](limitaciones.md) para comprobar la honestidad técnica.

---

### Si tienes 30 Minutos (Inspección Técnica de Código)
- **Objetivo**: Auditar la calidad del código, el almacén de datos y la arquitectura OOP.
- **Acciones**:
  1. Abre `src/analytics/mvp0_data_engineering.py` y `src/analytics/mvp6_supervised_analytics.py`.
  2. Ejecuta la aplicación interactiva localmente: `streamlit run src/analytics/mvp10_analyst_workspace.py -- streamlit`.
  3. Inspecciona las consultas SQL en `data/03_validated/basketball_analytics.duckdb`.

---

### Si tienes 60 Minutos (Auditoría Integral y Diligencia Debida)
- **Objetivo**: Replicabilidad total y validación completa de la suite.
- **Acciones**:
  1. Clona el repositorio y ejecuta la suite completa de tests: `python -m pytest tests -v`.
  2. Revisa la matriz de gobernanza de métricas en [docs/claims_y_limitaciones.md](claims_y_limitaciones.md).
  3. Comprueba que no existe ningún dato sintético presentado como dato real de club.
