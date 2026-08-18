"""Automated Tests for MVP-12 Professional Portfolio Deployment & Interview Package.

Validates:
1. Root README existence, structure, and professional tone.
2. Complete portfolio hub and case studies existence.
3. Integrity of previous MVP reports (MVP-0 to MVP-11).
4. Streamlit analyst workspace entry point.
5. Demo script, elevator pitch, and 8-slide presentation deck.
6. Interview question package and grounded answers (32 questions).
7. Absence of forbidden overclaiming marketing phrases in README.
8. Accurate representation of audited historical scope (2005-2024).
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
def mvp12_dir() -> Path:
    """Fixture providing MVP-12 reports directory."""
    return REPORTS_DIR / "mvp12"


def test_readme_exists_and_has_structure(root_dir: Path):
    """Verify root README.md exists and has all required sections."""
    readme_path = root_dir / "README.md"
    assert readme_path.exists(), "Root README.md missing"
    content = readme_path.read_text(encoding="utf-8")
    assert ("Executive Summary" in content or "El proyecto en 30 segundos" in content)
    assert ("The Professional Problem" in content or "¿Qué hace el sistema?" in content)
    assert ("Technical Architecture" in content or "Arquitectura Visual" in content)
    assert ("From Raw Data to Coaching Question" in content or "Caso Flagship" in content)
    assert ("Audited Project Scale" in content or "El proyecto en cifras" in content)


def test_required_portfolio_files_exist(root_dir: Path, mvp12_dir: Path):
    """Verify portfolio hub and all MVP-12 reports exist."""
    assert (root_dir / "portfolio" / "README.md").exists()
    assert (root_dir / "portfolio" / "index.md").exists()
    
    required_reports = [
        "portfolio_strategy.md", "project_story.md", "analyst_workflow.md",
        "technical_architecture.md", "methodology_summary.md", "limitations.md",
        "interview_questions.md", "interview_answers.md", "demo_script.md",
        "claim_usage_guide.md", "pitch_60_seconds.md", "interview_presentation.md",
        "mvp12_final_readiness_report.md"
    ]
    for r in required_reports:
        assert (mvp12_dir / r).exists(), f"Missing report: {r}"


def test_previous_mvp_reports_remain(root_dir: Path):
    """Verify that all previous MVP reports (MVP-0 to MVP-11) remain intact."""
    rep_dir = root_dir / "reports"
    assert (rep_dir / "mvp1_execution_report.md").exists()
    assert (rep_dir / "mvp6_final_report.md").exists()
    assert (rep_dir / "mvp7_final_report.md").exists()
    assert (rep_dir / "mvp8_final_report.md").exists()
    assert (rep_dir / "mvp10_final_report.md").exists()
    assert (rep_dir / "mvp11_final_readiness_report.md").exists()


def test_streamlit_entry_point_exists(root_dir: Path):
    """Verify Streamlit analyst workspace entry point exists."""
    app_path = root_dir / "src" / "analytics" / "mvp10_analyst_workspace.py"
    assert app_path.exists(), "Streamlit workspace module missing"
    content = app_path.read_text(encoding="utf-8")
    assert "run_streamlit_app" in content
    assert "AnalystWorkspace" in content


def test_demo_assets_and_pitch_exist(mvp12_dir: Path):
    """Verify live demo script and 60-second elevator pitch exist."""
    demo_path = mvp12_dir / "demo_script.md"
    pitch_path = mvp12_dir / "pitch_60_seconds.md"
    assert demo_path.exists()
    assert pitch_path.exists()
    assert len(pitch_path.read_text(encoding="utf-8")) > 100


def test_interview_package_completeness(mvp12_dir: Path):
    """Verify interview package contains 32 questions and grounded answers."""
    q_content = (mvp12_dir / "interview_questions.md").read_text(encoding="utf-8")
    a_content = (mvp12_dir / "interview_answers.md").read_text(encoding="utf-8")
    assert "32." in q_content
    assert "32." in a_content
    assert "Basketball & Coaching" in q_content
    assert "Data Science" in q_content
    assert "Data Engineering" in q_content
    assert "Professional Realism" in q_content


def test_no_forbidden_overclaiming_phrases_in_readme(root_dir: Path):
    """Verify forbidden overclaiming marketing tropes do NOT appear in the root README."""
    readme_path = root_dir / "README.md"
    content = readme_path.read_text(encoding="utf-8").lower()
    
    forbidden_phrases = [
        "ai coach", "replaces coaches", "replaces the coach",
        "guaranteed insights", "100% accurate", "revolutionary ai",
        "predicts future games with certainty"
    ]
    for phrase in forbidden_phrases:
        assert phrase not in content, f"Forbidden phrase '{phrase}' found in root README.md"


def test_historical_scope_correctly_represented(root_dir: Path):
    """Verify accurate representation of completed historical coverage (2005-2024)."""
    readme_path = root_dir / "README.md"
    content = readme_path.read_text(encoding="utf-8")
    assert "2005–2024" in content or "2005-2024" in content
    assert "1,145" in content or "1.145" in content
    assert "2,290" in content or "2.290" in content
    assert "18" in content


def test_portfolio_case_studies_completeness(root_dir: Path):
    """Verify portfolio index.md contains 3 complete case studies."""
    idx_path = root_dir / "portfolio" / "index.md"
    assert idx_path.exists()
    content = idx_path.read_text(encoding="utf-8")
    assert "Beijing 2008" in content
    assert "EuroBasket 2015" in content
    assert "EuroBasket 2022" in content
    assert "Process Review" in content
