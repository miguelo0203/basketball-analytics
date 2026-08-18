# Primary Flagship Selection & Specification
## International Basketball Historical Analytics (2005–2025)

--------------------------------------------------
1. SELECTED PRIMARY FLAGSHIP
--------------------------------------------------

**Title**: Quasi-Experimental Evaluation of the 2010 FIBA 3-Point Arc Extension (6.25m to 6.75m) Using Interrupted Time Series (ITS)

**Lead Methodological Question**:  
*Did the international 50-centimeter extension of the 3-point line in October 2010 cause an immediate structural drop in 3-point attempt rate (3PAr) and efficiency, or did secular global tactical evolution overwhelm the regulatory penalty?*

--------------------------------------------------
2. JUSTIFICATION & CRITERIA
--------------------------------------------------

1. **Data Integrity & Complete Population**:
   - The certified analytical warehouse contains 100% complete team-game boxscores for all 18 major senior men's tournaments from 2005 to 2025 ($N = 1,145$ games, $N = 2,290$ team-game observations).
   - Zero missing values across 3PAr, 3PM, 3PA, FGA, and Pace.

2. **Methodological Validity & Causal Discipline**:
   - Follows the approved econometric and biostatistical standard for single-population policy interventions: **Interrupted Time Series (ITS) with Segmented Regression**.
   - Explicitly rejects invalid Difference-in-Differences (DiD) specifications because all FIBA federations transitioned simultaneously, avoiding pseudoscientific causal claims.

3. **Basketball Relevance**:
   - The 2010 line extension represents the single largest geometric court modification in modern FIBA history.
   - Evaluates whether international basketball experienced the same volume surge as the NBA despite the geometric handicap.

4. **Portfolio & Technical Demonstration**:
   - Demonstrates senior competency in quasi-experimental modeling, Newey-West autocorrelation adjustments, cluster-robust standard errors, and sensitivity testing across tournament tiers.

--------------------------------------------------
3. STATISTICAL MODEL FORMULATION
--------------------------------------------------

The segmented regression model is specified as:

$$Y_{it} = \beta_0 + \beta_1 \cdot T_t + \beta_2 \cdot D_t + \beta_3 \cdot P_t + \mathbf{\Gamma} \mathbf{X}_{it} + \epsilon_{it}$$

Where:
- $Y_{it}$: Outcome metric for team $i$ in game $t$ (Primary: $3\text{PAr} = \text{FG3A} / \text{FGA}$; Secondary: $3\text{P\%} = \text{FG3M} / \text{FG3A}$, $eFG\%$, $\text{Pace}$).
- $T_t$: Continuous tournament sequence index ($T = 0, 1, \dots, 17$ spanning 2005 to 2024).
- $D_t$: Binary indicator for the post-2010 rule era ($D_t = 0$ for tournaments before Oct 2010; $D_t = 1$ for tournaments after Oct 2010).
- $P_t$: Post-intervention time elapsed ($P_t = 0$ before Oct 2010; $P_t = T_t - T_{\text{transition}}$ after Oct 2010).
- $\mathbf{X}_{it}$: Covariates (Competition type fixed effects, stage of tournament, game pace).
- $\beta_1$: Baseline secular trend in international basketball.
- $\beta_2$: Immediate structural level change (jump/drop) at the boundary (EuroBasket 2011).
- $\beta_3$: Differential slope change (acceleration or deceleration) post-2010.
- Standard Errors: Heteroskedasticity- and Autocorrelation-Consistent (HAC / Newey-West) clustered at the tournament level.
