import sys
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import duckdb
import pandas as pd

from src.config import VALIDATED_DB_PATH, ANALYTICS_DATA_DIR


def verify_cross_language_metrics():
    con = duckdb.connect(str(VALIDATED_DB_PATH), read_only=True)
    
    # 1. Total Tournaments
    n_tournaments = con.execute("SELECT COUNT(*) FROM dim_tournament").fetchone()[0]
    
    # 2. Total Games
    n_games = con.execute("SELECT COUNT(*) FROM fact_game").fetchone()[0]
    
    # 3. Total Team Games
    n_team_games = con.execute("SELECT COUNT(*) FROM fact_team_game").fetchone()[0]
    
    # 4. Total Player Games
    n_player_games = con.execute("SELECT COUNT(*) FROM fact_player_game").fetchone()[0]
    
    # 5. Qualified Campaigns in mart_player_roles
    roles_path = PROJECT_ROOT / "data" / "04_analytics" / "mart_player_roles.parquet"
    if roles_path.exists():
        roles_df = pd.read_parquet(roles_path)
        n_qualified_campaigns = len(roles_df)
    else:
        n_qualified_campaigns = con.execute("SELECT COUNT(*) FROM fact_player_tournament WHERE total_minutes >= 40").fetchone()[0]
        
    # 6. Team-level Averages
    team_metrics = con.execute("""
        SELECT 
            AVG((fgm + 0.5 * fg3m) * 1.0 / NULLIF(fga, 0)) as avg_efg,
            AVG(fga + 0.44 * fta - orb + tov) as avg_pace,
            AVG(fg3a * 1.0 / NULLIF(fga, 0)) as avg_3par
        FROM fact_team_game
    """).df()
    
    avg_efg = team_metrics['avg_efg'].iloc[0]
    avg_pace = team_metrics['avg_pace'].iloc[0]
    avg_3par = team_metrics['avg_3par'].iloc[0]
    
    con.close()
    
    print("================================================================================")
    print("PYTHON <-> DUCKDB CANONICAL METRICS")
    print("================================================================================")
    print(f"Torneos Oficiales:        {n_tournaments}")
    print(f"Partidos Totales:         {n_games}")
    print(f"Observaciones de Equipo:  {n_team_games}")
    print(f"Actuaciones de Jugador:   {n_player_games}")
    print(f"Campanas Cualificadas:    {n_qualified_campaigns}")
    print(f"eFG% Promedio Global:     {avg_efg:.4f}")
    print(f"Ritmo Promedio (Pace):    {avg_pace:.2f}")
    print(f"Tasa de Triples (3PAR):   {avg_3par:.4f}")
    print("================================================================================")


if __name__ == "__main__":
    verify_cross_language_metrics()
