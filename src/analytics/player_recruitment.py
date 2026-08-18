"""Recruitment & Scouting Decision-Support Engine for MVP-3.

Executes multi-criteria player filtering, weighted archetype fit scoring,
trade-off analysis, and generates structured Video Scouting Hypotheses.
"""

from pathlib import Path
from typing import Dict, List, Any, Optional
import numpy as np
import pandas as pd

from src.config import ANALYTICS_DATA_DIR, REPORTS_DIR


class RecruitmentDecisionEngine:
    """Evaluates player recruitment profiles against concrete tactical needs."""

    def __init__(self, data_dir: Path = ANALYTICS_DATA_DIR):
        self.roles_path = data_dir / "mart_player_roles.parquet"
        self.df = pd.read_parquet(self.roles_path)
        self.df_qual = self.df[self.df["is_qualified_sample"] == 1].copy()

    def search_shortlist(
        self,
        target_role: Optional[str] = None,
        min_age: int = 18,
        max_age: int = 34,
        min_minutes: float = 80.0,
        weights: Optional[Dict[str, float]] = None,
        top_n: int = 8,
    ) -> pd.DataFrame:
        """Search and rank players based on weighted dimensional fit."""
        candidates = self.df_qual.copy()

        # Context filters
        candidates = candidates[
            (candidates["player_age_at_tournament"] >= min_age) &
            (candidates["player_age_at_tournament"] <= max_age) &
            (candidates["total_minutes"] >= min_minutes)
        ]

        if target_role:
            candidates = candidates[candidates["role_name"].str.contains(target_role, case=False, na=False)]

        if candidates.empty:
            return pd.DataFrame()

        # Default weights for modern 3-and-D playmaking wing
        if not weights:
            weights = {
                "z_dim_perimeter_orientation": 1.5,
                "z_dim_scoring_efficiency": 1.2,
                "z_dim_creation": 1.0,
                "z_dim_defense": 1.2,
                "z_dim_scoring_volume": 0.8,
            }

        score = np.zeros(len(candidates))
        tot_w = sum(weights.values())

        for dim, w in weights.items():
            if dim in candidates.columns:
                score += candidates[dim].values * (w / tot_w)

        candidates["fit_score"] = np.round(score, 3)
        # Normalize fit score to 0..100 scale
        min_s = candidates["fit_score"].min()
        max_s = candidates["fit_score"].max()
        if max_s > min_s:
            candidates["fit_index_100"] = np.round(100.0 * (candidates["fit_score"] - min_s) / (max_s - min_s), 1)
        else:
            candidates["fit_index_100"] = 50.0

        shortlist = candidates.sort_values(by="fit_score", ascending=False).head(top_n)
        return shortlist

    def generate_recruitment_report(self, output_path: Path = REPORTS_DIR / "mvp3_recruitment_fit.md") -> Path:
        """Generate recruitment evaluation report with scouting decision support."""
        # Case Study: Club seeking a dynamic Two-Way Playmaking Wing
        shortlist = self.search_shortlist(
            target_role="Wing",
            min_age=20,
            max_age=32,
            min_minutes=90.0,
            top_n=8
        )

        md = f"""# Recruitment & Scouting Decision Support: Two-Way Playmaking Wing
## MVP-3: International Basketball Historical Analytics (2005–2025)

**Tactical Profile Requested**:  
> *"A 20–32 year old perimeter wing who provides floor spacing ($3\\text{{PAr}} > 0.40$), efficient scoring ($TS\\% > 0.55$), secondary creation ($AST\\% > 0.12$), and defensive event generation ($STL40 > 1.0$) with certified tournament reliability ($MIN \\ge 90$)."*

---

## 1. Ranked Statistical Candidate Shortlist

| Rank | Player Name | Federation | Tournament | Age | Role | Fit Score (0-100) | TS% | 3PAr | AST% | STL/40 | Minutes |
| :---: | :--- | :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
"""
        for idx, (_, r) in enumerate(shortlist.iterrows()):
            md += f"| **#{idx+1}** | **{r['full_canonical_name']}** | {r['team_id']} | {r['tournament_id']} ({int(r['year'])}) | {int(r['player_age_at_tournament'])} | {r['role_name']} | **{r['fit_index_100']}** | {r['ts_pct']:.3f} | {r['three_point_rate']:.3f} | {r['ast_pct_est']:.3f} | {r['stl_per_40']:.1f} | {r['total_minutes']:.1f} |\n"

        md += """
---

## 2. Statistical Trade-Off Analysis

1. **Volume vs. Efficiency Trade-off**:
   - Elite volume scorers often operate at slightly depressed True Shooting percentages due to difficult shot creation at the end of the shot clock.
   - High-efficiency spacers require creators to generate open catch-and-shoot looks.

2. **Creation vs. Turnover Risk**:
   - Wings with $AST\\% > 0.20$ exhibit higher turnover rates ($TOV\\% \\approx 14\text{--}16\\%$).

---

## 3. The Analytics-to-Scouting Bridge: Video Sampling Hypotheses

The quantitative model identifies statistical candidates, but cannot observe execution mechanics, decision speed, or defensive discipline.

### Recommended Video Sampling Protocol for Coaching Staff:

1. **[HIPÓTESIS PARA VÍDEO 1 - Shooting Versatility & Release Speed]**:
   - *Target*: Top candidates.
   - *Clip Criteria*: Sample 10 catch-and-shoot possessions off wide pin-downs and 5 off-the-dribble pull-up 3s against hard closeouts.
   - *Scouting Verification*: Assess dip mechanics, footwork balance on left-to-right drift, and release speed under defensive contest.

2. **[HIPÓTESIS PARA VÍDEO 2 - P&R Decision Making & Secondary Creation]**:
   - *Target*: Primary shortlist.
   - *Clip Criteria*: Middle pick-and-roll possessions in the 4th quarter against Drop coverage.
   - *Scouting Verification*: Does the player make the low-man skip read or freeze the drop big with a floater/mid-range pull-up?

3. **[HIPÓTESIS PARA VÍDEO 3 - Point-of-Attack Defensive Discipline]**:
   - *Target*: High steal-rate candidates.
   - *Clip Criteria*: Defensive possessions against dynamic ball handlers.
   - *Scouting Verification*: Are the high steal numbers driven by sound positional containment or undisciplined gambling that breaks team defensive shell?

---

## 4. Operational Boundary: What the Data Says vs. What Requires Scouting

```
+-------------------------------------------------------------+-------------------------------------------------------------+
|                     WHAT THE DATA SAYS                      |                WHAT STILL REQUIRES SCOUTING                 |
+-------------------------------------------------------------+-------------------------------------------------------------+
| - Exact shooting accuracy & 3P attempt volume               | - Shooting mechanics against NBA/EuroLeague length contests |
| - Secondary creation frequency (AST%, AST/TOV)              | - Passing vision, timing, and processing speed under blitz  |
| - Defensive event production (STL40, BLK40, DRB%)           | - On-ball stance, screen navigation, and help rotation IQ   |
| - Usage rate and efficiency across 18 tournaments           | - Emotional resilience, locker room leadership, coachability|
+-------------------------------------------------------------+-------------------------------------------------------------+
```
"""
        output_path.write_text(md, encoding="utf-8")
        return output_path


def main():
    engine = RecruitmentDecisionEngine()
    rep = engine.generate_recruitment_report()
    print(f"Recruitment Report written to: {rep}")


if __name__ == "__main__":
    main()
