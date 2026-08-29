[🇪🇸 Español](case_03_calibrated_ml_walk_forward.md) | [🇬🇧 English](case_03_calibrated_ml_walk_forward_EN.md)

# CASO DE ESTUDIO 3: MACHINE LEARNING CALIBRADO Y VALIDACIÓN WALK-FORWARD
## International Basketball Analytics (2005–2024)

> **Perfil de Audiencia**: *Lead Data Scientists, Quantitative Researchers, Directores de Machine Learning e Investigadores Deportivos.*  
> **Pregunta Clave**: *¿Cómo evitar el data leakage temporal en series deportivas y calibrar probabilidades realistas en competiciones cortas?*

---

## 1. El Problema del K-Fold Aleatorio en Deportes

El error más común en la modelización predictiva de eventos deportivos es utilizar validación cruzada aleatoria ($k$-fold estándar). 
Si se mezclan partidos de 2022 para entrenar un modelo que evalúa un partido de 2008, el algoritmo "aprende" la evolución táctica del futuro (el aumento del triple, el espaciado moderno) y produce métricas artificialmente infladas pero totalmente inútiles en producción.

---

## 2. Metodología de Validación Walk-Forward en 17 Folds

Implementamos un esquema expansivo cronológico estricto:

```text
Fold 01: Train [EuroBasket 2005]                 --> Test [World Cup 2006]
Fold 02: Train [2005..2006]                       --> Test [EuroBasket 2007]
...
Fold 17: Train [EuroBasket 2005..World Cup 2023] --> Test [Juegos Olímpicos 2024]
```

- **Muestra Total Evaluada Out-of-Sample**: **1.105 partidos** (sin que el modelo haya visto jamás un dato del torneo evaluado).
- **Entrenamiento**: Árboles de decisión con Gradient Boosting regularizado L2 (**LightGBM**).
- **Variables de Entrada**: Diferenciales históricos de Four Factors prepartido, ritmo relativo, días de descanso y continuidad del núcleo de jugadores.

---

## 3. Calibración Probabilística y Métricas Auditadas

En el deporte profesional, predecir con certeza absoluta es una falacia. Lo relevante es que las probabilidades estimadas sean **frecuentistamente fiables** (calibradas):

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        RESULTADOS AUDITADOS FUERA DE MUESTRA                           │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ • Brier Score (Error Cuadrático de Probabilidad):                                      │
│   0.1967 (frente al 0.2500 de un baseline naive no informativo, mejora del +21.3%)    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ • Expected Calibration Error (ECE):                                                    │
│   0.0314 (3.14% de desviación máxima entre probabilidad predicha y frecuencia real)   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ • Error Absoluto Medio (MAE) en Margen de Puntos:                                      │
│   11.74 puntos por encuentro (en línea con la varianza intrínseca del juego FIBA)      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Explicabilidad Local mediante TreeSHAP y Límites de Causalidad

- **Atribución Local**: Descomponemos cada predicción prepartido mediante valores SHAP para que el cuerpo técnico entienda qué factores empujan la probabilidad hacia la victoria (ej. diferencial en eFG% y control de pérdidas).
- **Distinción Crítica**: Dejamos explícito que la atribución matemática de SHAP describe relaciones en el espacio de características del modelo, **no garantías causales mecánicas en la pista**.

---

## 5. Qué Demuestra este Caso de Estudio

- Rigor metodológico para **eliminar el sobreajuste (overfitting)** y la fuga temporal.
- Dominio de **técnicas de calibración probabilística** (Platt Scaling e Isotonic Regression).
- Capacidad de comunicar **incertidumbre y límites científicos** a comités directivos.
