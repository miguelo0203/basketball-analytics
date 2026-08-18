# Professional Basketball Analytics & Scouting Benchmark
## MVP-3: Player Evaluation, Role Discovery & Recruitment Analytics

**Author**: Senior Basketball Data Engineer & Analytics Researcher  
**Framework**: International Basketball Historical Analytics (2005–2025)  
**Date**: 2026-08-18  

---

## 1. Executive Summary & Objective

The objective of this benchmark is to survey empirical methodologies and operational frameworks used by professional basketball analytics departments (NBA, EuroLeague, FIBA national teams) and MIT Sloan Sports Analytics research. 

Rather than treating player analytics as an abstract machine learning competition, this report establishes how professional front offices and coaching staffs evaluate players, define functional roles, compute player similarity, control for context, and integrate quantitative findings into actionable scouting decisions.

---

## 2. Review of 10 Professional & Academic Research Benchmarks

### 1. Dean Oliver (2004) — *Basketball on Paper* & The Four Factors Framework
- **Core Contribution**: Established the foundational division of basketball efficiency into Four Factors ($eFG\%, TOV\%, ORB\%, FTr$) and formalized individual Possession Usage ($USG\%$) vs. Offensive Rating ($ORtg$).
- **Key Professional Lesson**: Production volume ($PTS, FGA$) must always be separated from scoring efficiency ($TS\%, eFG\%$) and possession termination rate ($USG\%$). A player with high volume but low efficiency destroys team offensive rating unless paired with elite rebounding or creation.

### 2. Dan Rosenbaum & Roland Beech (2004) — Adjusted Plus-Minus (APM)
- **Core Contribution**: First econometric application of multivariate linear regression to simultaneous on-court substitution stints, isolating a player's marginal impact from the quality of their 4 teammates and 5 opponents.
- **Key Professional Lesson**: Raw plus-minus ($+/-$) is heavily confounded by lineup co-occurrences. In international tournament play where stint samples are small ($5\text{--}11$ games), pure APM overfits, necessitating regularized or rate-based boxscore priors.

### 3. Jeremias Engelmann & Steve Ilardi (2014) — Regularized Adjusted Plus-Minus (RAPM / RPM)
- **Core Contribution**: Introduced L2 ridge regression regularization and Bayesian boxscore priors (xRAPM) to stabilize noisy stint-level player impact estimates.
- **Key Professional Lesson**: Shrinkage toward the prior is mathematically necessary when sample sizes are small. For short international tournaments, boxscore metric representations provide more stable signal than unstabilized stint data.

### 4. Muthu Alagappan (2012 MIT Sloan Sports Analytics Conference) — *Redefining the Positions in Basketball*
- **Core Contribution**: Applied Topological Data Analysis (TDA) and network clustering to demonstrate that the traditional 5 positions (PG, SG, SF, PF, C) are obsolete. Discovered 13 functional archetypes (e.g. *Floor General*, *Scoring Ball Handler*, *Paint Protector*, *3-and-D Wing*, *Stretch Big*).
- **Key Professional Lesson**: Player roles must be derived from on-court *actions and shot distributions*, not nominal roster labels. Morphological traits (height) should describe discovered roles post-hoc rather than constrain the feature space.

### 5. Kirk Goldsberry (2012–2019) — *CourtVision & Spatial Shot Value*
- **Core Contribution**: Transformed player shot charts into spatial efficiency maps ($xPTS$), evaluating shot quality against league-average baselines by zone.
- **Key Professional Lesson**: A player’s shooting profile is characterized by two distinct dimensions: **Shot Selection Distribution** (where they shoot) and **Shot Making Efficiency** (relative accuracy above expected).

### 6. Kostas Pelechrinis et al. (2018 MIT Sloan Conference) — *Evaluating Basketball Roles and Lineup Synergies*
- **Core Contribution**: Modeled player role complementarity using non-negative matrix factorization and spatial event distributions, demonstrating that optimal lineups require balanced archetype combinations (e.g. primary creator + floor spacers + rim protector) rather than accumulating identical high-usage talents.
- **Key Professional Lesson**: Recruitment and scouting must evaluate *fit within the existing ecosystem* rather than ranking players on an absolute isolated scalar.

