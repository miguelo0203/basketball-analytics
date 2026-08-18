"""Ball-math and scoring accounting assertions."""

from typing import Tuple, List


def validate_scoring_math(
    pts: int,
    fg2m: int,
    fg3m: int,
    ftm: int,
) -> Tuple[bool, str]:
    """Verify that points match made shot values: PTS == 2*2PM + 3*3PM + FTM."""
    expected_pts = 2 * fg2m + 3 * fg3m + ftm
    if pts != expected_pts:
        return False, f"Score mismatch: recorded PTS={pts} != computed={expected_pts} (2PM={fg2m}, 3PM={fg3m}, FTM={ftm})"
    return True, "OK"


def validate_field_goal_math(
    fgm: int,
    fga: int,
    fg2m: int,
    fg2a: int,
    fg3m: int,
    fg3a: int,
) -> Tuple[bool, List[str]]:
    """Verify that FG totals match 2PT and 3PT component sums and bounds."""
    errors = []
    if fgm != (fg2m + fg3m):
        errors.append(f"FGM mismatch: FGM={fgm} != 2PM({fg2m}) + 3PM({fg3m})")
    if fga != (fg2a + fg3a):
        errors.append(f"FGA mismatch: FGA={fga} != 2PA({fg2a}) + 3PA({fg3a})")
    if fga < fgm:
        errors.append(f"Impossible shots: FGA({fga}) < FGM({fgm})")
    if fg2a < fg2m:
        errors.append(f"Impossible 2PT shots: 2PA({fg2a}) < 2PM({fg2m})")
    if fg3a < fg3m:
        errors.append(f"Impossible 3PT shots: 3PA({fg3a}) < 3PM({fg3m})")

    return (len(errors) == 0), errors


def validate_rebound_math(
    orb: int,
    drb: int,
    trb: int,
) -> Tuple[bool, str]:
    """Verify that total rebounds equal offensive plus defensive rebounds."""
    if trb != (orb + drb):
        return False, f"TRB mismatch: TRB={trb} != ORB({orb}) + DRB({drb})"
    return True, "OK"
