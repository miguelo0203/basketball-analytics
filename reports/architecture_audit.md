# Full Repository & Architecture Audit Report
## International Basketball Historical Analytics (2005–2025)

**Document ID**: `REP-AUD-001`  
**Audit Date**: 2026-08-18  
**Auditor**: Lead Data Architect & Sports Analytics Methodologist  
**Status**: APPROVED FOR REDESIGN  

---

## 1. Executive Verdict: RED (Fundamental Structural Redesign Required)

The draft architecture and discovery documents contained severe mathematical flaws, unverified coverage figures, causal over-claims, and architectural ambiguities that would prevent the project from meeting senior-level data engineering and analytics standards.

### Summary of Systemic Deficiencies
1. **Mathematical Inaccuracy in Overtime Accounting**: The accounting formula for player minutes in overtime was specified as $200 + 50 \times \text{OT}$, confusing total game player-minutes across both teams with single-team player-minutes ($200 + 25 \times \text{OT}$).
2. **Unverified Tournament Universe**: Stated 18 tournaments and 1,100 games without auditing the actual FIBA calendar (e.g., omitting EuroBasket 2025, which falls within 2005–2025).
3. **Causal Over-Claims**: Proposed Difference-in-Differences (DiD) on the 2010 3-point line without an unexposed control group.
4. **Epistemological Conflation of Possessions**: Mixed estimated boxscore possessions with exact possessions in a single untyped column.
5. **Morphological Bias in Unsupervised Learning**: Included raw `height_cm` directly in clustering, ensuring clusters reflected traditional positions rather than functional play styles.
6. **Fragile Entity Resolution**: Bound nationality permanently to `dim_player`, failing on historical federation dissolutions (Serbia & Montenegro) and naturalized players.

---

## 2. Findings Matrix

| Finding ID | Component | Severity | Description | Downstream Impact | Required Correction |
| :--- | :--- | :---: | :--- | :--- | :--- |
| **AUD-CRIT-01** | Validation Rules | **CRITICAL** | Formula $\sum \text{Player MIN} = 200 + 50 \times \text{OT}$ applied per team. | 100% of overtime games quarantined as errors. | Implement single-team rule: $200 + 25 \times \text{OT}$; both teams: $400 + 50 \times \text{OT}$. Store canonically in seconds ($12,000 + 1,500 \times \text{OT}$). |
| **AUD-CRIT-02** | Calendar Scope | **HIGH** | EuroBasket 2025 omitted; game count hard-coded as "~1,100". | Incorrect universe size; incomplete historical scope. | Audit exact calendar: 19 tournaments, 1,203 games, 2,406 team-games. |
| **AUD-CRIT-03** | Methodology | **HIGH** | DiD proposed for 2010 3PT rule change without control group. | Methodological rejection in statistical review. | Replace DiD with Interrupted Time Series (ITS) / Segmented Regression. |
| **AUD-CRIT-04** | Data Model | **HIGH** | Direct overwriting of raw data; lack of immutable raw staging. | Inability to audit discrepancies or re-parse. | Enforce 4-tier layer: `RAW` $\rightarrow$ `STAGING` $\rightarrow$ `VALIDATED` $\rightarrow$ `ANALYTICS`. |
| **AUD-MED-01** | Data Model | **MEDIUM** | `country_code` hardcoded in `dim_player`. | Breaks for multi-affiliation players (Ibaka, Mirotic, Brown, Pavlović). | Separate canonical person from tournament affiliation table. |
| **AUD-MED-02** | Metrics | **MEDIUM** | Possessions stored in single field without methodology flag. | Conflates Oliver simple estimate, bilateral estimate, and PBP exact count. | Split fields: `possessions_simple`, `possessions_bilateral`, `possessions_pbp`, `possession_method`. |
| **AUD-MED-03** | Clustering | **MEDIUM** | Raw height included in feature space alongside collinear volume metrics ($PTS/40, FGA/40, USG\%$). | Feature redundancy and trivial positional clustering. | Exclude raw height; use rate metrics ($USG\%, TS\%, 3PAr, AST\%, TOV\%, ORB\%, DRB\%, STL_{40}, BLK_{40}, FTr$). |
| **AUD-MED-04** | Prediction | **MEDIUM** | Unspecified feature timestamping allowing potential temporal leakage. | Target contamination / data leakage. | Implement `available_as_of(game_timestamp)` and strict Leave-One-Tournament-Out (LOTO) cross-validation. |

---

## 3. Contradictory Assumptions & Unverified Claims

1. **"PBP is 100% confirmed for 2014–2025"**: FIBA LiveStats endpoints change hash identifiers and data schemas across tournaments. PBP must be an optional Level 0–5 layer, not a hard core dependency.
2. **"Shot coordinates are 100% comparable 2019–2025"**: Coordinate systems in FIBA SVGs vary in court dimensions and basket offsets across host arenas. Spatial coordinates require geometric normalization before cross-tournament pooling.
3. **"FIBA Archive is always primary truth"**: Older archive boxscores have known integer rounding on player minutes ($\pm 1$ min error). Validation must allow configured tolerances on legacy data.

---

## 4. Proposed Target Architecture

```
Layer Hierarchy:
1. RAW (Immutable JSON/HTML with SHA-256 content hashes, retrieval metadata, and parser versions)
2. STAGING (DuckDB typed raw tables, preserving source identifiers and raw string values)
3. VALIDATED (Star Schema with QA flags: fact_game, fact_team_game, fact_player_game, dim_*)
4. ANALYTICS (Engineered feature store, possession-normalized metrics, tournament aggregations, ML matrices)
5. PRESENTATION (Quarto reports, Streamlit dashboard, Plotly/Seaborn editorial visuals)
```

---

## 5. Migration and Action Plan

1. **Phase 1: Configuration & Registries**
   - Create `config/tournaments.csv` (19 verified tournaments).
   - Create `config/rule_sets.csv` (explicit rule versioning).
   - Create `config/sources.yaml` (source registry and precedence).
2. **Phase 2: Core Engineering & QA Engine**
   - Implement `src/domain/` with immutable Pydantic models.
   - Implement `src/validation/` with correct $200 + 25 \times \text{OT}$ minute accounting and ball-math checks.
   - Implement `src/metrics/` with exact FIBA possession calibrations.
3. **Phase 3: Database & Storage**
   - Implement DuckDB relational star schema with explicit lineage fields.
4. **Phase 4: Statistical & Machine Learning Modules**
   - Implement ITS regression for 2010 rule change.
   - Implement non-redundant player-tournament clustering with formal $k$ evaluation.
   - Implement leak-free LOTO predictive pipeline.
5. **Phase 5: Automated Test Suite**
   - Unit, formula, schema, QA, and integration tests running deterministically without internet access.
