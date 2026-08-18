# Guía de Figuras Analíticas Públicas
## Explicación Visual y Metodológica de las Figuras Clave del Portfolio

**Ubicación de las imágenes**: `portfolio/figures/`  
**Objetivo**: Facilitar la interpretación rápida de los gráficos sin requerir tecnicismos innecesarios.

---

### Figura 1: El Flujo de Datos a Soporte a Decisiones (`fig1_evidence_pipeline.png`)
- **Pregunta que responde**: *¿Cómo transforma el analista actas dispersas y vídeo en un informe prepartido accionable para el entrenador?*
- **Fuente de datos**: Pipeline analítico completo (`mart_team_game_analytics`, `mart_tactical_video`).
- **Metodología**: Descomposición en 5 capas ($\text{Datos} \rightarrow \text{Análisis} \rightarrow \text{Evidencia} \rightarrow \text{Contexto} \rightarrow \text{Soporte a Decisiones}$).
- **Interpretación**: Separa formalmente la ingeniería de datos de la toma de decisiones tácticas.
- **Qué NO permite concluir**: No implica que el proceso sea completamente automático; requiere juicio del analista.

---

### Figura 2: Calibración de Probabilidades Out-of-Sample (`fig2_probability_calibration.png`)
- **Pregunta que responde**: *Cuando el modelo afirma que un equipo tiene un 70% de opciones de ganar, ¿gana realmente 7 de cada 10 veces?*
- **Fuente de datos**: 1.105 predicciones fuera de muestra en 17 folds temporales (2005–2024).
- **Metodología**: Diagrama de fiabilidad de Regresión Isotónica con cálculo de Error Esperado de Calibración ($\text{ECE} = 0.0314$).
- **Interpretación**: Las probabilidades del modelo están calibradas empíricamente y son seguras para simulaciones Monte Carlo.
- **Qué NO permite concluir**: No elimina la varianza estocástica ni garantiza el acierto en un partido individual.

---

### Figura 3: Mapa de Arquetipos Funcionales de Jugador (`fig3_player_archetypes_pca.png`)
- **Pregunta que responde**: *¿Cómo podemos clasificar a los jugadores según su uso de balón, tiro y pase en pista en lugar de su posición nominal tradicional?*
- **Fuente de datos**: 3.767 campañas de jugador cualificadas ($\ge 40$ minutos) en DuckDB.
- **Metodología**: Agrupamiento K-Means++ ($K=6$) proyectado en el plano de componentes principales (PCA).
- **Interpretación**: Identifica 6 perfiles funcionales (Iniciador Principal, Espaciador Móvil, Eje Interior, Director, Ancla Defensiva, Alero Equilibrado).
- **Qué NO permite concluir**: No mide intangibles defensivos ni química de vestuario.

---

### Figura 4: Evolución Histórica de los Four Factors (`fig4_four_factors_evolution.png`)
- **Pregunta que responde**: *¿Cómo ha cambiado estructuralmente el baloncesto internacional entre 2005 y 2024?*
- **Fuente de datos**: 2.290 observaciones de equipo en `fact_team_game`.
- **Metodología**: Comparación longitudinal de ritmo y Four Factors ajustados por posesión.
- **Interpretación**: Muestra la expansión masiva del volumen de triples ($27.4\% \rightarrow 38.6\%$) y la reducción de la tasa de tiros libres ($34.2\% \rightarrow 25.8\%$).
- **Qué NO permite concluir**: No demuestra causalidad exclusiva del cambio de línea de 3 puntos sin considerar la evolución atlética global.

---

### Figura 5: Motor de Detección de Contradicciones Tácticas (`fig5_contradiction_engine.png`)
- **Pregunta que responde**: *¿Qué ocurre cuando la estadística favorece claramente a un rival pero el vídeo revela un defecto defensivo aprovechable?*
- **Fuente de datos**: Feature store prepartido cruzado con 420 posesiones de vídeo táctico.
- **Metodología**: Matriz heurística de discrepancias entre Net Rating y coberturas de bloqueo directo.
- **Interpretación**: Alerta al cuerpo técnico de oportunidades tácticas ocultas (ej. atacar el drop con tiros en pick-and-pop).
- **Qué NO permite concluir**: Requiere validación con el plan de partido específico del entrenador.
