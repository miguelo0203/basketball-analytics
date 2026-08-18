# Professional Scouting Decision-Support Workflow
## The 12-Stage Pipeline from Recruitment Need to Human Decision

```
1. RECRUITMENT BRIEF (Tactical Need & Constraints)
   ↓
2. CANDIDATE UNIVERSE CONSTRUCTION (N = 4,350 Campaigns)
   ↓
3. ELIGIBILITY & MINIMUM SAMPLE SCREENING (MIN >= 40, G >= 3 → N = 3,767)
   ↓
4. TOURNAMENT CONTEXT NORMALIZATION (Z_tourney & Percentiles)
   ↓
5. MANDATORY TACTICAL FILTERING (Stage 1 Pool → N = 20)
   ↓
6. DECOMPOSABLE FIT SCORING & RELIABILITY ADJUSTMENT (Stage 2 Shortlist → N = 10)
   ↓
7. HISTORICAL COMPARABLES INTEGRATION (Multi-dimensional Alignment)
   ↓
8. FINAL SCOUTING DOSSIER SELECTION (Stage 3 Final Candidates → N = 5)
   ↓
9. COUNTERFACTUAL STABILITY & BLIND VALIDATION (Reputation Bias Audit)
   ↓
10. ANALYST-TO-SCOUT OPERATIONAL HANDOFF (Data vs Video vs Unknown)
   ↓
11. STRUCTURED VIDEO CLIP VALIDATION ([HIPÓTESIS PARA VÍDEO])
   ↓
12. FINAL COACHING & FRONT-OFFICE DECISION
```

---

## 1. Step-by-Step Operating Protocol

1. **Recruitment Brief**: The sporting director and head coach define tactical needs (e.g. secondary playmaking wing), positional constraints, and budget/age windows.
2. **Candidate Universe**: All historical player-tournament campaigns are gathered from the certified DuckDB warehouse.
3. **Eligibility Screening**: Candidates with $<40\text{ minutes}$ or $<3\text{ games}$ are excluded due to excessive sampling variance.
4. **Context Normalization**: Boxscore statistics are adjusted for competition pace, era regulatory differences (6.25m vs 6.75m 3PT line), and tournament talent density.
5. **Mandatory Filtering**: Hard criteria eliminate non-viable tactical profiles (e.g. $3\text{PAr} < 0.35$).
6. **Decomposable Scoring**: Candidates are ranked on transparent, interpretable dimensions rather than a single black-box number.
7. **Reliability Weighting**: Profiles with High Reliability ($MIN \ge 150, G \ge 6$) receive a stability bonus; Limited Sample profiles are flagged.
8. **Comparables Engine**: Nearest historical comparators are extracted to provide operational context for coaching staff.
9. **Counterfactual Robustness**: Shortlists are evaluated across 5 sensitivity variants (Strict TS%, High Sample, Post-2010, EuroBasket-only) to detect specification-sensitive candidates.
10. **Blind Validation**: Selection is audited without player names or team affiliations to eliminate reputation bias.
11. **Analyst-to-Scout Handoff**: Formulates structured **Video Scouting Hypotheses** (`[HIPÓTESIS PARA VÍDEO]`) targeting specific mechanics, coverage reads, and decision making.
12. **Final Human Decision**: Scouting staff reviews video clips and conducts interviews to make the final personnel decision.
