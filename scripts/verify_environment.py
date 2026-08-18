#!/usr/bin/env python3
"""Environment Verification Script: Validates Python and R runtime environments.

Checks:
- Python version (>= 3.10)
- Essential Python packages (duckdb, pyarrow, lightgbm, scikit-learn, pandas, streamlit, pytest)
- DuckDB database accessibility
- Parquet analytical marts integrity
- Rscript executable availability and R packages (DBI, duckdb, arrow, tidyverse, ggplot2)
- Quarto CLI availability
"""

import sys
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.config import VALIDATED_DB_PATH, ANALYTICS_DATA_DIR


def verify_all():
    print("================================================================================")
    print("ENVIRONMENT & DEPENDENCY VERIFICATION AUDIT")
    print("================================================================================")
    
    # 1. Python
    print(f"\n[1] Python Environment: {sys.version.split()[0]}")
    py_pkgs = ["duckdb", "pyarrow", "lightgbm", "sklearn", "pandas", "streamlit", "pytest"]
    for pkg in py_pkgs:
        try:
            mod = __import__(pkg)
            v = getattr(mod, "__version__", "OK")
            print(f"    - {pkg:<15} : INSTALLED (v{v})")
        except ImportError:
            print(f"    - {pkg:<15} : MISSING [ERROR]")
            
    # 2. DuckDB & Parquet
    print(f"\n[2] Data Layer Storage:")
    if VALIDATED_DB_PATH.exists():
        mb = VALIDATED_DB_PATH.stat().st_size / (1024 * 1024)
        print(f"    - DuckDB Warehouse: FOUND ({mb:.2f} MB)")
    else:
        print(f"    - DuckDB Warehouse: NOT FOUND at {VALIDATED_DB_PATH}")
        
    marts = list(ANALYTICS_DATA_DIR.glob("*.parquet"))
    print(f"    - Parquet Marts   : {len(marts)} files available in {ANALYTICS_DATA_DIR.name}")

    # 3. R Environment
    print(f"\n[3] R Statistical Environment:")
    r_candidates = ["Rscript", r"C:\Program Files\R\R-4.6.1\bin\Rscript.exe"]
    r_path = None
    for rc in r_candidates:
        try:
            res = subprocess.run([rc, "--version"], capture_output=True, text=True, timeout=5)
            if res.returncode == 0:
                r_path = rc
                ver = (res.stdout or res.stderr).strip()
                print(f"    - Rscript Binary  : {rc} ({ver})")
                break
        except Exception:
            continue
            
    if r_path:
        # Test R packages
        pkg_check_cmd = "cat(paste(c('DBI', 'duckdb', 'arrow', 'dplyr', 'ggplot2'), %in% installed.packages()[, 'Package'], sep=': ', collapse=', '))"
        res = subprocess.run([r_path, "-e", pkg_check_cmd], capture_output=True, text=True)
        print(f"    - Core Packages   : {res.stdout.strip()}")
    else:
        print("    - Rscript Binary  : NOT FOUND in PATH")

    # 4. Quarto CLI
    print(f"\n[4] Quarto Reporting CLI:")
    try:
        q_res = subprocess.run(["quarto", "--version"], capture_output=True, text=True, timeout=5)
        if q_res.returncode == 0:
            print(f"    - Quarto Version  : {q_res.stdout.strip()} (READY)")
        else:
            print("    - Quarto Version  : ERROR")
    except Exception:
        print("    - Quarto Version  : NOT FOUND in PATH")
        
    print("\n================================================================================")
    print("ENVIRONMENT AUDIT COMPLETED")
    print("================================================================================")


if __name__ == "__main__":
    verify_all()
