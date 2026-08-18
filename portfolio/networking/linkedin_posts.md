# ESTRATEGIA DE PUBLICACIONES EN LINKEDIN (LINKEDIN POSTS)
## International Basketball Analytics (2005–2024)

> **Regla de Publicación**: *Publicar con una cadencia sostenible (1 post cada 10–14 días). Cada post debe aportar un insight de baloncesto o de ingeniería real, acompañado de una imagen nítida o gráfico del proyecto. Cero contenido de autoayuda o sobreventa.*

---

### 📝 POST #1 — Presentación Oficial del Proyecto Insignia
**Visual adjunto**: Captura del diagrama de arquitectura de `docs/arquitectura.md` o captura del informe Quarto.

> ¿Cómo procesar 20 años de torneos internacionales de baloncesto para entregar información accionable a un cuerpo técnico?
>
> Durante los últimos meses he desarrollado **International Basketball Analytics (2005–2024)**, un sistema analítico integral construido sobre 18 torneos oficiales FIBA (EuroBasket, Copas del Mundo y Juegos Olímpicos — 1.145 partidos y más de 27.000 actuaciones individuales).
>
> 🔹 **Almacén Relacional OLAP**: 12 tablas en DuckDB y marts en Parquet con firmas SHA-256 inmutables y resolución de 2.124 jugadores únicos.  
> 🔹 **Validación Walk-Forward**: 17 particiones cronológicas con LightGBM (Brier Score = 0.1967 vs 0.2500 naive, ECE = 0.0314) para eliminar cualquier sesgo del futuro.  
> 🔹 **Analítica en R & Quarto**: Análisis longitudinales de eficiencia, intervalos de confianza bootstrap ($B=5.000$) y contrastes no paramétricos.  
> 🔹 **Soporte Real al Entrenador**: Briefs prepartido de 1.5 páginas con detección de contradicciones tácticas en pick-and-roll y workspace anti-hindsight.  
> 🔹 **Calidad de Software**: 227 tests automatizados en pytest con un 100% de tasa de éxito.
>
> El proyecto completo, el código y la documentación están disponibles en abierto:  
> 🔗 Repositorio GitHub: [github.com/miguel/basketball-analytics]
>
> Me encantaría conocer la opinión de entrenadores y analistas del sector. ¿Cómo estructuráis vosotros la información prepartido en semanas con varios encuentros?
>
> #BasketballAnalytics #SportsData #DataScience #DuckDB #RStats #Python #Scouting

---

### 📝 POST #2 — Arquitectura Dual: Por qué Python + R + DuckDB
**Visual adjunto**: Figura de comparación de métricas cruzadas Python ↔ R o código de conexión a DuckDB.

> En analítica deportiva a menudo se plantea el debate: "¿Python o R?". En este proyecto decidí que la respuesta correcta es: **ambos, con una separación estricta de responsabilidades sobre un almacén común en DuckDB**.
>
> ⚙️ **Python para la Ingeniería & ML**:
> - Pipelines de extracción y normalización determinista de actas.
> - Almacenamiento columnar en Apache Parquet.
> - Modelado predictivo con LightGBM y simulaciones Monte Carlo ($180\text{k}$ iteraciones).
> - Suite de 227 tests automatizados en pytest.
>
> 📊 **R para la Inferencia & Visualización**:
> - Conexión nativa a DuckDB vía `DBI` en modo solo lectura (0 duplicación de datos).
> - Análisis longitudinales de tiro (True Shooting % y Four Factors) con `tidyverse`.
> - Inferencia no paramétrica mediante bootstrap ($B=5.000$) y test de permutación.
> - Informes reproducibles de calidad editorial con Quarto y `ggplot2`.
>
> Al consultar el mismo almacén relacional, logramos exactamente 0 discrepancias numéricas en partidos, posesiones y tiros.
>
> Todo el código R y Python está disponible en el repositorio: [github.com/miguel/basketball-analytics]
>
> #DataEngineering #RStats #Python #DuckDB #SportsAnalytics

---

