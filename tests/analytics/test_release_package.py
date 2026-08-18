"""Automated Tests for the Final Portfolio Release & Outreach Package.

Validates:
1. Final project status document (FINAL_STATUS.md) declares PORTFOLIO READY.
2. Reproducibility guide (REPRODUCIBILITY.md) exists and specifies environment.
3. Flagship case study (portfolio/flagship_case.md) contains required tactical sections.
4. Curated public figures and figure guide exist in portfolio/figures/.
5. All 7 interview package modules exist in interview/.
6. All 6 career application package modules exist in career/.
7. Public claim registry (final_public_claim_registry.csv) exists with proper tiers.
8. LinkedIn long-form case study exists.
9. Complete absence of prohibited overclaiming words across all public assets.
"""

from pathlib import Path
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


def test_final_status_declared_ready(root_dir: Path):
    """Verify FINAL_STATUS.md exists and certifies PORTFOLIO READY."""
    status_path = root_dir / "FINAL_STATUS.md"
    assert status_path.exists(), "FINAL_STATUS.md missing"
    content = status_path.read_text(encoding="utf-8")
    assert "PROJECT STATUS: PORTFOLIO READY" in content
    assert "Strongest Asset" in content
    assert "Job-Search Strategy" in content


def test_reproducibility_guide_exists(root_dir: Path):
    """Verify REPRODUCIBILITY.md exists with environment setup instructions."""
    rep_path = root_dir / "REPRODUCIBILITY.md"
    assert rep_path.exists(), "REPRODUCIBILITY.md missing"
    content = rep_path.read_text(encoding="utf-8")
    assert "Python 3" in content
    assert "DuckDB" in content
    assert "streamlit run" in content
    assert "pytest" in content


def test_flagship_case_study_structure(root_dir: Path):
    """Verify portfolio/flagship_case.md contains standard tactical sections."""
    case_path = root_dir / "portfolio" / "flagship_case.md"
    assert case_path.exists(), "portfolio/flagship_case.md missing"
    content = case_path.read_text(encoding="utf-8")
    assert ("Tactical Decision Question" in content or "Pregunta de Baloncesto" in content)
    assert ("Pre-Game Information State" in content or "Información Disponible Antes del Salto Inicial" in content)
    assert ("Three Strongest Evidence Signals" in content or "Evidencia Estadística" in content)
    assert ("Critical Tactical Contradiction" in content or "Contradicción Táctica" in content)
    assert ("Post-Game Process Review" in content or "Qué Funcionó" in content)


def test_public_figures_and_guide_exist(root_dir: Path):
    """Verify curated figures and figure guide exist in portfolio/figures/."""
    guide_path = root_dir / "portfolio" / "figure_guide.md"
    assert guide_path.exists(), "portfolio/figure_guide.md missing"
    
    fig_dir = root_dir / "portfolio" / "figures"
    assert fig_dir.exists(), "portfolio/figures/ directory missing"
    
    required_figures = [
        "fig1_evidence_pipeline.png",
        "fig2_probability_calibration.png",
        "fig3_player_archetypes_pca.png",
        "fig4_four_factors_evolution.png",
        "fig5_contradiction_engine.png"
    ]
    for fig in required_figures:
        assert (fig_dir / fig).exists(), f"Missing figure: {fig}"


def test_interview_package_completeness(root_dir: Path):
    """Verify all 7 interview modules exist in interview/."""
    interview_dir = root_dir / "interview"
    assert interview_dir.exists(), "interview/ directory missing"
    
    required_docs = [
        "01_project_pitch.md",
        "02_flagship_case.md",
        "03_technical_questions.md",
        "04_basketball_questions.md",
        "05_data_engineering_questions.md",
        "06_methodology_defense.md",
        "07_questions_to_ask_employer.md"
    ]
    for doc in required_docs:
        p = interview_dir / doc
        assert p.exists(), f"Missing interview doc: {doc}"
        assert len(p.read_text(encoding="utf-8")) > 100


def test_career_package_completeness(root_dir: Path):
    """Verify all 6 career outreach modules exist in career/."""
    career_dir = root_dir / "career"
    assert career_dir.exists(), "career/ directory missing"
    
    required_docs = [
        "basketball_data_analyst_cv_bullets.md",
        "linkedin_about.md",
        "linkedin_featured_section.md",
        "cold_outreach_template.md",
        "internship_outreach_template.md",
        "project_description_100_words.md"
    ]
    for doc in required_docs:
        p = career_dir / doc
        assert p.exists(), f"Missing career doc: {doc}"
        assert len(p.read_text(encoding="utf-8")) > 80


def test_public_claim_registry_valid(reports_dir: Path):
    """Verify public claim registry CSV exists and has valid structure."""
    reg_path = reports_dir / "final_public_claim_registry.csv"
    assert reg_path.exists(), "final_public_claim_registry.csv missing"
    content = reg_path.read_text(encoding="utf-8")
    assert "claim_id,claim_text,category,metric_value,tier" in content
    assert "GREEN" in content
    assert "YELLOW" in content
    assert "RED" in content


def test_linkedin_case_study_exists(root_dir: Path):
    """Verify portfolio/linkedin_case_study.md exists and is properly formatted."""
    article_path = root_dir / "portfolio" / "linkedin_case_study.md"
    assert article_path.exists(), "portfolio/linkedin_case_study.md missing"
    content = article_path.read_text(encoding="utf-8")
    assert "Beijing 2008" in content
    assert "Four Factors" in content
    assert "What This Demonstrates" in content


def test_no_banned_language_in_public_release_assets(root_dir: Path):
    """Verify no banned marketing buzzwords appear in public assets."""
    banned_words = [
        "ai coach", "replaces the coach", "replaces coaches",
        "guaranteed insights", "100% accurate", "revolutionary ai",
        "predicts future games with certainty", "validated superiority"
    ]
    check_files = [
        root_dir / "README.md",
        root_dir / "FINAL_STATUS.md",
        root_dir / "REPRODUCIBILITY.md",
        root_dir / "portfolio" / "landing_page.md",
        root_dir / "portfolio" / "flagship_case.md",
        root_dir / "portfolio" / "linkedin_case_study.md",
        root_dir / "career" / "basketball_data_analyst_cv_bullets.md",
        root_dir / "career" / "linkedin_about.md",
        root_dir / "interview" / "01_project_pitch.md"
    ]
    for p in check_files:
        if p.exists():
            content = p.read_text(encoding="utf-8").lower()
            for w in banned_words:
                assert w not in content, f"Banned word '{w}' found in {p.name}"
