# GUÍA MAESTRA DE PREPARACIÓN PARA ENTREVISTAS (INTERVIEW FINAL)
## International Basketball Analytics (2005–2024)

> **Propósito**: Guía exhaustiva de respuestas honestas, técnicas y tácticas para defender el proyecto y la candidatura en entrevistas de trabajo ante cualquier perfil evaluador (Entrenador, Director Deportivo, Lead Data Scientist o Hiring Manager).

---

## 1. Respuestas por Duración de Pitch

### ⏱️ 30 Second Answer (Elevator Pitch)
> "He construido una infraestructura analítica dual en Python, R y DuckDB sobre 20 años de torneos internacionales FIBA (1.145 partidos y 27.353 actuaciones individuales). El sistema procesa actas oficiales y vídeo táctico para entregar briefs prepartido ejecutivos de 1.5 páginas con preguntas accionables para entrenadores, validados mediante 227 tests automatizados y esquemas out-of-sample sin sesgo retrospectivo."

### ⏱️ 60 Second Answer (Problem & Solution)
> "En el baloncesto de alta competición y torneos cortos, los cuerpos técnicos sufren sobrecarga de datos y distorsión por la varianza de tiro en muestras pequeñas. Para resolverlo, desarrollé un sistema que une ingeniería de datos relacional (DuckDB / Parquet), minería de roles funcionales (6 arquetipos con PCA/K-Means), Machine Learning supervisado calibrado (LightGBM con Brier Score de 0.1967) y análisis estadístico en R. En lugar de ofrecer predicciones mágicas, el sistema detecta contradicciones tácticas —como la vulnerabilidad del drop coverage en pick-and-roll frente a tiradores de élite— y entrega preguntas concretas para la sesión de vídeo antes de cada encuentro."

### ⏱️ 3 Minute Answer (Technical Architecture)
> "El proyecto se estructura en un pipeline determinista de cuatro capas:
> 1. **Ingesta y DuckDB**: Un almacén relacional OLAP de 12 tablas donde resolvemos más de 2.100 identidades de jugador con control de calidad (cuadre estricto de 200 min/partido) y hashes SHA-256.
> 2. **Capa Dual Python + R**: Python ejecuta el modelado predictivo y las simulaciones, mientras que R se conecta nativamente a DuckDB para análisis longitudinales, inferencia no paramétrica bootstrap ($B=5.000$) e informes en Quarto.
> 3. **Modelado y Simulación**: Evaluamos 1.105 partidos out-of-sample mediante 17 folds walk-forward cronológicos, logrando un Expected Calibration Error de 0.0314, y ejecutamos 180.000 simulaciones Monte Carlo con contracción bayesiana ($\lambda = 0.75$).
> 4. **Aislamiento Anti-Hindsight**: Una barrera temporal estricta garantiza que toda métrica prepartido solo consuma información disponible antes del salto inicial, reservando el marcador final para la auditoría de proceso posterior."

### ⏱️ 5 Minute Walkthrough (Primary Demo en Vivo)
1. **[0:00 - 1:00] Contexto & Arquitectura**: Mostrar `docs/arquitectura.md`, explicando la separación de responsabilidades entre Python, R y DuckDB.
2. **[1:00 - 2:00] Datos & Calidad**: Mostrar `data/03_validated/basketball_analytics.duckdb` y los 227 tests automatizados pasando en pytest.
3. **[2:00 - 3:00] Capa Estadística en R**: Mostrar el informe Quarto (`exploratory_analysis.html`) y las curvas longitudinales de TS% y Four Factors.
4. **[3:00 - 4:00] Brief Prepartido & Táctica**: Abrir un brief prepartido real (Pekín 2008 / EuroBasket 2022) y mostrar la alerta de P&R Drop.
5. **[4:00 - 5:00] Replay Anti-Hindsight & Código**: Ejecutar `python scripts/run_project.py` en directo y mostrar el flujo de ejecución unificada.

---

## 2. Adaptación por Perfil de Entrevistador

### 🏀 Versión para Entrenador / Director Deportivo
> *"Mi trabajo no es decirle cómo jugar ni discutir sus decisiones tácticas; mi objetivo es ahorrarle tiempo a usted y a sus ayudantes. Proceso los datos brutos del rival y se los entrego resumidos en una página y media con los Four Factors, las tendencias de sus generadores de pick-and-roll y las 3 preguntas clave que deberían responder en la sesión de vídeo."*

### 💻 Versión para Lead Data Scientist / Analytics Engineer
> *"He diseñado el sistema priorizando la reproducibilidad, la integridad criptográfica y la ausencia de data leakage. Utilizamos DuckDB y Parquet como capa OLAP común, validación walk-forward temporal en 17 particiones consecutivas, calibración de probabilidad con Brier Score y ECE, y una suite de 227 tests unitarios y de integración con CI/CD determinista."*

---

## 3. Limitaciones Honestamente Reconocidas

| Pregunta Trampa | Respuesta Honesta y Defendible |
|---|---|
| **¿Qué datos te faltan en este proyecto?** | *"El proyecto utiliza boxscores oficiales y anotación manual de vídeo. No dispone de datos de tracking óptico a 25Hz (coordenadas $X,Y$) ni telemetría física (cargas de salto o acelerometría)."* |
| **¿Qué harías con tracking real en un club?** | *"Calcularía métricas espaciales reales: calidad de tiro basada en la distancia del defensor más cercano, velocidad de recuperación en rotaciones defensivas y separación creada en bloqueos directos."* |
| **¿Qué necesitarías aprender al entrar al club?** | *"Adaptarme a los softwares propietarios internos (Synergy, Hudl Sportscode, NBN23) y, sobre todo, aprender los códigos de comunicación y preferencias del entrenador principal."* |

