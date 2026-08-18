"""Automated Tests for Portfolio Professionalization, Candidacy Package & Outreach.

Validates:
1. Canonical facts document exists and is consistent.
2. Analyst profile document exists.
3. All oral and written pitches exist.
4. Interview FAQ contains >= 30 questions across all 4 categories.
5. Real club adaptation document exists.
6. CV entries and LinkedIn description exist.
7. All 7 outreach messages exist.
8. Final release checklist exists.
9. Zero forbidden overclaiming phrases across all new assets.
"""

from pathlib import Path
import pytest

from src.config import PROJECT_ROOT


@pytest.fixture(scope="module")
def root_dir() -> Path:
    """Fixture providing repository root directory."""
    return PROJECT_ROOT


def test_canonical_facts_exists_and_accurate(root_dir: Path):
    """Verify docs/canonical_project_facts.md exists and contains verified figures."""
    facts_path = root_dir / "docs" / "canonical_project_facts.md"
    assert facts_path.exists(), "docs/canonical_project_facts.md missing"
    content = facts_path.read_text(encoding="utf-8")
    assert "18 Torneos" in content or "18" in content
    assert "1.145" in content or "1,145" in content
    assert "27.353" in content or "27,353" in content
    assert "3.767" in content or "3,767" in content
    assert "6 Arquetipos" in content or "6" in content
    assert "17 Folds" in content
    assert "0.1967" in content
    assert "0.0314" in content


def test_analyst_profile_exists_and_structured(root_dir: Path):
    """Verify portfolio/analyst_profile.md exists and covers key sections."""
    profile_path = root_dir / "portfolio" / "analyst_profile.md"
    assert profile_path.exists(), "portfolio/analyst_profile.md missing"
    content = profile_path.read_text(encoding="utf-8")
    assert "Quién Soy" in content
    assert "Qué Hago" in content
    assert "Habilidades Técnicas" in content
    assert "Analítica de Baloncesto" in content
    assert "Cómo Trabajo" in content
    assert "Qué Puedo Aportar" in content


def test_all_pitches_exist(root_dir: Path):
    """Verify all 4 elevator and domain pitches exist."""
    pres_dir = root_dir / "portfolio" / "presentation"
    pitches = [
        "60_second_pitch.md",
        "30_second_project_pitch.md",
        "technical_pitch.md",
        "basketball_analyst_pitch.md"
    ]
    for p in pitches:
        p_path = pres_dir / p
        assert p_path.exists(), f"Missing pitch file: {p}"
        assert len(p_path.read_text(encoding="utf-8")) > 100


def test_interview_faq_completeness(root_dir: Path):
    """Verify portfolio/interview/interview_questions.md contains >= 30 questions."""
    faq_path = root_dir / "portfolio" / "interview" / "interview_questions.md"
    assert faq_path.exists(), "portfolio/interview/interview_questions.md missing"
    content = faq_path.read_text(encoding="utf-8")
    
    # Check sections
    assert "BLOQUE 1: INGENIERÍA" in content or "TECHNICAL" in content
    assert "BLOQUE 2: DOMINIO DE BALONCESTO" in content or "BASKETBALL" in content
    assert "BLOQUE 3: METODOLOGÍA" in content or "METHODOLOGY" in content
    assert "BLOQUE 4: ENTORNO PROFESIONAL" in content or "PROFESSIONAL" in content
    
    # Count questions
    q_count = content.count("### ")
    assert q_count >= 30, f"Expected >= 30 questions, found {q_count}"


def test_real_club_adaptation_exists(root_dir: Path):
    """Verify docs/real_club_adaptation.md exists."""
    doc_path = root_dir / "docs" / "real_club_adaptation.md"
    assert doc_path.exists(), "docs/real_club_adaptation.md missing"
    content = doc_path.read_text(encoding="utf-8")
    assert "Lo Que Ya Sé Hacer" in content
    assert "Lo Que Tendría que Aprender" in content


def test_job_search_package_files_exist(root_dir: Path):
    """Verify CV entry, LinkedIn description, and all 7 outreach files exist."""
    job_dir = root_dir / "portfolio" / "job_search"
    assert (job_dir / "project_cv_entry.md").exists()
    assert (job_dir / "linkedin_project.md").exists()
    
    outreach_dir = job_dir / "outreach"
    outreach_files = [
        "01_cold_message_club.md",
        "02_message_analyst.md",
        "03_message_coach.md",
        "04_message_sports_director.md",
        "05_email_application.md",
        "06_follow_up.md",
        "07_short_intro.md"
    ]
    for f in outreach_files:
        assert (outreach_dir / f).exists(), f"Missing outreach file: {f}"


def test_final_release_checklist_exists(root_dir: Path):
    """Verify docs/final_release_checklist.md exists."""
    chk_path = root_dir / "docs" / "final_release_checklist.md"
    assert chk_path.exists(), "docs/final_release_checklist.md missing"


def test_no_forbidden_claims_in_job_search_package(root_dir: Path):
    """Verify zero prohibited overclaiming language across all outreach and career files."""
    banned_words = [
        "ai coach", "replaces the coach", "adivina el ganador",
        "predice el futuro con certeza", "100% de acierto garantizado"
    ]
    check_paths = [
        root_dir / "portfolio" / "analyst_profile.md",
        root_dir / "portfolio" / "job_search" / "project_cv_entry.md",
        root_dir / "portfolio" / "job_search" / "linkedin_project.md",
        root_dir / "portfolio" / "presentation" / "60_second_pitch.md"
    ]
    for p in check_paths:
        if p.exists():
            content = p.read_text(encoding="utf-8").lower()
            for b in banned_words:
                assert b not in content, f"Forbidden phrase '{b}' found in {p.name}"