### 📝 POST #3 — Hallazgo Analítico: La Distorsión de la Muestra Pequeña en Torneos Cortos
**Visual adjunto**: Gráfico de evolución de True Shooting % con bandas de confianza bootstrap de `reports/figures_r/fig_02_player_longitudinal_ts.png`.

> En un torneo de selecciones de 6 a 9 partidos, una racha de tiro de 15 triples puede convertir a un lanzador del 33% en un tirador del 55% aparente... y viceversa.
>
> Al analizar 3.767 campañas individuales cualificadas entre 2005 y 2024, comprobamos que el porcentaje de triple ($3\text{P}\%$) presenta una correlación año a año significativamente más baja que el True Shooting ($TS\%$) o la tasa de tiros libres ($FTR$).
>
> 📉 **¿Qué implica esto para el scouting prepartido?**  
> Si un cuerpo técnico prepara el plan de partido basándose exclusivamente en el $3\text{P}\%$ de los últimos 3 encuentros, corre el riesgo de ajustar su defensa sobre varianza pura.
>
> En el sistema implementamos **contracción bayesiana ($\lambda = 0.75$)** para estabilizar los perfiles de tiro hacia la media histórica del jugador, evitando que una racha corta distorsione la asignación defensiva.
>
> Más detalles en el informe Quarto del proyecto: [github.com/miguel/basketball-analytics]
>
> #BasketballScouting #ShootingVariance #Analytics #Coaching

---

### 📝 POST #4 — Validación Walk-Forward: El Peligro del Data Leakage en Deportes
**Visual adjunto**: Reliability diagram de calibración de probabilidades (`reports/figures/mvp6/fig_02_calibration_curves.png`).

> Uno de los errores más comunes al modelar resultados deportivos es utilizar cross-validation aleatorio (k-fold estándar). Si mezclas partidos de 2022 para entrenar un modelo que predice un partido de 2012, el modelo "conoce" la evolución táctica del futuro.
>
> En este proyecto aplicamos un esquema estricto de **Walk-Forward en 17 particiones cronológicas**:
> 1. Entrenar únicamente con torneos disputados hasta $T-1$.
> 2. Evaluar out-of-sample exclusivamente sobre el torneo $T$.
> 3. Expandir la ventana temporal y repetir para los 18 torneos (1.105 partidos evaluados).
>
> 🎯 **Resultados Calibrados (LightGBM)**:
> - Brier Score = `0.1967` (frente al `0.2500` de un baseline naive, una mejora del $+21.3\%$).
> - Expected Calibration Error ($ECE$) = `0.0314` (las probabilidades predichas se corresponden con las frecuencias reales observadas).
>
> Menos sobreajuste y más honestidad estadística.
>
> Repositorio completo: [github.com/miguel/basketball-analytics]
>
> #MachineLearning #ModelValidation #DataLeakage #SportsAnalytics

---

### 📝 POST #5 — Del Número a la Pizarra: El Brief Prepartido de 1.5 Páginas
**Visual adjunto**: Captura de un Brief Prepartido real de `reports/mvp10/` (por ejemplo, España vs EE.UU. 2008 o España vs Lituania 2022).

> El valor de los datos en un club no se mide por la complejidad del código, sino por su capacidad para **ahorrar tiempo al entrenador y hacerle las preguntas correctas**.
>
> Si un analista entrega un Excel de 40 pestañas a un cuerpo técnico dos días antes de un partido, el informe acaba en la papelera.
>
> Por eso diseñamos un generador de **Briefs Prepartido de 1.5 páginas**:
> 1. **Resumen de Ritmo y Four Factors**: Diferencial de rebote ofensivo, pérdidas y eficiencia de tiro efectivo (eFG%).
> 2. **Alertas de Contradicción Táctica**: Si el rival ejecuta defensa en *Drop* en pick-and-roll pero nosotros contamos con un generador con $>40\%$ en tiros tras bote, el sistema marca una ventaja inmediata.
> 3. **3 Preguntas Clave para el Vídeo**: Enfocadas en emparejamientos y asignaciones defensivas.
>
> Menos ruido, más claridad antes del salto inicial.
>
> ¿Cómo estructuráis en vuestros equipos la entrega de información previa a los partidos?
>
> #Coaching #BasketballScouting #GamePlan #DecisionSupport
