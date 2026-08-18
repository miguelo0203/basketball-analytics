# Analyst's Raw Working Note & Investigation Log
## Internal Analytical Scratchpad — EuroBasket 2015 Tactical Study

**Status**: Raw Internal Working Note (Not for Direct Coaching Distribution)  
**Analyst**: Quantitative Scouting Lead  
**Date**: Match Eve ($T-1$)  

---

### 1. Initial Hypothesis
- *Assumption*: I hypothesized that Lithuania's offensive rebounding strength ($\text{ORB}\% = 34.8\%$) would be their greatest threat against us, and that our best defensive adjustment would be packing the paint with two traditional bigs.

---

### 2. What I Expected to Find
- I expected the data to show that lineups with two traditional rim protectors (Gasol + Reyes) yielded our highest defensive rebounding percentage and lowest points conceded in the paint.

---

### 3. What the Data Actually Showed
- When running our DuckDB query on lineup Net Ratings across tournament games:
  * Two-big lineups did increase defensive rebounding rate ($\text{DREB}\% = 76.2\%$).
  * *However*, our offensive transition pace collapsed, and our offensive rating dropped from $116.4$ to $104.2$ due to congested lane spacing.
  * Lineups with one big (Gasol) and four perimeter movers (Mirotić/Claver as stretch-4, Llull, Ribas, Rodríguez) actually produced a $+14.8$ Net Rating differential despite conceding a slightly higher offensive rebound rate ($+2.1\%$).

---

### 4. What Surprised Me
- Lithuania's high 3-point percentage in the tournament ($42.0\%$) was almost entirely driven by uncontested transition kick-outs rather than half-court set execution. When forced into half-court sets with under 10 seconds on the shot clock, their effective field goal percentage plummeted to $41.5\%$.

---

### 5. Contradictory Evidence Surfaced
- **Model vs. Film Conflict**:
  * Statistical model indicated Lithuania's starting point guard was their highest-rated playmaker ($+3.2$ OBPM).
  * Video review revealed that when pressured beyond the 3-point line with full-court ball-denial, he committed 4 live-ball turnovers in the semi-final against Serbia.
  * The statistical metric reflected cumulative volume against weaker group-stage opponents rather than resilience against elite perimeter ball-pressure.

---

### 6. What I Initially Misunderstood
- I initially treated Lithuania's free throw rate as a major risk. On deeper inspection, their high free throw rate was accumulated against small-ball teams that fouled intentionally late in games. In half-court defensive possessions, Spain commits the fewest shooting fouls in the tournament ($\text{Opp FTR} = 21.4\%$).

---

### 7. What Additional Data Would Help
- Optical player tracking (Second Spectrum) to quantify exact lateral closeout distance on Lithuania's wing shooters.
- Possession-level paint touch counts per possession to verify whether post entry denial forces Lithuania into contested long mid-range jumpers.

---

### 8. What I Would NOT Tell the Coach Yet
- *Omitted Finding*: I found a regression model indicating that Lithuania's shooting guard shoots $12\%$ worse when playing on the second night of a back-to-back.
- *Reason for Omission*: The sample size is only 6 career back-to-back games in international play. Presenting a statistically noisy number could cause the coaching staff to leave him unguarded, leading to disastrous open corner threes. Keep it to yourself until verified across larger club samples.

---

### 9. Final Analytical Interpretation
- The tactical battle will be won on offensive spacing and P&R drop coverage punishment. Keep Gasol as the primary high-post decision-maker with four perimeter shooters, force Lithuania to defend in space, and live with giving up an occasional offensive rebound rather than compromising our half-court spacing.
