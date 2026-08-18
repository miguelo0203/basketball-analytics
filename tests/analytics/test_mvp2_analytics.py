"""Pytest suite for MVP-2 Analytical Data Marts, Descriptive Metrics, and Flagship ITS Model."""

import pytest
import pandas as pd
from pathlib import Path

from src.config import ANALYTICS_DATA_DIR, REPORTS_DIR
from src.analytics.data_mart import DataMartGenerator
from src.analytics.mvp2_descriptive import DescriptiveAnalysisEngine
from src.analytics.mvp2_flagship import ITSFlagshipModel
from src.analytics.mvp2_sensitivity import SensitivityAnalysisEngine


@pytest.fixture(scope="module")
def data_mart():
    gen = DataMartGenerator()
    paths = gen.generate_marts()
    return paths


def test_analytical_data_mart_existence_and_schema(data_mart):
    """Verify analytical data marts exist and have expected row counts."""
    tg_path = ANALYTICS_DATA_DIR / "mart_team_game_analytics.parquet"
    ts_path = ANALYTICS_DATA_DIR / "mart_tournament_summary.parquet"
    assert tg_path.exists()
    assert ts_path.exists()

    df_tg = pd.read_parquet(tg_path)
    df_ts = pd.read_parquet(ts_path)

    assert len(df_tg) == 2290, f"Expected 2,290 team-game rows, found {len(df_tg)}"
    assert len(df_ts) == 18, f"Expected 18 tournament summary rows, found {len(df_ts)}"
    assert "three_point_attempt_rate" in df_tg.columns
    assert "post_2010_rule" in df_tg.columns
    assert "time_after_2010" in df_tg.columns


def test_three_point_attempt_rate_bounds(data_mart):
    """Verify 3PAr is strictly bounded in [0.0, 1.0] with 0 NaNs."""
    df_tg = pd.read_parquet(ANALYTICS_DATA_DIR / "mart_team_game_analytics.parquet")
    par = df_tg["three_point_attempt_rate"].dropna()
    assert len(par) == 2290
    assert (par >= 0.0).all() and (par <= 1.0).all()


def test_shooting_percentages_bounds(data_mart):
    """Verify 2P% and 3P% are bounded in [0.0, 1.0]."""
    df_tg = pd.read_parquet(ANALYTICS_DATA_DIR / "mart_team_game_analytics.parquet")
    fg2_pct = df_tg["two_point_pct"].dropna()
    fg3_pct = df_tg["three_point_pct"].dropna()
    assert (fg2_pct >= 0.0).all() and (fg2_pct <= 1.0).all()
    assert (fg3_pct >= 0.0).all() and (fg3_pct <= 1.0).all()


def test_analytical_data_mart_deterministic_reproducibility():
    """Verify that regenerated data marts produce bitwise identical checksums."""
    gen = DataMartGenerator()
    csum1 = gen.compute_mart_checksum()
    gen.generate_marts()
    csum2 = gen.compute_mart_checksum()
    assert csum1 == csum2, "Data mart checksums must be bitwise identical"


def test_descriptive_analysis_engine(data_mart):
    """Verify DescriptiveAnalysisEngine computes valid distributions."""
    engine = DescriptiveAnalysisEngine()
    df_dist = engine.compute_distribution_metrics()
    assert len(df_dist) == 12
    assert "metric" in df_dist.columns
    assert "p_value_ttest" in df_dist.columns


def test_its_flagship_model_parameters(data_mart):
    """Verify primary ITS model execution, parameter signs, and significance."""
    model = ITSFlagshipModel()
    res = model.fit_primary_model()

    assert res["nobs"] == 2290
    params = res["params"]
    assert "post_2010_rule" in params
    assert "tournament_seq" in params
    assert "time_after_2010" in params

    # Verify baseline slope is positive and level shift is negative
    assert params["tournament_seq"] > 0, "Pre-2010 baseline slope should be positive"
    assert params["post_2010_rule"] < 0, "Immediate level shift should be negative"
    assert res["pvalues"]["post_2010_rule"] < 0.05, "Level shift must be statistically significant"


def test_sensitivity_engine_specifications(data_mart):
    """Verify that all 7 sensitivity specifications execute successfully."""
    engine = SensitivityAnalysisEngine()
    df_sens = engine.run_all_sensitivities()
    assert len(df_sens) >= 7
    assert "Specification" in df_sens.columns
    assert "Robustness_Verdict" in df_sens.columns
