# AUDITORÍA DEFINITIVA DE PUBLICACIÓN Y LANZAMIENTO PÚBLICO (MVP-23)
## International Basketball Analytics (2005–2024)

> **Objetivo**: Certificar la idoneidad, legalidad y limpieza técnica de todos los archivos y directorios del repositorio antes de su publicación como portfolio público en GitHub.

---

## 1. Declaración de la Arquitectura del Stack Técnico

El proyecto no es un script aislado ni un proyecto monotecnología. Responde a una arquitectura de ingeniería dual especializada:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               ARQUITECTURA DUAL: PYTHON + R + DUCKDB + PARQUET                         │
├───────────────────────────────────────────┬────────────────────────────────────────────┤
│ 🐍 PYTHON CORE (Ingeniería, ML & QA)      │ 📊 R STATISTICAL LAYER (EDA, Stats & Quarto│
│ • Pipelines de ingesta y normalización    │ • Análisis longitudinal de tiro y ritmo    │
│ • Conexión OLAP y consultas DuckDB        │ • Inferencia no paramétrica (Bootstrap)    │
│ • Modelado supervisado (LightGBM)         │ • Visualizaciones editoriales con ggplot2  │
│ • Simulación Monte Carlo (180k iter)      │ • Informes interactivos con Quarto CLI     │
│ • Suite de 227 tests en pytest (100% pass)│ • Conexión nativa de solo lectura a DuckDB │
├───────────────────────────────────────────┴────────────────────────────────────────────┤
│ 🗄️ ALMACÉN OLAP COLUMNAR COMÚN                                                          │
│ • DuckDB (basketball_analytics.duckdb, 28.51 MB con 12 tablas relacionales)            │
│ • Apache Parquet (11 marts analíticos con firmas criptográficas SHA-256)               │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Clasificación Exhaustiva de Archivos y Componentes

| Directorio / Archivo | Categoría de Publicación | Motivo y Justificación Legal / Técnica | Acción Recomendada |
|---|:---:|---|---|
| `README.md` | **PUBLICAR** | Portal de entrada principal en GitHub (<60s de lectura). | **PUBLICAR** |
| `LICENSE` | **PUBLICAR** | Licencia MIT de código abierto con aviso de datos públicos. | **PUBLICAR** |
| `CITATION.cff` | **PUBLICAR** | Metadatos estándar para citación académica y profesional. | **PUBLICAR** |
| `requirements.txt` | **PUBLICAR** | Dependencias deterministas fijadas sin conflictos. | **PUBLICAR** |
| `.gitignore` | **PUBLICAR** | Exclusión estricta de temporales, caches y entornos virtuales. | **PUBLICAR** |
| `src/` (33 módulos) | **PUBLICAR** | Código fuente en Python estructurado y tipado. | **PUBLICAR** |
| `R/` (6 scripts + Quarto) | **PUBLICAR** | Capa analítica en R (`ggplot2`, `tidyverse`, Quarto `.qmd`). | **PUBLICAR** |
| `scripts/` (4 scripts) | **PUBLICAR** | Entry points de ejecución unificada (`run_project.py`). | **PUBLICAR** |
| `tests/` (26 módulos) | **PUBLICAR** | 227 tests automatizados en pytest con 100% de éxito. | **PUBLICAR** |
| `data/01_raw/` | **PUBLICAR (LEGAL)** | Archivos brutos locales públicos para reproducción offline. | **PUBLICAR** |
| `data/03_validated/` | **PUBLICAR (LEGAL)** | Almacén certificado `basketball_analytics.duckdb` (28.51 MB). | **PUBLICAR** |
| `data/04_analytics/` | **PUBLICAR (LEGAL)** | 11 Marts Parquet con firmas SHA-256 verificadas. | **PUBLICAR** |
| `data/README.md` | **PUBLICAR** | Explicación de procedencia y arquitectura de medallón. | **PUBLICAR** |
| `docs/` (40 documentos) | **PUBLICAR** | Documentación técnica, linaje y manifiesto SHA-256. | **PUBLICAR** |
| `portfolio/` | **PUBLICAR** | CV, guías de entrevista, perfiles y networking. | **PUBLICAR** |
| `presentation/` | **PUBLICAR** | Acceso directo a la presentación de 30 diapositivas. | **PUBLICAR** |
| `reports/` | **PUBLICAR** | Informes de auditoría, briefs prepartido y figuras 300 DPI. | **PUBLICAR** |
| `config/` | **PUBLICAR** | Metadatos maestros de torneos, equipos y reglas FIBA. | **PUBLICAR** |
| `__pycache__/` | **NO PUBLICAR** | Bytecode compilado de Python. | **IGNORAR EN .GITIGNORE** |
| `.pytest_cache/` | **NO PUBLICAR** | Caches temporales de pytest. | **IGNORAR EN .GITIGNORE** |
| `.quarto/` & `*_files/` | **NO PUBLICAR** | Caches temporales de renderizado de Quarto. | **IGNORAR EN .GITIGNORE** |
| `.venv/` | **NO PUBLICAR** | Entornos virtuales locales. | **IGNORAR EN .GITIGNORE** |

---

## 3. Gobernanza y Procedencia de Datos

- **Naturaleza de los Datos**: Datos históricos públicos de eventos deportivos oficiales (FIBA / JJ.OO. 2005–2024).
- **Finalidad**: Investigación no comercial, portfolio técnico y demostración de habilidades de analítica deportiva.
- **Privacidad**: 0 datos médicos confidenciales, 0 telemetría biovigilada invasiva y 0 secretos corporativos.
- **Reproducción Offline Inmutable**: El repositorio incluye los archivos brutos locales estructurados en `data/01_raw/SRC_WIKI_ARCHIVE/`, lo que permite reconstruir el almacén de forma determinista sin ejecutar scraping en vivo contra servidores web.
