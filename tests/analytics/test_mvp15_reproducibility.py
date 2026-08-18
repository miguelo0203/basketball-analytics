"""MVP-15 Reproducibility and End-to-End Execution Validation Tests."""

import os
from pathlib import Path
import pytest
import duckdb
import pandas as pd

from src.config import PROJECT_ROOT, VALIDATED_DB_PATH, ANALYTICS_DATA_DIR


def test_mvp15_artifacts_exist():
    """Verify all MVP-15 audit documents and scripts exist."""
    required_files = [
        PROJECT_ROOT / "reports" / "mvp15_execution_audit.md",
        PROJECT_ROOT / "reports" / "mvp15_release_smoke_test.md",
        PROJECT_ROOT / "reports" / "mvp16_release_audit.md",
        PROJECT_ROOT / "reports" / "mvp17_claim_audit.md",
        PROJECT_ROOT / "reports" / "mvp17_readme_audit.md",
        PROJECT_ROOT / "reports" / "mvp17_data_provenance_audit.md",
        PROJECT_ROOT / "reports" / "mvp17_external_review.md",
        PROJECT_ROOT / "reports" / "mvp17_release_checklist.md",
        PROJECT_ROOT / "reports" / "mvp17_final_verdict.md",
        PROJECT_ROOT / "reports" / "mvp18_candidate_launch.md",
        PROJECT_ROOT / "reports" / "mvp18_madrid_networking_map.md",
        PROJECT_ROOT / "reports" / "mvp18_contact_strategy.md",
        PROJECT_ROOT / "reports" / "mvp18_community_and_events.md",
        PROJECT_ROOT / "reports" / "mvp19_project_distribution_audit.md",
        PROJECT_ROOT / "reports" / "mvp19_online_networking_map.md",
        PROJECT_ROOT / "reports" / "mvp19_remote_opportunities.md",
        PROJECT_ROOT / "reports" / "mvp19_github_presentation_audit.md",
        PROJECT_ROOT / "reports" / "mvp20_community_audit.md",
        PROJECT_ROOT / "reports" / "mvp20_community_map.md",
        PROJECT_ROOT / "reports" / "mvp20_learning_strategy.md",
        PROJECT_ROOT / "reports" / "mvp20_project_distribution.md",
        PROJECT_ROOT / "reports" / "mvp21_community_validation.md",
        PROJECT_ROOT / "reports" / "mvp21_community_ranking.md",
        PROJECT_ROOT / "reports" / "mvp21_madrid_communities.md",
        PROJECT_ROOT / "reports" / "mvp21_online_communities.md",
        PROJECT_ROOT / "reports" / "mvp21_project_showcase_strategy.md",
        PROJECT_ROOT / "reports" / "mvp21_micro_case_studies.md",
        PROJECT_ROOT / "reports" / "mvp21_90_day_plan.md",
        PROJECT_ROOT / "reports" / "mvp22_repository_audit.md",
        PROJECT_ROOT / "reports" / "mvp23_publication_audit.md",
        PROJECT_ROOT / "CITATION.cff",
        PROJECT_ROOT / "data" / "README.md",
        PROJECT_ROOT / "presentation" / "README.md",
        PROJECT_ROOT / "portfolio" / "community" / "community_tracker.csv",
        PROJECT_ROOT / "portfolio" / "networking" / "madrid_networking_tracker.csv",
        PROJECT_ROOT / "portfolio" / "networking" / "networking_tracker.csv",
        PROJECT_ROOT / "portfolio" / "networking" / "contact_templates.md",
        PROJECT_ROOT / "portfolio" / "networking" / "online_contact_strategy.md",
        PROJECT_ROOT / "portfolio" / "networking" / "linkedin_posts.md",
        PROJECT_ROOT / "portfolio" / "networking" / "community_strategy.md",
        PROJECT_ROOT / "portfolio" / "job_search" / "cv_final.md",
        PROJECT_ROOT / "portfolio" / "job_search" / "linkedin_final.md",
        PROJECT_ROOT / "portfolio" / "job_search" / "first_30_days.md",
        PROJECT_ROOT / "portfolio" / "job_search" / "interview_final.md",
        PROJECT_ROOT / "portfolio" / "job_search" / "outreach_final.md",
        PROJECT_ROOT / "docs" / "reproducibility_manifest.md",
        PROJECT_ROOT / "docs" / "execution_lineage.md",
        PROJECT_ROOT / "scripts" / "run_project.py",
        PROJECT_ROOT / "scripts" / "run_r_analysis.R",
        PROJECT_ROOT / "scripts" / "verify_environment.py",
        PROJECT_ROOT / "scripts" / "verify_cross_language.py",
    ]
    for rf in required_files:
        assert rf.exists(), f"Missing required MVP-15 artifact: {rf.name}"


def test_duckdb_and_parquet_coherence():
    """Verify DuckDB database and Parquet analytical marts have matching records."""
    assert VALIDATED_DB_PATH.exists()
    con = duckdb.connect(str(VALIDATED_DB_PATH), read_only=True)
    n_games = con.execute("SELECT COUNT(*) FROM fact_game").fetchone()[0]
    n_team_games = con.execute("SELECT COUNT(*) FROM fact_team_game").fetchone()[0]
    con.close()

    assert n_games == 1145
    assert n_team_games == 2290

    # Check Parquet marts
    team_parquet = ANALYTICS_DATA_DIR / "mart_team_game_analytics.parquet"
    if team_parquet.exists():
        df_team = pd.read_parquet(team_parquet)
        assert len(df_team) == 2290


def test_r_figures_generated():
    """Verify R generated figures exist and have valid file size."""
    figures_r_dir = PROJECT_ROOT / "reports" / "figures_r"
    assert figures_r_dir.exists()
    expected_figures = [
        "fig_01_tournament_trends.png",
        "fig_02_player_trajectories.png",
        "fig_03_archetype_distribution.png",
        "fig_04_four_factors_correlation.png",
        "fig_05_ts_distribution.png",
    ]
    for fig_name in expected_figures:
        fig_path = figures_r_dir / fig_name
        assert fig_path.exists(), f"Missing R figure: {fig_name}"
        assert fig_path.stat().st_size > 1000, f"R figure is too small or corrupt: {fig_name}"
