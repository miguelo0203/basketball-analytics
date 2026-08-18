"""Integration tests validating end-to-end analytics, clustering, and predictive pipelines."""

import pytest
import numpy as np
import pandas as pd
from src.analytics.clustering import PlayerClusteringPipeline
from src.analytics.predictive import PredictiveEvaluation
from src.analytics.longitudinal import classify_generation_cohort, calculate_cohort_production_shares


def test_clustering_pipeline_evaluation():
    # Create synthetic player-tournament dataset
    rng = np.random.default_rng(42)
    n_records = 150
    data = {
        "player_tournament_id": [f"pt_{i}" for i in range(n_records)],
        "usg_pct_avg": rng.uniform(10.0, 32.0, n_records),
        "ts_pct": rng.uniform(0.45, 0.68, n_records),
        "three_point_rate": rng.uniform(0.0, 0.60, n_records),
        "free_throw_rate": rng.uniform(0.10, 0.50, n_records),
        "fg2_pct": rng.uniform(0.40, 0.65, n_records),
        "fg3_pct": rng.uniform(0.25, 0.45, n_records),
        "ft_pct": rng.uniform(0.60, 0.90, n_records),
        "orb_pct_est": rng.uniform(0.02, 0.15, n_records),
        "drb_pct_est": rng.uniform(0.05, 0.25, n_records),
        "ast_pct_est": rng.uniform(0.05, 0.35, n_records),
        "tov_pct_est": rng.uniform(0.08, 0.22, n_records),
        "stl_per_40": rng.uniform(0.5, 3.0, n_records),
        "blk_per_40": rng.uniform(0.1, 2.5, n_records),
        "pf_per_40": rng.uniform(1.5, 4.5, n_records),
    }
    df = pd.DataFrame(data)

    pipeline = PlayerClusteringPipeline(random_state=42)
    X, _ = pipeline.prepare_features(df)

    # Evaluate k across range
    k_evals = pipeline.evaluate_k_range(X, k_min=3, k_max=6)
    assert len(k_evals) == 4
    for record in k_evals:
        assert "silhouette" in record
        assert "calinski_harabasz" in record
        assert "davies_bouldin" in record
        assert "gmm_bic" in record

    # Evaluate bootstrap stability
    stability = pipeline.evaluate_bootstrap_stability(X, k=4, n_bootstraps=10)
    assert 0.0 <= stability <= 1.0

    # Fit final model
    labels, model = pipeline.fit(df, k=4)
    assert len(labels) == n_records
    assert set(labels) == {0, 1, 2, 3}


def test_predictive_evaluation_loto():
    # Create synthetic tournament game dataset
    rng = np.random.default_rng(42)
    n_games = 60
    tournaments = ["eurobasket_2017", "worldcup_2019", "eurobasket_2022"]
    
    data = {
        "game_id": [f"g_{i}" for i in range(n_games)],
        "tournament_id": [tournaments[i % 3] for i in range(n_games)],
        "diff_net_rtg": rng.normal(0.0, 10.0, n_games),
        "diff_efg": rng.normal(0.0, 0.08, n_games),
        "diff_tov": rng.normal(0.0, 0.05, n_games),
        "home_win": rng.choice([0, 1], size=n_games),
        "margin_home": rng.normal(0.0, 12.0, n_games),
    }
    df = pd.DataFrame(data)

    pred = PredictiveEvaluation(random_state=42)
    feature_cols = ["diff_net_rtg", "diff_efg", "diff_tov"]

    # Win probability LOTO
    win_eval = pred.evaluate_win_probability_models(df, feature_cols=feature_cols)
    assert win_eval["n_evaluated_games"] == n_games
    assert "logistic_brier_score" in win_eval
    assert win_eval["logistic_brier_score"] >= 0.0

    # Margin LOTO
    margin_eval = pred.evaluate_margin_models(df, feature_cols=feature_cols)
    assert margin_eval["n_evaluated_games"] == n_games
    assert "ridge_mae" in margin_eval
    assert margin_eval["ridge_mae"] > 0


def test_generational_cohort_analysis():
    assert classify_generation_cohort(1980) == "1980-1985 Golden Generation"
    assert classify_generation_cohort(1990) == "1986-1994 Transition Core"
    assert classify_generation_cohort(2000) == "1995+ New Generation"

    sample_df = pd.DataFrame({
        "tournament_id": ["eb_2011", "eb_2011", "eb_2022"],
        "birth_year": [1980, 1990, 2000],
        "seconds_played": [1800, 1200, 2400],
        "pts": [25, 15, 30],
    })

    shares = calculate_cohort_production_shares(sample_df)
    assert "minute_share_pct" in shares.columns
    assert "point_share_pct" in shares.columns
    assert len(shares) == 3
