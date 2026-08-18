# Realistic Analyst Task Simulation: Generational Offensive Evolution
## Tactical Investigation for Coaching Staff & Basketball Operations

**Task Context**: Pre-Tournament Tactical Staff Meeting  
**Investigative Subject**: Tactical Evolution of Spain's Offensive Engine Across International Eras (2005–2015 vs. 2016–2024)  

---

# 1. The Coaching Question

> *"Our coaching staff believes that Spain's offensive identity fundamentally shifted across the 2005–2024 era from low-post interior hub dominance (Gasol era) to perimeter pick-and-roll creator gravity and movement spacing (post-2017 era). What does the data actually show, where are the largest uncertainties, and how should this inform our tactical preparation for modern tournament play?"*

---

# 2. Data Required & Provenance

- **Relational Tables**: `data/03_validated/basketball_analytics.duckdb` (`fact_game`, `fact_player_game`, `dim_tournament`).
- **Feature Marts**: `mart_team_game_analytics.parquet` (team-level Four Factors) and `mart_player_roles.parquet` (functional archetype usage shares).
- **Temporal Filter**: Era 1 (2005–2015, $9$ Tournaments, $76$ Games) vs. Era 2 (2016–2024, $9$ Tournaments, $66$ Games).

---

# 3. Analytical Approach

1. **Four Factors & Pace Decomposition**: Compare team-level Effective Field Goal Percentage ($\text{eFG}\%$), 3-Point Attempt Rate ($\text{3PAr}$), Turnover Rate ($\text{TOV}\%$), and Free Throw Rate ($\text{FTR}$).
2. **Functional Archetype Usage Audit**: Aggregate usage percentage ($\text{USG}\%$) and assist percentage ($\text{AST}\%$) shares across player roles (Interior Hubs vs. Primary Initiators vs. Movement Spacers).
3. **Statistical Uncertainty Modeling**: Compute non-parametric bootstrap 95% confidence intervals ($B = 5,000$) on era metric differentials.

---

# 4. The Quantitative Evidence

```
+----------------------------------------------------------------------------------------------------+
| OFFENSIVE METRIC              | ERA 1 (2005–2015) | ERA 2 (2016–2024) | DELTA & BOOTSTRAP 95% CI   |
+----------------------------------------------------------------------------------------------------+
| **Offensive Net Rating**      | 114.8 pts/100 poss| 109.2 pts/100 poss| -5.6 [-8.4, -2.8]          |
| **3-Point Attempt Rate (3PAr)**| 27.4% of FGA      | 38.6% of FGA      | +11.2% [+8.6%, +13.8%]     |
| **Free Throw Rate (FTR)**     | 34.2%             | 25.8%             | -8.4% [-11.2%, -5.6%]      |
| **Turnover Rate (TOV%)**      | 14.1%             | 13.2%             | -0.9% [-1.8%, +0.1%]       |
| **Interior Hub Usage Share**  | 42.6% of team USG | 21.4% of team USG | -21.2% [-25.4%, -17.0%]    |
| **Primary Initiator AST Share**| 31.5% of team AST| 48.2% of team AST | +16.7% [+12.4%, +21.0%]    |
+----------------------------------------------------------------------------------------------------+
```

---

# 5. Basketball Interpretation & Tactical Context

1. **From Interior Draw-and-Kick to P&R Spacing**:
   - In Era 1, offensive gravity originated inside-out: Pau and Marc Gasol operated as high-usage interior hubs ($42.6\%$ usage share), generating elite free throw rates ($\text{FTR} = 34.2\%$).
   - In Era 2, offensive gravity shifted entirely to high pick-and-roll initiation (Ricky Rubio, Lorenzo Brown), where primary ball-handlers generate $48.2\%$ of team assists and perimeter volume expanded to $38.6\%$ 3-point rate.
2. **Efficiency vs. Volatility Trade-Off**:
   - The modern perimeter profile is more volatile: when 3-point shots fall, Spain achieves blowout margins; when perimeter shooting slumps, the absence of low-post foul generation leads to scoring droughts.

---

# 6. Actionable Coaching Implications

- **P&R Scheme Focus**: In modern tournament play, opponent drop coverage must be attacked with dynamic pick-and-pop bigs to preserve the $38.6\%$ perimeter spacing engine.
- **Foul Generation Contingency**: Because modern lineups draw fewer free throws ($-8.4\%\ \text{FTR}$), coaching staff must design set actions that create downhill rim pressure during fourth-quarter dry spells.

---

# 7. What the Analysis CANNOT Establish (Limitations)

- **Cannot Prove Coaching Intent**: Data shows what happened on the court, not whether Sergio Scariolo actively intended to shoot more 3-pointers or was forced to by generational personnel changes.
- **Opponent Quality Confounding**: Era 2 coincided with a global rise in European defensive switching schemes that suppressed post entries across all FIBA teams.

---

# 8. Final Analyst Communication to Coaching Staff

> *"Coach, the data confirms your intuition: Spain's offensive engine shifted dramatically from interior foul-drawing ($34.2\%\ \text{FTR}$) to pick-and-roll creation and perimeter volume ($38.6\%\ \text{3PAr}$). Our primary risk tonight is shooting volatility. If the opponent plays physical drop coverage, our secondary guards must attack the paint to generate free throws when outside shots aren't falling."*
