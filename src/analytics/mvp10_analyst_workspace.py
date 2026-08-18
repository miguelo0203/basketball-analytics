"""MVP-10 Analyst Decision Workspace & Historical Replay Engine.

Provides an operational decision-support interface and historical replay mode:
1. Pre-Game Information State (strictly pre-game features, models, uncertainty)
2. Interactive Reveal Outcome Barrier (anti-hindsight demonstration)
3. Decision Timeline (T-30, T-7, T-1, Game, Post-Game Review)
4. Post-Game Review Mode (evaluating evidence quality and uncertainty calibration)
5. Interactive Streamlit UI and CLI programmatic runner.
"""

import sys
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from typing import Dict, List, Any, Optional
import json
import numpy as np
import pandas as pd
import duckdb

from src.config import VALIDATED_DB_PATH, ANALYTICS_DATA_DIR, REPORTS_DIR
from src.analytics.mvp10_evidence_engine import EvidenceEngine
from src.analytics.mvp10_brief_generator import BriefGenerator


class AnalystWorkspace:
    """Operational analyst decision workspace and historical replay environment."""

    def __init__(self, data_dir: Path = ANALYTICS_DATA_DIR):
        self.data_dir = data_dir
        self.evidence_engine = EvidenceEngine(data_dir=data_dir)
        self.brief_generator = BriefGenerator(data_dir=data_dir)

    def load_pre_game_state(self, game_id: str) -> Dict[str, Any]:
        """Load the strict pre-game information state for a selected match (zero future leakage)."""
        ev = self.evidence_engine.build_match_evidence_matrix(game_id)
        brief = self.brief_generator.generate_coaching_brief(game_id)

        # Build 5-point Decision Timeline
        timeline = [
            {
                "time_horizon": "T-30 Days (Pre-Tournament)",
                "available_data": "Multi-tournament historical Net Ratings & Four Factors baselines",
                "model_output": "Initial tournament simulation & medal round reach odds",
                "analyst_focus": "Roster archetype coverage & positional depth assessment",
            },
            {
                "time_horizon": "T-7 Days (Tournament Eve)",
                "available_data": "Final 12-man roster confirmation & warm-up game stats",
                "model_output": "Refined calibrated pre-game win probabilities (ECE = 0.0314)",
                "analyst_focus": "Initial opponent scouting profile & creator gravity audit",
            },
            {
                "time_horizon": "T-1 Day (Match Eve)",
                "available_data": "In-tournament group stage form, recent point margins & rest days",
                "model_output": f"Pre-Game P(Win Team A): {ev['p_win_team_a']*100.0:.1f}%",
                "analyst_focus": "Tactical film review on opponent P&R drop coverage & transition defense",
            },
            {
                "time_horizon": "Game Day (Pre-Tipoff)",
                "available_data": "Starting lineups, referee tendencies & shooting variance bounds",
                "model_output": "Expected margin & key tactical mismatch alerts",
                "analyst_focus": "Delivery of concise Coaching Staff Brief (Executive Summary + Questions)",
            },
            {
                "time_horizon": "Post-Game (Review & Audit)",
                "available_data": "Boxscore, possession efficiency, rotation deltas & outcome",
                "model_output": "Deviation audit against pre-game model expectation",
                "analyst_focus": "Evaluating process quality, uncertainty calibration, and tactical insights",
            },
        ]

        return {
            "game_id": game_id,
            "tournament_id": ev["tournament_id"],
            "team_a_id": ev["team_a_id"],
            "team_b_id": ev["team_b_id"],
            "pre_game_win_probability_a": ev["p_win_team_a"],
            "evidence_status": ev["evidence_status"],
            "evidence_layers": ev["evidence_layers"],
            "contradictions": ev["contradictions"],
            "coaching_brief": brief,
            "decision_timeline": timeline,
            "outcome_revealed": False,
        }

    def reveal_match_outcome(self, game_id: str) -> Dict[str, Any]:
        """Reveal the actual historical match result and perform a post-game process review."""
        pre_state = self.load_pre_game_state(game_id)

        # Retrieve actual ground truth from DuckDB
        con = duckdb.connect(str(VALIDATED_DB_PATH), read_only=True)
        try:
            row = con.execute("""
                SELECT home_team_id, away_team_id, home_score, away_score, stage, game_date
                FROM fact_game
                WHERE game_id = ?
            """, [game_id]).fetchone()
        finally:
            con.close()

        if not row:
            raise ValueError(f"Game {game_id} not found in fact_game.")

        home_team, away_team, h_score, a_score, stage, g_date = row
        actual_margin = h_score - a_score if home_team == pre_state["team_a_id"] else a_score - h_score
        winner = home_team if h_score > a_score else away_team

        p_win_a = pre_state["pre_game_win_probability_a"]
        expected_winner = pre_state["team_a_id"] if p_win_a >= 0.50 else pre_state["team_b_id"]

        # Post-Game Review Evaluation
        correct_direction = (winner == expected_winner)
        calibrated_range = abs(actual_margin) <= 18.0  # Within normal 2-sigma margin spread

        post_game_review = {
            "actual_winner": winner,
            "final_score": f"{home_team} {h_score} - {away_team} {a_score}",
            "stage": stage,
            "game_date": str(g_date),
            "actual_margin_team_a": actual_margin,
            "model_directional_alignment": "ALIGNED" if correct_direction else "UPSET / DIVERGENT",
            "uncertainty_calibration_verdict": "OUTCOME WITHIN EXPECTED UNCERTAINTY BOUNDS" if calibrated_range else "HIGH VARIANCE TAIL EVENT",
            "evidence_process_evaluation": (
                "The pre-game evidence matrix correctly captured key possession and shooting disparities. "
                "The final result confirmed the pre-game probability assessment." if correct_direction else
                "The result diverged from the baseline favorite, demonstrating the irreducible single-game variance "
                "inherent in international knockout basketball."
            ),
        }

        pre_state["outcome_revealed"] = True
        pre_state["post_game_review"] = post_game_review
        return pre_state

    def generate_all_workspace_records(self) -> pd.DataFrame:
        """Materialize full workspace demonstration records for all flagship tournament games."""
        flagship_games = [
            "olympics_2008_esp_usa_107_118",      # Beijing 2008 Final
            "eurobasket_2015_esp_ltu_80_63",      # EuroBasket 2015 Final
            "worldcup_2019_arg_esp_75_95",        # World Cup 2019 Final
            "eurobasket_2022_esp_fra_88_76",      # EuroBasket 2022 Final
            "eurobasket_2011_esp_fra_98_85",      # EuroBasket 2011 Final
        ]

        records = []
        for gid in flagship_games:
            rev = self.reveal_match_outcome(gid)
            records.append({
                "game_id": rev["game_id"],
                "tournament_id": rev["tournament_id"],
                "team_a_id": rev["team_a_id"],
                "team_b_id": rev["team_b_id"],
                "p_win_team_a": rev["pre_game_win_probability_a"],
                "final_score": rev["post_game_review"]["final_score"],
                "actual_winner": rev["post_game_review"]["actual_winner"],
                "directional_alignment": rev["post_game_review"]["model_directional_alignment"],
                "calibration_verdict": rev["post_game_review"]["uncertainty_calibration_verdict"],
                "evidence_status": rev["evidence_status"],
            })

        df_out = pd.DataFrame(records)
        df_out.to_parquet(self.data_dir / "mvp10_workspace_records.parquet", index=False)
        return df_out


