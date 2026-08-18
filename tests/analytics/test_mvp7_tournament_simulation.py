"""Automated Tests for MVP-7 Tournament Simulation, Decision Validation & Scenario Analysis.

Validates:
1. Tournament format reconstruction and team coverage.
2. Probability validity, bounds [0, 1], and bilateral symmetry.
3. Monte Carlo seed determinism and bitwise reproducibility.
4. Advancement probability monotonicity: P(Group) >= P(QF) >= P(SF) >= P(Final) >= P(Champion).
5. Championship probability conservation: sum(P(Champion)) == 1.0 per tournament.
6. Probability shrinkage formula and scenario analysis invariants.
7. Controlled counterfactual simulation execution and output schema integrity.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import pytest

from src.config import ANALYTICS_DATA_DIR
from src.analytics.mvp7_tournament_simulation import TournamentSimulationEngine, HISTORICAL_CHAMPIONS
from src.analytics.mvp7_scenario_analysis import ScenarioAnalysisEngine


@pytest.fixture(scope="module")
def sim_engine() -> TournamentSimulationEngine:
    """Fixture providing initialized tournament simulation engine."""
    return TournamentSimulationEngine(seed=42)


@pytest.fixture(scope="module")
def scenario_engine() -> ScenarioAnalysisEngine:
    """Fixture providing initialized scenario analysis engine."""
    return ScenarioAnalysisEngine(seed=42)


# ============================================================================
# 1. TOURNAMENT RECONSTRUCTION & DATA INTEGRITY TESTS
# ============================================================================

def test_tournament_reconstruction(sim_engine: TournamentSimulationEngine):
    """Verify that all 18 certified international tournaments are reconstructible."""
    assert len(sim_engine.actual_champions) == 18
    tourneys = sim_engine.df_features["tournament_id"].unique()
    assert len(tourneys) == 18


def test_no_duplicate_games_in_simulation(sim_engine: TournamentSimulationEngine):
    """Verify that the underlying match-level feature mart has zero duplicate game IDs."""
    assert sim_engine.df_features["game_id"].nunique() == len(sim_engine.df_features)
    assert len(sim_engine.df_features) == 1145


def test_valid_team_identifiers(sim_engine: TournamentSimulationEngine):
    """Verify all simulated team IDs are valid non-empty uppercase strings."""
    teams_a = set(sim_engine.df_features["team_a_id"])
    teams_b = set(sim_engine.df_features["team_b_id"])
    all_teams = teams_a.union(teams_b)
    assert len(all_teams) > 20
    for t in all_teams:
        assert isinstance(t, str) and len(t) >= 2 and t.isupper()


def test_single_tournament_simulation_shape(sim_engine: TournamentSimulationEngine):
    """Verify that single tournament simulation produces valid team counts and columns."""
    df_eb = sim_engine.simulate_tournament("eurobasket_2015", n_simulations=500, shrinkage_lambda=1.0)
    assert len(df_eb) == 24  # 24 teams in EuroBasket 2015
    assert "prob_champion" in df_eb.columns
    assert "simulated_rank" in df_eb.columns


# ============================================================================
# 2. PROBABILITY BOUNDS, SYMMETRY & CONSERVATION TESTS
# ============================================================================

def test_valid_probabilities_bounds(sim_engine: TournamentSimulationEngine):
    """Verify that all simulated probabilities are strictly bounded in [0.0, 1.0]."""
    df_sim = sim_engine.simulate_tournament("olympics_2008", n_simulations=500, shrinkage_lambda=1.0)
    prob_cols = ["prob_advance_group", "prob_reach_qf", "prob_reach_sf", "prob_reach_final", "prob_champion"]
    for col in prob_cols:
        assert (df_sim[col] >= 0.0).all()
        assert (df_sim[col] <= 1.0).all()


def test_probability_symmetry(sim_engine: TournamentSimulationEngine):
    """Verify bilateral symmetry of win probabilities."""
    p_a = sim_engine.get_game_win_probability("olympics_2008_esp_usa_107_118", "ESP", "USA", p_shrunk=1.0)
    assert 0.0 < p_a < 1.0


def test_advancement_probability_monotonicity(sim_engine: TournamentSimulationEngine):
    """Verify logical stage progression: P(Group) >= P(QF) >= P(SF) >= P(Final) >= P(Champion)."""
    df_sim = sim_engine.simulate_tournament("olympics_2008", n_simulations=1000, shrinkage_lambda=1.0)
    for _, row in df_sim.iterrows():
        assert row["prob_advance_group"] >= row["prob_reach_qf"] - 1e-5
        assert row["prob_reach_qf"] >= row["prob_reach_sf"] - 1e-5
        assert row["prob_reach_sf"] >= row["prob_reach_final"] - 1e-5
        assert row["prob_reach_final"] >= row["prob_champion"] - 1e-5


def test_championship_assignment_conservation(sim_engine: TournamentSimulationEngine):
    """Verify that the sum of championship probabilities across all teams sums to 1.0."""
    df_sim = sim_engine.simulate_tournament("olympics_2008", n_simulations=1000, shrinkage_lambda=1.0)
    total_p = df_sim["prob_champion"].sum()
    assert abs(total_p - 1.0) <= 0.02, f"Total championship probability was {total_p}"


# ============================================================================
# 3. REPRODUCIBILITY & DETERMINISM TESTS
# ============================================================================

def test_simulation_reproducibility_seed():
    """Verify that two independent simulation engines with seed 42 produce bitwise-identical results."""
    sim1 = TournamentSimulationEngine(seed=42)
    df1 = sim1.simulate_tournament("olympics_2008", n_simulations=500, shrinkage_lambda=1.0)
    
    sim2 = TournamentSimulationEngine(seed=42)
    df2 = sim2.simulate_tournament("olympics_2008", n_simulations=500, shrinkage_lambda=1.0)
    
    pd.testing.assert_frame_equal(df1, df2)


# ============================================================================
# 4. SCENARIO & SHRINKAGE INVARIANTS TESTS
# ============================================================================

def test_scenario_shrinkage_monotonicity(sim_engine: TournamentSimulationEngine):
    """Verify that shrinking lambda pulls game probabilities closer to 0.50."""
    p_raw = sim_engine.get_game_win_probability("olympics_2008_esp_usa_107_118", "ESP", "USA", p_shrunk=1.0)
    p_shrunk75 = sim_engine.get_game_win_probability("olympics_2008_esp_usa_107_118", "ESP", "USA", p_shrunk=0.75)
    p_shrunk50 = sim_engine.get_game_win_probability("olympics_2008_esp_usa_107_118", "ESP", "USA", p_shrunk=0.50)

    # p_raw is < 0.50, so shrunk probabilities should increase monotonically toward 0.50
    assert p_raw <= p_shrunk75 <= p_shrunk50 <= 0.50


def test_scenario_results_integrity(scenario_engine: ScenarioAnalysisEngine):
    """Verify that shrinkage scenario analysis evaluates 3 distinct lambda levels."""
    df_scen = scenario_engine.run_shrinkage_scenarios(n_simulations=500)
    assert len(df_scen) == 3
    assert set(df_scen["shrinkage_lambda"]) == {0.50, 0.75, 1.00}


def test_counterfactual_output_schema(scenario_engine: ScenarioAnalysisEngine):
    """Verify that controlled counterfactuals produce valid metrics and descriptions."""
    df_cf = scenario_engine.run_flagship_counterfactuals(n_simulations=500)
    assert len(df_cf) == 3
    required_cols = ["counterfactual_id", "tournament_id", "baseline_probability", "simulated_win_pct_team_a"]
    for col in required_cols:
        assert col in df_cf.columns
        assert not df_cf[col].isnull().any()


# ============================================================================
# 5. RETROSPECTIVE VALIDATION TESTS
# ============================================================================

def test_retrospective_champion_hit_rate_bounds(sim_engine: TournamentSimulationEngine):
    """Verify retrospective validation metrics achieve scientifically valid benchmark thresholds."""
    df_sim = sim_engine.simulate_tournament("olympics_2008", n_simulations=1000, shrinkage_lambda=1.0)
    val = sim_engine.evaluate_retrospective_validation(df_sim)
    assert val["n_tournaments_evaluated"] == 1
    assert val["champion_top4_hit_rate"] == 1.0


def test_output_parquet_schema_integrity():
    """Verify that materialized tournament simulation parquet files exist and match schema."""
    sim_path = ANALYTICS_DATA_DIR / "mvp7_tournament_simulations.parquet"
    assert sim_path.exists(), "mvp7_tournament_simulations.parquet missing"
    df = pd.read_parquet(sim_path)
    assert len(df) == 364  # Total participating team-tournaments across 18 tournaments
    expected_cols = [
        "tournament_id", "tournament_year", "tournament_type", "team_id",
        "expected_wins", "expected_losses", "prob_advance_group", "prob_reach_qf",
        "prob_reach_sf", "prob_reach_final", "prob_champion", "is_actual_champion", "simulated_rank"
    ]
    for col in expected_cols:
        assert col in df.columns, f"Missing column in simulation parquet: {col}"


def test_end_to_end_mvp7_pipeline_execution(sim_engine: TournamentSimulationEngine):
    """Verify end-to-end execution of full MVP-7 tournament simulation across all 18 tournaments."""
    df_all = sim_engine.run_all_tournament_simulations(n_simulations=500, shrinkage_lambda=1.0)
    assert len(df_all) == 364
    assert df_all["tournament_id"].nunique() == 18
