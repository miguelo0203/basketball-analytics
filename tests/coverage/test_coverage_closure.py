"""Coverage closure and complete universe verification tests for MVP-0.1."""

import pytest
import duckdb
import yaml
from pathlib import Path
from bs4 import BeautifulSoup
from src.config import VALIDATED_DB_PATH, CONFIG_DIR
from src.parsers.eurobasket_match_parser import parse_match_table
from src.validation.coverage_audit import CoverageAuditEngine
from src.domain.enums import ValidationStatus
from src.domain.models import TeamGame
from src.validation.qa_engine import QAEngine

MANIFEST_PATH = CONFIG_DIR / "expected_tournament_manifest.yaml"


def test_coverage_audit_100_percent_closure():
    """Verify that the Coverage Audit Engine certifies 100% complete coverage for all 8 EuroBaskets."""
    audit_engine = CoverageAuditEngine()
    df = audit_engine.run_audit(scope="mvp0")

    assert len(df) == 8, f"Expected 8 MVP-0 EuroBasket tournaments, found {len(df)}"
    assert df["missing_games"].sum() == 0, f"Expected 0 missing games, found {df['missing_games'].sum()}"
    assert df["duplicated_games"].sum() == 0, f"Expected 0 duplicated games, found {df['duplicated_games'].sum()}"
    assert df["promoted_games"].sum() == 559, f"Expected 559 promoted games, found {df['promoted_games'].sum()}"
    assert all(status == "COMPLETE" for status in df["status"]), "All tournaments must be status COMPLETE"


def test_database_foreign_keys_and_valid_ids():
    """Verify that all promoted games and team-games reference valid dimensions in DuckDB."""
    con = duckdb.connect(str(VALIDATED_DB_PATH), read_only=True)
    try:
        # Check invalid tournament references
        invalid_tourneys = con.execute("""
            SELECT COUNT(*) FROM fact_game g
            LEFT JOIN dim_tournament t ON g.tournament_id = t.tournament_id
            WHERE t.tournament_id IS NULL
        """).fetchone()[0]
        assert invalid_tourneys == 0, f"Found {invalid_tourneys} games referencing invalid tournaments"

        # Check invalid home team references
        invalid_home = con.execute("""
            SELECT COUNT(*) FROM fact_game g
            LEFT JOIN dim_team t ON g.home_team_id = t.canonical_team_id
            WHERE t.canonical_team_id IS NULL
        """).fetchone()[0]
        assert invalid_home == 0, f"Found {invalid_home} games referencing invalid home teams"

        # Check invalid away team references
        invalid_away = con.execute("""
            SELECT COUNT(*) FROM fact_game g
            LEFT JOIN dim_team t ON g.away_team_id = t.canonical_team_id
            WHERE t.canonical_team_id IS NULL
        """).fetchone()[0]
        assert invalid_away == 0, f"Found {invalid_away} games referencing invalid away teams"

        # Verify exactly 2 team-game rows per game
        mismatched_tgs = con.execute("""
            SELECT g.game_id, COUNT(tg.team_game_id) AS tg_count
            FROM fact_game g
            LEFT JOIN fact_team_game tg ON g.game_id = tg.game_id
            GROUP BY g.game_id
            HAVING COUNT(tg.team_game_id) != 2
        """).fetchall()
        assert len(mismatched_tgs) == 0, f"Found {len(mismatched_tgs)} games without exactly 2 team-game rows"
    finally:
        con.close()


def test_parser_real_2011_missing_fixture():
    """Verify parsing of 2011 Group E second round match fixture."""
    html_snippet = """
    <table>
        <tr><th>11 September 2011</th><th>Spain 84 - 59 France</th><th>Siemens Arena, Vilnius</th></tr>
        <tr><td>Scoring by quarter: 23-14, 20-18, 27-16, 14-11</td></tr>
        <tr><td>Pts: Navarro 16 Rebs: M. Gasol 7 Asts: Navarro 4</td></tr>
        <tr><td>Pts: Seraphin 18 Rebs: Diaw 5 Asts: Batum 3</td></tr>
    </table>
    """
    soup = BeautifulSoup(html_snippet, "html.parser")
    table = soup.find("table")
    parsed = parse_match_table(table, "eurobasket_2011", "Group E")

    assert parsed is not None
    assert parsed["home_team_id"] == "ESP"
    assert parsed["away_team_id"] == "FRA"
    assert parsed["home_score"] == 84
    assert parsed["away_score"] == 59
    assert parsed["overtimes"] == 0


def test_parser_real_2013_missing_fixture():
    """Verify parsing of 2013 Knockout Quarter-Final match fixture."""
    html_snippet = """
    <table>
        <tr><th>19 September 2013</th><th>Croatia 84 - 72 Ukraine</th><th>Arena Stozice, Ljubljana</th></tr>
        <tr><td>Scoring by quarter: 22-22, 29-13, 19-26, 14-11</td></tr>
        <tr><td>Pts: Simon 23 Rebs: Ukic 5 Asts: Draper 6</td></tr>
        <tr><td>Pts: Jeter 19 Rebs: Kravtsov 6 Asts: Jeter 6</td></tr>
    </table>
    """
    soup = BeautifulSoup(html_snippet, "html.parser")
    table = soup.find("table")
    parsed = parse_match_table(table, "eurobasket_2013", "Knockout Stage")

    assert parsed is not None
    assert parsed["home_team_id"] == "CRO"
    assert parsed["away_team_id"] == "UKR"
    assert parsed["home_score"] == 84
    assert parsed["away_score"] == 72
    assert parsed["overtimes"] == 0


def test_parser_2022_double_ot_fixture():
    """Verify parsing of 2022 Double Overtime fixture with template artifacts."""
    html_snippet = """
    <table>
        <tr><th>4 September 2022</th><th>Lithuania 107 - 109 0 (2OT) Germany</th><th>Lanxess Arena, Cologne</th></tr>
        <tr><td>Scoring by quarter: 19-19, 22-27, 24-20, 24-23, Overtime: 7-7, 11-13</td></tr>
        <tr><td>Pts: Valanciunas 34 Rebs: Valanciunas 14 Asts: Valanciunas 5</td></tr>
        <tr><td>Pts: Wagner 32 Rebs: Wagner 8 Asts: Schroder 8</td></tr>
    </table>
    """
    soup = BeautifulSoup(html_snippet, "html.parser")
    table = soup.find("table")
    parsed = parse_match_table(table, "eurobasket_2022", "Group B")

    assert parsed is not None
    assert parsed["home_team_id"] == "LTU"
    assert parsed["away_team_id"] == "GER"
    assert parsed["home_score"] == 107
    assert parsed["away_score"] == 109
    assert parsed["overtimes"] == 2


def test_quarantine_enforcement_on_synthetic_malformed_match(sample_team_game_regulation):
    """Verify that a malformed synthetic match is quarantined and blocked from promotion."""
    bad_dict = sample_team_game_regulation.model_dump()
    bad_dict["team_player_seconds_accounted"] = 8000  # Impossible minutes (8000s vs 12000s)
    bad_tg = TeamGame(**bad_dict)

    qa = QAEngine()
    status, issues = qa.validate_team_game(bad_tg, overtimes=0)
    assert status == ValidationStatus.QUARANTINED
    assert len(issues) > 0
    assert any(i.qa_flag == "MINUTES_ACCOUNTING_MISMATCH" for i in issues)
