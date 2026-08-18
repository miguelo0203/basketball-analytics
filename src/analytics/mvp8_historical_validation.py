"""MVP-8 Historical Decision Validation & Counterfactual Evaluation.

Reconstructs historical decision points across EuroBasket, World Cup, and Olympic Games,
comparing the MVP-8 Multi-Layer Decision System against simple baseline selection rules
(Naive PPG, Historical Experience) and actual historical coach selections and outcomes.
"""

from pathlib import Path
from typing import Dict, List, Any
import numpy as np
import pandas as pd

from src.config import ANALYTICS_DATA_DIR, REPORTS_DIR
from src.analytics.mvp8_decision_system import AnalystDecisionEngine


class HistoricalDecisionValidator:
    """Evaluates MVP-8 recommendations against historical decisions and simple baselines."""

    def __init__(self, data_dir: Path = ANALYTICS_DATA_DIR):
        self.data_dir = data_dir
        self.decision_engine = AnalystDecisionEngine(data_dir=data_dir)

    def evaluate_flagship_historical_decisions(self) -> pd.DataFrame:
        """Evaluate 5 flagship historical tournament decision scenarios."""
        decisions_specs = [
            {
                "decision_id": "DEC_01_EB11_BACKCOURT",
                "tournament_id": "eurobasket_2011",
                "team_id": "ESP",
                "decision_context": "Pre-tournament primary perimeter initiator selection",
                "candidate_ids": [
                    "eurobasket_2011_ESP_juan_carlos_navarro_1980",
                    "eurobasket_2011_ESP_jose_manuel_calderon_1981",
                    "eurobasket_2011_ESP_ricky_rubio_1990",
                ],
                "target_role": "Primary Initiator / Floor General",
                "actual_historical_choice": "eurobasket_2011_ESP_juan_carlos_navarro_1980",
                "historical_tournament_result": "Gold Medal (Navarro Tournament MVP, 18.7 PPG)",
            },
            {
                "decision_id": "DEC_02_EB15_FRONTCOURT",
                "tournament_id": "eurobasket_2015",
                "team_id": "ESP",
                "decision_context": "Pre-tournament primary interior anchor & hub selection",
                "candidate_ids": [
                    "eurobasket_2015_ESP_pau_gasol_1980",
                    "eurobasket_2015_ESP_felipe_reyes_1980",
                    "eurobasket_2015_ESP_nikola_mirotic_1991",
                ],
                "target_role": "Low-Block Anchor / Interior Scorer",
                "actual_historical_choice": "eurobasket_2015_ESP_pau_gasol_1980",
                "historical_tournament_result": "Gold Medal (Pau Gasol Tournament MVP, 25.6 PPG, 8.8 RPG)",
            },
            {
                "decision_id": "DEC_03_EB22_NATURALIZED_GUARD",
                "tournament_id": "eurobasket_2022",
                "team_id": "ESP",
                "decision_context": "Backcourt initiator integration during generational rebuild",
                "candidate_ids": [
                    "eurobasket_2022_ESP_lorenzo_brown_1990",
                    "eurobasket_2022_ESP_alberto_diaz_1994",
                    "eurobasket_2022_ESP_willy_hernangomez_1994",
                ],
                "target_role": "Primary Initiator / Floor General",
                "actual_historical_choice": "eurobasket_2022_ESP_lorenzo_brown_1990",
                "historical_tournament_result": "Gold Medal (Brown All-Tournament Team, 15.2 PPG, 7.6 APG)",
            },
            {
                "decision_id": "DEC_04_WC19_FLOOR_LEADER",
                "tournament_id": "worldcup_2019",
                "team_id": "ESP",
                "decision_context": "Pre-tournament offensive floor general and clutch initiator",
                "candidate_ids": [
                    "worldcup_2019_ESP_ricky_rubio_1990",
                    "worldcup_2019_ESP_marc_gasol_1985",
                    "worldcup_2019_ESP_rudy_fernandez_1985",
                ],
                "target_role": "Primary Initiator / Floor General",
                "actual_historical_choice": "worldcup_2019_ESP_ricky_rubio_1990",
                "historical_tournament_result": "Gold Medal (Rubio World Cup MVP, 16.4 PPG, 6.0 APG)",
            },
            {
                "decision_id": "DEC_05_RIO16_WING_CREATION",
                "tournament_id": "olympics_2016",
                "team_id": "ESP",
                "decision_context": "Olympic backcourt bench spark and secondary initiator",
                "candidate_ids": [
                    "olympics_2016_ESP_sergio_rodriguez_1986",
                    "olympics_2016_ESP_sergio_llull_1987",
                ],
                "target_role": "Primary Initiator / Floor General",
                "actual_historical_choice": "olympics_2016_ESP_sergio_rodriguez_1986",
                "historical_tournament_result": "Bronze Medal (Rodriguez 8.0 PPG, 4.3 APG in 18 MPG)",
            },
        ]

        results = []
        for spec in decisions_specs:
            c_dossiers = []
            for cid in spec["candidate_ids"]:
                dos = self.decision_engine.evaluate_player_decision_dossier(
                    cid, spec["target_role"], spec["team_id"], spec["tournament_id"]
                )
                c_dossiers.append(dos)

            df_c = pd.DataFrame(c_dossiers)

            # MVP-8 Choice: Candidate with highest recommendation_score
            mvp8_top = df_c.sort_values(by="recommendation_score", ascending=False).iloc[0]
            mvp8_choice = mvp8_top["player_tournament_id"]
            mvp8_score = mvp8_top["recommendation_score"]

            # Baseline A Choice: Highest PTS/40
            base_pts_top = df_c.sort_values(by="pts_per_40", ascending=False).iloc[0]
            base_pts_choice = base_pts_top["player_tournament_id"]

            # Baseline B Choice: Highest Total Minutes (Experience)
            base_exp_top = df_c.sort_values(by="total_minutes", ascending=False).iloc[0]
            base_exp_choice = base_exp_top["player_tournament_id"]

            actual_choice = spec["actual_historical_choice"]

            results.append({
                "decision_id": spec["decision_id"],
                "tournament_id": spec["tournament_id"],
                "decision_context": spec["decision_context"],
                "mvp8_recommended_candidate": mvp8_choice,
                "mvp8_recommendation_score": mvp8_score,
                "baseline_ppg_candidate": base_pts_choice,
                "baseline_exp_candidate": base_exp_choice,
                "actual_historical_choice": actual_choice,
                "mvp8_agrees_with_actual": (mvp8_choice == actual_choice),
                "baseline_ppg_agrees_with_actual": (base_pts_choice == actual_choice),
                "baseline_exp_agrees_with_actual": (base_exp_choice == actual_choice),
                "historical_tournament_result": spec["historical_tournament_result"],
            })

        df_res = pd.DataFrame(results)
        df_res.to_csv(self.data_dir / "mvp8_decision_evaluations.csv", index=False)
        return df_res


def main():
    val = HistoricalDecisionValidator()
    print("Evaluating MVP-8 Historical Decisions vs Baseline Rules...")
    df_eval = val.evaluate_flagship_historical_decisions()
    print("\n--- HISTORICAL DECISION EVALUATION SUMMARY ---")
    cols = ["decision_id", "tournament_id", "mvp8_recommended_candidate", "mvp8_agrees_with_actual", "baseline_ppg_agrees_with_actual"]
    print(df_eval[cols].to_string())


if __name__ == "__main__":
    main()
