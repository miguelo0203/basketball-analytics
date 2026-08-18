"""Tests for configuration files and directory paths."""

import pytest
import pandas as pd
from src.config import (
    TOURNAMENTS_CSV,
    RULE_SETS_CSV,
    SOURCES_YAML,
    TEAMS_CSV,
    ensure_directories_exist,
)
from src.domain.rulesets import RuleSetRegistry


def test_ensure_directories_exist():
    ensure_directories_exist()
    assert TOURNAMENTS_CSV.parent.exists()


def test_tournaments_registry_integrity():
    assert TOURNAMENTS_CSV.exists(), "tournaments.csv must exist"
    df = pd.read_csv(TOURNAMENTS_CSV)
    assert len(df) == 19, f"Expected exactly 19 verified tournaments, found {len(df)}"
    assert set(df["verification_status"]) == {"VERIFIED"}
    assert df["official_game_count"].sum() == 1221, f"Expected 1,221 total games across all 19 tournaments (1145 historical + 76 future), found {df['official_game_count'].sum()}"


def test_rule_sets_registry_integrity():
    assert RULE_SETS_CSV.exists()
    registry = RuleSetRegistry()
    rules = registry.all()
    assert "fiba_2005_2010" in rules
    assert "fiba_2011_2013" in rules
    assert "fiba_2014_present" in rules

    # Verify 3PT distances
    assert rules["fiba_2005_2010"].rule_3pt_distance_m == 6.25
    assert rules["fiba_2011_2013"].rule_3pt_distance_m == 6.75
    assert rules["fiba_2014_present"].shot_clock_orb_seconds == 14
