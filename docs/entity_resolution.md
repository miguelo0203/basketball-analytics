# Entity Resolution Architecture & Player Identity Specification
## International Basketball Historical Analytics (2005–2025)

---

## 1. Core Principles

1. **Separation of Canonical Person from Historical Affiliation**:
   - `dim_player` models the persistent physical human athlete.
   - Nationality and tournament roster spots are modeled per tournament in `fact_player_tournament`.
2. **Deterministic-First Priority**:
   - Never resolve identities via unconstrained fuzzy matching.
   - Match by official persistent source IDs first, exact alias mappings second, deterministic composite rules third, and route low-confidence matches to a human review queue.

---

## 2. Entity Resolution Pipeline

```
Raw Input: (raw_name, tournament_year, team_country, source_id, source_pid)
   |
   +---> Step 1: String Normalization (ASCII folding, lowercase, tokenisation)
   |
   +---> Step 2: Exact Source ID Lookup in dim_player_alias (EXACT)
   |
   +---> Step 3: Exact Normalized String + Country Match in dim_player_alias (DETERMINISTIC)
   |
   +---> Step 4: Deterministic Composite Match: Tokens + Country + Birth Year +/- 1 (DETERMINISTIC)
   |
   +---> Step 5: High-Threshold Jaro-Winkler (> 0.94) + Same Country + Height +/- 2cm (PROBABILISTIC)
   |
   +---> Step 6: Fallback: Route to data/quarantine/player_identity_review.csv (UNRESOLVED)
```

---

## 3. Identity Confidence Levels

| Confidence Level | Description | Automated Action |
| :--- | :--- | :--- |
| **`EXACT`** | Exact match on official persistent source player ID (`fiba_person_id` or `bref_slug`). | Automatically promoted to `fact_*`. |
| **`DETERMINISTIC`** | Exact match on normalized full name, birth year, and tournament federation. | Automatically promoted to `fact_*`. |
| **`MANUAL`** | Verified via curated entry in `config/manual_player_overrides.csv`. | Automatically promoted to `fact_*`. |
| **`PROBABILISTIC`** | High-score fuzzy match ($Score \ge 0.95$) with identical birth year and height. | Flagged with warning for auditing. |
| **`UNRESOLVED`** | Ambiguous or low-similarity candidate. | Quarantined. Requires human review. |

---

## 4. Complex Historical Edge Cases Resolved

1. **Changing National Federations / Historical Entities**:
   - *Aleksandar Pavlović*: Represented Serbia and Montenegro (`SCG`) in 2005. Canonical person: `aleksandar_pavlovic_1983`.
   - *Serge Ibaka*: Naturalized Spanish player. Represented Spain (`ESP`) in EuroBasket 2011 and London 2012. Canonical person: `serge_ibaka_1989`.
   - *Lorenzo Brown*: Naturalized Spanish point guard. Represented Spain in EuroBasket 2022 and Paris 2024. Canonical person: `lorenzo_brown_1990`.
2. **Identical / Similar Surnames**:
   - *Pau Gasol* (`pau_gasol_1980`) vs. *Marc Gasol* (`marc_gasol_1985`).
   - *Willy Hernangómez* (`willy_hernangomez_1994`) vs. *Juancho Hernangómez* (`juancho_hernangomez_1995`).
   - *Bojan Bogdanović* (Croatia, 1989, `bojan_bogdanovic_1989`) vs. *Bogdan Bogdanović* (Serbia, 1992, `bogdan_bogdanovic_1992`).
