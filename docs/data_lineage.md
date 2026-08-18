# Data Lineage & Metric Epistemology Specification
## International Basketball Historical Analytics (2005–2025)

---

## 1. Metric Epistemology Classification

To prevent presenting indirect estimates as observed empirical truth, every field in the analytics warehouse is explicitly mapped into exactly one epistemological category:

- **OBSERVED**: Direct event counts or physical measurements recorded at the arena.
- **ESTIMATED**: Approximations derived through statistical heuristics or unobserved possessions.
- **DERIVED**: Deterministic mathematical transformations of observed and/or estimated quantities.
- **MODELED**: Predictions, latent factors, or statistical inferences produced by machine learning/statistical models.

---

## 2. Metric Lineage & Provenance Table

| Target Field | Epistemology | Mathematical Formula | Input Fields | Source Table | Source Origin | Notes & FIBA Assumptions |
| :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `pts` | **OBSERVED** | $\sum \text{scoring events}$ | Direct boxscore | `fact_team_game` | FIBA / B-Ref | Reconciled against $2 \times 2PM + 3 \times 3PM + FTM$. |
| `seconds_played` | **OBSERVED** | Raw clock time | Direct boxscore / PBP | `fact_player_game` | FIBA / B-Ref | Canonical unit. If source provides mm:ss $\rightarrow$ converted to sec. |
| `minutes_decimal`| **DERIVED** | `seconds_played / 60.0` | `seconds_played` | `fact_player_game` | Derived | Exact decimal representation. |
| `possessions_simple` | **ESTIMATED** | $FGA + 0.44 \times FTA - ORB + TOV$ | $FGA, FTA, ORB, TOV$ | `fact_team_game` | Derived | Dean Oliver simple estimate. $0.44$ coefficient accounts for and-1s/technical FTs. |
| `possessions_bilateral` | **ESTIMATED** | $0.5 \times (\text{Poss}_{A} + \text{Poss}_{B})$ | Team A & B Boxscores | `fact_team_game` | Derived | Bilateral possession estimate. Enforces game symmetry. |
| `possessions_pbp`| **OBSERVED** | Count of distinct possession bounds | PBP event stream | `fact_game` | LiveStats | Available only when `pbp_coverage_level >= 4`. |
| `pace_40m` | **DERIVED** | $40 \times \frac{\text{possessions\_bilateral}}{\text{game\_duration\_seconds} / 60}$ | `possessions_bilateral`, `game_duration_seconds` | `fact_game` | Derived | Calibrated to FIBA 40-minute regulation. Normalises for OT. |
| `ortg` | **DERIVED** | $100 \times \frac{PTS}{\text{possessions\_bilateral}}$ | $PTS$, `possessions_bilateral` | `fact_team_game` | Derived | Points produced per 100 bilateral possessions. |
| `drtg` | **DERIVED** | $100 \times \frac{Opp\_PTS}{\text{possessions\_bilateral}}$ | $Opp\_PTS$, `possessions_bilateral` | `fact_team_game` | Derived | Points conceded per 100 bilateral possessions. |
| `net_rtg` | **DERIVED** | $\text{ortg} - \text{drtg}$ | `ortg`, `drtg` | `fact_team_game` | Derived | Net point differential per 100 possessions. |
| `efg_pct` | **DERIVED** | $\frac{FGM + 0.5 \times FG3M}{FGA}$ | $FGM, FG3M, FGA$ | `fact_team_game` | Derived | Effective field goal percentage. NULL if $FGA = 0$. |
| `tov_pct` | **DERIVED** | $\frac{TOV}{FGA + 0.44 \times FTA + TOV}$ | $TOV, FGA, FTA$ | `fact_team_game` | Derived | Turnover percentage per play. |
| `orb_pct` | **DERIVED** | $\frac{ORB}{ORB + Opp\_DRB}$ | $ORB$, $Opp\_DRB$ | `fact_team_game` | Derived | Offensive rebound rate. |
| `ftr` | **DERIVED** | $\frac{FTA}{FGA}$ | $FTA, FGA$ | `fact_team_game` | Derived | Free throw rate. |
| `ts_pct` | **DERIVED** | $\frac{PTS}{2 \times (FGA + 0.44 \times FTA)}$ | $PTS, FGA, FTA$ | `fact_player_game` | Derived | True shooting percentage. NULL if $FGA=0 \land FTA=0$. |
| `usg_pct` | **ESTIMATED** | $100 \times \frac{(FGA_p + 0.44 FTA_p + TOV_p) \times (Team\_MIN / 5)}{MIN_p \times (Team\_FGA + 0.44 Team\_FTA + Team\_TOV)}$ | Player & Team boxscores | `fact_player_game` | Derived | Usage rate. Null/0 if $MIN_p = 0$. |
| `computed_game_score` | **DERIVED** | Hollinger Game Score formula | Traditional boxscore stats | `fact_player_game` | Derived | 100% reproducible linear productivity metric. |
| `official_pir` | **OBSERVED** | FIBA PIR formula | Official scoresheet | `fact_player_game` | FIBA | Includes Fouls Drawn ($FD$). Stored when present. |
| `win_probability`| **MODELED** | Calibrated Logistic / GBDT Model | Pre-game historical features | `fact_game` | ML Pipeline | Generated strictly using data available before tip-off. |
