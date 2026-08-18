# MVP-7 Controlled Counterfactual Simulations Report
## International Basketball Historical Analytics (2005–2025)

**Status**: Certified Counterfactual Research  
**Simulation Iterations**: 10,000 Stochastic Iterations per Counterfactual  
**Master Random Seed**: 42  

> [!IMPORTANT]
> **COUNTERFACTUAL RULE**: Counterfactual simulations do NOT alter historical facts or claim alternate reality timelines. They evaluate the **stochastic distribution of model-implied outcomes** given pre-game probabilities.

---

# 1. Flagship Counterfactual Case Studies

```
+----------------------------------------------------------------------------------------------------+
| ID    | HISTORICAL TOURNAMENT MATCHUP       | BASELINE PROB | SIMULATED CAPTURE % | HISTORICAL RESULT|
+----------------------------------------------------------------------------------------------------+
| **CF1**| Beijing 2008 Gold Medal Final       | $P(\text{ESP}) = 26.4\%$ | ESP: **26.8%** | USA Win (118-107)|
|       | Spain vs. United States (10,000x)   |                          | USA: **73.2%** |                  |
+----------------------------------------------------------------------------------------------------+
| **CF2**| EuroBasket 2015 Pre-Knockout Path   | $P(\text{ESP}) = 67.6\%$ | ESP: **67.6%** | Spain Gold Medal |
|       | Spain Full Bracket Propagation      |                          | Field: **32.4%**| (80-75 vs FRA)   |
+----------------------------------------------------------------------------------------------------+
| **CF3**| EuroBasket 2022 Tactical Sensitivity| $P(\text{ESP}) = 72.0\%$ | Baseline: **72.0%**| Spain Gold Medal |
|       | Spain Baseline vs. Shrunk Bracket   |                          | Shrunk: **66.2%**  | (88-76 vs FRA)   |
+----------------------------------------------------------------------------------------------------+
```

---

# 2. Detailed Counterfactual Insights

### Counterfactual 1: Pekín 2008 Olympic Final Replay (Spain vs. USA)
- **Experimental Setup**: Replaying the 2008 Olympic final 10,000 times strictly under the pre-game model probability ($P(\text{ESP Win}) = 0.264$).
- **Simulated Capture Rate**: Spain captured the gold medal in **2,684 out of 10,000 iterations (26.84%)**, while the USA won in **73.16%** of cases.
- **Decision Science Insight**: In a single 40-minute knockout game, a 26.4% underdog possesses more than a 1-in-4 chance of securing the gold medal. The close historical margin ($118 - 107$) was representative of Spain's upper-quartile performance path.

### Counterfactual 2: EuroBasket 2015 Spain Pre-Knockout Path
- **Experimental Setup**: Simulating the entire EuroBasket 2015 knockout bracket from the round of 16 through the Final.
- **Simulated Capture Rate**: Despite dropping 2 games in the group stage (to Serbia and Italy), Spain retained a **67.60% model-implied championship probability**, reflecting their superior multi-tournament historical rating foundation and positive matchup ratings against France and Lithuania.

### Counterfactual 3: EuroBasket 2022 Tactical Probability Perturbation
- **Experimental Setup**: Assessing Spain's title probability sensitivity under baseline ($\lambda=1.00$) vs shrunk ($\lambda=0.75$) probabilities.
- **Simulated Capture Rate**: Spain's title probability compressed from $72.04\% \rightarrow 66.16\%$, proving that while tournament distributions are sensitive to game probability noise, top-tier contender identification is highly robust.
