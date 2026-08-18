"""MVP-7 Publication Visualizations Engine.

Generates 5 publication-quality figures under reports/figures/mvp7/:
- Fig 1: Actual Champion Simulated Tournament Probability across all 18 Tournaments
- Fig 2: Team x Advancement Stage Probability Heatmap
- Fig 3: Probability Shrinkage Sensitivity (lambda in {0.50, 0.75, 1.00})
- Fig 4: Simulated Advancement Probability vs Actual Tournament Outcomes
- Fig 5: Controlled Flagship Counterfactual Distributions (Pekin 2008, EB 2015, EB 2022)
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from src.config import ANALYTICS_DATA_DIR, REPORTS_DIR


class MVP7Visualizer:
    """Generates certified publication figures for MVP-7."""

    def __init__(self, data_dir: Path = ANALYTICS_DATA_DIR, output_dir: Path = REPORTS_DIR / "figures" / "mvp7"):
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

    def generate_fig1_champion_probabilities(self):
        """Figure 1: Simulated Title Probability of Actual Champions across 18 Tournaments."""
        df_sim = pd.read_parquet(self.data_dir / "mvp7_tournament_simulations.parquet")
        df_champs = df_sim[df_sim["is_actual_champion"] == 1].sort_values(by="tournament_year")

        fig, ax = plt.subplots(figsize=(12, 6))

        tourney_labels = [f"{r['tournament_id'].replace('_', ' ').title()}\n({r['team_id']})" for _, r in df_champs.iterrows()]
        probs = df_champs["prob_champion"].values * 100.0
        ranks = df_champs["simulated_rank"].values

        colors = ["#1b9e77" if r == 1 else "#386cb0" if r == 2 else "#d95f02" for r in ranks]
        bars = ax.bar(range(len(df_champs)), probs, color=colors, edgecolor="black", width=0.6)

        ax.set_xticks(range(len(df_champs)))
        ax.set_xticklabels(tourney_labels, rotation=45, ha="right", fontsize=8.5)
        ax.set_ylabel("Simulated Championship Probability (%)")
        ax.set_title("MVP-7 Retrospective Validation: Model-Implied Championship Probability of Actual Champions\n(10,000 Monte Carlo Iterations per Tournament, Seed=42)", fontweight="bold")
        ax.set_ylim(0, 105)

        for bar, rank, p in zip(bars, ranks, probs):
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, h + 2.0, f"#{rank} ({p:.1f}%)", ha="center", fontsize=8, fontweight="bold")

        # Add legend
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor="#1b9e77", edgecolor="black", label="Rank #1 Simulated Favorite (13/18 = 72.2%)"),
            Patch(facecolor="#386cb0", edgecolor="black", label="Rank #2 Contender (1/18 = 5.6%)"),
            Patch(facecolor="#d95f02", edgecolor="black", label="Rank #3-4 Contender (4/18 = 22.2%)"),
        ]
        ax.legend(handles=legend_elements, loc="upper right")

        plt.tight_layout()
        out_path = self.output_dir / "fig1_tournament_champion_probabilities.png"
        plt.savefig(out_path, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Generated {out_path.name}")

    def generate_fig2_advancement_heatmap(self):
        """Figure 2: Advancement Probability Matrix for Flagship Tournament (Pekin 2008 & EuroBasket 2015)."""
        df_sim = pd.read_parquet(self.data_dir / "mvp7_tournament_simulations.parquet")
        
        # Select Beijing 2008 (12 teams)
        df_sub = df_sim[df_sim["tournament_id"] == "olympics_2008"].sort_values(by="prob_champion", ascending=False)
        stages = ["prob_advance_group", "prob_reach_qf", "prob_reach_sf", "prob_reach_final", "prob_champion"]
        stage_names = ["Group Advance", "Reach QF", "Reach SF", "Reach Final", "Champion"]

        matrix = df_sub[stages].values * 100.0
        teams = df_sub["team_id"].tolist()

        fig, ax = plt.subplots(figsize=(9, 6.5))
        im = ax.imshow(matrix, cmap="Blues", aspect="auto", vmin=0, vmax=100)

        ax.set_xticks(range(len(stage_names)))
        ax.set_xticklabels(stage_names, fontweight="bold")
        ax.set_yticks(range(len(teams)))
        ax.set_yticklabels(teams, fontweight="bold")
        ax.set_title("Beijing 2008 Olympic Basketball: Simulated Stage Advancement Probabilities (%)\n(10,000 Monte Carlo Iterations from Pre-Game MVP-6 Probabilities)", fontweight="bold")

        # Annotate cell values
        for i in range(len(teams)):
            for j in range(len(stage_names)):
                val = matrix[i, j]
                col = "white" if val > 55 else "black"
                ax.text(j, i, f"{val:.1f}%", ha="center", va="center", color=col, fontsize=8.5, fontweight="bold")

        fig.colorbar(im, ax=ax, label="Simulated Probability (%)")
        plt.tight_layout()
        out_path = self.output_dir / "fig2_advancement_probability_heatmap.png"
        plt.savefig(out_path, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Generated {out_path.name}")

    def generate_fig3_shrinkage_sensitivity(self):
        """Figure 3: Champion Probability under Probability Shrinkage (lambda in {0.50, 0.75, 1.00})."""
        df_scen = pd.read_csv(self.data_dir / "mvp7_scenario_results.csv")

        fig, ax = plt.subplots(figsize=(8, 5))
        lambdas = df_scen["shrinkage_lambda"].values
        top1_rates = df_scen["champion_top1_hit_rate"].values * 100.0
        mean_probs = df_scen["mean_simulated_prob_of_actual_champion"].values * 100.0

        ax.plot(lambdas, top1_rates, "o-", color="#1b9e77", linewidth=2.5, markersize=8, label="Champion Top-1 Hit Rate (%)")
        ax.plot(lambdas, mean_probs, "s--", color="#d95f02", linewidth=2.5, markersize=8, label="Mean Title Probability of Actual Champion (%)")

        ax.set_xlabel("Probability Shrinkage Parameter λ (1.0 = Baseline, 0.5 = High Uncertainty)")
        ax.set_ylabel("Percentage (%)")
        ax.set_title("Probability Shrinkage Sensitivity Analysis\nTournament Simulation Stability under Game-Level Probability Uncertainty", fontweight="bold")
        ax.set_xlim(0.45, 1.05)
        ax.set_ylim(40, 85)
        ax.legend(loc="lower right")

        for x, y1, y2 in zip(lambdas, top1_rates, mean_probs):
            ax.text(x, y1 + 1.5, f"{y1:.1f}%", ha="center", fontweight="bold", color="#1b9e77")
            ax.text(x, y2 - 2.5, f"{y2:.1f}%", ha="center", fontweight="bold", color="#d95f02")

        plt.tight_layout()
        out_path = self.output_dir / "fig3_probability_shrinkage_sensitivity.png"
        plt.savefig(out_path, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Generated {out_path.name}")

    def generate_fig4_simulated_vs_actual(self):
        """Figure 4: Simulated Title Probability vs Actual Champion Outcome."""
        df_sim = pd.read_parquet(self.data_dir / "mvp7_tournament_simulations.parquet")

        fig, ax = plt.subplots(figsize=(8, 5.5))

        champs = df_sim[df_sim["is_actual_champion"] == 1]["prob_champion"].values * 100.0
        non_champs = df_sim[df_sim["is_actual_champion"] == 0]["prob_champion"].values * 100.0

        ax.hist(non_champs, bins=20, alpha=0.6, color="#7570b3", edgecolor="black", label=f"Non-Champions (N={len(non_champs)})")
        ax.hist(champs, bins=15, alpha=0.8, color="#1b9e77", edgecolor="black", label=f"Actual Champions (N={len(champs)})")

        ax.set_xlabel("Simulated Championship Probability (%)")
        ax.set_ylabel("Number of Team-Tournament Campaigns")
        ax.set_title("Distribution of Simulated Championship Probabilities: Champions vs Non-Champions\n(18 Tournaments, 364 Campaigns)", fontweight="bold")
        ax.legend(loc="upper right")

        plt.tight_layout()
        out_path = self.output_dir / "fig4_simulated_vs_actual_outcomes.png"
        plt.savefig(out_path, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Generated {out_path.name}")

    def generate_fig5_flagship_counterfactuals(self):
        """Figure 5: Flagship Historical Counterfactual Distributions."""
        df_cf = pd.read_csv(self.data_dir / "mvp7_counterfactual_results.csv")

        fig, ax = plt.subplots(figsize=(10, 5))
        
        labels = [f"{r['tournament_name']}\n[{r['counterfactual_id']}]" for _, r in df_cf.iterrows()]
        team_a_pcts = df_cf["simulated_win_pct_team_a"].values * 100.0
        team_b_pcts = df_cf["simulated_win_pct_team_b"].values * 100.0

        y_pos = np.arange(len(df_cf))
        ax.barh(y_pos, team_a_pcts, color="#1b9e77", edgecolor="black", height=0.45, label="Contender Simulated Capture %")
        ax.barh(y_pos, team_b_pcts, left=team_a_pcts, color="#d95f02", edgecolor="black", height=0.45, label="Field / Opponent Capture %")

        ax.set_yticks(y_pos)
        ax.set_yticklabels(labels, fontweight="bold")
        ax.set_xlabel("Simulated Outcome Distribution (%)")
        ax.set_title("Controlled Flagship Counterfactual Simulations (10,000 Iterations)\nReplaying Beijing 2008 Final, EuroBasket 2015 Title Run, and EuroBasket 2022 Perturbation", fontweight="bold")
        ax.set_xlim(0, 100)
        ax.legend(loc="lower right")

        for i, (a, b) in enumerate(zip(team_a_pcts, team_b_pcts)):
            ax.text(a/2, i, f"{a:.1f}%", va="center", ha="center", color="white", fontweight="bold", fontsize=9)
            ax.text(a + b/2, i, f"{b:.1f}%", va="center", ha="center", color="white", fontweight="bold", fontsize=9)

        plt.tight_layout()
        out_path = self.output_dir / "fig5_flagship_counterfactuals.png"
        plt.savefig(out_path, dpi=300, bbox_inches="tight")
        plt.close()
        print(f"Generated {out_path.name}")

    def generate_all_figures(self):
        """Generate all 5 certified MVP-7 figures."""
        self.generate_fig1_champion_probabilities()
        self.generate_fig2_advancement_heatmap()
        self.generate_fig3_shrinkage_sensitivity()
        self.generate_fig4_simulated_vs_actual()
        self.generate_fig5_flagship_counterfactuals()


def main():
    vis = MVP7Visualizer()
    vis.generate_all_figures()


if __name__ == "__main__":
    main()
