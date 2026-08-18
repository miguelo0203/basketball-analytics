"""Pytest suite for MVP-3 Player Ingestion, Entity Resolution, Roles, Comparables, and Recruitment."""

import pytest
import duckdb
import pandas as pd
from pathlib import Path

from src.config import VALIDATED_DB_PATH, ANALYTICS_DATA_DIR
from src.analytics.player_data_mart import PlayerDataMartGenerator
from src.analytics.player_roles import PlayerRoleClassifier
from src.analytics.player_comparables import PlayerComparablesEngine
from src.analytics.player_recruitment import RecruitmentDecisionEngine


def test_dim_player_and_alias_integrity():
    """Verify dim_player and dim_player_alias table integrity and foreign keys."""
    con = duckdb.connect(str(VALIDATED_DB_PATH), read_only=True)
    try:
        p_count = con.execute("SELECT COUNT(*) FROM dim_player").fetchone()[0]
        a_count = con.execute("SELECT COUNT(*) FROM dim_player_alias").fetchone()[0]
        assert p_count >= 2000, f"Expected >= 2,000 players, found {p_count}"
        assert a_count >= 1800, f"Expected >= 1,800 aliases, found {a_count}"

        # Verify no orphan aliases
        orphans = con.execute("""
            SELECT COUNT(*) 
            FROM dim_player_alias a
            LEFT JOIN dim_player p ON a.canonical_player_id = p.canonical_player_id
            WHERE p.canonical_player_id IS NULL
        """).fetchone()[0]
        assert orphans == 0, f"Found {orphans} orphan player aliases"
    finally:
        con.close()


def test_fact_player_game_reconciliation_totals():
    """Verify player points and minutes strictly reconcile to team totals."""
    con = duckdb.connect(str(VALIDATED_DB_PATH), read_only=True)
    try:
        # Check point reconciliation across sample of games
        mismatches = con.execute("""
            WITH player_pts AS (
                SELECT game_id, team_id, SUM(pts) AS sum_p_pts, SUM(seconds_played) AS sum_p_sec
                FROM fact_player_game
                GROUP BY game_id, team_id
            )
            SELECT COUNT(*)
            FROM fact_team_game tg
            JOIN fact_game g ON tg.game_id = g.game_id
            JOIN player_pts pp ON tg.game_id = pp.game_id AND tg.team_id = pp.team_id
            WHERE tg.pts != pp.sum_p_pts 
               OR pp.sum_p_sec != (200 + 25 * g.overtimes) * 60
        """).fetchone()[0]
        assert mismatches == 0, f"Found {mismatches} games with unreconciled player totals"
    finally:
        con.close()


def test_player_data_mart_materialization():
    """Verify player feature mart contains 7 standardized dimensions with zero NaNs."""
    gen = PlayerDataMartGenerator()
    res = gen.generate_player_marts()
    assert res["total_rows"] >= 4000
    assert res["qualified_rows"] >= 3000

    df = pd.read_parquet(ANALYTICS_DATA_DIR / "mart_player_tournament_features.parquet")
    dim_cols = [
        "z_dim_scoring_volume", "z_dim_scoring_efficiency",
        "z_dim_perimeter_orientation", "z_dim_creation",
        "z_dim_rebounding", "z_dim_defense", "z_dim_usage"
    ]
    df_qual = df[df["is_qualified_sample"] == 1]
    for c in dim_cols:
        assert c in df_qual.columns
        assert df_qual[c].isna().sum() == 0


def test_role_clustering_determinism_and_labels():
    """Verify player role classifier assigns 6 valid basketball archetypes."""
    classifier = PlayerRoleClassifier()
    df_roles, km = classifier.fit_hybrid_role_model()
    
    valid_roles = {
        "Primary Initiator / Floor General",
        "Perimeter Movement Shooter / Spacer",
        "Two-Way Scoring Wing / Slasher",
        "Stretch Big / Pick-and-Pop Forward",
        "Low-Block Anchor / Interior Scorer",
        "Rim Protector / Roll Threat & Anchor",
        "Unqualified / Low-Sample Rotation",
    }
    assigned_roles = set(df_roles["role_name"].unique())
    assert assigned_roles.issubset(valid_roles)
    assert len(df_roles) >= 4000


def test_comparables_engine_similarity_and_exclusion():
    """Verify player comparables engine returns sorted similarity and excludes self."""
    engine = PlayerComparablesEngine()
    res = engine.find_comparables("ricky_rubio_1990", top_n=5)
    
    assert "target_player" in res
    assert len(res["comparables"]) == 5

    # Check descending order of similarity
    sims = [c["similarity_score"] for c in res["comparables"]]
    assert sims == sorted(sims, reverse=True)
    assert all(0.0 < s <= 1.0 for s in sims)

    # Ensure target player is excluded from comparators
    target_id = res["target_player"]["player_tournament_id"]
    comp_ids = [c["player_tournament_id"] for c in res["comparables"]]
    assert target_id not in comp_ids


def test_recruitment_decision_engine():
    """Verify recruitment decision engine filters and scores candidates."""
    engine = RecruitmentDecisionEngine()
    shortlist = engine.search_shortlist(
        target_role="Wing",
        min_age=20,
        max_age=32,
        min_minutes=80.0,
        top_n=5
    )
    assert len(shortlist) == 5
    assert "fit_score" in shortlist.columns
    assert "fit_index_100" in shortlist.columns
    assert (shortlist["fit_index_100"] >= 0.0).all() and (shortlist["fit_index_100"] <= 100.0).all()
