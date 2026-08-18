# Methodology Summary for Basketball Professionals & Non-Technical Readers
## International Basketball Historical Analytics (2005–2025)

**Status**: Formally Certified Methodology Guide  
**Purpose**: Explaining 10 Core Analytical Methodologies: "What It Answers" vs. "What It Does NOT Answer"  

---

# 1. Four Factors of Basketball Success

- **What It Answers**: Which fundamental possession drivers (shooting efficiency $\text{eFG}\%$, turnover discipline $\text{TOV}\%$, offensive rebounding $\text{ORB}\%$, or free throw frequency $\text{FTR}$) explain why a team won or lost.
- **What It Does NOT Answer**: Why a specific shooter missed an open corner 3-pointer or whether a defensive rotation was executed with proper communication.

---

# 2. Net Rating (Pace-Adjusted Efficiency)

- **What It Answers**: How many points a team outscores or is outscored by an opponent per 100 possessions, removing the distorting effect of fast or slow game tempo.
- **What It Does NOT Answer**: How a team performs in high-pressure, late-game, single-possession clutch situations.

---

# 3. Functional Player Archetypes (K-Means++ & PCA)

- **What It Answers**: What statistical style of play and functional role a player occupies (e.g. Primary Initiator, Movement Shooter, Interior Hub) based on usage, shot profiles, and passing rates.
- **What It Does NOT Answer**: A player's defensive effort, vocal leadership in the locker room, or ability to execute a novel coaching adjustment.

---

# 4. Expanding Temporal Walk-Forward Validation

- **What It Answers**: How well a machine learning model generalizes to future, unseen tournaments when trained strictly on historical games available prior to tip-off.
- **What It Does NOT Answer**: Guaranteed real-time predictive accuracy if a major star suffers an injury 5 minutes before the game.

---

# 5. Probability Calibration (Expected Calibration Error)

- **What It Answers**: Whether the model's confidence corresponds to reality (e.g. when the model assigns a 70% win probability, do those teams actually win 70% of the time?).
- **What It Does NOT Answer**: Which specific team among those 70% favorites will definitely win tonight.

---

# 6. Clustered Non-Parametric Bootstrap

- **What It Answers**: How much statistical uncertainty and random variance surrounds our metric estimates when accounting for tournament clustering.
- **What It Does NOT Answer**: Unforeseen external shocks or sudden tactical innovations.

---

# 7. Permutation Testing & FDR Control

- **What It Answers**: Whether an observed difference between groups is genuinely distinct or merely the product of random sample noise, while controlling false discovery rates ($Q = 0.05$).
- **What It Does NOT Answer**: Whether that statistically significant difference is large enough to matter tactically on the basketball court.

---

# 8. Monte Carlo Tournament Simulation

- **What It Answers**: How single-game probabilistic uncertainty propagates through a multi-round bracket tournament over 10,000 independent tournament replays.
- **What It Does NOT Answer**: The exact chronological script of how a knockout game will unfold quarter by quarter.

---

# 9. Feature Attribution (TreeSHAP)

- **What It Answers**: Which pre-game variables contributed most strongly to shifting the model's output from the baseline prior.
- **What It Does NOT Answer**: Causal levers. Increasing a team's offensive rebounding rate will not automatically produce a win if it causes catastrophic transition defense breakdowns.

---

# 10. Structured Qualitative Video Evidence

- **What It Answers**: How a team executes tactical schemes (P&R drop depth, hedge aggressiveness, closeout recovery speed) across high-leverage possessions.
- **What It Does NOT Answer**: A complete, exhaustive census of all 40 minutes of game play across all 12 roster players.
