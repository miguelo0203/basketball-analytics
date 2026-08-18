# MVP-3 Methodological Limitations & Analytical Caveats
## International Basketball Historical Analytics (2005–2025)

--------------------------------------------------
1. SAMPLE SIZE & TOURNAMENT VOLATILITY
--------------------------------------------------

- **Short Tournament Windows**: Major international competitions feature only $5\text{ to }11$ games per national team. Even for players averaging $25\text{ minutes}$, total tournament sample sizes rarely exceed $250\text{ minutes}$.
- **Rate Estimator Variance**: Individual 3-point shooting percentages over $30\text{ to }50$ attempts have wide confidence intervals ($\pm 7\text{ percentage points}$). We mitigate this by evaluating **3-Point Attempt Rate ($3\text{PAr}$)** alongside accuracy, as shot selection stabilizes much faster than shot making.
- **Minimum Qualification Filtering**: Any player with $MIN < 40$ or $G < 3$ in a tournament is classified as `Unqualified / Low-Sample Rotation` and excluded from the core role clustering space to prevent skewed outliers.

--------------------------------------------------
2. LINEUP CO-OCCURRENCE & MULTICOLLINEARITY
--------------------------------------------------

- **Absence of Sub-Minute Stint Data Pre-2012**: Detailed substitution stint timestamps are unavailable across all federations for tournaments prior to 2012. Consequently, pure Adjusted Plus-Minus (APM) cannot be calculated for pre-2012 competitions without introducing severe imputation artifacts.
- **Teammate Synergy Confounding**: A player's assist totals are bounded by teammates' ability to convert open shots.

--------------------------------------------------
3. OPPONENT QUALITY & BLOWOUT DISTORTIONS
--------------------------------------------------

- **Tournament Group Stage Imbalances**: Group stage games frequently feature talent mismatches, where starters play reduced minutes in blowouts ($|\text{margin}| \ge 30$).
- **Garbage Time Stints**: End-of-bench players accumulating stats in non-competitive minutes must be interpreted with caution.

--------------------------------------------------
4. THE ANALYTICS-TO-SCOUTING BOUNDARY
--------------------------------------------------

- **Quantitative Data is Necessary but Insufficient**: Statistical rates indicate *what* a player produced in historical games, but cannot measure athletic ceiling, off-ball defensive footwork, pick-and-roll screen navigation habits, or coachability.
- **Mandatory Video Verification**: Quantitative shortlists must always be validated through systematic video clip sampling using the structured **Video Scouting Hypotheses** protocol.
