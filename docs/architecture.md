# System Architecture & Technical Specifications
## International Basketball Historical Analytics (2005–2025)

---

## 1. System Overview

The system implements an end-to-end data pipeline designed for high auditability, source-level reproducibility, and robust sports analytics. The repository follows a 4-tier layer isolation architecture.

```
+-----------------------------------------------------------------------------+
| 1. RAW LAYER (data/01_raw/)                                                 |
|    - Immutable JSON / HTML source payloads                                  |
|    - SHA-256 content hashes, HTTP metadata, parser version, ingestion run ID|
+-----------------------------------------------------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------------+
| 2. STAGING LAYER (data/02_staging/ - DuckDB staging schema)                 |
|    - Parsed tabular records, raw ID preservation, native string typing      |
+-----------------------------------------------------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------------+
| 3. VALIDATED LAYER (data/03_validated/ - DuckDB core star schema)           |
|    - Entity resolution applied (canonical_player_id, canonical_team_id)     |
|    - Strict accounting assertions: Ball-Math, Minutes (200 + 25*OT)         |
|    - Explicit validation status: VALIDATED vs QUARANTINED                   |
+-----------------------------------------------------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------------+
| 4. ANALYTICS LAYER (data/04_analytics/ - DuckDB analytics views / parquet)  |
|    - Method-explicit possessions (simple, bilateral, pbp)                   |
|    - Possession-adjusted ratings (Pace 40m, ORtg, DRtg, NetRtg, Four Factors)|
|    - Standardized player rates per 40 minutes & tournament aggregates       |
|    - Machine learning feature stores with temporal leakage protection       |
+-----------------------------------------------------------------------------+
```

---

## 2. Directory Layout

```
f:/España2005-2025/
├── config/
│   ├── tournaments.csv       # Verified tournament registry (19 tournaments)
│   ├── rule_sets.csv         # Rule set definitions (2005-10, 2011-13, 2014-present)
│   ├── sources.yaml          # Data source definitions and precedence rules
│   └── teams.csv             # Federation and team registry
├── data/
│   ├── 01_raw/               # Immutable raw payloads
│   ├── 02_staging/           # Staging DuckDB database
│   ├── 03_validated/         # Validated production DuckDB database
│   ├── 04_analytics/         # Analytical views and feature stores
│   └── quarantine/           # QA failure logs and identity review queues
├── docs/
│   ├── architecture.md       # This document
│   ├── data_model.md         # Star schema definitions, grains, and DDL
│   ├── data_lineage.md       # Traceability and formula derivations
│   ├── source_registry.md    # Source audit and status matrix
│   ├── methodology.md        # Statistical and analytical methodologies
│   ├── validation_framework.md # QA rules and error severity classification
│   ├── entity_resolution.md  # Multi-stage deterministic identity pipeline
│   ├── research_questions.md # Prioritized research question bank (Tiers 1-4)
│   ├── limitations.md        # Explicit data and inferential boundaries
│   └── portfolio_story.md    # High-level technical portfolio narrative
├── reports/
│   ├── architecture_audit.md # Initial adversarial findings
│   └── final_adversarial_audit.md # Final adversarial verification
├── src/
│   ├── acquisition/          # Fetchers, rate limiters, caching, provenance
│   ├── domain/               # Pydantic models, enums, rulesets
│   ├── parsers/              # Raw payload to staging parsers
│   ├── normalization/        # Slug generators, entity & team resolvers
│   ├── validation/           # QA engine, ball-math, minute accounting
│   ├── metrics/              # FIBA possessions, ratings, four factors
│   ├── storage/              # DuckDB database connection and DDL
│   └── analytics/            # Longitudinal, clustering, prediction pipelines
└── tests/
    ├── unit/                 # Domain and configuration tests
    ├── formulas/             # Mathematical metric validation
    ├── data_quality/         # QA engine and assertion suite
    ├── entity_resolution/    # Matching and alias resolver tests
    ├── schema/               # Relational integrity tests
    └── integration/          # End-to-end pipeline execution with fixtures
```

---

## 3. Technology Stack & Design Decisions

| Component | Technology | Rationale |
| :--- | :--- | :--- |
| **Relational Storage** | **DuckDB (v1.5.5)** | Fast analytical execution, zero-server embedded deployment, native SQL and Parquet export. |
| **DataFrames & Processing** | **Polars / Pandas / PyArrow** | High performance memory-efficient column operations. |
| **Domain Validation** | **Pydantic (v2.13)** | Strict typing, runtime schema enforcement, immutable domain objects. |
| **Statistical Modeling** | **Statsmodels / Scipy** | Robust standard errors, segmented ITS regression, Generalized Additive Models. |
| **Machine Learning** | **Scikit-Learn** | Clustering, cross-validation splits without leakage, calibration metrics. |
| **Testing** | **Pytest (v9.1)** | Comprehensive automated test suite runnable offline. |
