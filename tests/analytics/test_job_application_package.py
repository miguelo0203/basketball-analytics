"""Automated Tests for the Real-World Job Application Package.

Validates:
1. Candidate profile, CV master, and 1-page CV exist.
2. LinkedIn profile and post files exist.
3. Outreach strategy and all 7 standardized outreach messages exist.
4. All 6 interview preparation guides exist.
5. 5-minute project demo script exists.
6. Why Me and Skills Gap analysis exist.
7. Application tracker CSV exists with valid headers.
8. Final job application audit report exists.
9. Zero forbidden overclaiming phrases across all job search materials.
"""

from pathlib import Path
import pytest

from src.config import PROJECT_ROOT, REPORTS_DIR


@pytest.fixture(scope="module")
def job_search_dir() -> Path:
    """Fixture providing portfolio/job_search directory."""
    return PROJECT_ROOT / "portfolio" / "job_search"


@pytest.fixture(scope="module")
def pres_dir() -> Path:
    """Fixture providing portfolio/presentation directory."""
    return PROJECT_ROOT / "portfolio" / "presentation"


@pytest.fixture(scope="module")
def reports_dir() -> Path:
    """Fixture providing reports directory."""
    return REPORTS_DIR


def test_candidate_profile_and_cv_files_exist(job_search_dir: Path):
    """Verify candidate_profile.md, cv_master.md, and cv_one_page.md exist."""
    assert (job_search_dir / "candidate_profile.md").exists()
    assert (job_search_dir / "cv_master.md").exists()
    assert (job_search_dir / "cv_one_page.md").exists()
    
    cv_content = (job_search_dir / "cv_master.md").read_text(encoding="utf-8")
    assert "Basketball Data Analyst" in cv_content
    assert "Sports Data Analyst" in cv_content
    assert "LightGBM" in cv_content
    assert "DuckDB" in cv_content


def test_linkedin_package_files_exist(job_search_dir: Path):
    """Verify linkedin_profile.md and linkedin_post.md exist."""
    assert (job_search_dir / "linkedin_profile.md").exists()
    assert (job_search_dir / "linkedin_post.md").exists()
    
    post_content = (job_search_dir / "linkedin_post.md").read_text(encoding="utf-8")
    assert "International Basketball Analytics" in post_content
    assert "Four Factors" in post_content


def test_outreach_strategy_and_messages_exist(job_search_dir: Path):
    """Verify outreach_strategy.md and all 7 outreach files exist with placeholders."""
    assert (job_search_dir / "outreach_strategy.md").exists()
    
    outreach_dir = job_search_dir / "outreach"
    expected_files = [
        "01_club_application.md",
        "02_analyst_networking.md",
        "03_coach_message.md",
        "04_sports_director_message.md",
        "05_company_application.md",
        "06_linkedin_connection.md",
        "07_follow_up.md"
    ]
    for f in expected_files:
        f_path = outreach_dir / f
        assert f_path.exists(), f"Missing outreach file: {f}"
        content = f_path.read_text(encoding="utf-8")
        assert "[PERSON]" in content or "[CLUB]" in content or "[PROJECT LINK]" in content


def test_interview_preparation_suite_exists(job_search_dir: Path):
    """Verify all 6 interview preparation guides exist."""
    interview_dir = job_search_dir / "interview"
    expected_guides = [
        "01_project_walkthrough.md",
        "02_technical_questions.md",
        "03_basketball_questions.md",
        "04_methodology_defense.md",
        "05_weaknesses_and_limitations.md",
        "06_why_basketball_analytics.md"
    ]
    for g in expected_guides:
        g_path = interview_dir / g
        assert g_path.exists(), f"Missing interview guide: {g}"
        assert len(g_path.read_text(encoding="utf-8")) > 150


def test_five_minute_demo_exists(pres_dir: Path):
    """Verify 5_minute_project_demo.md exists and covers timing sections."""
    demo_path = pres_dir / "5_minute_project_demo.md"
    assert demo_path.exists(), "5_minute_project_demo.md missing"
    content = demo_path.read_text(encoding="utf-8")
    assert "0:00–0:30" in content
    assert "4:30–5:00" in content


def test_why_me_and_skills_gap_exist(job_search_dir: Path):
    """Verify why_me.md and skills_gap.md exist."""
    assert (job_search_dir / "why_me.md").exists()
    assert (job_search_dir / "skills_gap.md").exists()


def test_application_tracker_csv_valid(job_search_dir: Path):
    """Verify application_tracker.csv exists with correct header columns."""
    tracker_path = job_search_dir / "application_tracker.csv"
    assert tracker_path.exists(), "application_tracker.csv missing"
    header = tracker_path.read_text(encoding="utf-8").strip().split(",")
    expected_headers = [
        "date", "organization", "country", "competition", "contact", "role",
        "application_type", "github_sent", "cv_sent", "linkedin_contact",
        "response", "follow_up_date", "status", "notes"
    ]
    assert header == expected_headers


def test_final_job_application_audit_exists(reports_dir: Path):
    """Verify final_job_application_audit.md exists and approves application package."""
    audit_path = reports_dir / "final_job_application_audit.md"
    assert audit_path.exists(), "final_job_application_audit.md missing"
    content = audit_path.read_text(encoding="utf-8")
    assert "READY FOR JOB APPLICATION" in content
    assert "1.145" in content


def test_no_forbidden_overclaims_in_application_package(job_search_dir: Path):
    """Verify absence of prohibited overclaiming phrases across application suite."""
    banned_words = [
        "ai coach", "replaces the coach", "adivina el ganador",
        "predice el futuro con certeza", "100% de acierto garantizado",
        "revolutionary ai", "perfect prediction"
    ]
    check_files = [
        job_search_dir / "candidate_profile.md",
        job_search_dir / "cv_master.md",
        job_search_dir / "cv_one_page.md",
        job_search_dir / "linkedin_profile.md",
        job_search_dir / "linkedin_post.md",
        job_search_dir / "why_me.md",
        job_search_dir / "skills_gap.md"
    ]
    for p in check_files:
        if p.exists():
            content = p.read_text(encoding="utf-8").lower()
            for b in banned_words:
                assert b not in content, f"Forbidden phrase '{b}' found in {p.name}"
