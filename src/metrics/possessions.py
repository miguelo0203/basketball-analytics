"""Possession estimation engine using Dean Oliver's calibrated FIBA formulas."""


def calculate_possessions_simple(fga: int, fta: int, orb: int, tov: int) -> float:
    """Calculate single-team simple estimated possessions (Dean Oliver formula).

    Formula: FGA + 0.44 * FTA - ORB + TOV
    """
    poss = float(fga) + 0.44 * float(fta) - float(orb) + float(tov)
    return max(0.0, round(poss, 4))


def calculate_possessions_bilateral(poss_team_a: float, poss_team_b: float) -> float:
    """Calculate bilateral estimated game possessions ensuring opponent symmetry.

    Formula: 0.5 * (Poss_A + Poss_B)
    """
    return max(0.0, round(0.5 * (poss_team_a + poss_team_b), 4))
