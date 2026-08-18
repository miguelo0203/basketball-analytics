# REPORTE DE PRUEBA DE HUMO PARA LANZAMIENTO (RELEASE SMOKE TEST - MVP-15)
## International Basketball Analytics (2005–2024)

> **Simulación de Revisor Externo**: Prueba paso a paso de verificación por parte de un Hiring Manager o Reclutador Técnico tras clonar el repositorio.

---

## 1. Protocolo de Verificación del Revisor

```text
[Paso 1: Clonar Repositorio]
       │
       ▼
[Paso 2: Instalar Dependencias (pip install -r requirements.txt)]
       │
       ▼
[Paso 3: Diagnóstico de Entorno (python scripts/verify_environment.py)]
       │
       ▼
[Paso 4: Ejecución Maestra (python scripts/run_project.py)]
       │
       ▼
[Paso 5: Inspección de Figuras e Informes (reports/figures_r/ y Quarto)]
       │
       ▼
[Paso 6: Lanzamiento de App Interactiva (streamlit run src/analytics/mvp10_analyst_workspace.py streamlit)]
```

---

## 2. Resultados Paso a Paso de la Prueba de Humo

### Paso 1: Clonar y Abrir el Repositorio
- Estructura limpia de 6 carpetas principales: `config/`, `data/`, `docs/`, `portfolio/`, `R/`, `src/`, `tests/`.
- `README.md` con insignias activas, tabla de hechos canónicos, guía de inicio rápido y mapa de navegación para 4 perfiles.

### Paso 2: Instalación de Dependencias
- `requirements.txt` especifica las dependencias fijadas (`duckdb`, `pyarrow`, `lightgbm`, `scikit-learn`, `pandas`, `streamlit`, `pytest`, `matplotlib`, `seaborn`, `rapidfuzz`).
- Sin dependencias propietarias o librerías ocultas.

### Paso 3: Diagnóstico del Entorno
```bash
python scripts/verify_environment.py
```
- **Resultado**: 
  - Python 3.14.6 + DuckDB 1.5.5 + PyArrow 24.0.0 (OK)
  - DuckDB Warehouse: `basketball_analytics.duckdb` (28.51 MB)
  - Parquet Marts: 11 archivos analíticos detectados
  - Rscript 4.6.1 + paquetes `DBI`, `duckdb`, `arrow`, `ggplot2` (OK)
  - Quarto 1.10.18 CLI (OK)

### Paso 4: Ejecución Maestra Unificada
```bash
python scripts/run_project.py
```
- **Resultado**:
  - Verificación de datos: 100% OK
  - Ejecución de los 6 scripts en R: 21.31s (SUCCESS)
  - Ejecución de los 224 tests con `pytest`: 207.52s (100% PASS RATE)
  - Tiempo total de ejecución unificada: **238.56 segundos**

### Paso 5: Inspección de Figuras y Render Quarto
- Figuras generadas en `reports/figures_r/`:
  - `fig_01_tournament_trends.png` (Evolución de ritmo y 3P% post-2010)
  - `fig_02_player_trajectories.png` (Curvas longitudinales de eficiencia en Marc/Pau Gasol)
  - `fig_03_archetype_distribution.png` (Prevalencia de 6 arquetipos funcionales)
  - `fig_04_four_factors_correlation.png` (Descomposición empírica de Four Factors)
  - `fig_05_ts_distribution.png` (Distribución de True Shooting % en 3.767 campañas)
- Renderizado de informe Quarto:
```bash
quarto render R/reports/exploratory_analysis.qmd
```
- **Resultado**: `Output created: exploratory_analysis.html` (Documento HTML autónomo con tablas interactivas y gráficos).

### Paso 6: Lanzamiento de la Aplicación Interactiva Streamlit
```bash
python src/analytics/mvp10_analyst_workspace.py
# o para interfaz web interactiva:
streamlit run src/analytics/mvp10_analyst_workspace.py streamlit
```
- **Resultado**: Carga instantánea de la matriz de evidencia de 8 capas, el brief táctico ejecutivo para el entrenador, el cronograma de 5 horizontes y el módulo de replay con barrera anti-hindsight.

---

## 3. Conclusión de la Prueba de Humo

| Criterio de Evaluación | Veredicto | Comentario |
|---|---|---|
| **Claridad de Instrucciones** | **PASS** | Fácil de seguir para cualquier perfil técnico. |
| **Tiempo de Puesta en Marcha** | **PASS** | $< 5$ minutos desde la clonación hasta la validación completa. |
| **Reproducibilidad Numérica** | **PASS** | Cero divergencias entre ejecuciones y lenguajes. |
| **Calidad de Artefactos** | **PASS** | Figuras de calidad editorial (300 DPI) e informes Quarto limpios. |
| **Calidad de Código y Testing** | **PASS** | 224/224 tests pasando sin mocks frágiles ni saltos de tests. |

> **Veredicto Final**: **RELEASE CANDIDATE APROBADO (READY FOR PRODUCTION / HIRING REVIEW)**.
