# Tournament Data Coverage Gap & Audit Report (MVP0)
## International Basketball Historical Analytics (2005–2025)

**Audit Execution Date**: 2026-08-18T04:39:54.789304  
**Target Database**: `basketball_analytics.duckdb`  
**Manifest Source**: `expected_tournament_manifest.yaml`  

---

## 1. Tournament-by-Tournament Coverage Status

| Tournament ID | Official Name | Year | Expected | Raw | Parsed | Validated | Promoted | Missing | Quarantined | Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `eurobasket_2005` | FIBA EuroBasket 2005 | 2005 | 40 | 40 | 40 | 40 | **40** | 0 | 0 | **COMPLETE** |
| `eurobasket_2007` | FIBA EuroBasket 2007 | 2007 | 54 | 54 | 54 | 54 | **54** | 0 | 0 | **COMPLETE** |
| `eurobasket_2009` | FIBA EuroBasket 2009 | 2009 | 54 | 54 | 54 | 54 | **54** | 0 | 0 | **COMPLETE** |
| `eurobasket_2011` | FIBA EuroBasket 2011 | 2011 | 90 | 90 | 90 | 90 | **90** | 0 | 0 | **COMPLETE** |
| `eurobasket_2013` | FIBA EuroBasket 2013 | 2013 | 90 | 90 | 90 | 90 | **90** | 0 | 0 | **COMPLETE** |
| `eurobasket_2015` | FIBA EuroBasket 2015 | 2015 | 79 | 79 | 79 | 79 | **79** | 0 | 0 | **COMPLETE** |
| `eurobasket_2017` | FIBA EuroBasket 2017 | 2017 | 76 | 76 | 76 | 76 | **76** | 0 | 0 | **COMPLETE** |
| `eurobasket_2022` | FIBA EuroBasket 2022 | 2022 | 76 | 76 | 76 | 76 | **76** | 0 | 0 | **COMPLETE** |

---

## 2. Global Coverage Totals

- **Total Expected Games**: **559**
- **Total Promoted Games in DuckDB**: **559**
- **Total Missing Games**: **0**
- **Overall Coverage Ratio**: **100.00%**
- **Audit Verdict**: **COMPLETE (100% Verified Coverage)**
