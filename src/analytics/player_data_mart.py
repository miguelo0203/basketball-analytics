"""MVP-3 Player Data Mart Generator.

Transforms validated player tables in DuckDB into standardized feature matrices,
role dimensions, and analytical tables under data/04_analytics/.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import duckdb
from sklearn.preprocessing import StandardScaler

from src.config import VALIDATED_DB_PATH, ANALYTICS_DATA_DIR


class PlayerDataMartGenerator:
    """Generates player analytical marts with normalized dimensions and context controls."""

    def __init__(
        self,
        db_path: Path = VALIDATED_DB_PATH,
        output_dir: Path = ANALYTICS_DATA_DIR,
    ):
        self.db_path = db_path
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_player_marts(self) -> Dict[str, Path]:
        """Generate and save parquet marts."""
        con = duckdb.connect(str(self.db_path), read_only=True)
        try:
            query = """
                SELECT 
                    pt.player_tournament_id,
                    pt.tournament_id,
                    t.year,
                    t.competition_id,
                    pt.team_id,
                    pt.canonical_player_id,
                    p.full_canonical_name,
                    p.primary_position,
                    p.birth_year,
                    (t.year - p.birth_year) AS player_age_at_tournament,
                    pt.games_played,
                    pt.total_seconds,
                    pt.total_minutes,
                    pt.pts_per_40,
                    pt.fga_per_40,
                    pt.fg3a_per_40,
                    pt.fta_per_40,
                    pt.fg2_pct,
                    pt.fg3_pct,
                    pt.ft_pct,
                    pt.efg_pct,
                    pt.ts_pct,
                    pt.three_point_rate,
                    pt.free_throw_rate,
                    pt.orb_pct_est,
                    pt.drb_pct_est,
                    pt.ast_pct_est,
                    pt.tov_pct_est,
                    pt.stl_per_40,
                    pt.blk_per_40,
                    pt.pf_per_40,
                    pt.usg_pct_avg,
                    pt.avg_game_score,
                    pt.pir_per_40,
                    pt.height_cm_at_tournament,
                    CASE WHEN pt.total_minutes >= 40.0 AND pt.games_played >= 3 THEN 1 ELSE 0 END AS is_qualified_sample
                FROM fact_player_tournament pt
                JOIN dim_player p ON pt.canonical_player_id = p.canonical_player_id
                JOIN dim_tournament t ON pt.tournament_id = t.tournament_id
                ORDER BY t.year, pt.tournament_id, pt.team_id, pt.total_minutes DESC
            """
            df_raw = con.execute(query).df()

            # Fill missing rates cleanly
            rate_cols = ["fg2_pct", "fg3_pct", "ft_pct", "efg_pct", "ts_pct", "three_point_rate", "free_throw_rate"]
            for col in rate_cols:
                df_raw[col] = df_raw[col].fillna(0.0)

            # Construct 7 standardized basketball dimensions on qualified sample
            df_qual = df_raw[df_raw["is_qualified_sample"] == 1].copy()

            # 1. Scoring Volume
            # 2. Scoring Efficiency
            # 3. Perimeter Orientation (3PAr)
            # 4. Creation / Playmaking (AST% & AST/TOV proxy)
            # 5. Rebounding (ORB% + DRB%)
            # 6. Defensive Activity (STL40 + BLK40)
            # 7. Usage / Offensive Responsibility (USG%)
            
            features = pd.DataFrame(index=df_qual.index)
            features["dim_scoring_volume"] = df_qual["pts_per_40"]
            features["dim_scoring_efficiency"] = df_qual["ts_pct"]
            features["dim_perimeter_orientation"] = df_qual["three_point_rate"]
            features["dim_creation"] = df_qual["ast_pct_est"]
            features["dim_rebounding"] = df_qual["orb_pct_est"] + df_qual["drb_pct_est"]
            features["dim_defense"] = df_qual["stl_per_40"] + df_qual["blk_per_40"]
            features["dim_usage"] = df_qual["usg_pct_avg"]

            scaler = StandardScaler()
            scaled_matrix = scaler.fit_transform(features)
            
            for idx, c in enumerate(features.columns):
                df_qual[f"z_{c}"] = scaled_matrix[:, idx]

            # Merge back with full population
            df_merged = df_raw.merge(
                df_qual[["player_tournament_id", "z_dim_scoring_volume", "z_dim_scoring_efficiency",
                         "z_dim_perimeter_orientation", "z_dim_creation", "z_dim_rebounding",
                         "z_dim_defense", "z_dim_usage"]],
                on="player_tournament_id",
                how="left"
            )

            # Save Parquet
            out_path = self.output_dir / "mart_player_tournament_features.parquet"
            df_merged.to_parquet(out_path, index=False)

            return {
                "mart_player_tournament_features": out_path,
                "total_rows": len(df_merged),
                "qualified_rows": len(df_qual),
            }
        finally:
            con.close()


def main():
    gen = PlayerDataMartGenerator()
    res = gen.generate_player_marts()
    print("Player Data Mart Generated:", res)


if __name__ == "__main__":
    main()