---

## 4. Las 20 Preguntas Clave que Debes Responder en Entrevista

### 1. ¿Qué has construido?
Un sistema analítico integral y reproducible de soporte a decisiones para baloncesto internacional (2005–2024), con infraestructura DuckDB, modelado supervisado en Python, inferencia en R y briefs tácticos para entrenadores.

### 2. ¿Por qué elegiste baloncesto internacional de selecciones?
Porque los torneos cortos (6–9 partidos) representan el escenario más exigente para un analista: la varianza de tiro distorsiona la muestra pequeña y obliga a modelar con rigor estadístico y contexto de juego.

### 3. ¿Por qué Python para la ingeniería y el Machine Learning?
Python ofrece el ecosistema más robusto para pipelines de datos (DuckDB, Pandas, PyArrow), algoritmos de gradient boosting (LightGBM) y desarrollo de aplicaciones web interactivas (Streamlit).

### 4. ¿Por qué R para la capa exploratoria y de validación?
R y su ecosistema `tidyverse` / `ggplot2` / `Quarto` son la herramienta estándar de oro para análisis exploratorio, distribuciones empíricas, inferencia no paramétrica y generación de informes reproducibles con calidad editorial.

### 5. ¿Por qué DuckDB en lugar de SQLite o PostgreSQL?
DuckDB es un motor OLAP columnar embebido de altísimo rendimiento optimizado para consultas analíticas agregadas (sumas, promedios, particiones de ventana) sobre millones de registros sin requerir un servidor dedicado.

### 6. ¿Por qué Apache Parquet para los marts analíticos?
Parquet almacena los datos de forma columnar y comprimida (Snappy/Zstd), permitiendo lecturas vectorizadas ultrarrápidas y acceso concurrente transparente tanto desde Python como desde R.

### 7. ¿Por qué validación walk-forward en lugar de k-fold cross-validation estándar?
En series temporales y competiciones deportivas, el k-fold aleatorio mezcla partidos del futuro con el pasado, provocando fuga de datos (*data leakage*). Walk-forward simula la realidad: entrenar estrictamente en el pasado y evaluar en el siguiente torneo.

### 8. ¿Qué es data leakage y cómo lo evitaste?
Es la contaminación del modelo con información que no estaría disponible en el momento de la predicción. Lo evité filtrando todas las variables prepartido con `game_date < target_game_date`.

### 9. ¿Qué significa el Brier Score ($0.1967$)?
Es la media cuadrática del error de las probabilidades asignadas. Un modelo que asigna 50% a todo obtiene $0.2500$; nuestro $0.1967$ demuestra una reducción real del error del $+21.3\%$.

### 10. ¿Qué significa el Expected Calibration Error ($ECE = 0.0314$)?
Indica que cuando el modelo asigna un $70\%$ de probabilidad de victoria a un equipo, ese equipo realmente gana el $70\%$ de las veces (desviación media menor al $3.1\%$).

### 11. ¿Por qué LightGBM como algoritmo supervisado principal?
Por su capacidad nativa para capturar interacciones no lineales entre los Four Factors y el ritmo, su velocidad de entrenamiento y su resistencia al sobreajuste con regularización L2.

### 12. ¿Qué es el motor Monte Carlo y por qué utilizas contracción bayesiana?
Simula $10.000$ veces el cuadro del torneo jugando partido a partido. La contracción bayesiana ($\lambda = 0.75$) reduce las probabilidades extremas para evitar que una racha corta en fase de grupos sobreestime a un equipo.

### 13. ¿Qué significa el coeficiente Cohen's Kappa $\kappa = 0.80$?
Mide la fiabilidad del etiquetado de vídeo entre anotadores eliminando el azar. $\kappa = 1.00$ en tipo de cobertura y $\kappa = 0.80$ en resultado de tiro certifican una codificación sólida.

### 14. ¿Cómo validaste los 6 arquetipos funcionales?
Combinamos reducción de dimensionalidad (PCA con $>60\%$ de varianza explicada) y agrupamiento K-Means++, validando la interpretabilidad de baloncesto de los 6 perfiles resultantes sobre 3.767 campañas.

### 15. ¿Qué harías si tuvieras datos de tracking óptico a 25Hz?
Calcularía la calidad de tiro esperada ($q\text{SQ}$), la velocidad de cierre en rotaciones defensivas (*closeouts*) y la distancia de separación del defensor en situaciones de pick-and-roll.

### 16. ¿Qué harías si un entrenador no confía en un número o gráfico?
No discutiría con el número; le pediría ver juntos los clips de vídeo correspondientes. El dato no impone decisiones, solo señala dónde mirar el vídeo.

### 17. ¿Cuál es la principal limitación del proyecto?
La ausencia de datos espaciales ($X,Y$) a nivel de posesión en todo el histórico, lo que obliga a estimar el impacto táctico mediante boxscores y muestras codificadas de vídeo.

### 18. ¿Qué cambiarías si tuvieras los datos de un club profesional?
Integraría datos de entrenamientos diarios, cargas físicas del preparador (GPS/RPE) y el scouting específico de jugadas dibujadas (*after-timeout plays*).

### 19. ¿Qué aportarías durante tus primeros 30 días?
Automatización de la recopilación de datos de rivales, plantillas visuales de tiro y ritmo en una sola página, y entrega puntual de briefs prepartido a $T-48\text{h}$.

### 20. ¿Por qué deberíamos contratarte a ti como analista junior?
Porque combino el rigor de un ingeniero de datos (código limpio, DuckDB, 227 tests), la disciplina estadística (Python/R, calibración) y la capacidad de traducir números en lenguaje de baloncesto para el cuerpo técnico.