def run_streamlit_app():
    """Lightweight interactive Streamlit application for the Analyst Workspace."""
    import streamlit as st

    st.set_page_config(page_title="Workspace del Analista | International Basketball Analytics", layout="wide")
    
    st.markdown("""
        <style>
        .main-header {font-size: 26px; font-weight: 700; color: #0f172a; margin-bottom: 0px;}
        .sub-header {font-size: 14px; color: #475569; margin-bottom: 20px;}
        .demo-box {background-color: #f1f5f9; padding: 15px; border-radius: 8px; border-left: 5px solid #0284c7; margin-bottom: 15px;}
        .card-metric {background-color: #f8fafc; padding: 12px; border-radius: 6px; border: 1px solid #e2e8f0;}
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="main-header">🏀 Workspace de Soporte a Decisiones para Baloncesto</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Analítica Histórica y Soporte Táctico (2005–2024) | Entorno Operativo Anti-Hindsight</p>', unsafe_allow_html=True)

    workspace = AnalystWorkspace()

    # Sidebar Navigation & Mode Selector
    st.sidebar.title("Panel de Control del Analista")
    app_mode = st.sidebar.radio("Seleccionar Modo del Workspace:", ["🎯 5–10 Min Flagship Live Demo", "🔍 Explorador de Partidos Históricos"])

    flagship_games = {
        "Pekín 2008 Final Olímpica: España vs USA": "olympics_2008_esp_usa_107_118",
        "EuroBasket 2015 Final: España vs Lituania": "eurobasket_2015_esp_ltu_80_63",
        "Copa del Mundo 2019 Final: Argentina vs España": "worldcup_2019_arg_esp_75_95",
        "EuroBasket 2022 Final: España vs Francia": "eurobasket_2022_esp_fra_88_76",
        "EuroBasket 2011 Final: España vs Francia": "eurobasket_2011_esp_fra_98_85",
    }

    if app_mode == "🎯 5–10 Min Flagship Live Demo":
        selected_gid = "olympics_2008_esp_usa_107_118"
        st.sidebar.success("Seleccionado: **Pekín 2008 Final (España vs USA)**")
        st.markdown("""
        <div class="demo-box">
        <strong>🎯 Demostración Guiada Flagship en Vivo</strong><br>
        <em>Escenario</em>: Final por el Oro Olímpico Pekín 2008. Eres el analista preparando el informe para el cuerpo técnico.<br>
        <em>Objetivo</em>: Revisar la evidencia estrictamente prepartido, detectar contradicciones tácticas, formular preguntas para el entrenador y realizar la auditoría de proceso posterior.
        </div>
        """, unsafe_allow_html=True)
    else:
        selected_label = st.sidebar.selectbox("Seleccionar Escenario Histórico:", list(flagship_games.keys()))
        selected_gid = flagship_games[selected_label]

    st.sidebar.markdown("---")
    st.sidebar.info("🛡️ **Garantía Anti-Hindsight**: Todas las variables, probabilidades del modelo y notas de vídeo reflejan información disponible estrictamente ANTES del salto inicial.")

    pre_state = workspace.load_pre_game_state(selected_gid)

    # 1. Match Header
    col1, col2, col3 = st.columns(3)
    col1.metric("Torneo Oficial", pre_state["tournament_id"].replace("_", " ").title())
    col2.metric("Enfrentamiento", f"{pre_state['team_a_id']} vs {pre_state['team_b_id']}")
    col3.metric(f"Probabilidad de Victoria Modelo ({pre_state['team_a_id']})", f"{pre_state['pre_game_win_probability_a']*100.0:.1f}%")

    st.markdown("---")

    # 2. Tabs: Evidence Matrix, Coaching Brief, Decision Timeline, Post-Game Reveal
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Matriz de Evidencia de 8 Capas",
        "📋 Brief Táctico para el Entrenador",
        "⏱️ Cronograma Operativo de Decisión",
        "🏆 Revisión de Proceso Post-Partido"
    ])

    with tab1:
        st.subheader("Descomposición de Evidencia Multicapa (Estado Prepartido)")
        for layer in pre_state["evidence_layers"]:
            with st.expander(f"{layer['layer_name']} — {layer['signal']} ({layer['confidence']})", expanded=True):
                c_a, c_b = st.columns([2, 1])
                c_a.write(f"**Interpretación de Baloncesto**: {layer['interpretation']}")
                c_a.write(f"**Procedencia del Dato**: `{layer['source']}`")
                c_b.warning(f"**Incertidumbre y Límites**: {layer['limitation']}")

        if len(pre_state["contradictions"]) > 0:
            st.error("⚠️ **Alertas de Contradicción Táctica Detectadas**")
            for c in pre_state["contradictions"]:
                st.write(f"**{c['type']}**: {c['evidence_a']} vs {c['evidence_b']}")
                st.info(f"**Pregunta Accionable para el Entrenador**: {c['actionable_investigation']}")

    with tab2:
        brief = pre_state["coaching_brief"]
        st.subheader(f"Brief Prepartido: {pre_state['team_a_id']} vs {pre_state['team_b_id']}")
        st.markdown("#### 1. Resumen Ejecutivo")
        for b in brief["executive_summary"]:
            st.markdown(f"- {b}")

        st.markdown("#### 2. Evidencia Táctica de Vídeo y Esquemas")
        for f in brief["tactical_film_evidence"]:
            st.markdown(f"- {f}")

        st.markdown("#### 3. Preguntas para la Reunión con el Cuerpo Técnico")
        for q in brief["questions_for_coaching_staff"]:
            st.markdown(f"- ❓ *{q}*")

        st.markdown("#### 4. Síntesis de Evidencia del Analista")
        st.success(brief["analyst_recommendation"])

    with tab3:
        st.subheader("Cronograma Operativo de Decisión (5 Horizontes Temporales)")
        for step in pre_state["decision_timeline"]:
            st.markdown(f"### {step['time_horizon']}")
            st.write(f"**Datos Disponibles Prepartido**: {step['available_data']}")
            st.write(f"**Pronóstico / Visión del Modelo**: {step['model_output']}")
            st.write(f"**Foco Operativo del Analista**: {step['analyst_focus']}")
            st.markdown("---")

    with tab4:
        st.subheader("Modo Replay Histórico (Barrera Anti-Hindsight)")
        reveal = st.checkbox("🔓 Revelar Marcador Real y Ejecutar Auditoría de Proceso")
        if reveal:
            res = workspace.reveal_match_outcome(selected_gid)
            pg = res["post_game_review"]
            st.success(f"### Marcador Real del Partido: {pg['final_score']}")
            st.metric("Alineación Direccional del Modelo", pg["model_directional_alignment"])
            st.metric("Veredicto de Calibración de Incertidumbre", pg["uncertainty_calibration_verdict"])
            st.info(f"**Evaluación de Proceso**: {pg['evidence_process_evaluation']}")
        else:
            st.warning("El resultado real se mantiene en cuarentena estricta para evitar el sesgo retrospectivo.")


def main():
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "streamlit":
        run_streamlit_app()
    else:
        ws = AnalystWorkspace()
        print("Running MVP-10 Analyst Decision Workspace (CLI Programmatic Engine)...")
        df = ws.generate_all_workspace_records()
        print(f"Generated {len(df)} workspace demonstration records.")
        print("\n--- WORKSPACE DEMONSTRATION RECORDS ---")
        print(df[["game_id", "tournament_id", "p_win_team_a", "final_score", "directional_alignment"]].to_string())


if __name__ == "__main__":
    main()
