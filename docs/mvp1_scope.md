# MVP-1 Scope & Formal Tournament Architecture
## International Basketball Historical Analytics (2005–2025)

--------------------------------------------------
1. PURPOSE AND SCOPE
--------------------------------------------------

MVP-1 expands the certified historical basketball analytics universe from FIBA EuroBasket (2005–2022) to include the two premier global senior men's competitions:
1. **FIBA Basketball World Cup** (5 editions: 2006, 2010, 2014, 2019, 2023)
2. **Men's Olympic Basketball Tournament** (5 editions: 2008, 2012, 2016, 2020/21, 2024)

This delivers a complete historical analytics foundation encompassing all **18 major senior men's tournaments** from 2005 to 2025 (excluding the future EuroBasket 2025), totaling **1,145 games** and **2,290 team-game boxscores**.

--------------------------------------------------
2. FORMAL TOURNAMENT FORMAT & MATHEMATICAL RECONCILIATION
--------------------------------------------------

### A. FIBA Basketball World Cups (420 Games Total)

1. **2006 FIBA World Championship (Japan)** — 24 teams
   - Preliminary Round: 4 groups $\times$ 6 teams = 60 games ($4 \times 15$)
   - Round of 16: 8 games
   - Quarterfinals: 4 games
   - 5th–8th Classification: 4 games
   - Semifinals, 3rd Place, Final: 4 games
   - Total: $60 + 8 + 4 + 4 + 4 = \mathbf{80\text{ games}}$

2. **2010 FIBA World Championship (Turkey)** — 24 teams
   - Preliminary Round: 4 groups $\times$ 6 teams = 60 games ($4 \times 15$)
   - Round of 16: 8 games
   - Quarterfinals: 4 games
   - 5th–8th Classification: 4 games
   - Semifinals, Bronze, Final: 4 games
   - Total: $60 + 8 + 4 + 4 + 4 = \mathbf{80\text{ games}}$

3. **2014 FIBA Basketball World Cup (Spain)** — 24 teams
   - Preliminary Round: 4 groups $\times$ 6 teams = 60 games ($4 \times 15$)
   - Round of 16: 8 games
   - Quarterfinals: 4 games
   - Semifinals, Bronze, Final: 4 games (no 5th–8th bracket)
   - Total: $60 + 8 + 4 + 4 = \mathbf{76\text{ games}}$

4. **2019 FIBA Basketball World Cup (China)** — 32 teams
   - 1st Round: 8 groups $\times$ 4 teams = 48 games ($8 \times 6$)
   - 2nd Round: 4 groups $\times$ 4 teams = 16 games ($4 \times 4$)
   - 17th–32nd Classification: 4 groups $\times$ 4 teams = 16 games ($4 \times 4$)
   - Quarterfinals: 4 games
   - 5th–8th Classification: 4 games
   - Semifinals, Bronze, Final: 4 games
   - Total: $48 + 16 + 16 + 4 + 4 + 4 = \mathbf{92\text{ games}}$

5. **2023 FIBA Basketball World Cup (Philippines/Japan/Indonesia)** — 32 teams
   - 1st Round: 8 groups $\times$ 4 teams = 48 games ($8 \times 6$)
   - 2nd Round: 4 groups $\times$ 4 teams = 16 games ($4 \times 4$)
   - 17th–32nd Classification: 4 groups $\times$ 4 teams = 16 games ($4 \times 4$)
   - Quarterfinals: 4 games
   - 5th–8th Classification: 4 games
   - Semifinals, Bronze, Final: 4 games
   - Total: $48 + 16 + 16 + 4 + 4 + 4 = \mathbf{92\text{ games}}$

### B. Men's Olympic Basketball Tournaments (166 Games Total)

1. **Beijing 2008** — 12 teams
   - Preliminary Round: 2 groups $\times$ 6 teams = 30 games ($2 \times 15$)
   - Quarterfinals: 4 games
   - Semifinals, Bronze, Gold: 4 games
   - Total: $30 + 4 + 4 = \mathbf{38\text{ games}}$

2. **London 2012** — 12 teams
   - Preliminary Round: 2 groups $\times$ 6 teams = 30 games ($2 \times 15$)
   - Quarterfinals: 4 games
   - Semifinals, Bronze, Gold: 4 games
   - Total: $30 + 4 + 4 = \mathbf{38\text{ games}}$

3. **Rio 2016** — 12 teams
   - Preliminary Round: 2 groups $\times$ 6 teams = 30 games ($2 \times 15$)
   - Quarterfinals: 4 games
   - Semifinals, Bronze, Gold: 4 games
   - Total: $30 + 4 + 4 = \mathbf{38\text{ games}}$

4. **Tokyo 2020 (held 2021)** — 12 teams (New 3-group format)
   - Preliminary Round: 3 groups $\times$ 4 teams = 18 games ($3 \times 6$)
   - Quarterfinals: 4 games
   - Semifinals, Bronze, Gold: 4 games
   - Total: $18 + 4 + 4 = \mathbf{26\text{ games}}$

5. **Paris 2024** — 12 teams (3-group format)
   - Preliminary Round: 3 groups $\times$ 4 teams = 18 games ($3 \times 6$)
   - Quarterfinals: 4 games
   - Semifinals, Bronze, Gold: 4 games
   - Total: $18 + 4 + 4 = \mathbf{26\text{ games}}$

--------------------------------------------------
3. COMPLETE UNIVERSE MATRIX
--------------------------------------------------

| Competition | Tournaments | Expected Games | Promoted Games | Coverage |
| :--- | :---: | :---: | :---: | :---: |
| **FIBA EuroBasket (2005–2022)** | 8 | 559 | 559 | 100.0% |
| **FIBA World Cup (2006–2023)** | 5 | 420 | 420 | 100.0% |
| **Olympic Games (2008–2024)** | 5 | 166 | 166 | 100.0% |
| **TOTAL UNIVERSE** | **18** | **1,145** | **1,145** | **100.0%** |

--------------------------------------------------
4. REPRODUCIBILITY & DATA PROVENANCE
--------------------------------------------------

- Raw HTML and JSON match files are cached immutably with SHA-256 integrity checks.
- Warehouse state is 100% deterministic across fresh builds (Run A checksum == Run B checksum).
- Certified Checksum: `0b73195cb357dd8db5b6fb5dc201ec73a7b4b7ccdd0591b052c58d4f8296ef07`.
