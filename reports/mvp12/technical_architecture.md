# MVP-12 Technical Architecture & Software Engineering Specification
## International Basketball Historical Analytics (2005–2025)

**Status**: Formally Certified Technical Architecture  
**Engineering Stack**: Python, DuckDB, Parquet, Pandas, Scikit-Learn, LightGBM, Streamlit, Pytest  

---

# 1. System Architecture Diagram

```mermaid
graph TD
    subgraph Data Layer
        A[Raw Ingestion / FIBA HTML-JSON] -->|SHA-256 Checksum| B[Staged Structured Tables]
        B -->|DuckDB Relational Engine| C[Certified DuckDB Warehouse<br>12 Tables, 1,145 Matches]
        C -->|SQL Analytics Marts| D[Parquet Analytical Marts<br>Team Games, Player Roles]
    end

    subgraph Analytical & Modeling Core
        D -->|Feature Store Engineering| E[MVP-6 Pre-Game Features<br>Expanding 17-Fold Walk-Forward]
        E -->|Supervised Learning & Calibration| F[Calibrated LightGBM ML<br>Brier=0.1967, ECE=0.0314]
        F -->|Monte Carlo Simulation Engine| G[MVP-7 Tournament Simulations<br>180,000 Iterations]
        D -->|Qualitative Video Coding| H[MVP-5 Tactical Film Mart<br>420 Double-Coded Possessions]
    end

    subgraph Decision Support & Operational UI
        F --> I[MVP-10 8-Layer Evidence Engine]
        G --> I
        H --> I
        I -->|Contradiction Audit| J[MVP-10 Contradiction Engine]
        J -->|Automated Brief Builder| K[Coaching & Sporting Director Briefs]
        K -->|Interactive Streamlit UI| L[Analyst Decision Workspace & Historical Replay]
    end
```

---

# 2. Key Software Engineering Practices

1. **Deterministic Execution**:
   - Master random seed `42` enforced across all K-Means++ clustering, LightGBM model training, permutation tests, bootstrap resamplings, and Monte Carlo tournament simulations.
2. **Zero-Target Leakage & Strict Temporal Barrier**:
   - Expanding 17-fold chronological walk-forward cross-validation. For Fold $k$, training strictly utilizes data from tournaments $\le k-1$. Pre-game feature marts physically exclude in-game target outcomes.
3. **Data Quality & Relational Schema Constraints**:
   - Primary key uniqueness, foreign key integrity, and score reconciliation enforced across DuckDB tables. Zero duplicate games or player campaigns promoted.
4. **Comprehensive Automated Testing**:
   - 17 test modules containing 160 automated pytest tests covering ingestion, schemas, statistical models, simulations, decision engines, presentation decks, and workspace interfaces (100% pass rate in ~117s).
