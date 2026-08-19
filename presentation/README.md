# PRESENTACIÓN EJECUTIVA DEL PORTFOLIO (PRESENTATION HUB)
## International Basketball Analytics (2005–2024)

> **Propósito**: Deck ejecutivo maestro de 30 diapositivas en formato panorámico 16:9, diseñado con una estética profesional de Sports Analytics / Data Science para cuerpos técnicos, directores deportivos, analistas cuantitativos y comités de contratación técnica.

---

## 📂 Archivos de la Presentación

1. 📑 **[Presentación Ejecutiva Maestra (PDF Panorámico 16:9)](International_Basketball_Analytics_Presentation.pdf)**  
   *Documento de lectura ejecutiva (960×540 pt) optimizado para evaluación directa en pantalla, tablet o proyección.*

2. 📊 **[Presentación Editable en PowerPoint (.pptx)](International_Basketball_Analytics_Presentation.pptx)**  
   *Deck editable completo estructurado en 6 actos con paleta profesional (Dark Navy `#0A1128`, Deep Cyan `#0284C7`, Basketball Orange `#EA580C`).*

3. 📝 **[Guión y Estructura Visual (Markdown)](../portfolio/presentation/presentation_outline.md)**  
   *Esquema detallado con la pregunta analítica concreta que responde cada diapositiva.*

4. 🎙️ **[Notas del Orador (Speaker Notes)](../portfolio/presentation/speaker_notes.md)**  
   *Argumentario verbal completo para una exposición guiada de 25–35 minutos.*

---

## 🗺️ Estructura Narrativa en 6 Actos (30 Diapositivas)

```text
PRESENTATION MASTER DECK (16:9 WIDESCREEN)
│
├── 🏀 PORTADA & RESUMEN EJECUTIVO (Slides 1–3)
│   ├── Slide 1: Hero Cover (Identidad analítica y baloncesto)
│   ├── Slide 2: Resumen Ejecutivo en 4 Dimensiones
│   └── Slide 3: El Desafío: Sobrecarga de Datos vs. Señales Útiles
│
├── 🗄️ ACTO I: ARQUITECTURA DE DATOS & DUCKDB (Slides 4–7)
│   ├── Slide 4: Separador de Sección 01 (Data Architecture)
│   ├── Slide 5: Escala Canónica (1.145 partidos, 18 torneos, 27.353 actuaciones)
│   ├── Slide 6: Arquitectura de Medallón (01_raw ➔ 03_validated ➔ 04_analytics)
│   └── Slide 7: Control de Calidad y Cierre de Invariantes (200 min/partido)
│
├── 📈 ACTO II: MOTOR ESTADÍSTICO & MACHINE LEARNING (Slides 8–15)
│   ├── Slide 8: Separador de Sección 02 (Analytics & Modeling)
│   ├── Slide 9: Normalización de Ritmo y Four Factors de Dean Oliver
│   ├── Slide 10: Inferencia Longitudinal y Contracción Bayesiana (λ = 0.75)
│   ├── Slide 11: 6 Arquetipos Funcionales Objetivos (K-Means++ & PCA)
│   ├── Slide 12: Machine Learning Calibrado (LightGBM: Brier 0.1967, ECE 0.0314)
│   ├── Slide 13: Protocolo Temporal Walk-Forward en 17 Folds
│   ├── Slide 14: Simulación Monte Carlo de Torneos (180.000 iteraciones)
│   └── Slide 15: Workspace del Analista y Modo Anti-Hindsight (Streamlit)
│
├── 🎯 ACTO III: LOS 4 CASOS DE ESTUDIO EMBLEMÁTICOS (Slides 16–20)
│   ├── Slide 16: Separador de Sección 03 (Selected Case Studies)
│   ├── Slide 17: Caso 1 — Soporte Táctico: Final Pekín 2008 (P&R Drop y Zona 2-3)
│   ├── Slide 18: Caso 2 — Data Engineering: Almacén OLAP con DuckDB y Parquet
│   ├── Slide 19: Caso 3 — ML Riguroso: Validación Walk-Forward sin Data Leakage
│   └── Slide 20: Caso 4 — Inferencia en R: Estabilidad de Tiro y Quarto CLI
│
├── 🧪 ACTO IV: VALIDACIÓN & RIGOR DE INGENIERÍA (Slides 21–24)
│   ├── Slide 21: Separador de Sección 04 (Validation & Rigor)
│   ├── Slide 22: Suite de Pruebas Automatizadas (227 tests en pytest, 100% pass)
│   ├── Slide 23: Paridad Cross-Language (Python + R + DuckDB)
│   └── Slide 24: Reproducibilidad Determinista en 1 Comando (`run_project.py`)
│
└── 🛡️ ACTO V: LÍMITES, IMPACTO & CIERRE (Slides 25–30)
    ├── Slide 25: Separador de Sección 05 (Limitations & Scope)
    ├── Slide 26: Matriz de Límites: Qué Demuestra el Sistema vs Qué No Afirma
    ├── Slide 27: Propuesta de Valor por Rol (Entrenador, Scout, Director Técnico)
    ├── Slide 28: Plan de Integración en Clubes (Hoja de ruta a 30 días)
    ├── Slide 29: Conclusiones y Principios ("El dato estructura la evidencia...")
    └── Slide 30: Repositorio GitHub, Licencia MIT y Citación
```

---

## 🎨 Sistema Visual y Principios de Diseño

1. **Variedad de Composiciones**: Portadas y separadores oscuros (`#0A1128`), diapositivas de métricas gigantes, diagramas de flujo horizontal, matrices divididas en 2 columnas y rejillas de arquetipos.
2. **Jerarquía Visual de 3–7 Segundos**: Cada diapositiva comunica su conclusión principal de inmediato; el detalle secundario se explora en 15–30 segundos.
3. **Metodología Data-First**: Posicionamiento 100% transparente basado en actas oficiales y modelado estadístico, sin afirmaciones no respaldadas.
4. **Generación Automatizada**: El deck completo se compila deterministamente ejecutando:
   ```bash
   python scripts/generate_master_deck.py
   ```
