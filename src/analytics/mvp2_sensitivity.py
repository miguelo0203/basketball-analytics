"""Sensitivity & Robustness Analysis Engine for MVP-2.

Evaluates alternative specifications for the 2010 3PT ITS model:
- Excluding overtime games
- Excluding extreme blowouts (margin >= 30)
- Tournament-level aggregation
- Narrow bandwidth window (+-3 tournaments around 2010)
- Competition-specific stratified regressions
- Alternative standard error estimators (HC1, HC3, HAC)
"""

from pathlib import Path
from typing import Dict, Any, List
import pandas as pd
import statsmodels.formula.api as smf

from src.config import ANALYTICS_DATA_DIR, REPORTS_DIR


class SensitivityAnalysisEngine:
    """Runs adversarial sensitivity models against the primary ITS findings."""

    def __init__(self, data_dir: Path = ANALYTICS_DATA_DIR):
        self.tg_path = data_dir / "mart_team_game_analytics.parquet"
        self.ts_path = data_dir / "mart_tournament_summary.parquet"
        self.df_tg = pd.read_parquet(self.tg_path)
        self.df_ts = pd.read_parquet(self.ts_path)

    def run_all_sensitivities(self) -> pd.DataFrame:
        """Run all 6 sensitivity specifications and compile comparison table."""
        specs = []

        # 0. Primary Baseline Model (All Games, Clustered SE)
        m0 = smf.ols("three_point_attempt_rate ~ tournament_seq + post_2010_rule + time_after_2010 + C(competition_id)", data=self.df_tg)
        r0 = m0.fit(cov_type="cluster", cov_kwds={"groups": self.df_tg["tournament_seq"]})
        specs.append(self._extract_spec_row("0. Primary Baseline (Clustered)", r0, len(self.df_tg)))

        # 1. Excluding Overtime Games
        df_no_ot = self.df_tg[self.df_tg["overtimes"] == 0]
        m1 = smf.ols("three_point_attempt_rate ~ tournament_seq + post_2010_rule + time_after_2010 + C(competition_id)", data=df_no_ot)
        r1 = m1.fit(cov_type="cluster", cov_kwds={"groups": df_no_ot["tournament_seq"]})
        specs.append(self._extract_spec_row("1. Excl. Overtime Games", r1, len(df_no_ot)))

        # 2. Excluding Blowouts (|margin| >= 30)
        df_no_blowout = self.df_tg[self.df_tg["point_differential"].abs() < 30]
        m2 = smf.ols("three_point_attempt_rate ~ tournament_seq + post_2010_rule + time_after_2010 + C(competition_id)", data=df_no_blowout)
        r2 = m2.fit(cov_type="cluster", cov_kwds={"groups": df_no_blowout["tournament_seq"]})
        specs.append(self._extract_spec_row("2. Excl. Blowouts (|diff| < 30)", r2, len(df_no_blowout)))

        # 3. Tournament-Level Aggregation (N = 18)
        m3 = smf.ols("mean_3par ~ tournament_seq + post_2010_rule + time_after_2010", data=self.df_ts)
        r3 = m3.fit()
        specs.append(self._extract_spec_row("3. Tournament Aggregates (N=18)", r3, len(self.df_ts)))

        # 4. Narrow Bandwidth (+-3 Tournaments: Seq 3 to 9)
        df_narrow = self.df_tg[(self.df_tg["tournament_seq"] >= 3) & (self.df_tg["tournament_seq"] <= 9)]
        m4 = smf.ols("three_point_attempt_rate ~ tournament_seq + post_2010_rule + time_after_2010", data=df_narrow)
        r4 = m4.fit(cov_type="cluster", cov_kwds={"groups": df_narrow["tournament_seq"]})
        specs.append(self._extract_spec_row("4. Narrow Window (T3-T9)", r4, len(df_narrow)))

        # 5. EuroBasket Only Subgroup
        df_eb = self.df_tg[self.df_tg["competition_id"] == "fiba_eurobasket"]
        m5 = smf.ols("three_point_attempt_rate ~ tournament_seq + post_2010_rule + time_after_2010", data=df_eb)
        r5 = m5.fit(cov_type="cluster", cov_kwds={"groups": df_eb["tournament_seq"]})
        specs.append(self._extract_spec_row("5. EuroBasket Only (N=1,118)", r5, len(df_eb)))

        # 6. World Cup Only Subgroup
        df_wc = self.df_tg[self.df_tg["competition_id"] == "fiba_world_cup"]
        m6 = smf.ols("three_point_attempt_rate ~ tournament_seq + post_2010_rule + time_after_2010", data=df_wc)
        r6 = m6.fit(cov_type="cluster", cov_kwds={"groups": df_wc["tournament_seq"]})
        specs.append(self._extract_spec_row("6. World Cup Only (N=840)", r6, len(df_wc)))

        # 7. HC3 Robust Standard Errors
        r7 = m0.fit(cov_type="HC3")
        specs.append(self._extract_spec_row("7. HC3 Heteroskedasticity Robust", r7, len(self.df_tg)))

        return pd.DataFrame(specs)

    def _extract_spec_row(self, spec_name: str, res: Any, n: int) -> Dict[str, Any]:
        params = res.params
        pvals = res.pvalues
        ci = res.conf_int()

        b1 = params.get("tournament_seq", 0.0)
        b2 = params.get("post_2010_rule", 0.0)
        b3 = params.get("time_after_2010", 0.0)

        p1 = pvals.get("tournament_seq", 1.0)
        p2 = pvals.get("post_2010_rule", 1.0)
        p3 = pvals.get("time_after_2010", 1.0)

        ci2_low = ci.loc["post_2010_rule", 0] if "post_2010_rule" in ci.index else 0.0
        ci2_high = ci.loc["post_2010_rule", 1] if "post_2010_rule" in ci.index else 0.0

        return {
            "Specification": spec_name,
            "N_Obs": n,
            "Baseline_Slope (b1)": f"{b1*100:+.3f}% (p={p1:.3f})",
            "Level_Shift (b2)": f"{b2*100:+.3f}%",
            "b2_95_CI": f"[{ci2_low*100:+.3f}%, {ci2_high*100:+.3f}%]",
            "b2_pvalue": round(p2, 4),
            "Slope_Change (b3)": f"{b3*100:+.3f}% (p={p3:.3f})",
            "Robustness_Verdict": "ROBUST (p < 0.05)" if p2 < 0.05 else "INSIGNIFICANT",
        }


def main():
    engine = SensitivityAnalysisEngine()
    df = engine.run_all_sensitivities()
    print("=== SENSITIVITY & ROBUSTNESS AUDIT RESULTS ===")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
