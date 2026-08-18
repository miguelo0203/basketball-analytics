"""DuckDB database manager for schema migration and reference data loading."""

import duckdb
import pandas as pd
from pathlib import Path
from typing import Optional
from src.config import (
    STAGING_DB_PATH,
    VALIDATED_DB_PATH,
    TOURNAMENTS_CSV,
    RULE_SETS_CSV,
    SOURCES_YAML,
    TEAMS_CSV,
)
from src.storage.schema import STAGING_SCHEMA_DDL, VALIDATED_SCHEMA_DDL


class DatabaseManager:
    """Manager for DuckDB connections and automated migrations."""

    def __init__(self, db_path: Optional[Path] = None, read_only: bool = False):
        self.db_path = str(db_path or VALIDATED_DB_PATH)
        self.read_only = read_only

    def get_connection(self) -> duckdb.DuckDBPyConnection:
        """Create or get a DuckDB connection."""
        return duckdb.connect(self.db_path, read_only=self.read_only)

    def initialize_schema(self, is_staging: bool = False) -> None:
        """Execute DDL statements to set up all tables."""
        ddl = STAGING_SCHEMA_DDL if is_staging else VALIDATED_SCHEMA_DDL
        with self.get_connection() as con:
            con.execute(ddl)

    def load_master_dimensions(self) -> None:
        """Load tournaments, rulesets, teams, and sources from verified config files."""
        with self.get_connection() as con:
            # 1. Load Rule Sets
            if RULE_SETS_CSV.exists():
                df_rules = pd.read_csv(RULE_SETS_CSV)
                con.execute("""
                    INSERT OR IGNORE INTO dim_rule_set
                    SELECT 
                        rule_set_id,
                        CAST(effective_from AS DATE),
                        CAST(effective_to AS DATE),
                        rule_3pt_distance_m,
                        shot_clock_seconds,
                        shot_clock_orb_seconds,
                        lane_geometry,
                        no_charge_semicircle,
                        game_duration_minutes,
                        ot_duration_minutes,
                        description
                    FROM df_rules
                """)

            # 2. Load Competitions
            con.execute("""
                INSERT OR IGNORE INTO dim_competition VALUES
                ('fiba_eurobasket', 'FIBA EuroBasket', 'FIBA', 4),
                ('fiba_world_cup', 'FIBA World Cup', 'FIBA', 4),
                ('olympics_basketball', 'Olympic Games', 'IOC', 4)
            """)

            # 3. Load Tournaments
            if TOURNAMENTS_CSV.exists():
                df_tourneys = pd.read_csv(TOURNAMENTS_CSV)
                con.execute("""
                    INSERT OR IGNORE INTO dim_tournament
                    SELECT 
                        tournament_id,
                        CASE 
                            WHEN competition = 'FIBA EuroBasket' THEN 'fiba_eurobasket'
                            WHEN competition = 'FIBA World Cup' THEN 'fiba_world_cup'
                            ELSE 'olympics_basketball'
                        END AS competition_id,
                        rule_set_id,
                        year,
                        official_name,
                        host,
                        number_of_teams,
                        CAST(actual_start_date AS DATE),
                        CAST(actual_end_date AS DATE)
                    FROM df_tourneys
                """)

            # 4. Load Teams
            if TEAMS_CSV.exists():
                df_teams = pd.read_csv(TEAMS_CSV)
                con.execute("INSERT OR IGNORE INTO dim_team SELECT * FROM df_teams")

            # 5. Load Sources
            con.execute("""
                INSERT OR IGNORE INTO dim_source VALUES
                ('SRC_FIBA_ARCHIVE', 'FIBA Archive', 'https://archive.fiba.com', 'official_archive', 1),
                ('SRC_FIBA_MODERN', 'FIBA Modern API', 'https://www.fiba.basketball', 'official_api', 1),
                ('SRC_FIBA_LIVESTATS', 'FIBA LiveStats', 'https://fibalivestats.dcd.shared.geniussports.com', 'official_telemetry', 1),
                ('SRC_BREF', 'Basketball-Reference', 'https://www.basketball-reference.com/international', 'secondary_structured', 2),
                ('SRC_FEB', 'FEB Archive', 'https://www.feb.es', 'official_federation', 2),
                ('SRC_IOC', 'IOC Results', 'https://olympics.com', 'official_olympic', 1),
                ('SRC_WIKI_ARCHIVE', 'Wikipedia Match Archives', 'https://en.wikipedia.org', 'secondary_structured', 2)
            """)
