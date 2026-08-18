# Source Capability Registry & Fallback Architecture
## International Basketball Historical Analytics (2005–2025)

---

## 1. Audited Source Capability Matrix

| Source Identifier | Official Name | Type | Historical Coverage | Granularity Supported | PBP Capability | Shot Data Capability | Identifier Stability | Rate Limits | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| `SRC_FIBA_ARCHIVE` | FIBA Archive | Official Historical | 2005–2017 | Game, Team-Game, Player-Game | **PARTIAL** (Text log) | **UNAVAILABLE** | `pid`, `gid`, `tid` | 30 req/min | **CONFIRMED** |
| `SRC_FIBA_MODERN` | FIBA Modern Web Engine | Official API | 2018–2025 | Tournament, Game, Team, Player | **CONFIRMED** | **CONFIRMED** (SVG JSON) | `person_id`, `game_id` | 20 req/min | **CONFIRMED** |
| `SRC_FIBA_LIVESTATS`| Genius Sports LiveStats | Official Telemetry | 2014–2025 | PBP event stream, Lineup stints | **CONFIRMED** | **CONFIRMED** | `personId`, `gameId` | 20 req/min | **CONFIRMED** |
| `SRC_BREF` | Basketball-Reference | Secondary Structured | 2005–2025 | Tournament, Game, Team, Player | **UNAVAILABLE** | **UNAVAILABLE** | Slugs (`gasolpa01`) | 20 req/min | **CONFIRMED** |
| `SRC_FEB` | FEB Official Archive | Official Federation | 2005–2025 | Spain Player-Game & Team-Game | **UNAVAILABLE** | **UNAVAILABLE** | `IdJugador`, `IdPartido` | 20 req/min | **CONFIRMED** |
| `SRC_IOC` | IOC Results Books | Official Olympic | 2008–2024 | Game, Team, Player | **PARTIAL** (PDF logs) | **UNAVAILABLE** | Textual strings | 10 req/min | **CONFIRMED** |
| `SRC_PROBALLERS` | Proballers | Secondary Commercial | 2005–2025 | Player-Game | **UNAVAILABLE** | **UNAVAILABLE** | Proprietary | Anti-bot active | **DISCARDED** |

---

## 2. Source Precedence & Conflict Resolution Policy

1. **Precedence Hierarchy by Variable**:
   - **Game Scores & Overtime Duration**: Official Scoresheet (`SRC_FIBA_ARCHIVE` / `SRC_FIBA_MODERN` / `SRC_IOC`) $>$ Secondary (`SRC_BREF`).
   - **Player Boxscores**: Primary Official $>$ Secondary Structured.
   - **Player Identity Resolution**: Official FIBA Person ID $>$ Secondary Slugs $>$ Deterministic Name Matching.
   - **Spatial Shot Coordinates**: `SRC_FIBA_LIVESTATS` / `SRC_FIBA_MODERN` only.

2. **Conflict Handling Rule**:
   - Secondary sources **never silently overwrite primary data**.
   - When primary and secondary sources disagree on an observable metric (e.g. Points, Rebounds):
     1. The primary value is retained in the fact table with validation flag `SOURCE_CONFLICT`.
     2. An entry is written to `fact_validation_issue` logging `source_a`, `source_b`, `value_a`, `value_b`, and `discrepancy_type`.
