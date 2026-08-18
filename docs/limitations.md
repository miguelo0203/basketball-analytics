# Explicit Methodological & Data Limitations
## International Basketball Historical Analytics (2005–2025)

---

## 1. Small Sample Sizes in International Basketball

- **Tournament Brevity**: FIBA tournaments consist of 5 to 11 games per nation. Single-game knockout variance (e.g. World Cup 2014 Quarter-Final vs. France) cannot be interpreted as structural team failure.
- **Statistical Uncertainty**: Standard errors for individual player-tournament rates are inherently wide. All longitudinal curves and rankings must be interpreted alongside their bootstrap confidence intervals.

---

## 2. Inherent Limits of Boxscore-Derived Possessions

- **$0.44$ Free Throw Coefficient**: The Dean Oliver approximation uses $0.44 \times FTA$ to estimate possession-ending free-throw trips. In FIBA, and-1 fouls and technical free throws create minor discrepancies ($\pm 1-2$ possessions per game) compared to exact play-by-play tracking.
- **Bilateral Approximation**: The warehouse stores both single-team possession estimates and bilateral averages. Bilateral averages enforce conservation of possessions between opponents but remain approximations.

---

## 3. Epistemological Non-Causality

- **No Coaching Causality**: Tenures of Sergio Scariolo, Pepu Hernández, and Aíto García Reneses reflect the available player talent and opponent draw of each era. Stylistic differences are descriptive associations, not causal coaching effects.
- **No Quasi-Experimental DiD on Rule Changes**: The 2010 3-point line change was applied globally to all FIBA nations simultaneously. Interrupted Time Series models quantify association and structural breaks, not pure counterfactual causality.

---

## 4. Historical Data Availability Boundaries

- **Play-by-Play & Lineups**: Sub-possession lineups and exact substitution tracking are unreliable prior to 2012. Stint-level plus/minus is omitted for early tournaments (2005–2010).
- **Spatial Shot Charts**: Shot coordinates $(X, Y)$ are available solely for the modern era (2019–2025). Spatial findings cannot be extrapolated retroactively to the 2006–2015 golden generation.
