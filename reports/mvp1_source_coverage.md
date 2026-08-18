# MVP-1 Source Audit & Coverage Matrix Report
## International Basketball Historical Analytics (2005–2025)

**Audit Execution Date**: 2026-08-18  
**Scope**: 5 FIBA World Cups + 5 Olympic Men's Tournaments (10 tournaments total)

---

## 1. Source Capabilities Matrix

| Tournament ID | Primary Audited Source | Expected Games | Accessible Games | Complete Boxscore | Overtime Info | Source Reliability | Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `worldcup_2006` | `SRC_WIKI_ARCHIVE` | 80 | **80** | Yes | Yes | High | **ACTIVE** |
| `worldcup_2010` | `SRC_WIKI_ARCHIVE` | 80 | **80** | Yes | Yes | High | **ACTIVE** |
| `worldcup_2014` | `SRC_WIKI_ARCHIVE` | 76 | **76** | Yes | Yes | High | **ACTIVE** |
| `worldcup_2019` | `SRC_WIKI_ARCHIVE` | 92 | **92** | Yes | Yes | High | **ACTIVE** |
| `worldcup_2023` | `SRC_WIKI_ARCHIVE` | 92 | **92** | Yes | Yes | High | **ACTIVE** |
| `olympics_2008` | `SRC_WIKI_ARCHIVE` | 38 | **38** | Yes | Yes | High | **ACTIVE** |
| `olympics_2012` | `SRC_WIKI_ARCHIVE` | 38 | **38** | Yes | Yes | High | **ACTIVE** |
| `olympics_2016` | `SRC_WIKI_ARCHIVE` | 38 | **38** | Yes | Yes | High | **ACTIVE** |
| `olympics_2020` | `SRC_WIKI_ARCHIVE` | 26 | **26** | Yes | Yes | High | **ACTIVE** |
| `olympics_2024` | `SRC_WIKI_ARCHIVE` | 26 | **26** | Yes | Yes | High | **ACTIVE** |

---

## 2. Extraction & Ingestion Precedence

1. **Immutable RAW Storage**: Every payload is cached with its SHA-256 cryptographic hash under `data/01_raw/SRC_WIKI_ARCHIVE/` prior to parsing.
2. **Deterministic Entity Resolution**: Federation codes mapped to `config/teams.csv` using normalized canonical ISO/FIBA 3-letter codes.
3. **Validation Gates**: Every game record passes strict ball-math ($PTS = 2 \times 2PM + 3 \times 3PM + FTM$) and minute accounting ($(200 + 25 \times \text{OT}) \times 60$ s) before promotion to `basketball_analytics.duckdb`.
