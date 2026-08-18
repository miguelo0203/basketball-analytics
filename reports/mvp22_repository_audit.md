# AUDITORÍA PRE-PUBLICACIÓN Y EMPAQUETADO DEL REPOSITORIO (MVP-22)
## International Basketball Analytics (2005–2024)

> **Objetivo**: Clasificar todos los directorios y archivos del repositorio para asegurar una publicación pública limpia, profesional y libre de artefactos temporales o dependencias ocultas.

---

## 1. Clasificación de Componentes del Repositorio

| Directorio / Archivo | Categoría | Motivo y Justificación | Acción Recomendada |
|---|:---:|---|---|
| `README.md` | **A. PUBLICAR** | Puerta de entrada principal para hiring managers, analistas y entrenadores. | **PUBLICAR** (Mantener) |
| `LICENSE` | **A. PUBLICAR** | Licencia abierta MIT con aviso legal de procedencia de datos de baloncesto. | **PUBLICAR** (Mantener) |
| `CITATION.cff` | **A. PUBLICAR** | Formato estándar de citación para proyectos de investigación y software. | **PUBLICAR** (Mantener) |
| `requirements.txt` | **A. PUBLICAR** | Especificación exacta de dependencias deterministas de Python. | **PUBLICAR** (Mantener) |
| `.gitignore` | **A. PUBLICAR** | Control de exclusión de temporales, caches de Quarto, pytest y venv. | **PUBLICAR** (Mantener) |
| `src/` (33 módulos) | **A. PUBLICAR** | Código fuente en Python para ETL, validación de datos, ML supervisado y workspace. | **PUBLICAR** (Mantener) |
| `R/` (6 scripts + Quarto) | **A. PUBLICAR** | Capa analítica en R (`ggplot2`, `tidyverse`, Quarto `.qmd` compilado en HTML). | **PUBLICAR** (Mantener) |
| `scripts/` (4 scripts) | **A. PUBLICAR** | Scripts de ejecución unificada (`run_project.py`, `verify_environment.py`). | **PUBLICAR** (Mantener) |
| `tests/` (26 módulos) | **A. PUBLICAR** | Suite completa de 227 tests automatizados en pytest con 100% de tasa de éxito. | **PUBLICAR** (Mantener) |
| `data/01_raw/` | **A. PUBLICAR** | Archivos brutos archivados localmente para permitir reproducción offline. | **PUBLICAR** (Mantener) |
| `data/03_validated/` | **A. PUBLICAR** | Almacén relacional certificado `basketball_analytics.duckdb` (28.51 MB). | **PUBLICAR** (Mantener) |
| `data/04_analytics/` | **A. PUBLICAR** | 11 marts analíticos en Apache Parquet con firmas SHA-256 inmutables. | **PUBLICAR** (Mantener) |
| `docs/` (40 documentos) | **A. PUBLICAR** | Arquitectura, linaje de datos, diccionario de variables y manifiesto. | **PUBLICAR** (Mantener) |
| `portfolio/` | **A. PUBLICAR** | CV de 1 página, guías de entrevista, perfiles y presentación ejecutiva. | **PUBLICAR** (Mantener) |
| `presentation/` | **A. PUBLICAR** | Hub de acceso directo a la presentación de 30 diapositivas y guiones. | **PUBLICAR** (Mantener) |
| `reports/` | **A. PUBLICAR** | Informes técnicos de auditoría, figuras analíticas y briefs prepartido. | **PUBLICAR** (Mantener) |
| `config/` | **A. PUBLICAR** | Configuraciones maestras de torneos, equipos y reglas FIBA. | **PUBLICAR** (Mantener) |
| `.pytest_cache/` | **B. NO PUBLICAR** | Caches temporales de ejecución de tests. | **IGNORAR EN .GITIGNORE** |
| `.quarto/` & `*_files/` | **B. NO PUBLICAR** | Caches temporales de compilación de Quarto. | **IGNORAR EN .GITIGNORE** |
| `__pycache__/` | **B. NO PUBLICAR** | Bytecode compilado de Python. | **IGNORAR EN .GITIGNORE** |
| `career/` & `interview/` | **C. OPCIONAL** | Documentos internos de soporte previo consolidados en `portfolio/`. | **MANTENER / DOCUMENTAR** |

---

## 2. Mapa de Navegación Rápida para el Evaluador Externo (< 60 Segundos)

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        CÓMO REVISAR EL REPOSITORIO EN 3 PASOS                          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. ¿Qué es y qué resultados produce?                                                   │
│    └── Leer el README.md (30 segundos) y ver la presentación en presentation/README.md │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. ¿Cómo funciona la arquitectura y el código?                                         │
│    └── Consultar docs/arquitectura.md y ver la capa R en R/README.md                   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. ¿Cómo comprobar que todo ejecuta y es reproducible?                                 │
│    └── Ejecutar en un solo comando: `python scripts/run_project.py` (227 tests passing)│
└────────────────────────────────────────────────────────────────────────────────────────┘
```
