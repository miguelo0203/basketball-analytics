"""Tests for DuckDB schema creation and master dimensions loading."""

import pytest
import duckdb
from src.storage.db import DatabaseManager


def test_schema_initialization_and_master_dimensions(tmp_path):
    test_db = tmp_path / "test_basketball.duckdb"
    db_manager = DatabaseManager(db_path=test_db)

    # Initialize production schema
    db_manager.initialize_schema(is_staging=False)
    # Load master dimensions
    db_manager.load_master_dimensions()

    with db_manager.get_connection() as con:
        # Check tournaments table
        tourneys_count = con.execute("SELECT COUNT(*) FROM dim_tournament").fetchone()[0]
        assert tourneys_count == 19, f"Expected 19 tournaments loaded, found {tourneys_count}"

        # Check rulesets table
        rules_count = con.execute("SELECT COUNT(*) FROM dim_rule_set").fetchone()[0]
        assert rules_count == 3

        # Check teams table
        teams_count = con.execute("SELECT COUNT(*) FROM dim_team").fetchone()[0]
        assert teams_count > 50

        # Check sources table
        sources_count = con.execute("SELECT COUNT(*) FROM dim_source").fetchone()[0]
        assert sources_count == 7
