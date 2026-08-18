# SIMULACIÓN DE REVISIÓN EXTERNA EN 5 MINUTOS Y GUÍA DEMO (MVP-17)
## International Basketball Analytics (2005–2024)

> **Propósito**: Evaluar la navegabilidad del repositorio en una sesión de 5 minutos y definir el recorrido recomendado de demostración (Primary Demo).

---

## 1. Cronograma de Navegación del Revisor Externo (5 Minutos)

```text
[Minuto 0:00 - 1:00]  README.md
                      ├── Lee el bloque "El proyecto en 30 segundos"
                      ├── Revisa la tabla de cifras canónicas (1.145 partidos, 227 tests)
                      └── Identifica las tecnologías principales (DuckDB, Python, R, Quarto)

[Minuto 1:00 - 2:00]  Arquitectura y Linaje de Datos
                      ├── Abre docs/arquitectura.md y docs/execution_lineage.md
                      ├── Comprueba la separación dual-stack (Python para ML/ETL, R para EDA/Stats)
                      └── Observa la garantía anti-hindsight (aislamiento temporal prepartido)

[Minuto 2:00 - 3:00]  Demostración en R & Quarto
                      ├── Abre R/reports/exploratory_analysis.qmd y R/README.md
                      ├── Inspecciona las figuras generadas en reports/figures_r/
                      └── Comprueba el script de validación estadística (bootstrap B=5.000)

[Minuto 3:00 - 4:00]  Soporte a Decisiones del Entrenador
                      ├── Abre portfolio/presentation/5_minute_project_demo.md
                      ├── Examina un Brief Táctico Prepartido de 1.5 páginas (Pekín 2008 / EuroBasket 2022)
                      └── Revisa las alertas de contradicción táctica (P&R Drop vs Creador élite)

[Minuto 4:00 - 5:00]  Reproducibilidad y Candidatura
                      ├── Ejecuta en un solo comando: `python scripts/run_project.py`
                      ├── Abre portfolio/job_search/cv_one_page.md y candidate_profile.md
                      └── Conclusión: Perfil Junior+ técnicamente riguroso, estructurado y listo para entrevista.
```

---

## 2. Recorrido Recomendado de Demostración (PRIMARY DEMO)

Para una demostración en directo o entrevista técnica, el candidato debe seguir este flujo estructurado:

1. **Visión General del Proyecto**: [README.md](README.md)
   - Explicar el contexto: 20 años de torneos FIBA (2005–2024), 18 torneos y 1.145 partidos.
2. **Infraestructura de Datos y Almacén Común**: [docs/arquitectura.md](docs/arquitectura.md)
   - Mostrar cómo DuckDB (`basketball_analytics.duckdb`) y Parquet sirven de sustrato inmutable para Python y R.
3. **Capa Estadística y Visual en R**: [R/README.md](R/README.md)
   - Presentar el informe Quarto, las curvas longitudinales de jugadores y los intervalos bootstrap.
4. **Modelado Supervisado Calibrado y Simulación**: [reports/figures/](reports/figures/)
   - Demostrar el Brier Score ($0.1967$) y el ECE ($0.0314$) en 17 folds walk-forward.
5. **Brief Táctico y Soporte a Decisiones**: [src/analytics/mvp10_analyst_workspace.py](src/analytics/mvp10_analyst_workspace.py)
   - Enseñar la formulación de preguntas para el cuerpo técnico y la barrera anti-hindsight.
6. **Evidencia de Reproducibilidad en Vivo**: `python scripts/run_project.py`
   - Ejecutar la suite completa y mostrar los 227 tests pasando al 100%.

---

## 3. Obstáculos Detectados y Soluciones Aplicadas

| Posible Obstáculo | Dificultad Inicial | Medida Aplicada |
|---|---|---|
| Demasiados documentos en el repositorio | Revisor saturado | Se estructuraron 4 rutas de navegación específicas en [portfolio/README.md](portfolio/README.md). |
| Comprensión del uso de R sin Rscript en PATH | Dudas sobre ejecución | Se incluyó fallback automático y validación estática/dinámica en `tests/analytics/test_r_integration.py` y `scripts/run_r_analysis.R`. |
| Complejidad de los 14 MVPs históricos | Sobrecarga temporal | Se diseñó el script de 5 minutos en [portfolio/presentation/5_minute_project_demo.md](portfolio/presentation/5_minute_project_demo.md). |
