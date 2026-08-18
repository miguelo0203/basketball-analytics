"""Unit tests for FIBA mathematical formulas and metric calculations."""

import pytest
from src.metrics.possessions import calculate_possessions_simple, calculate_possessions_bilateral
from src.metrics.pace import calculate_pace_40m
from src.metrics.four_factors import (
    calculate_efg_pct,
    calculate_tov_pct,
    calculate_orb_pct,
    calculate_ftr,
    calculate_four_factors,
)
from src.metrics.ratings import calculate_ortg, calculate_drtg, calculate_net_rtg, calculate_ratings
from src.metrics.individual import (
    calculate_ts_pct,
    calculate_usg_pct,
    calculate_game_score,
    calculate_pir,
)


def test_possessions_simple_calculation():
    # Standard formula: FGA (65) + 0.44 * FTA (33) - ORB (13) + TOV (14) = 65 + 14.52 - 13 + 14 = 80.52
    poss = calculate_possessions_simple(fga=65, fta=33, orb=13, tov=14)
    assert poss == 80.52


def test_possessions_bilateral():
    poss = calculate_possessions_bilateral(80.0, 76.0)
    assert poss == 78.0


def test_pace_40m_regulation():
    # 40-minute regulation game: Pace equals possessions
    pace = calculate_pace_40m(possessions_bilateral=75.0, game_duration_seconds=2400)
    assert pace == 75.0


def test_pace_40m_overtime():
    # 45-minute (1 OT) game: Pace normalizes down to 40 min rate
    # 40 * (90.0 / 45.0) = 80.0
    pace = calculate_pace_40m(possessions_bilateral=90.0, game_duration_seconds=2700)
    assert pace == 80.0


def test_four_factors():
    # eFG%: (FGM=30 + 0.5 * 3PM=10) / FGA=60 = 35 / 60 = 0.5833
    efg = calculate_efg_pct(fgm=30, fg3m=10, fga=60)
    assert efg == 0.5833

    # TOV%: 12 / (60 + 0.44 * 20 + 12) = 12 / 80.8 = 0.1485
    tov_pct = calculate_tov_pct(tov=12, fga=60, fta=20)
    assert tov_pct == 0.1485

    # ORB%: 15 / (15 + 25) = 15 / 40 = 0.375
    orb_pct = calculate_orb_pct(team_orb=15, opp_drb=25)
    assert orb_pct == 0.375

    # FTr: 20 / 60 = 0.3333
    ftr = calculate_ftr(fta=20, fga=60)
    assert ftr == 0.3333


def test_ratings_calculation():
    # ORtg: 100 * (85 / 75.0) = 113.33
    ratings = calculate_ratings(pts=85, opp_pts=70, possessions=75.0)
    assert ratings["ortg"] == 113.33
    assert ratings["drtg"] == 93.33
    assert ratings["net_rtg"] == 20.0


def test_individual_metrics():
    # TS%: 25 / (2 * (15 + 0.44 * 8)) = 25 / (2 * 18.52) = 25 / 37.04 = 0.6749
    ts = calculate_ts_pct(pts=25, fga=15, fta=8)
    assert ts == 0.6749

    # Game Score
    gmsc = calculate_game_score(
        pts=20, fgm=7, fga=12, ftm=4, fta=5,
        orb=2, drb=6, stl=2, ast=4, blk=1, pf=2, tov=1
    )
    assert isinstance(gmsc, float)
    assert gmsc > 0

    # PIR
    pir = calculate_pir(
        pts=20, trb=8, ast=4, stl=2, blk=1, fouls_drawn=5,
        fga=12, fgm=7, fta=5, ftm=4, tov=1, pf=2
    )
    # Pos: 20 + 8 + 4 + 2 + 1 + 5 = 40
    # Neg: (12-7) + (5-4) + 1 + 2 = 5 + 1 + 1 + 2 = 9
    # PIR = 40 - 9 = 31
    assert pir == 31


def test_edge_cases_zeros():
    # Zero attempts should return 0.0 or None, never crash
    assert calculate_efg_pct(0, 0, 0) == 0.0
    assert calculate_ftr(0, 0) == 0.0
    assert calculate_ts_pct(0, 0, 0) is None
    assert calculate_usg_pct(0, 0, 0, 0.0, 50, 20, 10) == 0.0
    assert calculate_ortg(0, 0.0) == 0.0
