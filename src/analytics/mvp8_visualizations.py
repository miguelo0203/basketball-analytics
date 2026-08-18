"""MVP-8 Publication Visualizations Engine.

Generates 5 publication-quality figures under reports/figures/mvp8/:
- Fig 1: 6-Layer Decision Evidence Radar / Breakdown
- Fig 2: Decision System vs Simple Baseline Comparison
- Fig 3: Decision Confidence & Uncertainty Distribution
- Fig 4: Historical Decision Concordance & Tournament Success
- Fig 5: Decision Score Waterfall for Flagship Decisions (Lorenzo Brown 2022, Pau Gasol 2015)
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from src.config import ANALYTICS_DATA_DIR, REPORTS_DIR


class MVP8Visualizer:
    """Generates certified publication figures for MVP-8."""

    def __init__(self, data_dir: Path = ANALYTICS_DATA_DIR, output_dir: Path = REPORTS_DIR / "figures" / "mvp8"):
        self.data_dir = data_dir
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

        plt.rcParams.update({
            "font.family": "DejaVu Sans",
            "font.size": 10,
            "axes.titlesize": 12,
            "axes.labelsize": 10,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9,
            "legend.fontsize": 9,
            "figure.titlesize": 13,
            "axes.grid": True,
            "grid.alpha": 0.3,
            "grid.linestyle": ":",
        })

    def generate_fig1_evidence_layers(self):
        """Figure 1: 6-Layer Multi-Criteria Evidence Breakdown for Flagship Decisions."""
        df_dos = pd.read_parquet(self.data_dir / "mvp8_decision_dossiers.parquet")
        
        # Select 3 key candidates: Pau Gasol 2015, Lorenzo Brown 2022, Ricky Rubio 2019
        selected_ids = [
            "eurobasket_2015_ESP_pau_gasol_1980",
            "eurobasket_2022_ESP_lorenzo_brown_1990",
            "worldcup_2019_ESP_ricky_rubio_1990",
        ]
        sub = df_dos[df_dos["player_tournament_id"].isin(selected_ids)]

        fig, ax = plt.subplots(figsize=(10, 5.5))
        
        layers = ["Role Fit", "Efficiency (TS%)", "Sample Reliability", "Predictive Impact", "Video Film"]
        x = np.arange(len(layers))
        width = 0.25

        colors = ["#1b9e77", "#d95f02", "#7570b3"]
        labels = ["Pau Gasol (EB15)", "Lorenzo Brown (EB22)", "Ricky Rubio (WC19)"]

        for i, (_, row) in enumerate(sub.iterrows()):
            vals = [
                row["role_fit_score"],
                min(100.0, row["ts_pct"] * 140.0),
                100.0 if "High" in row["sample_reliability_tier"] else 85.0 if "Moderate" in row["sample_reliability_tier"] else 65.0,
                min(100.0, max(0.0, 50.0 + row["predictive_net_impact"] * 5.0)),
                row["film_quality_score"] * 25.0,
            ]
            ax.bar(x + (i - 1) * width, vals, width=width, label=labels[i], color=colors[i], edgecolor="black")

        ax.set_xticks(x)
        ax.set_xticklabels(layers, fontweight="bold")
        ax.set_ylabel("Normalized Layer Evidence Score (0 - 100)")
        ax.set_title("MVP-8 Multi-Layer Evidence Decomposition for Flagship Historical Decisions\n(Synthesizing Empirical Boxscores, Roles, Film, ML Predictions & Simulations)", fontweight="bold")
        ax.set_ylim(0, 110)
        ax.legend(loc="upper right")

        plt.tight_layout()
        out_path = self.output_dir / "fig1_decision_evidence_layers.png"
        plt.savefig(out_path, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Generated {out_path.name}")

    def generate_fig2_system_vs_baseline(self):
        """Figure 2: Decision System Concordance vs Naive Baseline Rules."""
        df_eval = pd.read_csv(self.data_dir / "mvp8_decision_evaluations.csv")

        fig, ax = plt.subplots(figsize=(8, 5))

        metrics = ["MVP-8 Multi-Layer System", "Baseline Rule A (Naive PPG)", "Baseline Rule B (Experience)"]
        hit_rates = [
            df_eval["mvp8_agrees_with_actual"].mean() * 100.0,
            df_eval["baseline_ppg_agrees_with_actual"].mean() * 100.0,
            df_eval["baseline_exp_agrees_with_actual"].mean() * 100.0,
        ]

        colors = ["#1b9e77", "#d95f02", "#7570b3"]
        bars = ax.bar(metrics, hit_rates, color=colors, edgecolor="black", width=0.5)

        ax.set_ylabel("Historical Selection Concordance Rate (%)")
        ax.set_title("Historical Decision Concordance: MVP-8 Integrated Stack vs Naive Baselines\n(Evaluating Flagship Tournament Roster & Rotation Decisions)", fontweight="bold")
        ax.set_ylim(0, 105)

        for bar, rate in zip(bars, hit_rates):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2.0, f"{rate:.1f}%", ha="center", fontweight="bold")

        plt.tight_layout()
        out_path = self.output_dir / "fig2_system_vs_baseline_comparison.png"
        plt.savefig(out_path, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Generated {out_path.name}")

    def generate_fig3_decision_uncertainty(self):
        """Figure 3: Decision Score and Uncertainty Distribution across Candidates."""
        df_dos = pd.read_parquet(self.data_dir / "mvp8_decision_dossiers.parquet")

        fig, ax = plt.subplots(figsize=(9, 5))

        df_sorted = df_dos.sort_values(by="recommendation_score", ascending=True)
        names = [f"{r['player_tournament_id'].split('_')[3].title()} ({r['tournament_id'].split('_')[1]})" for _, r in df_sorted.iterrows()]
        scores = df_sorted["recommendation_score"].values
        conf_colors = ["#1b9e77" if "High" in c else "#386cb0" if "Moderate" in c else "#d95f02" for c in df_sorted["confidence_tier"]]

        ax.barh(range(len(df_sorted)), scores, color=conf_colors, edgecolor="black", height=0.6)
        ax.set_yticks(range(len(df_sorted)))
        ax.set_yticklabels(names, fontsize=8.5)
        ax.set_xlabel("MVP-8 Recommendation Score (0 - 100)")
        ax.set_title("MVP-8 Candidate Recommendation Scores & Confidence Tiers\n(Green: Tier A High Confidence, Blue: Tier B Moderate, Red: Tier C Limited)", fontweight="bold")
        ax.axvline(70.0, color="#1b9e77", linestyle="--", alpha=0.7, label="Recommended Threshold (70.0)")
        ax.set_xlim(0, 100)
        ax.legend(loc="lower right")

        plt.tight_layout()
        out_path = self.output_dir / "fig3_decision_uncertainty_bounds.png"
        plt.savefig(out_path, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Generated {out_path.name}")

    def generate_fig4_historical_concordance(self):
        """Figure 4: Historical Decision Scenarios and Tournament Outcome Alignment."""
        df_eval = pd.read_csv(self.data_dir / "mvp8_decision_evaluations.csv")

        fig, ax = plt.subplots(figsize=(10, 5))

        dec_labels = [f"{r['decision_id']}\n({r['tournament_id']})" for _, r in df_eval.iterrows()]
        scores = df_eval["mvp8_recommendation_score"].values
        agreed = df_eval["mvp8_agrees_with_actual"].values

        colors = ["#1b9e77" if a else "#d95f02" for a in agreed]
        bars = ax.bar(dec_labels, scores, color=colors, edgecolor="black", width=0.5)

        ax.set_ylabel("MVP-8 Top Candidate Score")
        ax.set_title("Flagship Historical Decision Scenarios: Model Recommendation & Tournament Outcome Alignment\n(Green = Exact Historical Agreement, Orange = Nuanced Tactical Divergence)", fontweight="bold")
        ax.set_ylim(0, 100)

        for bar, s, res in zip(bars, scores, df_eval["historical_tournament_result"]):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5, f"{s:.1f}\n({res.split('(')[0].strip()})", ha="center", fontsize=7.5, fontweight="bold")

        plt.tight_layout()
        out_path = self.output_dir / "fig4_historical_decision_concordance.png"
        plt.savefig(out_path, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Generated {out_path.name}")

    def generate_fig5_dossier_waterfall(self):
        """Figure 5: Score Contribution Waterfall for Lorenzo Brown (EB22) and Pau Gasol (EB15)."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))

        components = ["Base", "Role Fit\n(25%)", "TS% Eff\n(25%)", "Reliability\n(20%)", "Predictive\n(15%)", "Film\n(15%)"]

        # 1. Lorenzo Brown 2022: Role=25.0, TS=23.8, Rel=17.0, Pred=9.5, Film=9.6 -> 84.9
        brown_contribs = [0, 25.0, 23.8, 17.0, 9.5, 9.6]
        brown_cum = np.cumsum(brown_contribs)
        ax1.bar(components[1:], brown_contribs[1:], color="#1b9e77", edgecolor="black", width=0.5)
        ax1.set_title("Lorenzo Brown (EuroBasket 2022)\nFinal Score: 84.9 (Tier B, RECOMMENDED)", fontweight="bold")
        ax1.set_ylabel("Score Points Added")
        ax1.set_ylim(0, 30)

        # 2. Pau Gasol 2015: Role=15.0, TS=22.4, Rel=20.0, Pred=11.4, Film=12.0 -> 80.8
        gasol_contribs = [0, 15.0, 22.4, 20.0, 11.4, 12.0]
        ax2.bar(components[1:], gasol_contribs[1:], color="#386cb0", edgecolor="black", width=0.5)
        ax2.set_title("Pau Gasol (EuroBasket 2015)\nFinal Score: 80.8 (Tier A, RECOMMENDED)", fontweight="bold")
        ax2.set_ylabel("Score Points Added")
        ax2.set_ylim(0, 30)

        plt.suptitle("MVP-8 Decision Score Component Waterfall for Historic Tournament MVPs", fontweight="bold")
        plt.tight_layout()
        out_path = self.output_dir / "fig5_flagship_dossier_waterfall.png"
        plt.savefig(out_path, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Generated {out_path.name}")

    def generate_all_figures(self):
        """Generate all 5 certified MVP-8 figures."""
        self.generate_fig1_evidence_layers()
        self.generate_fig2_system_vs_baseline()
        self.generate_fig3_decision_uncertainty()
        self.generate_fig4_historical_concordance()
        self.generate_fig5_dossier_waterfall()


def main():
    vis = MVP8Visualizer()
    vis.generate_all_figures()


if __name__ == "__main__":
    main()
