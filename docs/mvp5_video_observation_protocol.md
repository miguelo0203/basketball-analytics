# Qualitative Video Observation Coding Protocol
## Standard Operating Procedure for Basketball Film Analysis

---

## 1. Overview & Objective

This document formalizes the qualitative video coding standard for validating quantitative player-role profiles. The purpose is to ensure that video observations are systematic, objective, reproducible, and free from confirmation bias.

---

## 2. Possession-Level Sampling Rules

1. **Game Selection**:
   - Sample games across different tournament phases (Group Stage vs High-Leverage Elimination Rounds).
   - Prioritize games where opponents deployed distinct defensive schemes (e.g. Drop vs Switch vs Blitz).
2. **Possession Inclusion**:
   - Target actions directly relevant to the player's archetypal role (e.g. closeout attacks for wings, pick-and-pop depth for bigs).
   - Avoid coding isolated transition blowouts as evidence of half-court tactical quality.
3. **Timestamp Integrity**:
   - Never fabricate video timestamps. If exact timecodes are unavailable from public broadcast footage, leave `timestamp_start` and `timestamp_end` as `NULL` and document the possession context (Quarter, Score Margin, Action Type).

---

## 3. Standard Action Coding Definitions

```
+----------------------------------------------------------------------------------------------------+
| ACTION TYPE              | OBSERVABLE TECHNICAL FOCUS      | SCORING BENCHMARK (0-4 SCALE)         |
+----------------------------------------------------------------------------------------------------+
| `closeout_attack`        | Direction of first step; attack | 0: Fumbles / stops; 2: Baseline drive;|
|                          | high foot; gather balance.      | 4: Decisive paint collapse + kick-out.|
+----------------------------------------------------------------------------------------------------+
| `pnr_manipulation`       | Eye deception; tempo change;    | 0: Trapped / turnover; 2: Basic pass; |
|                          | freeze low-man defender.        | 4: Look-away pocket pass to roller.   |
+----------------------------------------------------------------------------------------------------+
| `movement_shooting`      | Footwork off screen; verticality| 0: Off-balance fade; 2: Standard set; |
|                          | on release against closeout.    | 4: Clean curl catch-and-shoot in stride|
+----------------------------------------------------------------------------------------------------+
| `screen_navigation`      | Fight over top vs trail; rear   | 0: Completely screened; 2: Recovers;  |
|                          | hand contest; angle cut.        | 4: Deflects pass / seals driving lane.|
+----------------------------------------------------------------------------------------------------+
| `pick_and_pop_depth`     | Depth behind arc (>= 6.75m);    | 0: Lingers in mid-range; 2: On line;  |
|                          | fluid catch-and-shoot rhythm.   | 4: Deep pop (7.2m) collapses defense. |
+----------------------------------------------------------------------------------------------------+
```
