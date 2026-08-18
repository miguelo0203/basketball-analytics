"""Pace calculation engine normalized to FIBA 40-minute regulation duration."""


def calculate_pace_40m(possessions_bilateral: float, game_duration_seconds: int = 2400) -> float:
    """Calculate Pace normalized to standard FIBA 40-minute regulation.

    Formula: 40.0 * (possessions_bilateral / (game_duration_seconds / 60.0))
    """
    if game_duration_seconds <= 0:
        return 0.0
    minutes = game_duration_seconds / 60.0
    pace = 40.0 * (possessions_bilateral / minutes)
    return round(pace, 2)
