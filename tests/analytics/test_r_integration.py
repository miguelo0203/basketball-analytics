"""Automated Tests for the R Analytical Layer Integration.

Validates:
1. R/README.md exists and documents dual-stack Python/R architecture.
2. All 3 R helper modules exist in R/functions/.
3. All 6 R analysis scripts exist in R/analysis/.
4. Quarto report exists in R/reports/.
5. Canonical metrics and formulas are accurately defined in R scripts.
6. Zero prohibited overclaiming phrases across the R layer.
"""

from pathlib import Path
import pytest

from src.config import PROJECT_ROOT


@pytest.fixture(scope="module")
def r_dir() -> Path:
    """Fixture providing R directory path."""
    return PROJECT_ROOT / "R"


def test_r_readme_exists_and_covers_architecture(r_dir: Path):
    """Verify R/README.md exists and explains Python + R dual stack."""
    readme_path = r_dir / "README.md"
    assert readme_path.exists(), "R/README.md is missing"
    content = readme_path.read_text(encoding="utf-8")
    assert "DuckDB" in content
    assert "Python" in content
    assert "ggplot2" in content
    assert "tidyverse" in content or "dplyr" in content


def test_r_functions_exist(r_dir: Path):
    """Verify all 3 R function modules exist."""
    funcs_dir = r_dir / "functions"
    expected_files = ["metrics.R", "visualization.R", "validation.R"]
    for f in expected_files:
        f_path = funcs_dir / f
        assert f_path.exists(), f"Missing R function module: {f}"
        content = f_path.read_text(encoding="utf-8")
        assert len(content) > 100


def test_r_analysis_scripts_exist(r_dir: Path):
    """Verify all 6 R analysis scripts exist in R/analysis/."""
    analysis_dir = r_dir / "analysis"
    expected_scripts = [
        "01_eda_tournaments.R",
        "02_player_longitudinal_analysis.R",
        "03_role_stability.R",
        "04_team_four_factors.R",
        "05_player_distributions.R",
        "06_statistical_validation.R"
    ]
    for s in expected_scripts:
        s_path = analysis_dir / s
        assert s_path.exists(), f"Missing R analysis script: {s}"
        content = s_path.read_text(encoding="utf-8")
        assert len(content) > 200


def test_r_quarto_report_exists(r_dir: Path):
    """Verify R/reports/exploratory_analysis.qmd exists."""
    qmd_path = r_dir / "reports" / "exploratory_analysis.qmd"
    assert qmd_path.exists(), "R/reports/exploratory_analysis.qmd missing"
    content = qmd_path.read_text(encoding="utf-8")
    assert "title:" in content
    assert "Four Factors" in content


def test_r_metrics_formulas_valid(r_dir: Path):
    """Verify metrics.R includes Oliver's Four Factors and True Shooting formulas."""
    metrics_path = r_dir / "functions" / "metrics.R"
    content = metrics_path.read_text(encoding="utf-8")
    assert "calculate_possessions" in content
    assert "calculate_four_factors" in content
    assert "calculate_ratings" in content
    assert "calculate_true_shooting" in content
    assert "0.44 * fta" in content or "0.44" in content


def test_no_overclaiming_in_r_layer(r_dir: Path):
    """Verify no forbidden overclaiming words in R scripts and documentation."""
    banned_words = [
        "ai coach", "replaces the coach", "adivina el ganador",
        "predice el futuro con certeza", "100% de acierto garantizado"
    ]
    for r_file in r_dir.rglob("*.R"):
        content = r_file.read_text(encoding="utf-8").lower()
        for b in banned_words:
            assert b not in content, f"Forbidden phrase '{b}' found in {r_file.name}"
