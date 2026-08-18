# Marco de Testing y Aseguramiento de Calidad

## 1. Cobertura de la Suite de Pruebas Automatizadas

El repositorio cuenta con una suite integral de **227 tests automatizados** distribuidos en 26 módulos de prueba (`tests/analytics/`), ejecutados con pytest.

```
+----------------------------------------------------------------------------------------------------+
| MÓDULO / CAPA TESTEADA       | NÚMERO | INVARIANTE Y PROPIEDAD TÉCNICA AUDITADA                    |
+----------------------------------------------------------------------------------------------------+
| **test_data_validation.py**  | 12     | Integridad relacional DuckDB, 200 min/partido, SHA-256.    |
| **test_econometrics.py**     | 10     | Regresión segmentada ITS, significancia empírica de regla. |
| **test_player_roles.py**     | 14     | Convergencia K-Means++, varianza explicada PCA (>60%).     |
| **test_scouting.py**         | 12     | Normalización de Candidate Fit Index y trade-offs de tiro. |
| **test_video_layer.py**      | 15     | Coeficientes Cohen's Kappa (κ=1.00 tipo, κ=0.80 score).    |
| **test_supervised_ml.py**    | 18     | 17 Folds walk-forward, Brier <= 0.20, ECE <= 0.05.         |
| **test_simulations.py**      | 15     | Suma estocástica de probabilidades = 1.0, shrinkage λ=0.75 |
| **test_decision_system.py**  | 15     | Matriz de decisión de 8 capas y detección de contradicción.|
| **test_workspace.py**        | 20     | Aislamiento temporal anti-hindsight y carga de briefs.    |
| **test_final_presentation.py**| 6     | Validación de 30 slides, guión visual y notas de orador.  |
| **test_professionalization.py**| 8    | Validación de perfil, pitches, FAQ y outreach package.    |
| **test_job_application.py**  | 9      | Validación de CV, LinkedIn, 6 guías de entrevista y tracker|
| **test_r_integration.py**    | 6      | Validación de funciones R, scripts EDA, Quarto y visual.   |
| **test_mvp15_reproducibility.py**| 3  | Validación de artefactos, coherencia Parquet/DuckDB y R fig|
| **test_portfolio_release.py**| 74     | Integridad de claims, rutas, gobernanza y reproducibilidad.|
| **TOTAL VERIFICADO**         | **227**| **100% DE TASA DE ÉXITO (0 errores, 0 fallos)**             |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. Ejecución Local de Tests

```bash
# Ejecutar suite completa en modo silencioso
python -m pytest tests -q

# Ejecutar con detalle de cada test
python -m pytest tests -v
```

---

## 3. Principio de Honestidad Metodológica

> [!IMPORTANT]
> **Qué demuestran y qué NO demuestran los tests**:
> - **Demuestran**: Integridad de la base de datos, corrección matemática de las fórmulas, ausencia de fuga temporal (*data leakage*) y reproducibilidad determinista del software.
> - **NO Demuestran**: Que los modelos predictivos sean infalibles ni que una recomendación táctica garantice la victoria en un partido real.
