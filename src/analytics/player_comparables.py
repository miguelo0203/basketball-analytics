"""Player Comparables Engine for MVP-3.

Calculates multi-dimensional statistical similarity between player campaigns,
returns top comparators with feature decompositions and explanations.
"""

from pathlib import Path
from typing import Dict, List, Any, Optional
import numpy as np
import pandas as pd

from src.config import ANALYTICS_DATA_DIR, REPORTS_DIR


class PlayerComparablesEngine:
    """Computes similarity vectors and nearest historical comparators for basketball players."""

    def __init__(self, data_dir: Path = ANALYTICS_DATA_DIR):
        self.roles_path = data_dir / "mart_player_roles.parquet"
        if not self.roles_path.exists():
            raise FileNotFoundError(f"Player roles mart {self.roles_path} not found.")
        self.df = pd.read_parquet(self.roles_path)
        self.df_qual = self.df[self.df["is_qualified_sample"] == 1].copy()

        self.dim_cols = [
            "z_dim_scoring_volume", "z_dim_scoring_efficiency",
            "z_dim_perimeter_orientation", "z_dim_creation",
            "z_dim_rebounding", "z_dim_defense", "z_dim_usage"
        ]

    def find_comparables(
        self,
        target_player_tournament_id: str,
        top_n: int = 5,
        same_role_only: bool = False,
    ) -> Dict[str, Any]:
        """Find top-N historical statistical comparables for a target player campaign."""
        target_rows = self.df_qual[self.df_qual["player_tournament_id"] == target_player_tournament_id]
        if target_rows.empty:
            # Fallback search by canonical_player_id
            target_rows = self.df_qual[self.df_qual["canonical_player_id"] == target_player_tournament_id]
            if target_rows.empty:
                raise ValueError(f"Player {target_player_tournament_id} not found in qualified dataset.")

        target = target_rows.iloc[0]
        target_vec = target[self.dim_cols].values.astype(float)
        target_name = target["full_canonical_name"]
        target_tourney = target["tournament_id"]
        target_role = target["role_name"]

        # Filter candidate pool (exclude same player's same tournament)
        candidates = self.df_qual[self.df_qual["player_tournament_id"] != target["player_tournament_id"]].copy()
        if same_role_only:
            candidates = candidates[candidates["role_name"] == target_role]

        cand_mat = candidates[self.dim_cols].values.astype(float)

        # Weighted Euclidean distance
        # Weights: Scoring(1.2), Creation(1.2), Perimeter(1.0), Defense(1.0), Rebounding(1.0), Efficiency(1.0), Usage(1.0)
        weights = np.array([1.2, 1.0, 1.0, 1.2, 1.0, 1.0, 1.0])
        diff = (cand_mat - target_vec) * np.sqrt(weights)
        dists = np.linalg.norm(diff, axis=1)
        sims = 1.0 / (1.0 + (dists / np.sqrt(sum(weights))))

        candidates["similarity_score"] = np.round(sims, 4)
        candidates["distance"] = np.round(dists, 4)

        top_matches = candidates.sort_values(by="similarity_score", ascending=False).head(top_n)

        results = []
        for idx, row in top_matches.iterrows():
            # Determine primary match driver
            vec = row[self.dim_cols].values.astype(float)
            dim_diffs = np.abs(vec - target_vec)
            closest_dim_idx = np.argmin(dim_diffs)
            dim_names = ["Scoring Volume", "True Shooting", "3P Attempt Rate", "Creation/AST%", "Rebounding", "Defensive Activity", "Usage Rate"]
            closest_dim = dim_names[closest_dim_idx]

            results.append({
                "rank": len(results) + 1,
                "player_tournament_id": row["player_tournament_id"],
                "full_canonical_name": row["full_canonical_name"],
                "tournament_id": row["tournament_id"],
                "year": int(row["year"]),
                "team_id": row["team_id"],
                "role_name": row["role_name"],
                "similarity_score": float(row["similarity_score"]),
                "pts_per_40": float(row["pts_per_40"]),
                "ts_pct": float(row["ts_pct"]),
                "three_point_rate": float(row["three_point_rate"]),
                "ast_pct_est": float(row["ast_pct_est"]),
                "primary_match_factor": f"High alignment in {closest_dim} (Δ = {dim_diffs[closest_dim_idx]:.2f}σ)",
            })

        return {
            "target_player": {
                "player_tournament_id": target["player_tournament_id"],
                "full_canonical_name": target_name,
                "tournament_id": target_tourney,
                "year": int(target["year"]),
                "team_id": target["team_id"],
                "role_name": target_role,
                "pts_per_40": float(target["pts_per_40"]),
                "ts_pct": float(target["ts_pct"]),
                "three_point_rate": float(target["three_point_rate"]),
                "ast_pct_est": float(target["ast_pct_est"]),
                "total_minutes": float(target["total_minutes"]),
            },
            "comparables": results,
        }

    def generate_comparables_report(self, output_path: Path = REPORTS_DIR / "mvp3_comparables.md") -> Path:
        """Generate comprehensive comparables report evaluating 3 diverse target stars."""
        # Test targets: Ricky Rubio (EuroBasket 2011), Pau Gasol (EuroBasket 2015), Bogdan Bogdanovic (World Cup 2019)
        targets_to_test = [
            ("eurobasket_2011_ESP_ricky_rubio_1990", "ricky_rubio_1990"),
            ("eurobasket_2015_ESP_pau_gasol_1980", "pau_gasol_1980"),
            ("worldcup_2019_SRB_bogdan_bogdanovic_1992", "bogdan_bogdanovic_1992"),
        ]

        md = f"""# Multi-Dimensional Player Comparables Engine
## MVP-3: International Basketball Historical Analytics (2005–2025)

**Methodology**: Weighted Euclidean Dimensional Distance and Normalized Similarity ($S = \\frac{{1}}{{1 + D}}$)  
**Database Universe**: $N = {len(self.df_qual)}$ qualified international campaigns across 18 tournaments  

---
"""

        for t_id, fallback_id in targets_to_test:
            try:
                res = self.find_comparables(t_id, top_n=5)
            except Exception:
                # Find by canonical ID
                match = self.df_qual[self.df_qual["canonical_player_id"] == fallback_id]
                if match.empty:
                    continue
                res = self.find_comparables(match.iloc[0]["player_tournament_id"], top_n=5)

            tgt = res["target_player"]
            md += f"""
## Target Evaluation: **{tgt['full_canonical_name']}** ({tgt['team_id']}, {tgt['tournament_id']} / {tgt['year']})
- **Discovered Role**: `{tgt['role_name']}`
- **Production Profile**: `{tgt['pts_per_40']:.1f} PTS/40`, `{tgt['ts_pct']:.3f} TS%`, `{tgt['three_point_rate']:.3f} 3PAr`, `{tgt['ast_pct_est']:.3f} AST%`
- **Sample Context**: `{tgt['total_minutes']:.1f} Total Minutes`

### Top-5 Historical Statistical Comparators

| Rank | Player Name | Tournament | Team | Role | Similarity Score | Why Selected |
| :---: | :--- | :---: | :---: | :--- | :---: | :--- |
"""
            for c in res["comparables"]:
                md += f"| **#{c['rank']}** | **{c['full_canonical_name']}** | {c['tournament_id']} ({c['year']}) | {c['team_id']} | {c['role_name']} | **{c['similarity_score']:.3f}** | {c['primary_match_factor']} |\n"

            md += "\n---\n"

        output_path.write_text(md, encoding="utf-8")
        return output_path


def main():
    engine = PlayerComparablesEngine()
    rep = engine.generate_comparables_report()
    print(f"Comparables Report written to: {rep}")


if __name__ == "__main__":
    main()
