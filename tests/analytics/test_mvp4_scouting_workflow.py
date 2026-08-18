"""Pytest suite for MVP-4 Scouting Decision-Support, Candidate Universe, Robustness, and Blind Tests."""

import pytest
import pandas as pd
import numpy as np

from src.config import ANALYTICS_DATA_DIR
from src.analytics.mvp4_decision_support import ScoutingDecisionSupportEngine


@pytest.fixture(scope="module")
def engine():
    return ScoutingDecisionSupportEngine()


def test_candidate_universe_audit_counts(engine):
    """Verify candidate universe total, eligible, and excluded counts."""
    audit = engine.get_candidate_universe_audit()
    assert audit["total_campaigns"] == 4350
    assert audit["eligible_campaigns"] == 3767
    assert audit["excluded_campaigns"] == 583
    assert audit["exclusion_breakdown"]["low_minutes_under_40"] == 583


def test_reliability_tier_assignment(engine):
    """Verify all player campaigns have a valid reliability tier."""
    df = engine.df
    valid_tiers = {"HIGH RELIABILITY", "MODERATE RELIABILITY", "LIMITED SAMPLE", "INSUFFICIENT SAMPLE"}
    assert set(df["reliability_tier"].unique()).issubset(valid_tiers)
    
    # Check consistency of rules
    high_rel = df[df["reliability_tier"] == "HIGH RELIABILITY"]
    assert (high_rel["total_minutes"] >= 150.0).all()
    assert (high_rel["games_played"] >= 6).all()


def test_context_normalization_zscores(engine):
    """Verify tournament-relative Z-scores are computed cleanly."""
    df = engine.df
    assert "z_tourney_ts_pct" in df.columns
    assert "z_tourney_three_point_rate" in df.columns
    assert "pctile_ts_pct" in df.columns
    assert df["z_tourney_ts_pct"].isna().sum() == 0


def test_recruitment_workflow_cases_execution(engine):
    """Verify execution of Case A, Case B, and Case C recruitment workflows."""
    # Case A
    res_a = engine.execute_recruitment_workflow(
        case_name="Case A: Secondary Creation Wing",
        target_roles=["Wing", "Spacer"],
        min_age=20, max_age=32, min_height=192,
        mandatory_filters={"three_point_rate": 0.35, "ts_pct": 0.50, "ast_pct_est": 0.10, "stl_per_40": 0.8},
        weights={"z_dim_perimeter_orientation": 1.2, "z_dim_creation": 1.2, "z_dim_scoring_efficiency": 1.1, "z_dim_defense": 1.1, "z_dim_scoring_volume": 0.8},
        min_minutes=80.0
    )
    assert res_a["stage1_initial_count"] == 20
    assert res_a["stage2_shortlist_count"] == 10
    assert res_a["stage3_final_count"] == 5
    assert len(res_a["stage3_dossiers"]) == 5

    # Case B
    res_b = engine.execute_recruitment_workflow(
        case_name="Case B: Defensive / Spacing Guard",
        target_roles=["Spacer", "Initiator"],
        min_age=20, max_age=32, min_height=180,
        mandatory_filters={"three_point_rate": 0.45, "ts_pct": 0.52, "stl_per_40": 1.0},
        weights={"z_dim_perimeter_orientation": 1.5, "z_dim_scoring_efficiency": 1.3, "z_dim_defense": 1.3, "z_dim_creation": 0.6, "z_dim_scoring_volume": 0.8},
        min_minutes=80.0
    )
    assert res_b["stage3_final_count"] == 5

    # Case C
    res_c = engine.execute_recruitment_workflow(
        case_name="Case C: Stretch / Connector Forward",
        target_roles=["Stretch Big", "Interior"],
        min_age=21, max_age=34, min_height=202,
        mandatory_filters={"three_point_rate": 0.25, "ts_pct": 0.52},
        weights={"z_dim_perimeter_orientation": 1.3, "z_dim_rebounding": 1.3, "z_dim_scoring_efficiency": 1.2, "z_dim_defense": 0.8, "z_dim_scoring_volume": 0.9},
        min_minutes=80.0
    )
    assert res_c["stage3_final_count"] == 5


def test_dossier_required_structure(engine):
    """Verify that every final candidate dossier contains all required keys and evidence."""
    res = engine.execute_recruitment_workflow(
        case_name="Test Case",
        target_roles=["Wing", "Spacer"],
        min_age=20, max_age=34, min_height=190,
        mandatory_filters={"three_point_rate": 0.30},
        weights={"z_dim_scoring_volume": 1.0, "z_dim_perimeter_orientation": 1.0},
        min_minutes=60.0
    )
    dossiers = res["stage3_dossiers"]
    assert len(dossiers) >= 1
    required_keys = {
        "rank", "player_tournament_id", "canonical_player_id", "full_canonical_name",
        "team_id", "tournament_id", "year", "player_age", "height_cm", "role_name",
        "reliability_tier", "fit_index_100", "metrics", "strengths", "risks",
        "top_comparables", "recommendation"
    }
    for d in dossiers:
        assert required_keys.issubset(set(d.keys()))
        assert len(d["strengths"]) >= 1
        assert len(d["risks"]) >= 1
        assert d["recommendation"] in {"PRIORITY SCOUT", "SCOUT", "MONITOR"}


def test_shortlist_robustness_stability_classification(engine):
    """Verify shortlist stability matrix and classifications."""
    names = ["Bogdan Bogdanović", "Rudy Fernández", "Luka Dončić"]
    df_stab = engine.evaluate_shortlist_robustness("Case A", ["Wing"], names)
    assert len(df_stab) == len(names)
    assert "Stability_Classification" in df_stab.columns
    valid_classes = {"HIGHLY STABLE", "STABLE", "SENSITIVE", "HIGHLY SENSITIVE"}
    assert set(df_stab["Stability_Classification"].unique()).issubset(valid_classes)


def test_blind_validation_experiment(engine):
    """Verify blind validation experiment runs without reputation bias."""
    res = engine.run_blind_validation_experiment()
    assert res["total_blind_cases"] >= 4
    for r in res["results"]:
        assert r["reputation_bias_detected"] is False
        assert r["validation_status"] == "SUCCESSFUL ROLE IDENTIFICATION"
        assert r["comparator_similarity"] > 0.80