### 7. Kostya Medvedovsky (2019–present) — *DARKO (Daily Advanced Real-Time Kind-of-Plus-Minus)*
- **Core Contribution**: Developed a production Bayesian state-space framework tracking player talent progression via Kalman filtering, exponential time decay, and age-curve priors.
- **Key Professional Lesson**: A player's talent estimate should be an evolving continuous distribution. Historical international tournament play must account for athlete career phase (ascending prospect, prime, veteran).

### 8. Nathan Sandholtz & Luke Bornn (2020 MIT Sloan Conference) — *Markov Decision Processes in Basketball*
- **Core Contribution**: Framed basketball possessions as state-action Markov chains, quantifying how player decision-making (pass vs shoot vs drive) shifts expected possession value ($EPV$).
- **Key Professional Lesson**: Decision-making quality and creation value are distinct from shooting skill. Passing volume and assist-to-turnover ratio serve as robust boxscore proxies for offensive decision reliability.

### 9. Sanjit Bedi & Brian Macdonald (2021 MIT Sloan Conference) — *Possession Flow & Creation Value*
- **Core Contribution**: Quantified how secondary creators and ball movers generate "hockey assists" and unselfish ball reversal, creating high-efficiency corner 3s.
- **Key Professional Lesson**: Secondary playmaking is a distinct, highly sought-after archetype in modern basketball (e.g. playmaking wings and short-roll passing bigs).

### 10. Sergio Scariolo & Professional FIBA/EuroLeague Staff Scouting Protocols
- **Core Contribution**: Integrated quantitative analytical profiling with structured video clip sampling in international national team preparation.
- **Key Professional Lesson**: Quantitative data indicates **WHAT** a player produces; qualitative video scouting assesses **HOW** and **WHY** (footwork, pick-and-roll defensive coverage execution, mental resilience under pressure, off-ball discipline). Analytics must explicitly generate **Scouting Questions** for the coaching staff.

---

## 3. Synthesis: Recurring Professional Analytics & Scouting Patterns

```
+--------------------------------------------------------------------------------------------------+
|                               PROFESSIONAL EVALUATION PIPELINE                                   |
+--------------------------------------------------------------------------------------------------+
| 1. DATA AUDIT          | Separate OBSERVED from ESTIMATED; enforce accounting integrity.         |
| 2. VOLUME vs. EFFICIENCY| Never judge volume (PTS, FGA) without efficiency (TS%, eFG%, TOV%).    |
| 3. ROLE DISCOVERY      | Group by on-court function (Creation, Spacing, Rebounding, Defense).     |
| 4. CONTEXT & USAGE     | Control for team pace, minutes share, opponent tier, and sample size.   |
| 5. SIMILARITY ENGINE   | Multi-dimensional nearest-neighbor distance with feature transparency.   |
| 6. RECRUITMENT FIT     | Match statistical profiles to concrete tactical system needs.            |
| 7. SCOUTING BRIDGE     | Formulate explicit video verification questions ("What the data says"    |
|                        | vs. "What still requires manual scouting review").                       |
+--------------------------------------------------------------------------------------------------+
```

---

## 4. Methodological Commitments for MVP-3

1. **Avoid Black-Box Single Numbers**: We will not summarize players into a single opaque rating. We will construct a multi-dimensional, interpretable functional role profile.
2. **Explicit Sample Size Governance**: Players with $MIN < 40$ or $G < 3$ in a tournament will be flagged with uncertainty warnings.
3. **Transparent Player Similarity**: Comparators will report exact feature-by-feature distance and explain *why* two players match statistically.
4. **The Analytics-to-Scouting Boundary**: Every player evaluation report will terminate with an explicit section: **"What the Data Says" vs. "What Still Requires Video Scouting."**
