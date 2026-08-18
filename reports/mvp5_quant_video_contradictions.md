# MVP-5 Quantitative Signals vs. Film Contradiction Analysis
## International Basketball Historical Analytics (2005–2025)

**Status**: Core Methodological Audit & Scout Calibration Document  
**Date**: 2026-08-18  

---

# 1. Executive Principle

The most valuable contribution of a sports analytics department is identifying **where the statistical data is incomplete or misleading**. Boxscore metrics measure event frequency and efficiency outcomes, but do not capture movement mechanics, coverage complexity, or advantage scalability.

Below are the 5 critical quantitative-to-video contradictions identified during the MVP-5 tactical validation.

---

# 2. Key Contradiction Case Studies

```
+----------------------------------------------------------------------------------------------------+
| # | STATISTICAL PROXY            | FILM OBSERVATION REALITY        | TACTICAL CONTRADICTION EXPLANATION |
+----------------------------------------------------------------------------------------------------+
| 1 | High Assist Rate             | Secondary Swing / Outlet Pass   | Player accumulated high AST% via   |
|   | (AST% >= 22.0%)              | rather than P&R manipulation.   | hit-ahead transition passes and    |
|   |                              |                                 | basic second-side swing passes     |
|   |                              |                                 | rather than collapsing defense.    |
+----------------------------------------------------------------------------------------------------+
| 2 | High 3-Point Attempt Rate    | Pure Stationary Spot-Up         | High 3PAr reflected willingness to |
|   | (3PAr >= 0.55)               | shooter; cannot shoot on curl.  | stand in corner against zone, but  |
|   |                              |                                 | zero movement gravity off screens. |
+----------------------------------------------------------------------------------------------------+
| 3 | High Steal Rate              | Passing-Lane Gambling;          | Elevated STL/40 achieved by lunging|
|   | (STL/40 >= 2.2)              | dies on on-ball screens.        | out of position, conceding direct  |
|   |                              |                                 | downhill blow-bys at point-of-attack|
+----------------------------------------------------------------------------------------------------+
| 4 | High True Shooting %         | Low-Volume Transition Dumps     | 65% TS% achieved on uncontested fast|
|   | (TS% >= 64.0%)               | against disorganized retreat.   | breaks; unable to create or finish |
|   |                              |                                 | in half-court vs Drop/Switch.      |
+----------------------------------------------------------------------------------------------------+
| 5 | High Rebound Rate            | Uncontested Defensive Boards    | Grabbed long rebounds with no box- |
|   | (DRB% >= 24.0%)              | falling into backcourt.         | out contact; pushed under rim by   |
|   |                              |                                 | physical frontcourt opponents.     |
+----------------------------------------------------------------------------------------------------+
```

---

# 3. Methodological Calibration: Proposed Model Revisions

These qualitative discoveries justify specific calibration recommendations for future model iterations:

1. **Deconstruct Assist Rate ($AST\%$)**:
   - Split creation into `Transition Creation Proxy` vs `Half-Court Creation Proxy` using possession pace and usage interactions.
2. **Defensive Steal-to-Foul Ratio**:
   - Penalize high $STL/40$ when accompanied by high personal fouls ($PF/40 \ge 4.5$), which indicates uncontrolled gambling rather than disciplined containment.
3. **Movement Gravity Index**:
   - Distinguish spot-up spacers from movement spacers by interacting $3\text{PAr}$ with free throw attempt rate ($FTR$) and field goal percentage off curls.
