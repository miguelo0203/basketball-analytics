"""Pytest suite verifying MVP-1 global tournament coverage, referential integrity, and regression protection."""

import pytest
import duckdb
import yaml
from pathlib import Path
from bs4 import BeautifulSoup

from src.config import VALIDATED_DB_PATH, CONFIG_DIR
from src.parsers.eurobasket_match_parser import parse_match_table, parse_compact_group_table

MANIFEST_PATH = CONFIG_DIR / "expected_tournament_manifest.yaml"


@pytest.fixture(scope="module")
def manifest():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def db_con():
    con = duckdb.connect(str(VALIDATED_DB_PATH), read_only=True)
    yield con
    con.close()


def test_manifest_integrity_mvp1(manifest):
    """Verify manifest defines exactly 18 tournaments with 1,145 total games."""
    all_tourneys = {**manifest["mvp0_tournaments"], **manifest["mvp1_tournaments"]}
    assert len(all_tourneys) == 18
    total_exp = sum(int(t["expected_games"]) for t in all_tourneys.values())
    assert total_exp == 1145


def test_mvp1_database_tournament_count(db_con):
    """Verify all 18 tournaments exist in dim_tournament."""
    count = db_con.execute("SELECT COUNT(*) FROM dim_tournament WHERE tournament_id != 'eurobasket_2025'").fetchone()[0]
    assert count == 18


def test_mvp1_game_coverage_exact(db_con, manifest):
    """Verify fact_game contains exactly 1,145 games matching manifest expectations."""
    total_games = db_con.execute("SELECT COUNT(*) FROM fact_game").fetchone()[0]
    assert total_games == 1145

    all_tourneys = {**manifest["mvp0_tournaments"], **manifest["mvp1_tournaments"]}
    games_per_t = db_con.execute("""
        SELECT tournament_id, COUNT(*) as cnt 
        FROM fact_game 
        GROUP BY tournament_id
    """).df()
    actual_map = dict(zip(games_per_t["tournament_id"], games_per_t["cnt"]))

    for t_id, meta in all_tourneys.items():
        exp = int(meta["expected_games"])
        act = actual_map.get(t_id, 0)
        assert act == exp, f"Tournament {t_id} mismatch: expected {exp}, got {act}"


def test_eurobasket_regression_protection(db_con):
    """Verify EuroBasket 2005-2022 baseline remains exactly 559 games with 0 regressions."""
    eb_games = db_con.execute("""
        SELECT COUNT(*) FROM fact_game 
        WHERE tournament_id LIKE 'eurobasket_%' AND tournament_id != 'eurobasket_2025'
    """).fetchone()[0]
    assert eb_games == 559


def test_worldcup_coverage_by_tournament(db_con):
    """Verify exact game counts for all 5 FIBA World Cups (420 games)."""
    wc_expected = {
        "worldcup_2006": 80,
        "worldcup_2010": 80,
        "worldcup_2014": 76,
        "worldcup_2019": 92,
        "worldcup_2023": 92,
    }
    for t_id, exp in wc_expected.items():
        cnt = db_con.execute("SELECT COUNT(*) FROM fact_game WHERE tournament_id = ?", [t_id]).fetchone()[0]
        assert cnt == exp, f"World Cup {t_id} mismatch: expected {exp}, got {cnt}"


def test_olympics_coverage_by_tournament(db_con):
    """Verify exact game counts for all 5 Olympic Tournaments (166 games)."""
    oly_expected = {
        "olympics_2008": 38,
        "olympics_2012": 38,
        "olympics_2016": 38,
        "olympics_2020": 26,
        "olympics_2024": 26,
    }
    for t_id, exp in oly_expected.items():
        cnt = db_con.execute("SELECT COUNT(*) FROM fact_game WHERE tournament_id = ?", [t_id]).fetchone()[0]
        assert cnt == exp, f"Olympics {t_id} mismatch: expected {exp}, got {cnt}"


def test_mvp1_team_game_cardinality(db_con):
    """Verify fact_team_game has exactly 2,290 rows and 2 rows per fact_game."""
    total_tg = db_con.execute("SELECT COUNT(*) FROM fact_team_game").fetchone()[0]
    assert total_tg == 2290

    # Ensure every game has exactly 2 team observations
    mismatches = db_con.execute("""
        SELECT game_id, COUNT(*) as cnt
        FROM fact_team_game
        GROUP BY game_id
        HAVING COUNT(*) != 2
    """).fetchall()
    assert len(mismatches) == 0


def test_foreign_key_referential_integrity(db_con):
    """Verify all teams referenced in fact_game and fact_team_game exist in dim_team."""
    orphan_games = db_con.execute("""
        SELECT g.game_id 
        FROM fact_game g
        LEFT JOIN dim_team h ON g.home_team_id = h.canonical_team_id
        LEFT JOIN dim_team a ON g.away_team_id = a.canonical_team_id
        WHERE h.canonical_team_id IS NULL OR a.canonical_team_id IS NULL
    """).fetchall()
    assert len(orphan_games) == 0

    orphan_tgs = db_con.execute("""
        SELECT tg.team_game_id
        FROM fact_team_game tg
        LEFT JOIN dim_team t ON tg.team_id = t.canonical_team_id
        LEFT JOIN dim_team o ON tg.opponent_id = o.canonical_team_id
        WHERE t.canonical_team_id IS NULL OR o.canonical_team_id IS NULL
    """).fetchall()
    assert len(orphan_tgs) == 0


def test_spain_game_identification(db_con):
    """Verify Spain (ESP) games are properly flagged across all tournaments."""
    spain_games = db_con.execute("""
        SELECT COUNT(DISTINCT game_id) 
        FROM fact_team_game 
        WHERE team_id = 'ESP' AND is_spain = TRUE
    """).fetchone()[0]
    assert spain_games > 0

    # Verify no non-Spain row has is_spain = True
    non_spain_err = db_con.execute("""
        SELECT COUNT(*) FROM fact_team_game
        WHERE team_id != 'ESP' AND is_spain = TRUE
    """).fetchone()[0]
    assert non_spain_err == 0


def test_parser_compact_table_fixture():
    """Verify compact summary table parser accurately extracts games."""
    sample_html = """
    <table class="wikitable">
      <tr>
        <td>19 August 2006</td>
        <td align="right"><b>Germany</b></td>
        <td align="center"><b>81</b>–70</td>
        <td>Japan</td>
        <td>Saitama Super Arena</td>
      </tr>
      <tr>
        <td>19 August 2006</td>
        <td align="right"><b>Angola</b></td>
        <td align="center"><b>83</b>–70</td>
        <td>Panama</td>
        <td>Saitama Super Arena</td>
      </tr>
    </table>
    """
    soup = BeautifulSoup(sample_html, "html.parser")
    table = soup.find("table")
    games = parse_compact_group_table(table, "worldcup_2006", "Preliminary Round")
    assert len(games) == 2
    assert games[0]["home_team_id"] == "GER"
    assert games[0]["away_team_id"] == "JPN"
    assert games[0]["home_score"] == 81
    assert games[0]["away_score"] == 70
    assert games[1]["home_team_id"] == "ANG"
    assert games[1]["away_team_id"] == "PAN"
    assert games[1]["home_score"] == 83
    assert games[1]["away_score"] == 70
