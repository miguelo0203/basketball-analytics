"""Four Factors of Basketball Success (Dean Oliver)."""

from typing import Dict, Optional


def calculate_efg_pct(fgm: int, fg3m: int, fga: int) -> float:
    """Calculate Effective Field Goal Percentage (eFG%).

    Formula: (FGM + 0.5 * FG3M) / FGA
    """
    if fga <= 0:
        return 0.0
    return round((float(fgm) + 0.5 * float(fg3m)) / float(fga), 4)


def calculate_tov_pct(tov: int, fga: int, fta: int) -> float:
    """Calculate Turnover Percentage (TOV%).

    Formula: TOV / (FGA + 0.44 * FTA + TOV)
    """
    denom = float(fga) + 0.44 * float(fta) + float(tov)
    if denom <= 0:
        return 0.0
    return round(float(tov) / denom, 4)


def calculate_orb_pct(team_orb: int, opp_drb: int) -> float:
    """Calculate Offensive Rebound Percentage (ORB%).

    Formula: Team_ORB / (Team_ORB + Opponent_DRB)
    """
    denom = float(team_orb) + float(opp_drb)
    if denom <= 0:
        return 0.0
    return round(float(team_orb) / denom, 4)


def calculate_ftr(fta: int, fga: int) -> float:
    """Calculate Free Throw Rate (FTr).

    Formula: FTA / FGA
    """
    if fga <= 0:
        return 0.0
    return round(float(fta) / float(fga), 4)


def calculate_four_factors(
    fgm: int,
    fg3m: int,
    fga: int,
    ftm: int,
    fta: int,
    orb: int,
    tov: int,
    opp_drb: int,
) -> Dict[str, float]:
    """Calculate all four offensive factors for a team."""
    return {
        "efg_pct": calculate_efg_pct(fgm, fg3m, fga),
        "tov_pct": calculate_tov_pct(tov, fga, fta),
        "orb_pct": calculate_orb_pct(orb, opp_drb),
        "ftr": calculate_ftr(fta, fga),
    }
