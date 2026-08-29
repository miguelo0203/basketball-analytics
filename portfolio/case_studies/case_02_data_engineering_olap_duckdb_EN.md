[🇬🇧 English](case_02_data_engineering_olap_duckdb_EN.md) | [🇪🇸 Español](case_02_data_engineering_olap_duckdb.md)

# Case Study 02: High-Performance OLAP Data Engineering with DuckDB

## 1. The Challenge
Analyzing 20 years of international basketball (18 tournaments, 1,145 games, 27,353 player box scores) requires rapid multi-table aggregations without heavy database server infrastructure.

## 2. The Architecture
Built an embedded **DuckDB OLAP Data Mart** featuring:
- Automated ingestion and entity resolution for players and national teams.
- Star schema with pre-computed analytical views for Four Factors and ratings.
- Sub-15 millisecond analytical query execution.

## 3. Results
100% reproducible, self-contained data pipeline tested with 227 automated Pytest checks.
