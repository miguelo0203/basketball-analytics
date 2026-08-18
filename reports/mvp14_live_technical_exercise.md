# Technical Interview Live-Coding Exercise: 20–30 Minute Practical Assessment
## Basketball Data Engineering & Analytical Query Assessment

**Target Role**: Basketball Data Analyst / Quantitative Scout  
**Assessment Duration**: 20–30 Minutes  
**Tooling**: Python 3, SQL / DuckDB, Pandas  

---

# 1. The Interview Problem Statement

> *"Using our certified DuckDB warehouse, write a clean Python/SQL query to compute the Four Factors and possession-adjusted Net Rating for Spain across two historical tournament eras (2005–2015 vs. 2016–2024). Explain the basketball meaning of the metric shift and identify any potential sample size or confounding risks."*

---

# 2. Dataset & Tables to Use

- **Database Path**: `data/03_validated/basketball_analytics.duckdb`
- **Tables**: `fact_game`, `fact_team_game`
- **Parquet Mart Alternative**: `data/04_marts/analytics/mart_team_game_analytics.parquet`

---

# 3. Expected Reasoning & Mathematical Formulation

An analyst must calculate Dean Oliver's Four Factors per 100 possessions:
1. **Pace**: $\text{Possessions} = \text{FGA} + 0.44 \times \text{FTA} - \text{ORB} + \text{TOV}$
2. **Effective Field Goal % (eFG%)**: $\frac{\text{FGM} + 0.5 \times \text{3PM}}{\text{FGA}}$
3. **Turnover Rate (TOV%)**: $\frac{\text{TOV}}{\text{Possessions}}$
4. **Offensive Rebound Rate (ORB%)**: $\frac{\text{ORB}}{\text{ORB} + \text{Opp DREB}}$
5. **Free Throw Rate (FTR)**: $\frac{\text{FTA}}{\text{FGA}}$
6. **Net Rating**: $\frac{\text{Points Scored} - \text{Points Conceded}}{\text{Possessions}} \times 100$

---

# 4. Reference Python / SQL Solution

```python
import duckdb
import pandas as pd

def run_era_comparison(db_path: str = "data/03_validated/basketball_analytics.duckdb") -> pd.DataFrame:
    """Compute pace-adjusted Four Factors for Spain by tournament era."""
    con = duckdb.connect(db_path, read_only=True)
    
    query = """
    SELECT 
        CASE WHEN t.year <= 2015 THEN 'Era 1 (2005-2015)' ELSE 'Era 2 (2016-2024)' END AS era,
        COUNT(*) AS games_played,
        ROUND(AVG(tg.possessions_bilateral), 1) AS avg_pace,
        ROUND(AVG(tg.ortg), 1) AS offensive_rating,
        ROUND(AVG(tg.drtg), 1) AS defensive_rating,
        ROUND(AVG(tg.net_rtg), 1) AS net_rating,
        ROUND(SUM(tg.fgm + 0.5 * tg.fg3m) * 100.0 / SUM(tg.fga), 1) AS efg_pct,
        ROUND(AVG(tg.tov_pct * 100.0), 1) AS tov_pct,
        ROUND(AVG(tg.orb_pct * 100.0), 1) AS orb_pct,
        ROUND(AVG(tg.ftr * 100.0), 1) AS ft_rate
    FROM fact_team_game tg
    JOIN fact_game g ON tg.game_id = g.game_id
    JOIN dim_tournament t ON g.tournament_id = t.tournament_id
    WHERE tg.is_spain = TRUE
    GROUP BY era
    ORDER BY era;
    """
    df = con.execute(query).df()
    con.close()
    return df

if __name__ == "__main__":
    df = run_era_comparison()
    print(df.to_markdown(index=False))
```

---

# 5. Expected Output

```text
| era               | games_played | avg_pace | offensive_rating | defensive_rating | net_rating | efg_pct | tov_pct | orb_pct | ft_rate |
|:------------------|:-------------|:---------|:-----------------|:-----------------|:-----------|:--------|:--------|:--------|:--------|
| Era 1 (2005-2015) | 76           | 73.4     | 114.8            | 98.4             | 16.4       | 53.2    | 14.1    | 32.4    | 34.2    |
| Era 2 (2016-2024) | 66           | 71.8     | 109.2            | 99.8             | 9.4        | 52.8    | 13.2    | 29.8    | 25.8    |
```

---

# 6. Common Mistakes to Look Out For

1. **Sum of Averages Error**: Averaging $\text{eFG}\%$ across games instead of dividing total made shots by total attempts ($\frac{\sum \text{FGM}}{\sum \text{FGA}}$).
2. **Improper Rebounding Denominator**: Calculating $\text{ORB}\%$ as $\frac{\text{ORB}}{\text{Total Team Rebounds}}$ rather than $\frac{\text{Team ORB}}{\text{Team ORB} + \text{Opp DREB}}$.
3. **Pace Distortion**: Comparing raw points per game instead of possessions per 100 possessions.
4. **Ignoring FIBA Rules**: Using NBA $0.44 \times \text{FTA}$ without understanding bonus foul structures.

---

# 7. What a Strong Candidate Answer Sounds Like

> *"The query shows that Spain's Net Rating declined from +16.4 in Era 1 to +9.4 in Era 2. However, this was not caused by a collapse in field goal shooting (eFG% remained stable at 53.2% vs 52.8%). The structural difference is Dean Oliver's fourth factor: Free Throw Rate dropped from 34.2% to 25.8% (-8.4%). In Era 1, post touches drew high foul volume; in Era 2, perimeter pick-and-rolls produced fewer trips to the line. As an analyst, my takeaway for the coaching staff is that our modern half-court offense needs designed rim-pressure sets to generate free throws when outside shots aren't falling."*
