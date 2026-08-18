# Preguntas y Respuestas para Entrevistas de Baloncesto y Analytics
## Banco Exhaustivo de 32 Preguntas Técnicas, Tácticas, Metodológicas y Profesionales

---

# BLOQUE 1: INGENIERÍA Y MACHINE LEARNING (TECHNICAL)

### 1. ¿Por qué utilizaste DuckDB en lugar de una base de datos relacional tradicional (PostgreSQL) o Pandas puro?
> **Respuesta**: DuckDB es un motor OLAP columnar en proceso (*in-process*) optimizado para análisis analíticos masivos. A diferencia de Pandas, ejecuta consultas SQL complejas con ejecución vectorizada en memoria y procesamiento paralelo sin requerir infraestructura externa de servidor como PostgreSQL. Permite consultar directamente archivos Parquet y DuckDB de forma inmutable y determinista.

### 2. ¿Por qué exportar los marts analíticos a formato Parquet?
> **Respuesta**: Parquet es un formato de almacenamiento columnar binario con compresión eficiente (Snappy/ZSTD) y tipado estricto. Permite consultar únicamente las columnas necesarias (*column pruning*) y saltar bloques de datos mediante estadísticas de metadatos (*predicate pushdown*), acelerando la lectura en scripts de Python y aplicaciones Streamlit.

### 3. ¿Por qué implementaste validación temporal walk-forward en lugar de un K-Fold aleatorio convencional?
> **Respuesta**: En deportes y series temporales, las observaciones futuras no son independientes de las pasadas. Un K-Fold aleatorio mezcla partidos futuros en el conjunto de entrenamiento, contaminando el modelo con *data leakage*. El esquema walk-forward expansivo entrena estrictamente con datos hasta el torneo $T-1$ y evalúa sobre el torneo $T$, simulando el estado de información real de un analista antes de cada competición.

### 4. ¿Cómo garantizaste matemáticamente la ausencia total de fuga de datos (Data Leakage)?
> **Respuesta**: Todo el feature store prepartido se calcula utilizando únicamente ventanas retrospectivas estrictas previas al salto inicial del partido ($< \text{game\_date}$). Además, las estadísticas del torneo en curso solo acumulan los partidos jugados en la fase de grupos previa, excluyendo cualquier información del propio partido evaluado o de rondas posteriores.

### 5. ¿Por qué elegiste LightGBM frente a otros algoritmos de Gradient Boosting o Deep Learning?
> **Respuesta**: LightGBM maneja eficientemente características tabulares heterogéneas, es robusto ante correlaciones lineales entre métricas y permite un ajuste fino de regularización (profundidad máxima corta `max_depth=3`, número de hojas reducido `num_leaves=7` y `min_child_samples=15`) para evitar el sobreajuste en muestras de 1.145 partidos, donde las redes neuronales profundas tienden a memorizar el ruido.

### 6. ¿Qué representa el Brier Score y por qué lo utilizaste como métrica principal?
> **Respuesta**: El Brier Score es una regla de puntuación estrictamente adecuada (*strictly proper scoring rule*) que mide el error cuadrático medio de las probabilidades asignadas: $\text{BS} = \frac{1}{N}\sum (p_i - y_i)^2$. A diferencia de la precisión binaria (Accuracy), que descarta la calibración, el Brier Score castiga fuertemente la sobreconfianza en probabilidades erróneas. Nuestro modelo alcanzó `0.1967`, superando ampliamente el `0.2500` de un modelo aleatorio o el `0.2450` del baseline ingenuo.

### 7. ¿Qué es el Expected Calibration Error (ECE) y qué significa que sea 0.0314?
> **Respuesta**: El ECE mide la diferencia ponderada absoluta entre la probabilidad pronosticada y la frecuencia real de victoria observada agrupada en 10 intervalos. Un ECE de `0.0314` (3.14%) significa que cuando el modelo estima una probabilidad del 70%, empíricamente el equipo gana el 67%–73% de las veces, lo que garantiza que las probabilidades son fiables para simulaciones de torneo.

