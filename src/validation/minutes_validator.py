"""Minute and overtime accounting validation engine operating in seconds."""

from typing import Tuple


def get_expected_team_seconds(overtimes: int = 0) -> int:
    """Calculate expected single-team player seconds: (200 + 25 * OT) * 60."""
    return (200 + 25 * overtimes) * 60


def get_expected_game_seconds(overtimes: int = 0) -> int:
    """Calculate expected combined game player seconds across both teams: (400 + 50 * OT) * 60."""
    return (400 + 50 * overtimes) * 60


def validate_team_minutes(
    accounted_seconds: int,
    overtimes: int = 0,
    tolerance_seconds: int = 60,
) -> Tuple[bool, str]:
    """Validate that the sum of team player seconds matches FIBA regulation + OT accounting."""
    expected = get_expected_team_seconds(overtimes)
    diff = abs(accounted_seconds - expected)
    if diff > tolerance_seconds:
        return False, (
            f"Minute accounting error: Accounted seconds ({accounted_seconds}s / {accounted_seconds/60:.1f}m) "
            f"differs from expected ({expected}s / {expected/60:.1f}m for {overtimes} OT) by {diff}s > {tolerance_seconds}s tolerance."
        )
    return True, "OK"


def validate_game_minutes(
    combined_seconds: int,
    overtimes: int = 0,
    tolerance_seconds: int = 120,
) -> Tuple[bool, str]:
    """Validate that combined player seconds across both teams match total expected game seconds."""
    expected = get_expected_game_seconds(overtimes)
    diff = abs(combined_seconds - expected)
    if diff > tolerance_seconds:
        return False, (
            f"Game minute accounting error: Combined seconds ({combined_seconds}s) "
            f"differs from expected ({expected}s for {overtimes} OT) by {diff}s > {tolerance_seconds}s tolerance."
        )
    return True, "OK"
