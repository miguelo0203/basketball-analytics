"""Analytical Data Mart Generator for MVP-2.

Creates reproducible analytical datasets, views, and Parquet tables under data/04_analytics/
from the certified warehouse in data/03_validated/basketball_analytics.duckdb.
"""

from pathlib import Path
import hashlib
import duckdb
import pandas as pd

from src.config import VALIDATED_DB_PATH, ANALYTICS_DATA_DIR, DOCS_DIR


class DataMartGenerator:
    """Generates certified analytical data marts for downstream modeling."""

    def __init__(
        self,
        db_path: Path = VALIDATED_DB_PATH,
        output_dir: Path = ANALYTICS_DATA_DIR,
    ):
        self.db_path = db_path
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_marts(self) -> Dict[str, Path]:
        """Generate and materialize all analytical marts to Parquet and DuckDB."""
        if not self.db_path.exists():
            raise FileNotFoundError(f"Database {self.db_path} does not exist.")

        con = duckdb.connect(str(self.db_path), read_only=True)
        try:
            # 1. Master Team Game Analytics Mart
            query_tg = """
                WITH ranked_tourneys AS (
                    SELECT 
                        tournament_id,
                        competition_id,
                        rule_set_id,
                        year,
                        official_name,
                        DENSE_RANK() OVER (ORDER BY year, tournament_id) - 1 AS tournament_seq
                    FROM dim_tournament
                    WHERE tournament_id != 'eurobasket_2025'
                )
                SELECT 
                    tg.team_game_id,
                    tg.game_id,
                    g.tournament_id,
                    rt.tournament_seq,
                    rt.year,
                    rt.competition_id,
                    rt.official_name AS tournament_name,
                    r.rule_set_id,
                    r.rule_3pt_distance_m,
                    r.lane_geometry,
                    CASE WHEN r.rule_3pt_distance_m >= 6.75 THEN 1 ELSE 0 END AS post_2010_rule,
                    CASE 
                        WHEN r.rule_3pt_distance_m >= 6.75 THEN (rt.tournament_seq - 6)
                        ELSE 0 
                    END AS time_after_2010,
                    g.game_date,
                    g.stage,
                    tg.team_id,
                    tg.opponent_id,
                    tg.is_spain,
                    tg.is_winner,
                    tg.pts,
                    (g.home_score + g.away_score - tg.pts) AS opp_pts,
                    (tg.pts - (g.home_score + g.away_score - tg.pts)) AS point_differential,
                    g.overtimes,
                    g.game_duration_seconds,
                    g.pace_40m,
                    tg.possessions_bilateral,
                    tg.fga,
                    tg.fgm,
                    tg.fg2a,
                    tg.fg2m,
                    tg.fg3a,
                    tg.fg3m,
                    tg.fta,
                    tg.ftm,
                    ROUND(CAST(tg.fg3a AS FLOAT) / NULLIF(CAST(tg.fga AS FLOAT), 0), 4) AS three_point_attempt_rate,
                    ROUND(CAST(tg.fg3m AS FLOAT) / NULLIF(CAST(tg.fg3a AS FLOAT), 0), 4) AS three_point_pct,
                    ROUND(CAST(tg.fg2m AS FLOAT) / NULLIF(CAST(tg.fg2a AS FLOAT), 0), 4) AS two_point_pct,
                    ROUND(CAST(tg.ftm AS FLOAT) / NULLIF(CAST(tg.fta AS FLOAT), 0), 4) AS free_throw_pct,
                    tg.orb,
                    tg.drb,
                    tg.trb,
                    tg.ast,
                    tg.stl,
                    tg.blk,
                    tg.tov,
                    tg.pf,
                    tg.ortg,
                    tg.drtg,
                    tg.net_rtg,
                    tg.efg_pct,
                    tg.tov_pct,
                    tg.orb_pct,
                    tg.ftr
                FROM fact_team_game tg
                JOIN fact_game g ON tg.game_id = g.game_id
                JOIN ranked_tourneys rt ON g.tournament_id = rt.tournament_id
                JOIN dim_rule_set r ON rt.rule_set_id = r.rule_set_id
                ORDER BY rt.tournament_seq, g.game_date, tg.game_id, tg.team_id
            """
            df_tg = con.execute(query_tg).df()
            tg_mart_path = self.output_dir / "mart_team_game_analytics.parquet"
            df_tg.to_parquet(tg_mart_path, index=False)

            # 2. Tournament Summary Mart
            query_ts = """
                SELECT 
                    rt.tournament_seq,
                    t.tournament_id,
                    t.official_name AS tournament_name,
                    t.year,
                    t.competition_id,
                    r.rule_set_id,
                    r.rule_3pt_distance_m,
                    CASE WHEN r.rule_3pt_distance_m >= 6.75 THEN 1 ELSE 0 END AS post_2010_rule,
                    CASE WHEN r.rule_3pt_distance_m >= 6.75 THEN (rt.tournament_seq - 6) ELSE 0 END AS time_after_2010,
                    COUNT(DISTINCT g.game_id) AS total_games,
                    COUNT(tg.team_game_id) AS total_team_observations,
                    SUM(CASE WHEN g.overtimes > 0 THEN 1 ELSE 0 END) AS ot_games,
                    ROUND(AVG(g.pace_40m), 2) AS mean_pace_40m,
                    ROUND(AVG(tg.pts), 2) AS mean_pts,
                    ROUND(AVG(tg.fga), 2) AS mean_fga,
                    ROUND(AVG(tg.fg3a), 2) AS mean_fg3a,
                    ROUND(AVG(tg.fg3m), 2) AS mean_fg3m,
                    ROUND(AVG(CAST(tg.fg3a AS FLOAT) / NULLIF(CAST(tg.fga AS FLOAT), 0)), 4) AS mean_3par,
                    ROUND(AVG(CAST(tg.fg3m AS FLOAT) / NULLIF(CAST(tg.fg3a AS FLOAT), 0)), 4) AS mean_3p_pct,
                    ROUND(AVG(tg.efg_pct), 4) AS mean_efg_pct,
                    ROUND(AVG(tg.tov_pct), 4) AS mean_tov_pct,
                    ROUND(AVG(tg.orb_pct), 4) AS mean_orb_pct,
                    ROUND(AVG(tg.ftr), 4) AS mean_ftr,
                    ROUND(AVG(tg.ortg), 2) AS mean_ortg
                FROM dim_tournament t
                JOIN (
                    SELECT tournament_id, DENSE_RANK() OVER (ORDER BY year, tournament_id) - 1 AS tournament_seq
                    FROM dim_tournament WHERE tournament_id != 'eurobasket_2025'
                ) rt ON t.tournament_id = rt.tournament_id
                JOIN dim_rule_set r ON t.rule_set_id = r.rule_set_id
                JOIN fact_game g ON t.tournament_id = g.tournament_id
                JOIN fact_team_game tg ON g.game_id = tg.game_id
                WHERE t.tournament_id != 'eurobasket_2025'
                GROUP BY rt.tournament_seq, t.tournament_id, t.official_name, t.year, t.competition_id, r.rule_set_id, r.rule_3pt_distance_m
                ORDER BY rt.tournament_seq
            """
            df_ts = con.execute(query_ts).df()
            ts_mart_path = self.output_dir / "mart_tournament_summary.parquet"
            df_ts.to_parquet(ts_mart_path, index=False)

            return {
                "mart_team_game_analytics": tg_mart_path,
                "mart_tournament_summary": ts_mart_path,
            }
        finally:
            con.close()

    def compute_mart_checksum(self) -> str:
        """Compute cryptographic hash of the generated analytical data marts."""
        tg_path = self.output_dir / "mart_team_game_analytics.parquet"
        ts_path = self.output_dir / "mart_tournament_summary.parquet"
        blob = tg_path.read_bytes() + ts_path.read_bytes()
        return hashlib.sha256(blob).hexdigest()

    def generate_documentation(self, output_path: Path = DOCS_DIR / "mvp2_data_mart.md") -> Path:
        """Generate data mart documentation."""
        tg_path = self.output_dir / "mart_team_game_analytics.parquet"
        df_tg = pd.read_parquet(tg_path)

        md = f"""# Analytical Data Mart Architecture & Data Dictionary
## International Basketball Historical Analytics (2005–2025)

**Location**: `data/04_analytics/`  
**Generated Date**: {pd.Timestamp.now().isoformat()}  
**Source Warehouse**: `data/03_validated/basketball_analytics.duckdb`  

---

## 1. Materialized Marts Overview

| Mart Name | Format | Rows | Columns | Primary Key | Description |
| :--- | :--- | :---: | :---: | :--- | :--- |
| `mart_team_game_analytics` | Parquet | {len(df_tg)} | {len(df_tg.columns)} | `team_game_id` | Core analytical feature table for game-level and team-level modeling |
| `mart_tournament_summary` | Parquet | 18 | 24 | `tournament_seq` | Longitudinal tournament time-series aggregates for ITS and macro trends |

---

## 2. Data Dictionary: `mart_team_game_analytics`

| Column Name | Type | Epistemology | Formula / Lineage | Description |
| :--- | :--- | :--- | :--- | :--- |
| `team_game_id` | String | OBSERVED | Source primary key | Unique team-game identifier |
| `game_id` | String | OBSERVED | `fact_game.game_id` | Foreign key to game record |
| `tournament_seq` | Integer | DERIVED | Dense rank (0 to 17) | Chronological tournament index |
| `year` | Integer | OBSERVED | `dim_tournament.year` | Tournament calendar year |
| `competition_id` | String | OBSERVED | `dim_tournament.competition_id` | Federation competition category |
| `rule_3pt_distance_m` | Float | OBSERVED | `dim_rule_set.rule_3pt_distance_m` | Official 3PT line distance (6.25m or 6.75m) |
| `post_2010_rule` | Integer | DERIVED | $1(\\text{{rule}} \\ge 6.75)$ | Indicator for post-2010 3PT distance era |
| `time_after_2010` | Integer | DERIVED | $\\max(0, T - 6)$ | Relative time elapsed since 2010 rule change |
| `three_point_attempt_rate` | Float | DERIVED | $\\text{{FG3A}} / \\text{{FGA}}$ | 3-Point Attempt Rate ($3\\text{{PAr}}$) |
| `three_point_pct` | Float | DERIVED | $\\text{{FG3M}} / \\text{{FG3A}}$ | 3-Point Accuracy ($3\\text{{P}}\\%$) |
| `two_point_pct` | Float | DERIVED | $\\text{{FG2M}} / \\text{{FG2A}}$ | 2-Point Accuracy ($2\\text{{P}}\\%$) |
| `free_throw_pct` | Float | DERIVED | $\\text{{FTM}} / \\text{{FTA}}$ | Free Throw Accuracy ($\\text{{FT}}\\%$) |
| `efg_pct` | Float | DERIVED | $(\\text{{FGM}} + 0.5 \\times \\text{{FG3M}}) / \\text{{FGA}}$ | Effective Field Goal Percentage |
| `tov_pct` | Float | ESTIMATED | $\\text{{TOV}} / (\\text{{FGA}} + 0.44 \\cdot \\text{{FTA}} + \\text{{TOV}})$ | Turnover Rate |
| `orb_pct` | Float | ESTIMATED | $\\text{{ORB}} / (\\text{{ORB}} + \\text{{Opp\\_DRB}})$ | Offensive Rebound Rate |
| `ftr` | Float | DERIVED | $\\text{{FTA}} / \\text{{FGA}}$ | Free Throw Rate |
| `possessions_bilateral`| Float | ESTIMATED | Dean Oliver $0.44$ Possessions | Game pace denominator |
| `ortg` | Float | ESTIMATED | $100 \\times \\text{{PTS}} / \\text{{Poss}}$ | Offensive Rating per 100 possessions |
| `drtg` | Float | ESTIMATED | $100 \\times \\text{{Opp\\_PTS}} / \\text{{Poss}}$ | Defensive Rating per 100 possessions |
| `net_rtg` | Float | ESTIMATED | $\\text{{ORtg}} - \\text{{DRtg}}$ | Net Rating per 100 possessions |

---

## 3. Provenance & Reproducibility
All transformations are 100% deterministic and execute directly against the immutable validated DuckDB warehouse.
"""
        output_path.write_text(md, encoding="utf-8")
        return output_path


def main():
    gen = DataMartGenerator()
    paths = gen.generate_marts()
    print("Marts generated:")
    for k, v in paths.items():
        print(f"  {k}: {v}")
    csum = gen.compute_mart_checksum()
    print(f"Data Mart Checksum: {csum}")
    doc_path = gen.generate_documentation()
    print(f"Data Mart Documentation written to: {doc_path}")


if __name__ == "__main__":
    main()