### 8. ¿Por qué el ROC-AUC fue 0.7613 y no más alto (ej. 0.90)?
> **Respuesta**: El baloncesto internacional de selecciones tiene una varianza intrínseca elevada (acierto exterior en torneos de 6–9 partidos). Un ROC-AUC de `0.7613` evaluado estrictamente fuera de muestra es un resultado honesto y realista. Modelos con AUC $> 0.90$ en este dominio suelen sufrir de sobreajuste o fuga retrospectiva de datos.

### 9. ¿Cómo realizaste la atribución de características e interpretabilidad?
> **Respuesta**: Utilizamos Permutation Importance sobre los pliegues de prueba fuera de muestra midiendo la caída en el Brier Score tras permutar aleatoriamente cada variable. Evaluamos la estabilidad temporal de los rankings mediante correlaciones de Spearman entre pliegues ($\rho = 0.854$).

---

# BLOQUE 2: DOMINIO DE BALONCESTO Y TÁCTICA (BASKETBALL)

### 10. ¿Por qué los Four Factors de Dean Oliver son superiores a la estadística tradicional de boxscore?
> **Respuesta**: Los Four Factors normalizan el juego por posesiones, aislando la eficiencia del ritmo. Descomponen el rendimiento en los cuatro pilares fundamentales del baloncesto: acierto en el tiro ponderando triples (eFG%), cuidado del balón (TOV%), dominio del rebote ofensivo (ORB%) y capacidad de sacar faltas (FTR).

### 11. ¿Por qué los Puntos por Partido (PPG) pueden engañar a un cuerpo técnico?
> **Respuesta**: Un jugador puede anotar 20 PPG jugando a un ritmo muy alto de 85 posesiones o consumiendo un 35% de las posesiones de su equipo con un porcentaje de tiro mediocre (TS% < 48%). Esto genera una falsa sensación de productividad pero resta eficiencia global al quinteto.

### 12. ¿Qué significa el Net Rating y cómo se interpreta en la práctica?
> **Respuesta**: Es la diferencia entre la eficiencia ofensiva (puntos anotados por 100 posesiones) y la defensiva (puntos encajados por 100 posesiones). Permite comparar equipos o quintetos que juegan a velocidades radicalmente distintas (ej. un equipo lento de 68 posesiones vs. uno rápido de 80 posesiones).

### 13. Si las estadísticas dicen que el rival es débil en el rebote defensivo, pero el vídeo muestra que cierran bien el aro, ¿cómo lo interpretas?
> **Respuesta**: Compruebo el contexto: el rival puede tener un bajo porcentaje de rebote defensivo porque juega con quintetos pequeños y envía a sus cuatro exteriores a correr el contraataque de forma agresiva. El vídeo ayuda a cualificar el número y a decidir si nos conviene cargar el rebote ofensivo o asegurar el balance defensivo para no conceder canastas fáciles.

### 14. ¿Cómo explicarías a un entrenador que un jugador tiene un +/- negativo a pesar de haber jugado un buen partido?
> **Respuesta**: El +/- bruto está fuertemente contaminado por el rendimiento de los otros 4 compañeros en pista y por los parciales del rival durante sus minutos de descanso. Si el jugador mantuvo una buena selección de tiro y ejecutó el plan defensivo, el +/- negativo puede deberse a rachas fortuitas de tiro exterior del rival o a minutos compartidos con la segunda unidad.

### 15. ¿Cómo traduces una debilidad estadística en una instrucción de pizarra?
> **Respuesta**: No le digo al cuerpo técnico *"su Defensive Rating es 112"*. Traduzco el dato a: *"Su pívot defiende el bloqueo directo muy hundido en la pintura (drop profundo) y conceden un 42% en tiros de media distancia tras bote; debemos involucrar a nuestros exteriores con tiro tras bote y generar situaciones de pick-and-pop"*.

