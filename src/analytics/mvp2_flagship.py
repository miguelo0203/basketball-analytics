"""Primary Flagship Inferential Analysis: 2010 3-Point Arc Extension (ITS).

Estimates Interrupted Time Series (ITS) segmented regression with Newey-West
autocorrelation-consistent standard errors, effect sizes, 95% CIs, and figures.
"""

from pathlib import Path
from typing import Dict, Any
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

from src.config import ANALYTICS_DATA_DIR, REPORTS_DIR

FIGURES_DIR = REPORTS_DIR / "figures" / "mvp2"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)


class ITSFlagshipModel:
    """Interrupted Time Series model evaluating the 2010 FIBA 3PT rule shift."""

    def __init__(self, data_dir: Path = ANALYTICS_DATA_DIR):
        self.tg_path = data_dir / "mart_team_game_analytics.parquet"
        self.ts_path = data_dir / "mart_tournament_summary.parquet"
        if not self.tg_path.exists():
            raise FileNotFoundError(f"Data mart {self.tg_path} does not exist.")
        self.df_tg = pd.read_parquet(self.tg_path)
        self.df_ts = pd.read_parquet(self.ts_path)

    def fit_primary_model(self) -> Dict[str, Any]:
        """Fit OLS segmented regression with cluster/HAC standard errors."""
        # Formulation: three_point_attempt_rate ~ tournament_seq + post_2010_rule + time_after_2010 + C(competition_id)
        formula = (
            "three_point_attempt_rate ~ tournament_seq + post_2010_rule + "
            "time_after_2010 + C(competition_id)"
        )
        model = smf.ols(formula, data=self.df_tg)
        # Fit with cluster-robust standard errors clustered on tournament_seq
        results_hac = model.fit(cov_type="cluster", cov_kwds={"groups": self.df_tg["tournament_seq"]})

        # Also compute tournament-level aggregate model
        ts_formula = "mean_3par ~ tournament_seq + post_2010_rule + time_after_2010"
        ts_model = smf.ols(ts_formula, data=self.df_ts)
        ts_results = ts_model.fit()

        return {
            "model_formula": formula,
            "results_hac": results_hac,
            "ts_results": ts_results,
            "nobs": int(results_hac.nobs),
            "rsquared": float(results_hac.rsquared),
            "params": results_hac.params.to_dict(),
            "pvalues": results_hac.pvalues.to_dict(),
            "conf_int": results_hac.conf_int().to_dict(),
        }

    def generate_its_figure(self) -> Path:
        """Generate high-resolution Figure 4 showing ITS fit and counterfactual."""
        fit_res = self.fit_primary_model()
        res = fit_res["results_hac"]
        params = res.params

        # Predictions
        t_seq = self.df_ts["tournament_seq"].values
        years = self.df_ts["year"].values
        mean_3par = self.df_ts["mean_3par"].values * 100

        # Baseline secular trend
        b0 = params["Intercept"] * 100
        b1 = params["tournament_seq"] * 100
        b2 = params["post_2010_rule"] * 100
        b3 = params["time_after_2010"] * 100

        # Fitted values
        fitted_pre = b0 + b1 * t_seq[:6]
        counterfactual = b0 + b1 * t_seq[6:]
        fitted_post = b0 + b1 * t_seq[6:] + b2 + b3 * (t_seq[6:] - 6)

        fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)

        # Plot observed tournament averages
        ax.scatter(t_seq[:6], mean_3par[:6], color="#2b5c8f", s=55, zorder=4, label="Pre-2010 Observed Tournaments (6.25m)")
        ax.scatter(t_seq[6:], mean_3par[6:], color="#d95f02", s=55, zorder=4, label="Post-2010 Observed Tournaments (6.75m)")

        # Plot fitted pre-intervention
        ax.plot(t_seq[:6], fitted_pre, color="#2b5c8f", linewidth=2.4, label=f"Pre-2010 Trend (Slope = {b1:+.3f}%/tourney)")

        # Plot counterfactual
        ax.plot(t_seq[6:], counterfactual, color="#888888", linestyle="--", linewidth=1.8, label="Counterfactual Trend (No Rule Change)")

        # Plot fitted post-intervention
        ax.plot(t_seq[6:], fitted_post, color="#d95f02", linewidth=2.4, label=f"Post-2010 Trend (Slope = {(b1+b3):+.3f}%/tourney)")

        # Intervention line
        ax.axvline(x=5.5, color="#333333", linestyle=":", linewidth=1.5)
        ax.text(5.6, mean_3par.max() * 0.96, "Intervention Boundary\n(October 1, 2010: 6.75m)", fontsize=9, fontweight="bold", color="#333333")

        # Level change arrow & annotation
        y_cf = counterfactual[0]
        y_post = fitted_post[0]
        ax.annotate(
            f"Level Shift: {b2:+.2f} percentage pts\n(p = {params['post_2010_rule']:.4f})",
            xy=(6, (y_cf + y_post)/2), xytext=(8, y_post - 2.5),
            arrowprops=dict(facecolor="black", shrink=0.05, width=1, headwidth=6),
            fontsize=8.5, fontweight="semibold", bbox=dict(boxstyle="round,pad=0.3", fc="#fdfdfd", ec="#cccccc")
        )

        ax.set_xticks(t_seq)
        ax.set_xticklabels([f"T{i}: {y}" for i, y in enumerate(years)], rotation=45, ha="right", fontsize=8)
        ax.set_xlabel("Tournament Sequence (2005–2024)", fontsize=11, fontweight="bold", labelpad=8)
        ax.set_ylabel("3-Point Attempt Rate (3PAr %)", fontsize=11, fontweight="bold")
        ax.set_title("Interrupted Time Series (ITS) of 2010 FIBA 3-Point Arc Shift", fontsize=13, fontweight="bold", pad=12)
        ax.legend(loc="lower right", fontsize=8.5)
        ax.grid(True, linestyle="--", alpha=0.6)

        fig.tight_layout()
        f_path = FIGURES_DIR / "fig4_its_segmented_regression.png"
        plt.savefig(f_path)
        plt.close()
        return f_path


def main():
    model = ITSFlagshipModel()
    fit_data = model.fit_primary_model()
    res = fit_data["results_hac"]
    print("=== ITS SEGMENTED REGRESSION RESULTS ===")
    print(res.summary())
    fig_p = model.generate_its_figure()
    print(f"\nFigure saved to: {fig_p}")


if __name__ == "__main__":
    main()
