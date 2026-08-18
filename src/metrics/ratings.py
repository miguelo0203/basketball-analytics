"""Team Offensive, Defensive, and Net Ratings per 100 possessions."""

from typing import Dict


def calculate_ortg(pts: int, possessions: float) -> float:
    """Calculate Offensive Rating (points scored per 100 possessions)."""
    if possessions <= 0:
        return 0.0
    return round(100.0 * (float(pts) / possessions), 2)


def calculate_drtg(opp_pts: int, possessions: float) -> float:
    """Calculate Defensive Rating (points allowed per 100 possessions)."""
    if possessions <= 0:
        return 0.0
    return round(100.0 * (float(opp_pts) / possessions), 2)


def calculate_net_rtg(ortg: float, drtg: float) -> float:
    """Calculate Net Rating (ORtg - DRtg)."""
    return round(ortg - drtg, 2)


def calculate_ratings(pts: int, opp_pts: int, possessions: float) -> Dict[str, float]:
    """Calculate ORtg, DRtg, and NetRtg."""
    ortg = calculate_ortg(pts, possessions)
    drtg = calculate_drtg(opp_pts, possessions)
    return {
        "ortg": ortg,
        "drtg": drtg,
        "net_rtg": calculate_net_rtg(ortg, drtg),
    }
