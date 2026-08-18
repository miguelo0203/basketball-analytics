# AUDITORÍA DEL SHOWCASE DE PORTFOLIO Y CASOS DE ESTUDIO (MVP-26)
## International Basketball Analytics (2005–2024)

> **Objetivo**: Evaluar la representatividad, rigor y capacidad de demostración práctica de los casos de estudio seleccionados para el portfolio profesional.

---

## 1. Verificación de Evidencia Real en los 4 Casos de Estudio

| Caso de Estudio | Área de Dominio | Archivos Fuente Auditados | Métricas Verificables | Veredicto |
|---|---|---|---|:---:|
| **Caso 1: Soporte Táctico y Briefs** | Basketball Decision Support | `reports/mvp10/`, `src/analytics/mvp10_brief_generator.py` | Pekín 2008 (-8.4 pts pred vs -11 pts real), Four Factors, alertas P&R Drop (κ=0.80). | **VERIFICADO (PASS)** |
| **Caso 2: Ingeniería OLAP con DuckDB** | Sports Data Engineering | `data/03_validated/`, `src/normalization/entity_resolver.py` | 12 tablas, 2.124 jugadores únicos, 200 min/partido, SHA-256 inmutables. | **VERIFICADO (PASS)** |
| **Caso 3: ML Calibrado Walk-Forward** | Machine Learning & Statistics | `src/analytics/mvp6_supervised_models.py`, `reports/figures/mvp6/` | 17 folds, 1.105 partidos test, Brier Score 0.1967, ECE 0.0314, MAE 11.74 pts. | **VERIFICADO (PASS)** |
| **Caso 4: Inferencia R y Arquetipos** | Exploratory Data Analysis & Scouting | `R/exploratory_analysis.qmd`, `src/analytics/player_roles.py` | 3.767 campañas, 6 arquetipos K-Means/PCA (>60% var), bootstrap B=5.000 (λ=0.75). | **VERIFICADO (PASS)** |

---

## 2. Mapa de Valor por Audiencia Profesional

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        QUÉ DEMUESTRA EL PORTFOLIO A CADA PERFIL                        │
├───────────────────────────────┬────────────────────────────────────────────────────────┤
│ Head Coach / Ayudante         │ "Puedo darte briefs de 1.5 páginas que te ahorren      │
│                               │ tiempo y te hagan las preguntas clave antes del partido"│
├───────────────────────────────┼────────────────────────────────────────────────────────┤
│ Director Deportivo / Scout    │ "Puedo mapear arquetipos funcionales objetivos y       │
│                               │ neutralizar la varianza de tiro al evaluar jugadores"  │
├───────────────────────────────┼────────────────────────────────────────────────────────┤
│ Lead Data Engineer            │ "Puedo construir almacenes relacionales OLAP limpios,  │
│                               │ deterministas y con 227 tests automatizados en pytest" │
├───────────────────────────────┼────────────────────────────────────────────────────────┤
│ Sports Tech / Data Scientist  │ "Puedo entrenar modelos sin data leakage y calibrar    │
│                               │ probabilidades con rigor científico (Brier y ECE)"     │
└───────────────────────────────┴────────────────────────────────────────────────────────┘
```
