"""Automated Tests for MVP-13 Final Professionalization & Sanity Pass.

Validates:
1. Root README professional positioning (WHO, WHAT, WHY, SCOPE, TECH, OUTPUT, LIMITATION).
2. Demonstrated vs Simulated boundary documentation.
3. Day-One 30-day analyst integration roadmap.
4. Pre-game coaching report template and Sporting Director strategic template.
5. 5-minute live demo script and 14-stage master project map (MVP-0 to MVP-13).
6. Absence of forbidden overclaiming marketing language in public documents.
7. Verification that all markdown-referenced file paths exist on disk.
"""

from pathlib import Path
import re
import pytest

from src.config import PROJECT_ROOT, REPORTS_DIR


@pytest.fixture(scope="module")
def root_dir() -> Path:
    """Fixture providing root project directory."""
    return PROJECT_ROOT


@pytest.fixture(scope="module")
def reports_dir() -> Path:
    """Fixture providing reports directory."""
    return REPORTS_DIR


def test_readme_professional_positioning(root_dir: Path):
    """Verify root README.md has clear professional positioning banner."""
    readme_path = root_dir / "README.md"
    assert readme_path.exists(), "Root README.md missing"
    content = readme_path.read_text(encoding="utf-8")
    assert "WHO:" in content
    assert "WHAT:" in content
    assert "WHY:" in content
    assert "SCOPE:" in content
    assert "TECHNOLOGY:" in content
    assert "OUTPUT:" in content
    assert "LIMITATION:" in content


def test_demonstrated_vs_simulated_boundary_exists(reports_dir: Path):
    """Verify boundary document explicitly separates capabilities."""
    doc_path = reports_dir / "mvp13_demonstrated_vs_simulated.md"
    assert doc_path.exists(), "mvp13_demonstrated_vs_simulated.md missing"
    content = doc_path.read_text(encoding="utf-8")
    assert "Demonstrated Capabilities" in content
    assert "Simulated Operational Workflow" in content
    assert "Not Yet Demonstrated" in content


def test_day_one_workflow_exists(reports_dir: Path):
    """Verify day-one integration plan covers the 30-day roadmap."""
    doc_path = reports_dir / "mvp13_day_one_analyst_workflow.md"
    assert doc_path.exists(), "mvp13_day_one_analyst_workflow.md missing"
    content = doc_path.read_text(encoding="utf-8")
    assert "Days 1–3" in content or "Days 1-3" in content
    assert "Week 1" in content
    assert "Week 2" in content
    assert "Week 3" in content
    assert "Week 4" in content


def test_coaching_report_template_exists(reports_dir: Path):
    """Verify pre-game coaching report template contains key tactical sections."""
    doc_path = reports_dir / "mvp13_coaching_report_template.md"
    assert doc_path.exists(), "mvp13_coaching_report_template.md missing"
    content = doc_path.read_text(encoding="utf-8")
    assert "Opponent Identity" in content
    assert "Three Things That Matter" in content
    assert "Three Questions for the Coaching Staff" in content
    assert "Uncertainty & Methodological Limitations" in content


def test_sporting_director_template_exists(reports_dir: Path):
    """Verify sporting director strategic template covers balance and succession."""
    doc_path = reports_dir / "mvp13_sporting_director_report_template.md"
    assert doc_path.exists(), "mvp13_sporting_director_report_template.md missing"
    content = doc_path.read_text(encoding="utf-8")
    assert "Functional Archetype Distribution" in content
    assert "Succession Planning" in content
    assert "Strategic Questions for Basketball Leadership" in content


def test_final_demo_script_exists(reports_dir: Path):
    """Verify master 5-minute live demonstration script exists."""
    doc_path = reports_dir / "mvp13_final_demo_script.md"
    assert doc_path.exists(), "mvp13_final_demo_script.md missing"
    content = doc_path.read_text(encoding="utf-8")
    assert "0:00–0:30" in content or "0:00-0:30" in content
    assert "4:15–5:00" in content or "4:15-5:00" in content
    assert "Beijing 2008" in content


def test_project_map_exists_and_covers_all_mvps(reports_dir: Path):
    """Verify project map covers all 15 stages from MVP-0 to MVP-14."""
    doc_path = reports_dir / "mvp13_project_map.md"
    assert doc_path.exists(), "mvp13_project_map.md missing"
    content = doc_path.read_text(encoding="utf-8")
    for i in range(0, 15):
        assert f"MVP-{i}" in content or f"MVP-0.{i}" in content, f"Missing MVP-{i} in project map"


def test_no_banned_overclaim_language_in_public_docs(root_dir: Path):
    """Verify public-facing README and landing page contain no banned hype words."""
    readme_content = (root_dir / "README.md").read_text(encoding="utf-8").lower()
    landing_content = (root_dir / "portfolio" / "landing_page.md").read_text(encoding="utf-8").lower()
    
    banned_words = [
        "ai coach", "replaces the coach", "replaces coaches",
        "guaranteed insights", "100% accurate", "revolutionary ai",
        "predicts future games with certainty", "validated superiority"
    ]
    for w in banned_words:
        assert w not in readme_content, f"Banned word '{w}' found in README.md"
        assert w not in landing_content, f"Banned word '{w}' found in landing_page.md"


def test_landing_page_structure(root_dir: Path):
    """Verify portfolio landing page exists and has structured sections."""
    lp_path = root_dir / "portfolio" / "landing_page.md"
    assert lp_path.exists(), "portfolio/landing_page.md missing"
    content = lp_path.read_text(encoding="utf-8")
    assert "The Problem" in content
    assert "The Approach" in content
    assert "What I Built" in content
    assert "Flagship Demonstration" in content
    assert "Limitations & Professional Boundaries" in content


def test_referenced_repository_paths_exist(root_dir: Path):
    """Verify key documents linked in README actually exist on disk."""
    key_paths = [
        root_dir / "reports" / "mvp13_day_one_analyst_workflow.md",
        root_dir / "reports" / "mvp13_coaching_report_template.md",
        root_dir / "reports" / "mvp13_sporting_director_report_template.md",
        root_dir / "reports" / "mvp13_demonstrated_vs_simulated.md",
        root_dir / "reports" / "mvp13_project_map.md",
        root_dir / "reports" / "mvp12" / "interview_answers.md",
        root_dir / "portfolio" / "index.md",
        root_dir / "portfolio" / "landing_page.md"
    ]
    for p in key_paths:
        assert p.exists(), f"Linked path missing: {p}"
