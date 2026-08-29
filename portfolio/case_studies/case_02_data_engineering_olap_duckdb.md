[🇪🇸 Español](case_02_data_engineering_olap_duckdb.md) | [🇬🇧 English](case_02_data_engineering_olap_duckdb_EN.md)

# CASO DE ESTUDIO 2: INGENIERÍA DE DATOS Y ALMACÉN OLAP CON DUCKDB Y PARQUET
## International Basketball Analytics (2005–2024)

> **Perfil de Audiencia**: *Lead Data Engineers, Analytics Engineers, CTOs y Directores de Tecnología en Sports Tech.*  
> **Pregunta Clave**: *¿Cómo diseñar un pipeline analítico determinista para 20 años de competiciones heterogéneas con cero data leakage y ejecución 100% offline?*

---

## 1. El Reto Técnico de los Datos Deportivos Históricos

Los datos de torneos internacionales (FIBA / JJ.OO.) abarcan dos décadas (2005–2024) con múltiples cambios de formato:
1. **Heterogeneidad de Nombres**: Caracteres diacríticos variables, transliteraciones fonéticas (ej. *Dirk Nowitzki*, *Vassilis Spanoulis*, *Bojan Bogdanović* vs *Bogdan Bogdanović*) y falta de IDs federativos únicos persistentes.
2. **Inconsistencias de Actas**: Actas históricas con errores en suma de puntos o minutos no cuadriláteros.
3. **Escalabilidad y Dependencias**: Necesidad de un almacenamiento columnar ligero, portable y que no dependa de servidores Postgres/Snowflake en la nube.

---

## 2. Arquitectura de Medallón Implementada

```text
data/
├── 01_raw/             # 18 Torneos FIBA archivados localmente (HTML/JSON brutos)
├── 02_staging/         # Esquema de preparación temporal
├── 03_validated/       # Almacén OLAP relacional en DuckDB (12 tablas, 28.5 MB)
└── 04_analytics/       # 11 Marts columnares en Apache Parquet con firmas SHA-256
```

---

## 3. Componentes de Ingeniería Clave

### 🧩 1. Motor de Resolución Determinista de Entidades (`entity_resolver.py`)
- Unificación de **2.124 jugadores canónicos** a través de 27.353 actuaciones de partido sin APIs comerciales de pago.
- Generación de identificadores inmutables basados en *slugs* estandarizados y año de nacimiento verificado (ej. `pau_gasol_1980`).

### 🛡️ 2. Motor de Validación y Control de Calidad (`qa_engine.py`)
- **Regla de Cuadre de Minutos**: Verificación matemática estricta de exactamente **200 minutos por partido** (más 25 min adicionales por prórroga de 5 min) distribuidos entre los 5 jugadores en pista.
- **Cuadre de Puntuación**: Suma de tiros de campo ($2\text{P} + 3\text{P} + \text{TL}$) contrastada contra el tanteo final del acta.

### ⚡ 3. Almacén DuckDB y Marts Parquet
- **12 Tablas Relacionales**: Dimensiones (`dim_tournament`, `dim_team`, `dim_player`) y Hechos (`fact_team_game`, `fact_player_game`, `fact_tactical_possessions`).
- **Lectura Concurrente Python & R**: Acceso nativo vía `duckdb-python` y `DBI::dbConnect(duckdb::duckdb(read_only=TRUE))` con **0 duplicación de almacenamiento**.

---

## 4. Qué Demuestra este Caso de Estudio

- Dominio de **modelado dimensional (Star Schema / Medallion Architecture)**.
- Capacidad de construir **software robusto con 227 tests automatizados en pytest** (100% de éxito).
- Principios de **inmutabilidad y reproducibilidad criptográfica (SHA-256)**.
