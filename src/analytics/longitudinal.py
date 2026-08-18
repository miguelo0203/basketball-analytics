"""Longitudinal career and generational cohort analysis."""

import pandas as pd
from typing import Dict, Any, List


def classify_generation_cohort(birth_year: int) -> str:
    """Classify player birth year into strategic generational cohorts."""
    if birth_year < 1986:
        return "1980-1985 Golden Generation"
    elif birth_year < 1995:
        return "1986-1994 Transition Core"
    else:
        return "1995+ New Generation"


def calculate_cohort_production_shares(df_player_game: pd.DataFrame) -> pd.DataFrame:
    """Calculate proportion of minutes and points produced by cohort per tournament."""
    df = df_player_game.copy()
    if "cohort" not in df.columns and "birth_year" in df.columns:
        df["cohort"] = df["birth_year"].apply(classify_generation_cohort)

    grouped = df.groupby(["tournament_id", "cohort"]).agg(
        total_seconds=("seconds_played", "sum"),
        total_points=("pts", "sum"),
    ).reset_index()

    # Calculate percentages within tournament
    tourney_totals = df.groupby("tournament_id").agg(
        tourney_seconds=("seconds_played", "sum"),
        tourney_points=("pts", "sum"),
    ).reset_index()

    merged = pd.merge(grouped, tourney_totals, on="tournament_id")
    merged["minute_share_pct"] = (merged["total_seconds"] / merged["tourney_seconds"]) * 100.0
    merged["point_share_pct"] = (merged["total_points"] / merged["tourney_points"]) * 100.0

    return merged.round(2)
