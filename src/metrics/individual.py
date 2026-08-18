"""Individual player performance metrics: TS%, USG%, Game Score, PIR."""

from typing import Optional


def calculate_ts_pct(pts: int, fga: int, fta: int) -> Optional[float]:
    """Calculate True Shooting Percentage (TS%).

    Formula: PTS / (2 * (FGA + 0.44 * FTA))
    """
    denom = 2.0 * (float(fga) + 0.44 * float(fta))
    if denom <= 0:
        return None
    return round(float(pts) / denom, 4)


def calculate_usg_pct(
    player_fga: int,
    player_fta: int,
    player_tov: int,
    player_minutes: float,
    team_fga: int,
    team_fta: int,
    team_tov: int,
    team_minutes: float = 200.0,
) -> Optional[float]:
    """Calculate Usage Rate (USG%).

    Formula: 100 * [ (FGA_p + 0.44 * FTA_p + TOV_p) * (Team_MIN / 5) ] /
                   [ MIN_p * (Team_FGA + 0.44 * Team_FTA + Team_TOV) ]
    """
    if player_minutes <= 0:
        return 0.0
    team_denom = float(team_fga) + 0.44 * float(team_fta) + float(team_tov)
    if team_denom <= 0:
        return 0.0
    player_num = (float(player_fga) + 0.44 * float(player_fta) + float(player_tov)) * (team_minutes / 5.0)
    denom = player_minutes * team_denom
    return round(100.0 * (player_num / denom), 2)


def calculate_game_score(
    pts: int,
    fgm: int,
    fga: int,
    ftm: int,
    fta: int,
    orb: int,
    drb: int,
    stl: int,
    ast: int,
    blk: int,
    pf: int,
    tov: int,
) -> float:
    """Calculate John Hollinger's Game Score."""
    gmsc = (
        float(pts)
        + 0.4 * float(fgm)
        - 0.7 * float(fga)
        - 0.4 * (float(fta) - float(ftm))
        + 0.7 * float(orb)
        + 0.3 * float(drb)
        + float(stl)
        + 0.7 * float(ast)
        + 0.7 * float(blk)
        - 0.4 * float(pf)
        - float(tov)
    )
    return round(gmsc, 2)


def calculate_pir(
    pts: int,
    trb: int,
    ast: int,
    stl: int,
    blk: int,
    fouls_drawn: int,
    fga: int,
    fgm: int,
    fta: int,
    ftm: int,
    tov: int,
    pf: int,
) -> int:
    """Calculate official FIBA Performance Index Rating (PIR).

    Formula: (PTS + TRB + AST + STL + BLK + FD) - ((FGA - FGM) + (FTA - FTM) + TOV + PF)
    """
    positive = pts + trb + ast + stl + blk + fouls_drawn
    negative = (fga - fgm) + (fta - ftm) + tov + pf
    return positive - negative
