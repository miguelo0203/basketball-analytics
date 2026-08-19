# Technical Reproducibility Guide
## Deterministic Setup & Execution Instructions

**Status**: Formally Certified Reproducibility Specification  
**Environment**: Python 3.10+ (Tested on Python 3.14 64-bit on Windows / Linux / macOS) & R 4.4+  
**Database**: DuckDB in-process columnar database & Apache Parquet  

---

# 1. Quick Start Installation

```bash
# 1. Clone repository from your public repository URL
git clone <PUBLIC_REPOSITORY_URL>
cd basketball-analytics

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

# 2. Database & Data Provenance Initialization

The complete historical dataset is pre-packaged and validated within the repository:
- **DuckDB Warehouse Path**: `data/03_validated/basketball_analytics.duckdb` (12 relational tables)
- **Analytical Marts**: `data/04_analytics/*.parquet` (11 columnar marts)
- **Raw Immutable Hashes**: Verified against SHA-256 signatures in `data/01_raw/`.

To inspect the database structure directly in Python:
```python
import duckdb
con = duckdb.connect("data/03_validated/basketball_analytics.duckdb", read_only=True)
print(con.execute("SHOW TABLES;").df())
con.close()
```

---

# 3. One-Command Master Execution Runner

Run the full end-to-end verification pipeline (environment check, database validation, R statistical layer, and full test suite):

```bash
python scripts/run_project.py
```

---

# 4. Running the Interactive Streamlit Analyst Workspace

Launch the operational decision workspace locally:

```bash
streamlit run src/analytics/mvp10_analyst_workspace.py
```
- **Access**: Open browser at `http://localhost:8501`.
- **Flagship Walkthrough**: Select the Beijing 2008 Spain vs. USA pre-game evidence state.

---

# 5. Running the Complete Automated Test Suite

Execute all 227 unit, integration, and regression tests across all 26 test modules:

```bash
python -m pytest tests -q
```
*Expected Output: `227 passed (100% pass rate)`.*

---

# 6. Data Licensing & Open-Source Attribution

- All match records and boxscores represent publicly available historical international senior men's basketball tournament data (FIBA EuroBasket, World Cup, Olympic Games 2005–2024).
- No proprietary club data, commercial API keys, or private feeds are required to execute any pipeline or test in this repository.
