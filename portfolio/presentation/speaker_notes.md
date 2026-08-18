# Notas del Orador para la Presentación Ejecutiva
## Guía de Exposición Oral (25–35 Minutos)

**Presentador**: Miguel  
**Objetivo**: Guiar al panel evaluador a través de la metodología, el pensamiento probabilístico y el valor operativo del analista de baloncesto.

---

### Diapositiva 1 — Portada (0:00–0:45)
- **Mensaje Clave**: *"Buenos días. Hoy quiero presentarles un proyecto de analítica e ingeniería de datos de baloncesto que sintetiza 20 años de competiciones internacionales oficiales. La misión central de este trabajo no es construir un algoritmo que pretenda adivinar marcadores, sino demostrar cómo un analista transforma datos heterogéneos en evidencia interpretable y accionable para apoyar la toma de decisiones de un cuerpo técnico."*

---

### Diapositiva 2 — La Idea en 30 Segundos (0:45–1:30)
- **Mensaje Clave**: *"Si tuviera que resumir este proyecto en una frase: construí un sistema reproducible de 9 capas que conecta datos brutos de partido con la pizarra del entrenador. Seguimos un flujo estricto: Datos ➔ Análisis ➔ Validación ➔ Contexto ➔ Decisión. El foco está puesto en la calidad del proceso analítico y en cuantificar la incertidumbre."*

---

### Diapositiva 3 — Qué Problema Resuelve un Analista (1:30–2:30)
- **Mensaje Clave**: *"En el baloncesto de alta competición, los entrenadores no sufren por falta de datos, sino por exceso de ruido: boxscores descontextualizados, varianza de tiro en torneos cortos y el inevitable sesgo retrospectivo de evaluar las decisiones solo por si el balón entró o no. El rol del analista es filtrar ese ruido, unir la estadística con el vídeo y estructurar preguntas claras para la reunión técnica."*

---

### Diapositiva 4 — Qué Construí: Arquitectura en 9 Capas (2:30–3:30)
- **Mensaje Clave**: *"Aquí vemos la arquitectura desacoplada: desde la ingesta con firmas criptográficas SHA-256 y el almacén relacional DuckDB, pasando por la minería de roles funcionales, la validación de vídeo, el Machine Learning calibrado y la simulación Monte Carlo, hasta llegar al Workspace operativo en Streamlit."*

---

### Diapositiva 5 — Escala y Cifras Clave (3:30–4:30)
- **Mensaje Clave**: *"El sistema abarca 18 torneos oficiales entre 2005 y 2024, 1.145 partidos y más de 27.000 registros individuales. Evaluamos 1.105 partidos fuera de muestra en 17 folds walk-forward y ejecutamos 180.000 simulaciones Monte Carlo, todo respaldado por una suite de 195 tests automatizados con el 100% de éxito."*

---

### Diapositiva 6 — Calidad de Datos y QA (4:30–5:30)
- **Mensaje Clave**: *"Un principio innegociable en ingeniería de datos: 'Un análisis sofisticado construido sobre datos incorrectos sigue siendo incorrecto'. Diseñé un pipeline determinista que unificó 2.124 identidades de jugador y validó que cada partido cuadre exactamente en 200 minutos y en la suma de puntos con el tanteo final."*

---

### Diapositiva 7 — Más Allá de los PPG (5:30–6:30)
- **Mensaje Clave**: *"En el baloncesto profesional, los puntos por partido (PPG) pueden ser una trampa. Un jugador con 18 PPG pero bajo True Shooting y alto uso de balón puede restar eficiencia al quinteto. Por eso descomponemos el juego en posesiones normalizadas, eficiencia de tiro ponderada y Four Factors."*

---

### Diapositiva 8 — Four Factors y Contexto (6:30–7:30)
- **Mensaje Clave**: *"Utilizamos los Four Factors de Dean Oliver como disparadores de preguntas tácticas: el eFG% nos habla de selección de tiro; el TOV% de seguridad de balón; el ORB% de segundas oportunidades vs. balance defensivo; y el FTR de agresividad vertical atacando el aro rival."*

---

### Diapositiva 9 — Player Analytics (7:30–8:30)
- **Mensaje Clave**: *"Al analizar jugadores, la pregunta relevante no es '¿cuánto produce?', sino '¿qué función desempeña en el sistema?'. Evaluamos estadísticas por 40 minutos, ratios de asistencia/pérdida y la estabilidad del perfil a lo largo de múltiples torneos."*

