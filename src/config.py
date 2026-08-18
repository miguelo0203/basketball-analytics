"""Configuration and path management for the analytics pipeline."""

from pathlib import Path
import os

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Core subdirectories
CONFIG_DIR = PROJECT_ROOT / "config"
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DIR = PROJECT_ROOT / "docs"
REPORTS_DIR = PROJECT_ROOT / "reports"
TESTS_DIR = PROJECT_ROOT / "tests"

# Layered data directories
RAW_DATA_DIR = DATA_DIR / "01_raw"
STAGING_DATA_DIR = DATA_DIR / "02_staging"
VALIDATED_DATA_DIR = DATA_DIR / "03_validated"
ANALYTICS_DATA_DIR = DATA_DIR / "04_analytics"
QUARANTINE_DATA_DIR = DATA_DIR / "quarantine"

# Database file paths
STAGING_DB_PATH = STAGING_DATA_DIR / "staging.duckdb"
VALIDATED_DB_PATH = VALIDATED_DATA_DIR / "basketball_analytics.duckdb"

# Master configuration files
TOURNAMENTS_CSV = CONFIG_DIR / "tournaments.csv"
RULE_SETS_CSV = CONFIG_DIR / "rule_sets.csv"
SOURCES_YAML = CONFIG_DIR / "sources.yaml"
TEAMS_CSV = CONFIG_DIR / "teams.csv"


def ensure_directories_exist() -> None:
    """Ensure all required directories exist."""
    for directory in [
        CONFIG_DIR,
        DATA_DIR,
        DOCS_DIR,
        REPORTS_DIR,
        TESTS_DIR,
        RAW_DATA_DIR,
        STAGING_DATA_DIR,
        VALIDATED_DATA_DIR,
        ANALYTICS_DATA_DIR,
        QUARANTINE_DATA_DIR,
    ]:
        directory.mkdir(parents=True, exist_ok=True)
