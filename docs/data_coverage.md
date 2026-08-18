# Empirical Data Coverage & Ingestion Status
## International Basketball Historical Analytics (2005–2025)

**Generated Directly from Validated DuckDB Warehouse**: `basketball_analytics.duckdb`  
**Last Updated**: 2026-08-19T00:07:01.012878  

---

## 1. Validated Tournament Ingestion Summary (EuroBasket, World Cups, Olympics)

| Tournament ID | Official Name | Year | Competition | Manifest Teams | Ingested Games | Team-Game Rows | OT Games | Avg Pace (40m) | Avg Team PTS |
| :--- | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `eurobasket_2005` | FIBA EuroBasket 2005 | 2005 | fiba_eurobasket | 16 | **40** | 80 | 6.0 | 72.53 | 74.53 |
| `worldcup_2006` | FIBA World Championship 2006 | 2006 | fiba_world_cup | 24 | **80** | 160 | 8.0 | 76.18 | 78.24 |
| `eurobasket_2007` | FIBA EuroBasket 2007 | 2007 | fiba_eurobasket | 16 | **54** | 108 | 6.0 | 71.71 | 73.52 |
| `olympics_2008` | Beijing 2008 Men's Olympic Basketball Tournament | 2008 | olympics_basketball | 12 | **38** | 76 | 2.0 | 79.3 | 81.3 |
| `eurobasket_2009` | FIBA EuroBasket 2009 | 2009 | fiba_eurobasket | 16 | **54** | 108 | 8.0 | 71.63 | 73.48 |
| `worldcup_2010` | FIBA World Championship 2010 | 2010 | fiba_world_cup | 24 | **80** | 160 | 4.0 | 75.19 | 77.11 |
| `eurobasket_2011` | FIBA EuroBasket 2011 | 2011 | fiba_eurobasket | 24 | **90** | 180 | 6.0 | 72.46 | 74.32 |
| `olympics_2012` | London 2012 Men's Olympic Basketball Tournament | 2012 | olympics_basketball | 12 | **38** | 76 | 0.0 | 78.49 | 80.45 |
| `eurobasket_2013` | FIBA EuroBasket 2013 | 2013 | fiba_eurobasket | 24 | **90** | 180 | 16.0 | 71.19 | 73.04 |
| `worldcup_2014` | FIBA Basketball World Cup 2014 | 2014 | fiba_world_cup | 24 | **76** | 152 | 6.0 | 74.73 | 76.62 |
| `eurobasket_2015` | FIBA EuroBasket 2015 | 2015 | fiba_eurobasket | 24 | **79** | 158 | 14.0 | 73.22 | 75.2 |
| `olympics_2016` | Rio 2016 Men's Olympic Basketball Tournament | 2016 | olympics_basketball | 12 | **38** | 76 | 2.0 | 79.77 | 81.95 |
| `eurobasket_2017` | FIBA EuroBasket 2017 | 2017 | fiba_eurobasket | 24 | **76** | 152 | 6.0 | 76.15 | 78.14 |
| `worldcup_2019` | FIBA Basketball World Cup 2019 | 2019 | fiba_world_cup | 32 | **92** | 184 | 10.0 | 77.49 | 79.52 |
| `olympics_2020` | Tokyo 2020 Men's Olympic Basketball Tournament | 2021 | olympics_basketball | 12 | **26** | 52 | 0.0 | 84.28 | 86.38 |
| `eurobasket_2022` | FIBA EuroBasket 2022 | 2022 | fiba_eurobasket | 24 | **76** | 152 | 14.0 | 80.6 | 82.84 |
| `worldcup_2023` | FIBA Basketball World Cup 2023 | 2023 | fiba_world_cup | 32 | **92** | 184 | 6.0 | 82.32 | 84.49 |
| `olympics_2024` | Paris 2024 Men's Olympic Basketball Tournament | 2024 | olympics_basketball | 12 | **26** | 52 | 4.0 | 83.67 | 85.92 |

---

## 2. Global Metric Integrity & Quality Counts

- **Total Ingested Games**: `1145`
- **Total Ingested Team-Games**: `2290`
- **Critical Accounting Failures**: `0` (Target: 0)
- **Warning Issues**: `0`
- **Ball-Math Verification**: 100% Passed ($PTS = 2 \times 2PM + 3 \times 3PM + FTM$)
- **Minute Accounting Verification**: 100% Passed ($(200 + 25 \times \text{OT}) \times 60$ s per team)
- **Possession Epistemology**: Explicitly tracked as `EST_BILATERAL` (Dean Oliver $0.44$ coefficient)