---

### Diapositiva 10 — Arquetipos Funcionales (8:30–9:30)
- **Mensaje Clave**: *"Mediante K-Means++ y PCA sobre 3.767 campañas cualificadas, identificamos 6 roles funcionales objetivos: Iniciadores, Espaciadores, Ejes Interiores, Directores, Anclas Defensivas y Aleros Equilibrados. Esto ayuda a directores deportivos a auditar la complementariedad de una plantilla."*

---

### Diapositiva 11 — Del Número a la Pista (9:30–10:30)
- **Mensaje Clave**: *"La analítica no termina en una tabla de Excel. El proceso requiere tender un puente: la estadística detecta un patrón, formulamos una hipótesis táctica, auditamos la cinta de vídeo y traducimos la conclusión a una recomendación comprensible para el entrenador."*

---

### Diapositiva 12 — Validación Táctica en Vídeo (10:30–11:30)
- **Mensaje Clave**: *"Para incorporar rigor científico a la observación cualitativa, implementamos un protocolo de doble codificación independiente en 420 posesiones, logrando un Cohen's Kappa de κ = 0.80 en la calificación defensiva de drop en pick-and-roll. La fiabilidad es lo que convierte la opinión en evidencia."*

---

### Diapositiva 13 — Machine Learning Supervisado (11:30–12:30)
- **Mensaje Clave**: *"Desarrollamos modelos supervisados comparando baselines simples con LightGBM. Nuestro modelo calibrado alcanzó un Brier Score de 0.1967 y un ECE de 0.0314. Presentamos estos números con rigor: describen el comportamiento histórico del modelo bajo este protocolo, no una promesa de infalibilidad."*

---

### Diapositiva 14 — Validación Walk-Forward (12:30–13:30)
- **Mensaje Clave**: *"Esta es una de las diapositivas clave: utilizamos 17 folds walk-forward expansivos. El modelo de 2008 solo vio datos hasta 2007; el de 2024 vio datos hasta 2023. Cero data leakage del futuro. Prefiero una métrica honesta a una precisión inflada con trampas temporales."*

---

### Diapositiva 15 — Incertidumbre y Calibración (13:30–14:30)
- **Mensaje Clave**: *"En deporte, no solo importa lo que dice el modelo, sino cuánto deberíamos confiar en él. La calibración isotónica asegura que las probabilidades reflejen frecuencias reales, y el bootstrap agrupado con 5.000 iteraciones nos entrega intervalos de confianza empíricos al 95%."*

---

### Diapositiva 16 — Atribución TreeSHAP (14:30–15:30)
- **Mensaje Clave**: *"Aviso imprescindible: 'Estas asociaciones son predictivas, no causales'. Los valores SHAP muestran qué variables desplazan la probabilidad condicional del algoritmo, pero no garantizan que cambiar el ritmo en la pista produzca automáticamente una victoria."*

---

### Diapositiva 17 — Simulación Monte Carlo (15:30–16:30)
- **Mensaje Clave**: *"Propagamos las probabilidades calibradas a través de 10.000 iteraciones Monte Carlo por torneo aplicando shrinkage (λ = 0.75). Esto nos permite proyectar la distribución empírica de avance en el cuadro considerando cruces y posibles sorpresas."*

---

### Diapositiva 18 — Por Qué Simular un Torneo (16:30–17:30)
- **Mensaje Clave**: *"Un partido y un campeonato son problemas distintos. En un partido individual, la varianza de tiro puntual puede decidirlo todo. La simulación permite entender cómo una victoria en fase de grupos altera la dificultad del cruce y maximiza las opciones de medalla."*

---

### Diapositiva 19 — Del Análisis a la Decisión (17:30–18:30)
- **Mensaje Clave**: *"Integración de 6 capas de evidencia: producción, fiabilidad, rol, vídeo, impacto predictivo y contexto de torneo. Ninguna capa decide por sí sola: la decisión surge de contrastar las distintas fuentes de información."*

---

### Diapositiva 20 — Detección de Contradicciones (18:30–19:30)
- **Mensaje Clave**: *"El verdadero valor del analista aparece cuando los datos y el vídeo discrepan. Si las estadísticas agregadas dicen que un rival es favorito por +30 puntos, pero el vídeo revela que su pívot concede tiros abiertos en pick-and-pop por defender en drop muy profundo, no ocultamos el conflicto: lo hacemos explícito para el cuerpo técnico."*

