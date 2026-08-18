# ESTRUCTURA Y PROCEDENCIA DE DATOS (DATA DIRECTORY)
## International Basketball Analytics (2005–2024)

Este directorio contiene los datos del proyecto organizados en 4 niveles de madurez siguiendo la arquitectura de medallón (*Medallion Architecture*):

```text
data/
├── 01_raw/             # Archivos brutos locales estructurados (18 torneos oficiales FIBA)
│   └── SRC_WIKI_ARCHIVE/
├── 02_staging/         # Base de datos de preparación intermedia (staging.duckdb)
├── 03_validated/       # Almacén OLAP certificado (basketball_analytics.duckdb, 28.51 MB)
└── 04_analytics/       # Marts analíticos en formato Apache Parquet (11 archivos)
```

---

## 1. Niveles de Datos

### `01_raw/` (Datos Brutos)
- Contiene los archivos HTML y JSON archivados localmente correspondientes a los 18 torneos oficiales disputados entre 2005 y 2024 (EuroBasket, Copas del Mundo y Juegos Olímpicos).
- Permite la reconstrucción del almacén DuckDB de forma **100% offline**, reproducible y sin necesidad de ejecutar peticiones activas de scraping contra servidores federativos.

### `02_staging/` (Staging)
- Esquema temporal generado por `src/ingestion/run_mvp0.py` donde se ejecutan los parsers iniciales de actas y plantillas.

### `03_validated/` (Almacén OLAP Validado)
- Base de datos relacional columnar `basketball_analytics.duckdb` (28.51 MB) con 12 tablas (dimensiones y hechos).
- Incluye 1.145 partidos oficiales, 2.290 observaciones de equipo, 2.124 jugadores canónicos y 27.353 actuaciones individuales, validada mediante reglas deterministas (cuadre estricto de 200 min/partido).

### `04_analytics/` (Marts Analíticos en Parquet)
- Marts columnares comprimidos en formato Apache Parquet para lectura concurrente de alto rendimiento desde Python y R.
- Incluyen variables de Four Factors, ratios por 40 minutos, características prepartido para Machine Learning y simulaciones Monte Carlo.

---

## 2. Procedencia y Ética

- **Fuente**: Actas oficiales y registros públicos de eventos deportivos internacionales de selecciones nacionales absolutas masculinas (FIBA / COI 2005–2024).
- **Finalidad**: Investigación no comercial, modelado cuantitativo, educación y demostración de competencias en ingeniería de datos y analítica deportiva.
- **Integridad Criptográfica**: Las firmas SHA-256 de todos los datos validados y marts están documentadas en [docs/reproducibility_manifest.md](../docs/reproducibility_manifest.md).
