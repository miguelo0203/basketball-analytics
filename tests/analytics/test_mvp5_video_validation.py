"""Pytest suite for MVP-5 Video Tactical Validation, Inter-Rater Reliability, and Scouting Briefs."""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path

from src.config import ANALYTICS_DATA_DIR, REPORTS_DIR
from src.analytics.mvp5_tactical_validation import TacticalValidationEngine


@pytest.fixture(scope="module")
def engine():
    return TacticalValidationEngine()


def test_video_observations_schema_and_counts(engine):
    """Verify video observations table schema, row counts, and null timestamp ethics."""
    df_obs = engine.df_obs
    assert len(df_obs) >= 300, f"Expected >= 300 observations, found {len(df_obs)}"

    required_cols = {
        "observation_id", "player_tournament_id", "canonical_player_id", "tier",
        "tournament_id", "game_id", "quarter", "timestamp_start", "timestamp_end",
        "action_type", "role_category", "observed_behavior", "quality_score",
        "confidence", "supporting_note", "analyst_id"
    }
    assert required_cols.issubset(set(df_obs.columns))

    # Verify timestamps are explicitly NULL (no fabrication)
    assert df_obs["timestamp_start"].isna().all()
    assert df_obs["timestamp_end"].isna().all()


def test_valid_categorical_rubric_values(engine):
    """Verify all qualitative observations conform strictly to the standardized YAML rubric."""
    df_obs = engine.df_obs
    valid_behaviors = {"YES", "NO", "MIXED", "NOT_OBSERVED"}
    assert set(df_obs["observed_behavior"].unique()).issubset(valid_behaviors)

    valid_scores = {0, 1, 2, 3, 4}
    assert set(df_obs["quality_score"].unique()).issubset(valid_scores)

    valid_conf = {"HIGH", "MEDIUM", "LOW"}
    assert set(df_obs["confidence"].unique()).issubset(valid_conf)


def test_inter_rater_reliability_statistics(engine):
    """Verify inter-rater reliability double coding exceeds 20% and achieves high Cohen's Kappa."""
    irr = engine.compute_inter_rater_reliability()
    assert irr["status"] == "DOUBLE_CODED_VALIDATION_COMPLETE"
    assert irr["pct_of_total_observations"] >= 20.0
    assert irr["cohens_kappa_categorical"] >= 0.80
    assert irr["cohens_kappa_ordinal_weighted"] >= 0.70


def test_quantitative_qualitative_agreement_logic(engine):
    """Verify player-level validation results and agreement status classifications."""
    df_res = engine.compute_validation_results()
    assert len(df_res) >= 14
    valid_agreements = {"STRONG", "PARTIAL", "CONTRADICTORY"}
    assert set(df_res["agreement_status"].unique()).issubset(valid_agreements)
    assert (df_res["observed_tactical_quality"] >= 0.0).all()
    assert (df_res["observed_tactical_quality"] <= 4.0).all()


def test_agreement_matrix_and_hypotheses(engine):
    """Verify agreement matrix includes both Archetype breakdown and 4 tactical hypotheses."""
    df_matrix = engine.compute_agreement_matrix()
    assert len(df_matrix) >= 5
    cat_types = set(df_matrix["category_type"].unique())
    assert "Archetype" in cat_types
    assert "Hypothesis" in cat_types

    # Verify all 4 hypotheses present
    hyp_names = " ".join(df_matrix[df_matrix["category_type"] == "Hypothesis"]["category_name"].tolist())
    assert "H1: Closeout Attack Quality" in hyp_names
    assert "H2: P&R Read Manipulation" in hyp_names
    assert "H3: On-Ball Screen Navigation" in hyp_names
    assert "H4: Pick-and-Pop Depth" in hyp_names


def test_tier_a_player_briefs_generation(engine):
    """Verify generation and markdown structure of Tier A priority scouting briefs."""
    briefs = engine.generate_tier_a_player_briefs()
    assert len(briefs) == 5
    for b_path in briefs:
        assert b_path.exists()
        text = b_path.read_text(encoding="utf-8")
        assert "Quantitative Baseline & Analytical Profile" in text
        assert "Video Tactical Validation Summary" in text
        assert "Evidence-Backed Tactical Strengths" in text
        assert "Specific Questions for Live / Tape Scouting" in text
        assert "SCOUTING RECOMMENDATION" in text


def test_blind_validation_concordance(engine):
    """Verify blind validation sample cases are present and successfully evaluated."""
    df_res = engine.compute_validation_results()
    blind_cases = df_res[df_res["tier"] == "TIER_C_BLIND"]
    assert len(blind_cases) == 4
    for _, r in blind_cases.iterrows():
        assert r["agreement_status"] in {"STRONG", "PARTIAL"}
        assert r["observed_tactical_quality"] >= 2.8


def test_deterministic_reproducibility(engine):
    """Verify that repeating the validation workflow produces identical results."""
    df1 = engine.compute_validation_results()
    df2 = engine.compute_validation_results()
    pd.testing.assert_frame_equal(df1, df2)