---

### Diapositiva 21 — Caso Real: Pekín 2008 (19:30–21:00)
- **Mensaje Clave**: *"Ejemplo real: la Final Olímpica de Pekín 2008. España venía de perder por 37 puntos en grupos. El modelo daba un 26.8% de opciones a España. Al analizar la media pista, España tenía un Net Rating superior y detectamos la debilidad en el drop de EE. UU. España usó zona 2-3 y pick-and-pop, situándose a 4 puntos a falta de 2 minutos. El resultado (118–107) cayó dentro del intervalo del 95%: una realización probabilística coherente con el análisis previo."*

---

### Diapositiva 22 — Caso Real: EuroBasket 2015 (21:00–22:00)
- **Mensaje Clave**: *"En el EuroBasket 2015, España perdió 2 partidos en grupos por rachas extremas de triple rival. La prensa hablaba de fin de ciclo, pero el sistema mantuvo una proyección de título del 67.6% al ver que el Net Rating subyacente y la dominancia de Pau Gasol estaban intactos. España ganó el Oro. El analista aporta valor evitando el pánico ante muestras pequeñas."*

---

### Diapositiva 23 — Qué Puede Hacer un Entrenador con Esto (22:00–23:00)
- **Mensaje Clave**: *"El analista no le dice al entrenador a quién poner; le entrega respuestas a 6 preguntas críticas: dónde perdemos eficiencia, de dónde vienen las pérdidas, qué quintetos son sostenibles, qué ajustes de P&R explotar, qué sensibilidad tiene el cuadro y qué conclusiones tienen evidencia sólida."*

---

### Diapositiva 24 — Ejemplo de Brief Prepartido (23:00–24:00)
- **Mensaje Clave**: *"Aquí vemos el formato de informe prepartido: 1.5 páginas estructuradas en contexto, 3 prioridades tácticas, alerta de contradicción, preguntas para el cuerpo técnico y límites de incertidumbre. Diseñado para leerse en 2.5 minutos antes del shootaround."*

---

### Diapositiva 25 — Qué Haría Diferente en un Club Real (24:00–25:00)
- **Mensaje Clave**: *"Reconozco con total honestidad que este proyecto es histórico. En un club profesional de ACB o Euroliga, conectaríamos esta misma metodología a las cámaras de tracking 25Hz de Second Spectrum, a los datos físicos de Catapult GPS y a la base de datos de contratos para scouting de mercado."*

---

### Diapositiva 26 — Qué Aportaría como Analista (25:00–26:00)
- **Mensaje Clave**: *"Desde el primer día aportaría valor en 6 áreas: ingeniería de datos con DuckDB/SQL, analítica avanzada y ML, dominio del lenguaje táctico de baloncesto, control estricto de calidad y testing, comunicación ejecutiva y soporte directo a la toma de decisiones."*

---

### Diapositiva 27 — Lo Que NO Haría (26:00–27:00)
- **Mensaje Clave**: *"Mis líneas rojas profesionales: jamás sustituiría el criterio del entrenador, jamás vendería correlación como causalidad, jamás prometería certezas imposibles ni usaría datos del futuro para maquillar conclusiones."*

---

### Diapositiva 28 — Límites Metodológicos (27:00–28:00)
- **Mensaje Clave**: *"Tratamos los límites como una muestra de madurez: torneos cortos con varianza de tiro, ausencia de tracking continuo en datos históricos y cambios en la línea de tres puntos en 2010. Conocer los límites es lo que hace fiable al analista."*

---

### Diapositiva 29 — El Repositorio en GitHub (28:00–29:00)
- **Mensaje Clave**: *"Todo este trabajo es 100% público, auditable y reproducible en GitHub, estructurado con itinerarios de lectura de 2, 5, 15 y 30+ minutos para que cualquier evaluador pueda verificar el código y los 195 tests en 90 segundos."*

---

### Diapositiva 30 — Cierre y Filosofía (29:00–30:00)
- **Mensaje Clave**: *"Concluyo con la frase que resume mi vocación: 'El modelo no toma la decisión. Ayuda a que la decisión tenga mejor información detrás'. Muchas gracias, quedo a su entera disposición para cualquier pregunta."*