---

# BLOQUE 3: METODOLOGÍA Y LÍMITES (METHODOLOGY)

### 16. ¿Qué parte de tu sistema es causal y qué parte es meramente predictiva?
> **Respuesta**: Todo el modelo de machine learning y los Four Factors son descriptivos y predictivos; reflejan asociaciones condicionales históricas. La única capa con inferencia cuasi-causal es el análisis de series temporales interrumpidas (ITS) para evaluar el impacto de los cambios de reglas FIBA (línea de tres a 6.75m en 2010). Jamás afirmo que modificar una variable estadística cause automáticamente una victoria.

### 17. ¿Cómo afecta la varianza del tiro de tres puntos en torneos cortos de 15 días?
> **Respuesta**: En torneos de 6 a 9 partidos, el porcentaje de triple de un equipo está dominado por la varianza de muestra corta. Un equipo con un 38% real de calidad de tiro puede encestar un 25% o un 50% en un torneo concreto. Por eso el sistema utiliza intervalos de confianza bootstrap y no sobrerreacciona a rachas puntuales.

### 18. ¿Por qué aplicaste Shrinkage (λ=0.75) en las simulaciones Monte Carlo?
> **Respuesta**: En eliminatorias a partido único, los modelos ML puros tienden a asignar probabilidades extremas (ej. 92% para el favorito). El shrinkage bayesiano contrae las probabilidades hacia una distribución más conservadora ($\lambda = 0.75$), reflejando la realidad de que en el baloncesto FIBA cualquier equipo de élite puede perder en un mal día de tiro.

### 19. ¿Cómo tratarías los cambios de convocatoria (*roster turnover*) entre veranos en selecciones?
> **Respuesta**: El sistema reconstruye las características del equipo ponderando las campañas individuales recientes de los jugadores convocados (mediante sus arquetipos funcionales y estadísticas por 40 minutos), en lugar de asumir que la selección mantiene su nivel histórico si ha cambiado a sus figuras principales.

### 20. ¿Qué harías si un jugador clave se lesiona dos horas antes del partido?
> **Respuesta**: El sistema modular permite recalcular instantáneamente la matriz de evidencia sustituyendo los minutos y el arquetipo del jugador lesionado por los de su reemplazo en la rotación, actualizando el perfil de quintetos y recalculando las proyecciones de ritmo y Four Factors.

---

# BLOQUE 4: ENTORNO PROFESIONAL Y CLUB REAL (PROFESSIONAL)

### 21. ¿Qué harías si el entrenador jefe rechaza una recomendación táctica basada en datos?
> **Respuesta**: Respeto absoluto a la autoridad del entrenador. El trabajo del analista es presentar la evidencia de forma clara, objetiva y sin sesgos, destacando pros, contras y niveles de incertidumbre. La decisión final siempre corresponde al cuerpo técnico; el analista apoya, no impone.

### 22. ¿Cómo priorizarías las tareas durante una semana con 3 partidos (ej. Euroliga + ACB)?
> **Respuesta**: Automatizo la generación de los briefs prepartido estándar (Four Factors, tendencias de rotación y tiros frecuentes) para tenerlos listos en cuanto termina la jornada anterior. Dedico el tiempo manual a los aspectos cualitativos críticos del siguiente rival: cambios de cobertura defensiva en los últimos 3 partidos y emparejamientos individuales clave.

### 23. ¿Cómo te integrarías y trabajarías con un analista senior o responsable de rendimiento?
> **Respuesta**: Con actitud de aprendizaje, rigor en la entrega y proactividad. Asumiría la carga técnica de ingesta, limpieza de datos, consultas SQL complejas y mantenimiento de pipelines para liberar tiempo del analista senior, adaptándome a los estándares metodológicos del club.

