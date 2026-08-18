# Machine Learning, Calibración e Inferencia Estadística

## 1. Formulación del Problema Predictivo Prepartido

El subsistema de Machine Learning (`src/analytics/mvp6_supervised_analytics.py`) estima la distribución condicional prepartido:
$$P(\text{Victoria Team A} \mid \mathcal{F}_{t-1})$$
y el margen de puntos esperado $\mathbb{E}[\Delta \text{Pts} \mid \mathcal{F}_{t-1}]$, donde $\mathcal{F}_{t-1}$ representa la información conocida estrictamente antes del salto inicial.

---

## 2. Validación Temporal Walk-Forward en 17 Folds

Para evitar el sesgo de fuga de información (*data leakage*), no se utiliza validación cruzada aleatoria tradicional (k-fold shuffle). 

Se implementa un esquema de **ventana temporal expansiva en 17 particiones**:
- Para predecir el torneo $k$, el modelo se entrena exclusivamente con los torneos $1, \dots, k-1$.
- Total de partidos evaluados fuera de muestra (*out-of-sample*): **1.105 partidos**.

```
Fold 1 (Entrena T1..T1)  -> Prueba T2
Fold 2 (Entrena T1..T2)  -> Prueba T3
...
Fold 17 (Entrena T1..T17) -> Prueba T18 (JJ.OO. París 2024)
```

---

## 3. Calibración de Probabilidades (Brier Score y ECE)

En el ámbito deportivo, la precisión clasificatoria pura ($0/1$) es insuficiente porque los partidos son sucesos probabilísticos. Un equipo con un $70\%$ de opciones de victoria debe ganar 7 de cada 10 veces.

El modelo LightGBM base se calibra mediante **Regresión Isotónica out-of-sample**:
- **Brier Score Out-of-Sample**: **$0.1967$** (frente a $0.2500$ de un modelo aleatorio no informativo).
- **Expected Calibration Error ($\text{ECE}$)**: **$0.0314$** ($3.14\%$), demostrando una excelente alineación entre probabilidades pronosticadas y frecuencias empíricas reales.
- **Error Absoluto Medio de Margen ($\text{MAE}$)**: **$11.74\text{ puntos}$**.

---

## 4. Interpretabilidad mediante TreeSHAP (Atribución $\ne$ Causalidad)

Se calculan valores de Shapley mediante el algoritmo TreeSHAP para explicar cómo cada factor desplaza la probabilidad respecto a la base del torneo:
- **Net Rating diferencial**: Mayor contribuyente global al desplazamiento log-odds.
- **Diferencial de eFG% y TOV%**: Principales motores tácticos.

> [!IMPORTANT]
> **Atribución frente a Causalidad**:
> Los valores SHAP describen cómo el modelo pondera estadísticamente las asociaciones históricas. **No demuestran una relación causal directa**. Aumentar el ritmo de juego en un partido no garantiza un incremento proporcional en la eficiencia.

---

## 5. Simulación Monte Carlo de Torneos (180.000 Iteraciones)

Las probabilidades calibradas se propagan a través de $10.000$ iteraciones Monte Carlo por torneo con un parámetro de shrinkage ($\lambda = 0.75$) para proyectar probabilidades de medalla y avance de ronda contemplando la varianza de emparejamientos.
