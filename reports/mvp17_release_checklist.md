# LISTA DE CONTROL PARA LANZAMIENTO PÚBLICO (RELEASE CHECKLIST - MVP-17)
## International Basketball Analytics (2005–2024)

> **Propósito**: Evaluación final de 19 dimensiones críticas para asegurar la preparación de publicación del portfolio.

---

## 1. Matriz de Control de Lanzamiento

| Área / Dimensión | Estado | Evidencia de Verificación Real | Acción Requerida |
|---|:---:|---|---|
| **1. Code Quality** | **GREEN** | Código modular bajo `src/` y `R/` con docstrings y tipado estricto. | Mantener |
| **2. Raw & Staging Data** | **GREEN** | Archivos brutos archivados localmente en `data/01_raw/SRC_WIKI_ARCHIVE/`. | Mantener |
| **3. Python Runtime** | **GREEN** | Python 3.14.6 con DuckDB 1.5.5, PyArrow 24.0.0 y Scikit-Learn 1.9.0. | Mantener |
| **4. R Statistical Layer** | **GREEN** | 6 scripts R ejecutables con Rscript 4.6.1 en 24.41s (exit code 0). | Mantener |
| **5. DuckDB Warehouse** | **GREEN** | `basketball_analytics.duckdb` (28.51 MB) con 12 tablas relacionales. | Mantener |
| **6. Machine Learning** | **GREEN** | 17 folds walk-forward, Brier 0.1967, ECE 0.0314, MAE 11.739. | Mantener |
| **7. Statistics & Invariance**| **GREEN** | Inferencia Bootstrap ($B=5.000$) y test de permutación ($P=10.000$). | Mantener |
| **8. Visualizations** | **GREEN** | 11 figuras regeneradas en alta resolución en `figures/` y `figures_r/`.| Mantener |
| **9. Quarto Reporting** | **GREEN** | `quarto render` genera `exploratory_analysis.html` en 12.80s. | Mantener |
| **10. Streamlit App** | **GREEN** | `src/analytics/mvp10_analyst_workspace.py` operativo con replay anti-hindsight.| Mantener |
| **11. Test Suite** | **GREEN** | **227 tests en pytest pasando al 100% (0 fallos, 0 errores)**. | Mantener |
| **12. Reproducibility** | **GREEN** | Manifiesto criptográfico SHA-256 en [docs/reproducibility_manifest.md](../docs/reproducibility_manifest.md). | Mantener |
| **13. Documentation** | **GREEN** | 40 documentos técnicos exhaustivos en español e inglés. | Mantener |
| **14. Portfolio Hub** | **GREEN** | Hub central en `portfolio/` con 4 rutas según perfil de audiencia. | Mantener |
| **15. CV Master & 1-Page** | **GREEN** | Plantillas de CV realistas en `portfolio/job_search/` sin puestos falsos.| Mantener |
| **16. LinkedIn Package** | **GREEN** | 5 headlines, 3 'About' y post de lanzamiento en `portfolio/job_search/`.| Mantener |
| **17. Data Provenance** | **GREEN** | Fuentes públicas oficiales documentadas en [config/sources.yaml](../config/sources.yaml). | Mantener |
| **18. Git Hygiene** | **GREEN** | `.gitignore` configurado, **0 secretos/API keys encontrados en escaneo**. | Mantener |
| **19. Interview Defensibility**| **GREEN** | 20 claims técnicos clave defendibles en entrevista con evidencia empírica.| Mantener |

---

## 2. Veredicto Global del Checklist

> **ESTADO DE LANZAMIENTO**: **19 / 19 DIMENSIONES EN VERDE (GREEN)**.  
> El repositorio se encuentra 100% listo para ser presentado a reclutadores, analistas de baloncesto y directores deportivos.
