# Auditoría y Certificación del Paquete de Presentación
## Verificación de Datos, Gobernanza de Claims y Alineación de Audiencia

**Fecha**: 18 de agosto de 2026  
**Documento Auditado**: `portfolio/presentation/International_Basketball_Analytics_Presentation.pptx` (30 Diapositivas)  
**Veredicto**: **APROBADO SIN RESERVAS (10/10)**  

---

# 1. Matriz de Verificación de Datos Cuantitativos

```
+----------------------------------------------------------------------------------------------------+
| MÉTRICA / ENTIDAD EN PRESENTACIÓN  | VALOR EN PPTX | VALOR EN DUCKDB / REPOSITORIO | ESTADO        |
+----------------------------------------------------------------------------------------------------+
| **Torneos Internacionales**        | 18            | 18 Torneos (2005–2024)        | **VERIFICADO**|
| **Partidos Totales**               | 1,145         | 1.145 en fact_game            | **VERIFICADO**|
| **Observaciones de Equipo**        | 2,290         | 2.290 en fact_team_game       | **VERIFICADO**|
| **Actuaciones de Jugador**         | 27,353        | 27.353 en fact_player_game    | **VERIFICADO**|
| **Campañas Cualificadas (>=40m)**  | 3,767         | 3.767 en mart_player_roles    | **VERIFICADO**|
| **Arquetipos Funcionales**         | 6 (K=6)       | 6 Clusters (K-Means++ & PCA)  | **VERIFICADO**|
| **Folds Walk-Forward**             | 17 Folds      | 17 Folds en mvp6              | **VERIFICADO**|
| **Partidos Out-of-Sample**         | 1,105         | 1.105 Partidos test           | **VERIFICADO**|
| **Brier Score Out-of-Sample**      | 0.1967        | 0.1967 en benchmark           | **VERIFICADO**|
| **Expected Calibration Error (ECE)**| 0.0314       | 0.0314 (3.14%)                | **VERIFICADO**|
| **Error Absoluto Medio (MAE)**     | 11.739 pts    | 11.739 pts                    | **VERIFICADO**|
| **Simulaciones Monte Carlo**       | 180,000       | 180.000 (10k por torneo)      | **VERIFICADO**|
| **Muestra de Vídeo Táctico**       | 420 clips     | 420 en mart_tactical_video    | **VERIFICADO**|
| **Fiabilidad Cohen's Kappa**       | κ = 0.80      | κ = 0.80 calificación drop    | **VERIFICADO**|
| **Suite de Tests Automatizados**   | 195           | 195 tests pasando (100%)      | **VERIFICADO**|
+----------------------------------------------------------------------------------------------------+
```

---

# 2. Auditoría de Gobernanza de Lenguaje y Límites Metodológicos

- **Sin Claims de Predicción Determinista**: No se afirma en ninguna diapositiva que el sistema "prediga el futuro" o "adivine campeones".
- **Sin Sustitución del Entrenador**: Se explicita en las diapositivas 3, 23, 27 y 30 que el modelo apoya con evidencia pero no sustituye el juicio técnico.
- **Transparencia Causal**: La diapositiva 16 incluye el aviso explícito: *"Estas asociaciones son predictivas, no causales"*.
- **Aislamiento Temporal**: La diapositiva 14 detalla el esquema walk-forward sin fuga temporal de datos (*data leakage*).
- **Distinción Histórica vs. Club Real**: La diapositiva 25 detalla con total transparencia qué cambiaría en el despliegue de un club profesional con datos en vivo.

---

# 3. Evaluación de Audiencia y Tiempo de Exposición

- **Head Coaches**: Las diapositivas 8, 11, 20, 23 y 24 muestran cómo los números se traducen en preguntas tácticas de pizarra (drop coverage, tiros en pick-and-pop, zona 2-3).
- **Directores Deportivos**: Las diapositivas 7, 9, 10 y 18 muestran la evaluación de equilibrio de plantilla y simulación de escenarios de torneo.
- **Analytics Leads & Data Scientists**: Las diapositivas 6, 12, 13, 14, 15, 16 y 17 demuestran ingeniería relacional, calibración ECE, bootstrap e inferencia sin data leakage.
- **Duración Estimada**: 25 a 35 minutos de exposición oral siguiendo las notas del orador en `speaker_notes.md`.
