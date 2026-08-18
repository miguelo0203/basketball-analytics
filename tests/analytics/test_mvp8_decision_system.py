"""Automated Tests for MVP-8 End-to-End Analyst Decision System & Historical Decision Validation.

Validates:
1. Decision engine data ingestion across all 6 upstream layers.
2. Multi-criteria recommendation score mathematical bounds [0, 100].
3. Sample reliability tiering and confidence classification.
4. Qualitative film validation and contradiction detection logic.
5. Historical decision scenario reconstruction and baseline comparison.
6. Determinism and reproducibility across repeated evaluations.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import pytest

from src.config import ANALYTICS_DATA_DIR
from src.analytics.mvp8_decision_system import AnalystDecisionEngine
from src.analytics.mvp8_historical_validation import HistoricalDecisionValidator


@pytest.fixture(scope="module")
def decision_engine() -> AnalystDecisionEngine:
    """Fixture providing initialized analyst decision engine."""
    return AnalystDecisionEngine(seed=42)


@pytest.fixture(scope="module")
def validator() -> HistoricalDecisionValidator:
    """Fixture providing initialized historical decision validator."""
    return HistoricalDecisionValidator()


# ============================================================================
# 1. DATA INGESTION & DOSSIER STRUCTURE TESTS
# ============================================================================

def test_decision_engine_initialization(decision_engine: AnalystDecisionEngine):
    """Verify engine initializes and loads all 5 analytical marts."""
    assert len(decision_engine.df_player_feats) == 4350
    assert len(decision_engine.df_roles) == 4350
    assert len(decision_engine.df_team_analytics) == 2290
    assert len(decision_engine.df_sims) == 364
    assert len(decision_engine.df_video) == 420


def test_decision_dossier_structure(decision_engine: AnalystDecisionEngine):
    """Verify single candidate evaluation produces complete 21-column dictionary."""
    dos = decision_engine.evaluate_player_decision_dossier(
        "eurobasket_2015_ESP_pau_gasol_1980",
        "Low-Block Anchor / Interior Scorer",
        "ESP",
        "eurobasket_2015",
    )
    required_keys = [
        "player_tournament_id", "full_canonical_name", "team_id", "tournament_id",
        "target_role", "assigned_role", "total_minutes", "pts_per_40", "ts_pct",
        "sample_reliability_tier", "role_fit_score", "film_observations_count",
        "film_quality_score", "film_contradiction_detected", "predictive_net_impact",
        "simulated_title_prob", "simulated_contender_rank", "recommendation_score",
        "confidence_tier", "recommendation_status"
    ]
    for k in required_keys:
        assert k in dos, f"Missing key in decision dossier: {k}"


# ============================================================================
# 2. MATHEMATICAL BOUNDS & CLASSIFICATION LOGIC TESTS
# ============================================================================

def test_recommendation_score_bounds(decision_engine: AnalystDecisionEngine):
    """Verify recommendation score is strictly bounded in [0.0, 100.0]."""
    df_dos = decision_engine.generate_all_flagship_dossiers()
    assert (df_dos["recommendation_score"] >= 0.0).all()
    assert (df_dos["recommendation_score"] <= 100.0).all()


def test_sample_reliability_classification(decision_engine: AnalystDecisionEngine):
    """Verify minute-based sample reliability classifications."""
    # Gasol 2015 played > 200m -> High Reliability
    dos_gasol = decision_engine.evaluate_player_decision_dossier(
        "eurobasket_2015_ESP_pau_gasol_1980", "Low-Block Anchor / Interior Scorer", "ESP", "eurobasket_2015"
    )
    assert "High Reliability" in dos_gasol["sample_reliability_tier"]


def test_video_evidence_integration(decision_engine: AnalystDecisionEngine):
    """Verify that video observations are attached and scored."""
    dos_gasol = decision_engine.evaluate_player_decision_dossier(
        "eurobasket_2015_ESP_pau_gasol_1980", "Low-Block Anchor / Interior Scorer", "ESP", "eurobasket_2015"
    )
    assert dos_gasol["film_observations_count"] > 0
    assert dos_gasol["film_quality_score"] > 0.0
    assert isinstance(dos_gasol["film_contradiction_detected"], bool)


def test_predictive_impact_contribution(decision_engine: AnalystDecisionEngine):
    """Verify predictive impact computation."""
    dos = decision_engine.evaluate_player_decision_dossier(
        "eurobasket_2022_ESP_lorenzo_brown_1990", "Primary Initiator / Floor General", "ESP", "eurobasket_2022"
    )
    assert isinstance(dos["predictive_net_impact"], float)


def test_simulation_title_prob_extraction(decision_engine: AnalystDecisionEngine):
    """Verify title probability is extracted from MVP-7 simulations."""
    dos = decision_engine.evaluate_player_decision_dossier(
        "eurobasket_2022_ESP_lorenzo_brown_1990", "Primary Initiator / Floor General", "ESP", "eurobasket_2022"
    )
    assert dos["simulated_title_prob"] > 0.50
    assert dos["simulated_contender_rank"] == 1


def test_confidence_tier_assignment(decision_engine: AnalystDecisionEngine):
    """Verify confidence tier assignment logic."""
    df_dos = decision_engine.generate_all_flagship_dossiers()
    valid_tiers = {"Tier A: High Confidence", "Tier B: Moderate Confidence", "Tier C: Limited / High Uncertainty"}
    assert set(df_dos["confidence_tier"]).issubset(valid_tiers)


# ============================================================================
# 3. HISTORICAL VALIDATION & BASELINE TESTS
# ============================================================================

def test_historical_validation_execution(validator: HistoricalDecisionValidator):
    """Verify that historical decision validator evaluates 5 flagship scenarios."""
    df_eval = validator.evaluate_flagship_historical_decisions()
    assert len(df_eval) == 5
    assert "mvp8_agrees_with_actual" in df_eval.columns


def test_baseline_rules_evaluation(validator: HistoricalDecisionValidator):
    """Verify baseline PPG and Experience rules produce valid candidate selections."""
    df_eval = validator.evaluate_flagship_historical_decisions()
    assert not df_eval["baseline_ppg_candidate"].isnull().any()
    assert not df_eval["baseline_exp_candidate"].isnull().any()


def test_decision_concordance_schema(validator: HistoricalDecisionValidator):
    """Verify schema of generated decision evaluations dataset."""
    eval_path = ANALYTICS_DATA_DIR / "mvp8_decision_evaluations.csv"
    assert eval_path.exists()
    df = pd.read_csv(eval_path)
    assert len(df) == 5
    assert df["mvp8_agrees_with_actual"].dtype == bool


def test_decision_system_reproducibility_seed():
    """Verify that two independent decision engines produce identical recommendation scores."""
    eng1 = AnalystDecisionEngine(seed=42)
    df1 = eng1.generate_all_flagship_dossiers()

    eng2 = AnalystDecisionEngine(seed=42)
    df2 = eng2.generate_all_flagship_dossiers()

    pd.testing.assert_frame_equal(df1, df2)


def test_dossiers_generation_completeness(decision_engine: AnalystDecisionEngine):
    """Verify all flagship candidates are evaluated into Parquet and CSV."""
    df = decision_engine.generate_all_flagship_dossiers()
    assert len(df) >= 12
    assert (ANALYTICS_DATA_DIR / "mvp8_decision_dossiers.parquet").exists()
    assert (ANALYTICS_DATA_DIR / "mvp8_recommendation_matrix.csv").exists()


def test_flagship_mvp_high_recommendation(decision_engine: AnalystDecisionEngine):
    """Verify that historic tournament MVPs (Pau Gasol 2015, Lorenzo Brown 2022) achieve RECOMMENDED status."""
    df = decision_engine.generate_all_flagship_dossiers()
    gasol = df[df["player_tournament_id"] == "eurobasket_2015_ESP_pau_gasol_1980"].iloc[0]
    brown = df[df["player_tournament_id"] == "eurobasket_2022_ESP_lorenzo_brown_1990"].iloc[0]

    assert gasol["recommendation_status"] == "RECOMMENDED"
    assert gasol["recommendation_score"] >= 75.0
    assert brown["recommendation_status"] == "RECOMMENDED"
    assert brown["recommendation_score"] >= 80.0


def test_end_to_end_mvp8_pipeline():
    """Verify complete end-to-end MVP-8 pipeline execution."""
    eng = AnalystDecisionEngine()
    df_dos = eng.generate_all_flagship_dossiers()
    val = HistoricalDecisionValidator()
    df_eval = val.evaluate_flagship_historical_decisions()
    assert len(df_dos) > 10
    assert len(df_eval) == 5
