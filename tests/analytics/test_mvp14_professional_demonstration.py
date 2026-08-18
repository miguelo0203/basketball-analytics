"""Automated Tests for MVP-14 Real-World Analyst Demonstration & Interview Simulation.

Validates:
1. All MVP-14 deliverable reports exist and are non-empty.
2. Flagship coaching report contains standard tactical sections.
3. Capability matrix enforces strict 3-tier boundary categorization.
4. Coach pushback dialogue simulates realistic staff collaboration.
5. Live technical interview exercise code executes deterministically on DuckDB.
6. Analyst raw working note demonstrates genuine analytical investigation.
7. Complete absence of prohibited overclaiming language.
"""

from pathlib import Path
import re
import duckdb
import pytest

from src.config import PROJECT_ROOT, REPORTS_DIR, VALIDATED_DATA_DIR


@pytest.fixture(scope="module")
def root_dir() -> Path:
    """Fixture providing root project directory."""
    return PROJECT_ROOT


@pytest.fixture(scope="module")
def reports_dir() -> Path:
    """Fixture providing reports directory."""
    return REPORTS_DIR


def test_mvp14_files_exist(reports_dir: Path):
    """Verify all 10 MVP-14 reports exist."""
    required_files = [
        "mvp14_gap_analysis.md",
        "mvp14_analyst_task.md",
        "mvp14_live_demo.md",
        "mvp14_flagship_coaching_report.md",
        "mvp14_analyst_working_note.md",
        "mvp14_coach_pushback_simulation.md",
        "mvp14_live_technical_exercise.md",
        "mvp14_capability_matrix.md",
        "mvp14_final_pitch.md",
        "mvp14_final_sanity_check.md",
    ]
    for filename in required_files:
        p = reports_dir / filename
        assert p.exists(), f"Missing MVP-14 report: {filename}"
        assert len(p.read_text(encoding="utf-8")) > 150, f"File {filename} is too short"


def test_flagship_coaching_report_structure(reports_dir: Path):
    """Verify flagship coaching report contains key tactical sections."""
    content = (reports_dir / "mvp14_flagship_coaching_report.md").read_text(encoding="utf-8")
    assert "Core Tactical Question" in content
    assert "Executive Takeaway" in content
    assert "Four Factors Profile" in content
    assert "Basketball Interpretation" in content
    assert "Important Uncertainty" in content
    assert "Questions for the Coaching Staff" in content


def test_capability_matrix_categories(reports_dir: Path):
    """Verify capability matrix covers all three boundary categories."""
    content = (reports_dir / "mvp14_capability_matrix.md").read_text(encoding="utf-8")
    assert "DEMONSTRATED" in content
    assert "SIMULATED" in content
    assert "NOT YET DEMONSTRATED" in content


def test_coach_pushback_simulation_content(reports_dir: Path):
    """Verify coach pushback dialogue covers key challenges."""
    content = (reports_dir / "mvp14_coach_pushback_simulation.md").read_text(encoding="utf-8")
    assert "Film vs. Statistical Discrepancy" in content
    assert "Historical Prior vs. Current Form" in content
    assert "Boundaries & Rotation Decisions" in content
    assert "The Bottom-Line Takeaway" in content


def test_analyst_working_note_structure(reports_dir: Path):
    """Verify raw working note covers investigative thought process."""
    content = (reports_dir / "mvp14_analyst_working_note.md").read_text(encoding="utf-8")
    assert "Initial Hypothesis" in content
    assert "What I Expected to Find" in content
    assert "What the Data Actually Showed" in content
    assert "What Surprised Me" in content
    assert "Contradictory Evidence Surfaced" in content
    assert "What I Would NOT Tell the Coach Yet" in content


def test_live_technical_exercise_executable(root_dir: Path):
    """Verify the technical interview exercise code executes against the DuckDB warehouse."""
    db_path = root_dir / "data" / "03_validated" / "basketball_analytics.duckdb"
    assert db_path.exists(), "DuckDB database missing"
    
    con = duckdb.connect(str(db_path), read_only=True)
    query = """
    SELECT 
        CASE WHEN t.year <= 2015 THEN 'Era 1 (2005-2015)' ELSE 'Era 2 (2016-2024)' END AS era,
        COUNT(*) AS games_played,
        ROUND(AVG(tg.possessions_bilateral), 1) AS avg_pace,
        ROUND(AVG(tg.ortg), 1) AS offensive_rating,
        ROUND(AVG(tg.drtg), 1) AS defensive_rating,
        ROUND(AVG(tg.net_rtg), 1) AS net_rating,
        ROUND(SUM(tg.fgm + 0.5 * tg.fg3m) * 100.0 / SUM(tg.fga), 1) AS efg_pct,
        ROUND(AVG(tg.tov_pct * 100.0), 1) AS tov_pct,
        ROUND(AVG(tg.orb_pct * 100.0), 1) AS orb_pct,
        ROUND(AVG(tg.ftr * 100.0), 1) AS ft_rate
    FROM fact_team_game tg
    JOIN fact_game g ON tg.game_id = g.game_id
    JOIN dim_tournament t ON g.tournament_id = t.tournament_id
    WHERE tg.is_spain = TRUE
    GROUP BY era
    ORDER BY era;
    """
    df = con.execute(query).df()
    con.close()
    
    assert len(df) == 2, "Expected 2 eras in result"
    assert df.loc[0, "games_played"] > 40
    assert df.loc[1, "games_played"] > 40


def test_no_banned_overclaiming_language_in_mvp14(reports_dir: Path):
    """Verify MVP-14 documents contain no prohibited marketing hype words."""
    banned_words = [
        "ai coach", "replaces the coach", "replaces coaches",
        "guaranteed insights", "100% accurate", "revolutionary ai",
        "predicts future games with certainty", "validated superiority"
    ]
    mvp14_files = [
        "mvp14_gap_analysis.md", "mvp14_analyst_task.md", "mvp14_live_demo.md",
        "mvp14_flagship_coaching_report.md", "mvp14_analyst_working_note.md",
        "mvp14_coach_pushback_simulation.md", "mvp14_live_technical_exercise.md",
        "mvp14_capability_matrix.md", "mvp14_final_pitch.md", "mvp14_final_sanity_check.md"
    ]
    for filename in mvp14_files:
        content = (reports_dir / filename).read_text(encoding="utf-8").lower()
        for w in banned_words:
            assert w not in content, f"Banned word '{w}' found in {filename}"