### 24. ¿Cómo comunicarías la incertidumbre estadística a personas que no tienen formación matemática?
> **Respuesta**: Evito tecnicismos como *"intervalo de confianza del 95% con distribución no paramétrica"*. Utilizo lenguaje intuitivo de escenarios: *"En 7 de cada 10 situaciones similares bajo este ritmo de partido el resultado se mantiene en una ventaja de entre 2 y 8 puntos a nuestro favor, pero si permiten que su tirador entre en racha, el margen se reduce a una posesión"*.

### 25. ¿Qué necesitas del cuerpo técnico para desempeñar tu trabajo de forma óptima?
> **Respuesta**: Comunicación abierta sobre sus prioridades tácticas y sus dudas principales para el siguiente partido. Si sé qué aspectos preocupan al entrenador (ej. cómo frenar el bloqueo directo lateral o el rebote del 4 rival), puedo enfocar el análisis en responder exactamente a esas preguntas.

### 26. ¿Qué diferencia este proyecto de un simple notebook de Kaggle con modelos de predicción?
> **Respuesta**: Un notebook de Kaggle optimiza una métrica abstracta mezclando datos sin considerar el tiempo. Este proyecto es un sistema de ingeniería completo con base de datos relacional DuckDB, 201 tests automatizados, validación temporal walk-forward sin fuga de datos, validación cualitativa en vídeo con Cohen's Kappa, motor de contradicciones y briefs prepartido enfocados en decisiones reales de baloncesto.

### 27. ¿Cómo evitarías que el equipo caiga en el sesgo de confirmación al analizar vídeo?
> **Respuesta**: Contrastando la selección de clips de vídeo con la distribución estadística completa. Si el cuerpo técnico recuerda una canasta dolorosa de un tirador rival, compruebo la muestra completa de sus tiros en esa situación específica para determinar si fue un hecho aislado o una tendencia sistemática.

### 28. ¿Qué herramientas de tracking óptico te gustaría aprender e incorporar en un club?
> **Respuesta**: Second Spectrum y Synergy Sports para analizar datos espaciales 2D/3D (posicionamiento de defensores, velocidad de closeouts, calidad de tiros generados / Shot Quality) combinándolos con datos físicos de Catapult GPS para monitorizar cargas de entrenamiento y frescura en pista.

### 29. ¿Cómo valoras el trabajo en equipo y la colaboración interdisciplinar en un club?
> **Respuesta**: La analítica no opera en una burbuja aislada. Debe integrarse armónicamente con los preparadores físicos, fisioterapeutas, analistas de vídeo y cuerpo técnico. El dato es una herramienta al servicio de todos los departamentos para mejorar el rendimiento del equipo.

### 30. ¿Por qué deberíamos contratarte como Basketball Data Analyst?
> **Respuesta**: Porque combino una sólida base técnica en ingeniería de datos, SQL, Python y modelado estadístico riguroso con un profundo entendimiento del juego de baloncesto. No busco deslumbrar con algoritmos de caja negra; busco aportar soluciones prácticas, automatizar flujos de trabajo y entregar evidencia útil y calibrada para ayudar al equipo a ganar partidos.

### 31. ¿Qué harías si detectas que la fuente de datos externa contiene errores en un partido clave?
> **Respuesta**: Activo las comprobaciones del pipeline de QA (regla de los 200 minutos por quinteto y cuadre exacto de puntos). Si detecto una discrepancia no reconciliable, aíslo el partido en la base de datos, documento la inconsistencia e informo al staff de que para ese encuentro concreto debemos apoyarnos exclusivamente en la codificación manual de vídeo hasta corregir la fuente.

### 32. ¿Cómo mantienes actualizados tus conocimientos en analítica deportiva?
> **Respuesta**: Sigo activamente conferencias especializadas (MIT Sloan Sports Analytics Conference), publicaciones académicas de modelado deportivo (Journal of Quantitative Analysis in Sports), comunidades de desarrollo en Python/R y el análisis táctico continuo de competiciones de élite (ACB, Euroliga, NBA y torneos FIBA).
