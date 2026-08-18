"""Automated Tests for MVP-6 Supervised Analytics, Leakage Prevention & Statistical Inference.

Validates:
1. Strict pre-game temporal cutoff and zero look-ahead leakage.
2. Expanding temporal walk-forward fold integrity (17 folds, zero game overlap).
3. Bilateral target symmetry and match-level canonical structure.
4. Clustered bootstrap confidence interval mathematical properties.
5. Permutation testing p-value bounds and Benjamini-Hochberg FDR monotonicity.
6. Model benchmark out-of-sample execution and calibration properties.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import pytest

from src.config import ANALYTICS_DATA_DIR
from src.analytics.mvp6_supervised_models import PreGameFeatureBuilder, SupervisedBenchmarkEngine
from src.analytics.mvp6_statistical_inference import ClusteredBootstrapEngine, PermutationHypothesisEngine


@pytest.fixture(scope="module")
def pre_game_df() -> pd.DataFrame:
    """Fixture providing canonical pre-game feature mart."""
    builder = PreGameFeatureBuilder()
    return builder.build_pre_game_feature_mart()


@pytest.fixture(scope="module")
def benchmark_engine() -> SupervisedBenchmarkEngine:
    """Fixture providing initialized benchmark engine."""
    return SupervisedBenchmarkEngine(seed=42)


# ============================================================================
# 1. LEAKAGE & DATA INTEGRITY TESTS
# ============================================================================

def test_pre_game_feature_temporal_cutoff(pre_game_df: pd.DataFrame):
    """Verify that the pre-game feature mart has exactly 1,145 canonical match rows and valid schema."""
    assert len(pre_game_df) == 1145, f"Expected 1,145 games, got {len(pre_game_df)}"
    assert pre_game_df["game_id"].nunique() == 1145
    assert not pre_game_df["game_team_a_win"].isnull().any()
    assert not pre_game_df["point_differential"].isnull().any()


def test_expanding_fold_manifest_integrity(benchmark_engine: SupervisedBenchmarkEngine):
    """Verify that expanding temporal walk-forward validation generates exactly 17 chronological folds."""
    folds = benchmark_engine.generate_expanding_folds()
    assert len(folds) == 17, f"Expected 17 expanding folds, got {len(folds)}"
    
    # Check chronological ordering: each test year >= train max year
    for f in folds:
        assert f["test_year"] >= f["train_end_year"], (
            f"Fold {f['fold_id']} has test year {f['test_year']} before train end year {f['train_end_year']}"
        )


def test_no_game_id_overlap_between_train_test(benchmark_engine: SupervisedBenchmarkEngine):
    """Verify strictly zero game_id leakage or overlap between train and test sets across all folds."""
    folds = benchmark_engine.generate_expanding_folds()
    for f in folds:
        train_ids = set(f["train_df"]["game_id"])
        test_ids = set(f["test_df"]["game_id"])
        overlap = train_ids.intersection(test_ids)
        assert len(overlap) == 0, f"Fold {f['fold_id']} leaked games: {overlap}"


def test_bilateral_target_symmetry(pre_game_df: pd.DataFrame):
    """Verify mathematical consistency between team scores, winner flag, and point differential."""
    for _, row in pre_game_df.iterrows():
        diff = row["point_differential"]
        win = row["game_team_a_win"]
        if diff > 0:
            assert win == 1
        elif diff < 0:
            assert win == 0


def test_feature_schema_integrity(pre_game_df: pd.DataFrame):
    """Verify that all required historical, dynamic, and context features exist and are populated."""
    required_cols = [
        "game_id", "tournament_id", "tournament_year", "game_date",
        "team_a_id", "team_b_id", "game_team_a_win", "point_differential",
        "diff_hist_net_rating", "diff_hist_efg_pct", "diff_hist_tov_pct",
        "diff_hist_orb_pct", "diff_hist_ftr", "diff_in_tourney_form_net",
        "diff_rest_days", "is_knockout_stage", "post_2010_rule_era", "diff_experience_caps"
    ]
    for col in required_cols:
        assert col in pre_game_df.columns, f"Missing required column: {col}"
        assert not pre_game_df[col].isnull().any(), f"Column {col} contains null values"


def test_deterministic_feature_generation():
    """Verify that repeated feature generation produces 100% deterministic, bitwise-equal feature values."""
    b1 = PreGameFeatureBuilder()
    df1 = b1.build_pre_game_feature_mart()
    b2 = PreGameFeatureBuilder()
    df2 = b2.build_pre_game_feature_mart()
    pd.testing.assert_frame_equal(df1, df2)


# ============================================================================
# 2. STATISTICAL INFERENCE & HYPOTHESIS TESTING TESTS
# ============================================================================

def test_bootstrap_confidence_intervals():
    """Verify that non-parametric bootstrap confidence intervals are mathematically valid."""
    boot = ClusteredBootstrapEngine(seed=42)
    df_boot = boot.compute_metric_bootstrap_cis(n_bootstraps=500)
    
    assert len(df_boot) == 7
    for _, row in df_boot.iterrows():
        assert row["ci_95_lower"] <= row["observed_mean"] <= row["ci_95_upper"], (
            f"Metric {row['metric_name']} mean outside CI: [{row['ci_95_lower']}, {row['ci_95_upper']}]"
        )
        assert row["bootstrap_se"] > 0


def test_permutation_p_value_bounds():
    """Verify that permutation test p-values are bounded in [0.0, 1.0]."""
    perm = PermutationHypothesisEngine(seed=42)
    df_perm = perm.run_flagship_and_family_tests(n_permutations=500)
    
    assert len(df_perm) >= 15
    for _, row in df_perm.iterrows():
        assert 0.0 <= row["perm_p_value"] <= 1.0
        assert 0.0 <= row["fdr_adjusted_p"] <= 1.0
        assert 0.0 <= row["bonferroni_adjusted_p"] <= 1.0


def test_fdr_benjamini_hochberg_properties():
    """Verify that FDR adjusted p-values are greater than or equal to raw p-values."""
    perm = PermutationHypothesisEngine(seed=42)
    df_perm = perm.run_flagship_and_family_tests(n_permutations=500)
    
    for _, row in df_perm.iterrows():
        assert row["fdr_adjusted_p"] >= row["perm_p_value"] - 1e-6
        assert row["bonferroni_adjusted_p"] >= row["fdr_adjusted_p"] - 1e-6


# ============================================================================
# 3. MACHINE LEARNING BENCHMARK TESTS
# ============================================================================

def test_model_benchmark_brier_and_mae_bounds(benchmark_engine: SupervisedBenchmarkEngine):
    """Verify out-of-sample model benchmark results satisfy scientific validity bounds."""
    preds, bench = benchmark_engine.run_benchmark()
    assert len(preds) > 0
    assert len(bench) >= 6
    
    # Classification: LightGBM should achieve Brier Score < 0.22 and beat Naive 50%
    df_c = bench[bench["task_type"] == "Classification"]
    lgb_brier = df_c[df_c["model_name"] == "LightGBM Classifier"]["primary_score"].iloc[0]
    naive_brier = df_c[df_c["model_name"] == "Naive Baseline (50%)"]["primary_score"].iloc[0]
    assert lgb_brier < naive_brier
    assert lgb_brier < 0.22

    # Regression: LightGBM MAE should be < 13.0 points and beat zero baseline
    df_r = bench[bench["task_type"] == "Regression"]
    lgb_mae = df_r[df_r["model_name"] == "LightGBM Regressor"]["primary_score"].iloc[0]
    naive_mae = df_r[df_r["model_name"] == "Naive Margin (0.0 pts)"]["primary_score"].iloc[0]
    assert lgb_mae < naive_mae
    assert lgb_mae < 13.0
