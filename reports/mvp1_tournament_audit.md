# MVP-1 Tournament Format & Expected Universe Audit
## International Basketball Historical Analytics (2005–2025)

**Audit Execution Date**: 2026-08-18  
**Scope**: 5 FIBA World Cups + 5 Olympic Men's Tournaments (10 tournaments total)

---

## 1. Overview of MVP-1 Tournament Universe

| Tournament ID | Official Name | Year | Host Nation | Format / Phase Breakdown | Expected Teams | Expected Games | Expected Rule Set |
| :--- | :--- | :---: | :---: | :--- | :---: | :---: | :---: |
| `worldcup_2006` | FIBA World Championship 2006 | 2006 | Japan | Preliminary (4x6 = 60) + R16 (8) + QF (4) + SF (2) + Medal (2) + Class 5-8 (4) | 24 | **80** | `fiba_2005_2010` |
| `worldcup_2010` | FIBA World Championship 2010 | 2010 | Turkey | Preliminary (4x6 = 60) + R16 (8) + QF (4) + SF (2) + Medal (2) + Class 5-8 (4) | 24 | **80** | `fiba_2005_2010` |
| `worldcup_2014` | FIBA Basketball World Cup 2014 | 2014 | Spain | Preliminary (4x6 = 60) + R16 (8) + QF (4) + SF (2) + Medal (2) | 24 | **76** | `fiba_2014_present` |
| `worldcup_2019` | FIBA Basketball World Cup 2019 | 2019 | China | 1st Round (8x4 = 48) + 2nd Round (4x4 = 16) + Class 17-32 (4x4 = 16) + Final Round (12) | 32 | **92** | `fiba_2014_present` |
| `worldcup_2023` | FIBA Basketball World Cup 2023 | 2023 | PHI / JPN / INA | 1st Round (8x4 = 48) + 2nd Round (4x4 = 16) + Class 17-32 (4x4 = 16) + Final Round (12) | 32 | **92** | `fiba_2014_present` |
| `olympics_2008` | Beijing 2008 Olympic Basketball | 2008 | China | Preliminary (2x6 = 30) + QF (4) + SF (2) + Medal (2) | 12 | **38** | `fiba_2005_2010` |
| `olympics_2012` | London 2012 Olympic Basketball | 2012 | United Kingdom | Preliminary (2x6 = 30) + QF (4) + SF (2) + Medal (2) | 12 | **38** | `fiba_2011_2013` |
| `olympics_2016` | Rio 2016 Olympic Basketball | 2016 | Brazil | Preliminary (2x6 = 30) + QF (4) + SF (2) + Medal (2) | 12 | **38** | `fiba_2014_present` |
| `olympics_2020` | Tokyo 2020 Olympic Basketball | 2021 | Japan | Preliminary (3x4 = 18) + QF (4) + SF (2) + Medal (2) | 12 | **26** | `fiba_2014_present` |
| `olympics_2024` | Paris 2024 Olympic Basketball | 2024 | France | Preliminary (3x4 = 18) + QF (4) + SF (2) + Medal (2) | 12 | **26** | `fiba_2014_present` |
| **TOTALS** | **10 MVP-1 Competitions** | — | — | — | — | **586** | — |

---

## 2. Schedule Evidence & Verification Notes

1. **Olympic 12-Team Formats**:
   - **2008–2016 (Beijing, London, Rio)**: 2 pools of 6 teams ($2 \times 15 = 30$ matches) + 4 quarterfinals + 2 semifinals + Bronze medal match + Gold medal match = **38 total matches**.
   - **2020–2024 (Tokyo, Paris)**: FIBA revised the format to 3 pools of 4 teams ($3 \times 6 = 18$ matches) + 4 quarterfinals + 2 semifinals + Bronze medal match + Gold medal match = **26 total matches**.
2. **World Cup Formats**:
   - **2006, 2010 (Japan, Turkey)**: 24 teams, 4 groups of 6 ($4 \times 15 = 60$ matches). Knockout included Round of 16 (8), QF (4), SF (2), Bronze (1), Final (1), and 5th–8th classification playoffs (4) = **80 total matches**.
   - **2014 (Spain)**: 24 teams, 4 groups of 6 ($4 \times 15 = 60$ matches). Knockout did NOT have 5th–8th classification playoffs ($8 + 4 + 2 + 1 + 1 = 16$) = **76 total matches**.
   - **2019, 2023 (China, Philippines/Japan/Indonesia)**: 32 teams, 8 groups of 4 ($8 \times 6 = 48$ matches). Second Round 4 groups of 4 ($4 \times 4 = 16$ matches). Classification 17th–32nd 4 groups of 4 ($4 \times 4 = 16$ matches). Final round ($4 + 2 + 1 + 1 + 4 = 12$ matches) = **92 total matches**.

---

## 3. Discrepancies Found and Resolved

- **Draft Table Typos**: Previous drafts listed 32 games for Olympics 2008, 2012, 2016. Verified mathematically and empirically that $30 \text{ (group)} + 8 \text{ (knockout)} = \mathbf{38 \text{ matches}}$, correcting the target to 38 games.
- **World Cup 2006 Summary Tables**: 2006 preliminary matches are hosted on the main tournament page within summary tables, whereas 2010–2023 utilize modular subpages. The unified parser handles both structures seamlessly.
