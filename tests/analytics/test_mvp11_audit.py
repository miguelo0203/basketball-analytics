"""Automated Tests for MVP-11 Adversarial Professional Portfolio Audit.

Validates:
1. Complete claim registry CSV exists and has all required columns.
2. Temporal integrity audit report exists and details walk-forward boundaries.
3. Statistical audit report exists and evaluates ML and simulation claims.
4. Data quality audit report exists and reconciles warehouse entities.
5. Professional realism audit report exists and categorizes capabilities.
6. Master adversarial audit and final readiness reports exist with final verdict.
"""

from pathlib import Path
import pandas as pd
import pytest

from src.config import REPORTS_DIR


@pytest.fixture(scope="module")
def reports_dir() -> Path:
    """Fixture providing reports directory path."""
    return REPORTS_DIR


def test_claim_registry_structure(reports_dir: Path):
    """Verify claim registry CSV exists and has proper schema."""
    reg_path = reports_dir / "mvp11_claim_registry.csv"
    assert reg_path.exists(), "mvp11_claim_registry.csv missing"
    df = pd.read_csv(reg_path)
    expected_cols = [
        "claim_id", "claim_text", "source_file", "source_dataset",
        "calculation_method", "reproducibility_status", "statistical_validity",
        "temporal_validity", "risk_level", "recommended_action"
    ]
    for col in expected_cols:
        assert col in df.columns, f"Missing column {col} in claim registry"
    assert len(df) >= 15


def test_temporal_integrity_audit_exists(reports_dir: Path):
    """Verify temporal integrity report exists and covers walk-forward isolation."""
    doc_path = reports_dir / "mvp11_temporal_integrity_audit.md"
    assert doc_path.exists(), "mvp11_temporal_integrity_audit.md missing"
    content = doc_path.read_text(encoding="utf-8")
    assert "Walk-Forward" in content
    assert "Anti-Hindsight" in content


def test_statistical_audit_exists(reports_dir: Path):
    """Verify statistical audit report exists and reviews LightGBM and simulation metrics."""
    doc_path = reports_dir / "mvp11_statistical_audit.md"
    assert doc_path.exists(), "mvp11_statistical_audit.md missing"
    content = doc_path.read_text(encoding="utf-8")
    assert "0.1967" in content
    assert "0.0314" in content
    assert "Double-Dipping" in content or "Post-Clustering" in content


def test_data_quality_audit_exists(reports_dir: Path):
    """Verify data quality audit report exists and reconciles entity cardinalities."""
    doc_path = reports_dir / "mvp11_data_quality_audit.md"
    assert doc_path.exists(), "mvp11_data_quality_audit.md missing"
    content = doc_path.read_text(encoding="utf-8")
    assert "1,145" in content
    assert "27,353" in content
    assert "4,350" in content


def test_professional_realism_audit_exists(reports_dir: Path):
    """Verify realism audit report separates demonstrated from simulated capabilities."""
    doc_path = reports_dir / "mvp11_professional_realism_audit.md"
    assert doc_path.exists(), "mvp11_professional_realism_audit.md missing"
    content = doc_path.read_text(encoding="utf-8")
    assert "DEMONSTRATED" in content
    assert "SIMULATED" in content
    assert "NOT DEMONSTRATED" in content


def test_final_readiness_verdict(reports_dir: Path):
    """Verify final readiness report produces a certified verdict."""
    doc_path = reports_dir / "mvp11_final_readiness_report.md"
    assert doc_path.exists(), "mvp11_final_readiness_report.md missing"
    content = doc_path.read_text(encoding="utf-8")
    assert "READY WITH QUALIFICATIONS" in content
    assert "Scorecard" in content
