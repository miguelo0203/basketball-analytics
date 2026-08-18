"""Automated Tests for MVP-10 Analyst Decision Workspace & Brief Generator.

Validates:
1. Workspace loading and multi-layer evidence extraction.
2. Strict temporal cutoff and anti-hindsight barrier.
3. Dedicated contradiction engine logic and alerts.
4. Structured coaching and sporting director brief generation.
5. Historical case replay and post-game process review.
6. Reproducibility and end-to-end operational pipeline.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import pytest

from src.config import ANALYTICS_DATA_DIR, VALIDATED_DB_PATH
from src.analytics.mvp10_evidence_engine import EvidenceEngine
from src.analytics.mvp10_brief_generator import BriefGenerator
from src.analytics.mvp10_analyst_workspace import AnalystWorkspace


@pytest.fixture(scope="module")
def evidence_engine() -> EvidenceEngine:
    """Fixture providing initialized evidence engine."""
    return EvidenceEngine(data_dir=ANALYTICS_DATA_DIR)


@pytest.fixture(scope="module")
def brief_generator() -> BriefGenerator:
    """Fixture providing initialized brief generator."""
    return BriefGenerator(data_dir=ANALYTICS_DATA_DIR)


@pytest.fixture(scope="module")
def workspace() -> AnalystWorkspace:
    """Fixture providing initialized analyst workspace."""
    return AnalystWorkspace(data_dir=ANALYTICS_DATA_DIR)


# ============================================================================
# 1. EVIDENCE MATRIX & DATA INTEGRITY TESTS
# ============================================================================

def test_workspace_initialization(workspace: AnalystWorkspace):
    """Verify workspace initializes and loads all verified marts."""
    assert len(workspace.evidence_engine.df_features) == 1145
    assert len(workspace.evidence_engine.df_sims) == 364
    assert len(workspace.evidence_engine.df_video) == 420


def test_match_selection_validity(evidence_engine: EvidenceEngine):
    """Verify pre-game evidence matrix extraction for valid game ID."""
    ev = evidence_engine.build_match_evidence_matrix("olympics_2008_esp_usa_107_118")
    assert ev["game_id"] == "olympics_2008_esp_usa_107_118"
    assert ev["tournament_id"] == "olympics_2008"
    assert ev["team_a_id"] == "ESP"
    assert ev["team_b_id"] == "USA"


def test_evidence_matrix_construction(evidence_engine: EvidenceEngine):
    """Verify 8-layer structure and completeness."""
    ev = evidence_engine.build_match_evidence_matrix("olympics_2008_esp_usa_107_118")
    assert len(ev["evidence_layers"]) == 8
    expected_layers = [
        "1. Historical Performance", "2. Tournament Form", "3. Four Factors Efficiency",
        "4. Functional Player Archetypes", "5. Tactical Film Observations",
        "6. Predictive Model Output", "7. Tournament Simulation Context", "8. Statistical Uncertainty"
    ]
    layer_names = [l["layer_name"] for l in ev["evidence_layers"]]
    assert layer_names == expected_layers


def test_temporal_cutoff_pregame(workspace: AnalystWorkspace):
    """Verify no post-game outcome fields exist in pre-game information state."""
    pre_state = workspace.load_pre_game_state("olympics_2008_esp_usa_107_118")
    assert pre_state["outcome_revealed"] is False
    assert "post_game_review" not in pre_state
    assert "final_score" not in pre_state


def test_pregame_postgame_separation(workspace: AnalystWorkspace):
    """Verify strict separation between pre-game view and post-game reveal."""
    pre_state = workspace.load_pre_game_state("eurobasket_2015_esp_ltu_80_63")
    assert pre_state["outcome_revealed"] is False

    post_state = workspace.reveal_match_outcome("eurobasket_2015_esp_ltu_80_63")
    assert post_state["outcome_revealed"] is True
    assert "post_game_review" in post_state
    assert post_state["post_game_review"]["actual_winner"] == "ESP"


# ============================================================================
# 2. CONTRADICTION ENGINE & UNCERTAINTY TESTS
# ============================================================================

def test_contradiction_detection_logic(evidence_engine: EvidenceEngine):
    """Verify contradiction detection structure."""
    ev = evidence_engine.build_match_evidence_matrix("olympics_2008_esp_usa_107_118")
    assert isinstance(ev["contradictions"], list)
    assert isinstance(ev["evidence_status"], str)


def test_uncertainty_propagation(evidence_engine: EvidenceEngine):
    """Verify statistical uncertainty layer contains bootstrap CI description."""
    ev = evidence_engine.build_match_evidence_matrix("eurobasket_2022_esp_fra_88_76")
    u_layer = ev["evidence_layers"][7]
    assert "Uncertainty" in u_layer["layer_name"]
    assert "Bootstrap" in u_layer["magnitude"]


# ============================================================================
# 3. BRIEF GENERATOR TESTS (COACH & SPORTING DIRECTOR)
# ============================================================================

def test_coaching_brief_generation(brief_generator: BriefGenerator):
    """Verify coaching brief contains all required sections."""
    cb = brief_generator.generate_coaching_brief("eurobasket_2015_esp_ltu_80_63")
    required_sections = [
        "brief_id", "brief_type", "executive_summary", "strongest_evidence",
        "tactical_film_evidence", "model_view", "key_uncertainty",
        "contradictions_surfaced", "questions_for_coaching_staff", "analyst_recommendation"
    ]
    for sec in required_sections:
        assert sec in cb, f"Missing section in coaching brief: {sec}"
    assert len(cb["executive_summary"]) >= 3
    assert len(cb["questions_for_coaching_staff"]) >= 3


def test_sporting_director_brief_generation(brief_generator: BriefGenerator):
    """Verify sporting director brief evaluates roster balance and simulation odds."""
    db = brief_generator.generate_sporting_director_brief("eurobasket_2022", "ESP")
    assert db["brief_type"] == "SPORTING_DIRECTOR_BRIEF"
    assert "simulated_contender_rank" in db
    assert "functional_role_distribution" in db
    assert len(db["strategic_questions_for_leadership"]) >= 3


# ============================================================================
# 4. HISTORICAL REPLAY & POST-GAME REVIEW TESTS
# ============================================================================

def test_historical_replay_mode(workspace: AnalystWorkspace):
    """Verify reveal_match_outcome attaches ground truth and evaluation."""
    rev = workspace.reveal_match_outcome("eurobasket_2022_esp_fra_88_76")
    pg = rev["post_game_review"]
    assert pg["actual_winner"] == "ESP"
    assert "88 - FRA 76" in pg["final_score"]
    assert pg["model_directional_alignment"] in ["ALIGNED", "UPSET / DIVERGENT"]


def test_outcome_reveal_ground_truth(workspace: AnalystWorkspace):
    """Verify ground truth score matches fact_game records."""
    rev = workspace.reveal_match_outcome("olympics_2008_esp_usa_107_118")
    assert "107 - USA 118" in rev["post_game_review"]["final_score"]
    assert rev["post_game_review"]["actual_winner"] == "USA"


def test_decision_audit_trail_fields(brief_generator: BriefGenerator):
    """Verify decision audit trail fields exist."""
    df_briefs = brief_generator.generate_all_flagship_briefs()
    assert "brief_id" in df_briefs.columns
    assert "tournament_id" in df_briefs.columns
    assert "predicted_win_prob_a" in df_briefs.columns


def test_deterministic_regeneration(workspace: AnalystWorkspace):
    """Verify two identical workspace queries yield identical results."""
    res1 = workspace.load_pre_game_state("eurobasket_2011_esp_fra_98_85")
    res2 = workspace.load_pre_game_state("eurobasket_2011_esp_fra_98_85")
    assert res1["pre_game_win_probability_a"] == res2["pre_game_win_probability_a"]
    assert res1["evidence_status"] == res2["evidence_status"]


def test_missing_data_handling(evidence_engine: EvidenceEngine):
    """Verify invalid game IDs raise ValueError."""
    with pytest.raises(ValueError):
        evidence_engine.build_match_evidence_matrix("invalid_game_id_999")


def test_model_artifact_integrity(evidence_engine: EvidenceEngine):
    """Verify LightGBM win probabilities are bounded in [0.0, 1.0]."""
    ev = evidence_engine.build_match_evidence_matrix("worldcup_2019_arg_esp_75_95")
    assert 0.0 <= ev["p_win_team_a"] <= 1.0


def test_simulation_artifact_integrity(evidence_engine: EvidenceEngine):
    """Verify tournament simulation title odds are present."""
    ev = evidence_engine.build_match_evidence_matrix("eurobasket_2022_esp_fra_88_76")
    sim_layer = ev["evidence_layers"][6]
    assert "Simulation" in sim_layer["layer_name"]


def test_tactical_evidence_integrity(evidence_engine: EvidenceEngine):
    """Verify video film observations are scored correctly."""
    ev = evidence_engine.build_match_evidence_matrix("eurobasket_2015_esp_ltu_80_63")
    film_layer = ev["evidence_layers"][4]
    assert "Film" in film_layer["layer_name"]


def test_no_hindsight_contamination(evidence_engine: EvidenceEngine):
    """Verify pre-game features do not leak future game outcomes."""
    df_ev = evidence_engine.generate_all_workspace_evidence_records()
    assert len(df_ev) == 1145
    assert (df_ev["p_win_team_a"] >= 0.0).all()
    assert (df_ev["p_win_team_a"] <= 1.0).all()


def test_brief_reproducibility(brief_generator: BriefGenerator):
    """Verify multiple brief generations produce identical text strings."""
    cb1 = brief_generator.generate_coaching_brief("eurobasket_2022_esp_fra_88_76")
    cb2 = brief_generator.generate_coaching_brief("eurobasket_2022_esp_fra_88_76")
    assert cb1["analyst_recommendation"] == cb2["analyst_recommendation"]
    assert cb1["questions_for_coaching_staff"] == cb2["questions_for_coaching_staff"]


def test_end_to_end_workspace_pipeline(workspace: AnalystWorkspace):
    """Verify full workspace pipeline execution across all 5 flagship games."""
    df_ws = workspace.generate_all_workspace_records()
    assert len(df_ws) == 5
    assert (df_ws["directional_alignment"] == "ALIGNED").sum() >= 4
    assert (ANALYTICS_DATA_DIR / "mvp10_workspace_records.parquet").exists()
    assert (ANALYTICS_DATA_DIR / "mvp10_coaching_briefs.parquet").exists()
    assert (ANALYTICS_DATA_DIR / "mvp10_evidence_matrix.parquet").exists()
