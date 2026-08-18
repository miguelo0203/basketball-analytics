# MVP-8 Multi-Layer Analyst Decision System Architecture Report
## International Basketball Historical Analytics (2005–2025)

**Status**: Certified Decision System Specification  
**Architecture**: 6-Tier Epistemological Synthesis  
**Target Unit**: Player $\times$ Tournament $\times$ Decision Point  
**Total Automated Tests**: 128 Passing (100% Pass Rate)  

---

# 1. Executive Summary & Decision Framework

The MVP-8 Analyst Decision System unifies all analytical layers built across the 20-year international basketball dataset into a structured, auditable decision-making framework for basketball analysts, technical directors, and coaches.

```
+----------------------------------------------------------------------------------------------------+
|                               MVP-8 DECISION ARCHITECTURE                                         |
+----------------------------------------------------------------------------------------------------+
| TIER 1: EMPIRICAL EVIDENCE   | Historical per-40 boxscores, shooting efficiency (TS%), Four Factors|
| TIER 2: STATISTICAL INFERENCE| Clustered Bootstrap 95% CIs & sample reliability classification     |
| TIER 3: TACTICAL ARCHETYPE   | K-Means++ functional role assignment & centroid fit score           |
| TIER 4: VIDEO OBSERVATIONS   | Qualitative film coding (P&R reads, closeout defense, execution)    |
| TIER 5: PREDICTIVE IMPACT    | Out-of-sample LightGBM win probability delta & net rating shift     |
| TIER 6: TOURNAMENT SIMULATION| Monte Carlo tournament medal & title probability sensitivity        |
+----------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+----------------------------------------------------------------------------------------------------+
|                                MULTI-CRITERIA RECOMMENDATION SCORE                                 |
| $$S_{\text{rec}} = 0.25 \text{Role} + 0.25 \text{TS\%} + 0.20 \text{Rel} + 0.15 \text{Pred} + 0.15 \text{Film}$$ |
+----------------------------------------------------------------------------------------------------+
```

---

# 2. Mathematical Scoring & Weighting Rationale

The final recommendation score $S_{\text{rec}} \in [0, 100]$ reflects a balanced multi-criteria decision model:

1. **Role Fit ($25\%$)**: $S_{\text{role}} = \text{Fit}(\text{TargetRole}, \text{AssignedRole}) \cdot \text{Confidence}_{\text{role}} \cdot 100$.
2. **Scoring Efficiency ($25\%$)**: $S_{\text{TS}} = \min(100.0, TS\% \cdot 140.0)$ (anchored at true shooting efficiency benchmark).
3. **Sample Reliability ($20\%$)**: Categorized based on sample exposure ($N \ge 150m \rightarrow 100\%, 90-150m \rightarrow 85\%, 40-90m \rightarrow 65\%, <40m \rightarrow 35\%$).
4. **Predictive Net Impact ($15\%$)**: $S_{\text{pred}} = \min(100.0, \max(0.0, 50.0 + \Delta \text{NetImpact} \cdot 5.0))$.
5. **Film & Tactical Quality ($15\%$)**: $S_{\text{film}} = \text{MeanQualityScore} \cdot 25.0$ (from double-coded IRR observations).

---

# 3. Confidence Tiering & Recommendation Status

- **Tier A: High Confidence**: Requires $N \ge 150$ tournament minutes AND double-coded video observations with high inter-rater agreement ($\kappa \ge 0.80$).
- **Tier B: Moderate Confidence**: Requires $N \ge 90$ minutes or strong multi-tournament prior evidence.
- **Tier C: Limited / High Uncertainty**: Sample exposure $<90$ minutes; recommendations flagged with explicit wide uncertainty intervals.

### Status Classifications:
- **RECOMMENDED**: $S_{\text{rec}} \ge 70.0$ AND zero major tactical contradictions.
- **PROCEED WITH CAUTION**: $S_{\text{rec}} \in [55.0, 70.0)$ OR minor sample uncertainty.
- **NOT RECOMMENDED**: $S_{\text{rec}} < 55.0$ OR acute tactical contradictions detected on film.
