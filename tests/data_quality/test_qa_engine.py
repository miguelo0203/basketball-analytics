"""Tests for the Data Quality Engine and basketball accounting assertions."""

import pytest
from src.domain.enums import ValidationStatus, ValidationSeverity
from src.domain.models import TeamGame
from src.validation.qa_engine import QAEngine
from src.validation.minutes_validator import (
    get_expected_team_seconds,
    validate_team_minutes,
)


def test_minute_accounting_rules():
    # Regulation: 200 player minutes = 12000s
    assert get_expected_team_seconds(0) == 12000
    # 1 OT: 225 player minutes = 13500s (200 + 25*1 = 225)
    assert get_expected_team_seconds(1) == 13500
    # 2 OT: 250 player minutes = 15000s (200 + 25*2 = 250)
    assert get_expected_team_seconds(2) == 15000

    # Test validator directly
    ok, _ = validate_team_minutes(12000, overtimes=0, tolerance_seconds=0)
    assert ok is True

    ok_ot, _ = validate_team_minutes(13500, overtimes=1, tolerance_seconds=0)
    assert ok_ot is True

    bad, msg = validate_team_minutes(12000, overtimes=1, tolerance_seconds=60)
    assert bad is False
    assert "Minute accounting error" in msg


def test_qa_engine_valid_regulation_game(sample_team_game_regulation):
    qa = QAEngine(minute_tolerance_seconds=60)
    status, issues = qa.validate_team_game(sample_team_game_regulation, overtimes=0)
    assert status == ValidationStatus.VALIDATED
    assert len(issues) == 0


def test_qa_engine_valid_overtime_game(sample_team_game_1_ot):
    qa = QAEngine(minute_tolerance_seconds=60)
    status, issues = qa.validate_team_game(sample_team_game_1_ot, overtimes=1)
    assert status == ValidationStatus.VALIDATED
    assert len(issues) == 0


def test_qa_engine_catches_ball_math_mismatch(sample_team_game_regulation):
    # Corrupt score: PTS 95 -> 100 while shots remain identical
    bad_data = sample_team_game_regulation.model_dump()
    bad_data["pts"] = 100
    corrupt_team_game = TeamGame(**bad_data)

    qa = QAEngine()
    status, issues = qa.validate_team_game(corrupt_team_game, overtimes=0)
    assert status == ValidationStatus.QUARANTINED
    assert any(i.qa_flag == "BALL_MATH_MISMATCH" for i in issues)
    assert any(i.severity == ValidationSeverity.CRITICAL for i in issues)


def test_qa_engine_catches_minute_mismatch(sample_team_game_regulation):
    # Corrupt minutes: 10,000s instead of 12,000s
    bad_data = sample_team_game_regulation.model_dump()
    bad_data["team_player_seconds_accounted"] = 10000
    corrupt_team_game = TeamGame(**bad_data)

    qa = QAEngine()
    status, issues = qa.validate_team_game(corrupt_team_game, overtimes=0)
    assert status == ValidationStatus.QUARANTINED
    assert any(i.qa_flag == "MINUTES_ACCOUNTING_MISMATCH" for i in issues)
