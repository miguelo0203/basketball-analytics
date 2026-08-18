# 05 — Data Engineering & Database Questions & Answers
## DuckDB, Parquet, Relational Schemas & Provenance

---

### Q1: Why did you choose DuckDB and Parquet over PostgreSQL or MySQL?
**Answer**:
> *"DuckDB is an in-process columnar OLAP database optimized for analytical queries on multi-million row datasets. It provides zero-configuration deployment, runs directly inside Python processes without network latency, reads and writes directly to compressed Parquet files, and executes complex window functions and CTEs at C++ speeds."*

---

### Q2: How did you ensure data provenance and entity resolution across 20 years of international tournaments?
**Answer**:
> *"Raw FIBA JSON and boxscore files were stored in an immutable raw layer and validated with SHA-256 cryptographic hashes. I built a deterministic entity resolution pipeline mapping multi-lingual player spelling variations (e.g. 'Pau Gasol', 'P. Gasol', 'Gasol Sáez') to a canonical `player_id` with zero duplicate entities across 2,124 players."*

---

### Q3: How did you mathematically reconcile boxscore anomalies?
**Answer**:
> *"I implemented automated reconciliation checks verifying that individual player minutes sum to 200 regulation minutes (or 225/250 in overtimes), that player points sum exactly to final team scores, and that possession formulas match bilateral team possession counts."*
