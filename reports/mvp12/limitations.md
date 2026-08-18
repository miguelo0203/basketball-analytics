# Comprehensive Analytical & Operational Limitations
## International Basketball Historical Analytics (2005–2025)

**Status**: Formally Certified Limitations Document  
**Ethical & Scientific Requirement**: Transparent Disclosure of Systemic Constraints  

---

# 1. Ten Core Methodological Limitations

1. **Historical Dataset Boundaries (2005–2024)**:
   - The verified relational warehouse covers 18 completed historical tournaments from 2005 through 2024. The 2025 tournament cycle represents the current forward window; no fabricated 2025 data exists in the database.
2. **International Basketball Sample Sizes**:
   - National teams play only 6 to 9 games per tournament, leading to substantial variance in raw perimeter shooting percentages ($\text{3P}\%$) and boxscore totals.
3. **Roster Turnover & Player Availability**:
   - Multi-year national team ratings can be distorted by retirements, NBA/EuroLeague club commitments, or late injuries not captured in historical boxscores.
4. **Qualitative Video Sample Constraints ($N=420$)**:
   - Double-coded video events cover 420 high-leverage possessions across 36 games. While inter-rater reliability is high ($\kappa = 0.80$), this sample is exploratory and hypothesis-generating, not an exhaustive census of all historical possessions.
5. **Statistical Player Clusters vs On-Court Coaching Demands**:
   - K-Means++ archetypes cluster players based on statistical usage profiles. They do not dictate how a specific head coach may deploy a player in a tailored tactical scheme.
6. **Tournament Simulation Bracket Assumptions**:
   - Monte Carlo simulations ($180,000$ iterations) assume fixed bracket advancement rules and constant baseline ratings; they do not simulate in-tournament injuries or sudden tactical evolutions between rounds.
7. **Historical Decision Validation Scale ($N=5$)**:
   - The 80% concordance rate is evaluated across 5 reconstructed historical decisions. It serves as an illustrative qualitative case demonstration, not a formal statistically powered superiority trial.
8. **Absence of Optical Tracking Telemetry**:
   - Public FIBA boxscores do not contain XYZ optical player coordinates (Second Spectrum/Synergy), limiting spatial analysis of passing lanes and contest angles.
9. **Zero Live Club or Transfer Market Data**:
   - This project strictly analyzes international tournament basketball. It does not evaluate club contract negotiations, transfer fees, or domestic league salary caps.
10. **Absence of Causal Proof & Live Prediction Guarantees**:
    - Machine learning models identify conditional associations and feature attributions (TreeSHAP); they do not prove causal levers or guarantee live real-time game outcomes.
