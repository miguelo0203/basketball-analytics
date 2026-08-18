# 04 — Defensa Metodológica (Methodology Defense)
## Alcance Histórico, Validación en Vídeo y Simulación

---

### 1. ¿Por qué elegiste baloncesto internacional de selecciones y no una liga de clubes como ACB o Euroliga?
> **Respuesta**: Las competiciones internacionales de selecciones nacionales absolutas (EuroBasket, Mundiales FIBA y Juegos Olímpicos) ofrecen un entorno histórico público completo, transparente y auditable a lo largo de dos décadas. Esto permite verificar públicamente cada partido y cada registro sin depender de datos propietarios cerrados, demostrando la capacidad metodológica de forma reproducible.

---

### 2. ¿Por qué el alcance es estrictamente 2005 a 2024?
> **Respuesta**: 2005 marca el inicio de la era moderna de digitalización de actas oficiales FIBA con boxscores completos y detallados. 2024 cierra el ciclo histórico con los Juegos Olímpicos de París 2024. Mantener este límite garantiza que no se incluyen torneos incompletos ni datos provisionales.

---

### 3. ¿Cómo validaste científicamente la capa cualitativa de vídeo?
> **Respuesta**: Para evitar que la observación en vídeo dependiera del criterio subjetivo de una sola persona, establecí un protocolo de **doble codificación independiente con dos analistas ciegos entre sí** sobre 420 posesiones estructuradas en 36 partidos clave. Medimos la concordancia mediante el coeficiente de **Cohen's Kappa**, obteniendo $\kappa = 1.00$ en el tipo de acción táctica y $\kappa = 0.80$ en la calificación defensiva de coberturas de bloqueo directo.

---

### 4. ¿Por qué aplicaste Shrinkage Bayesiano ($\lambda = 0.75$) en las simulaciones Monte Carlo?
> **Respuesta**: En competiciones de eliminatoria directa a partido único, los modelos estadísticos puros tienden a sobrestimar la probabilidad de victoria de los grandes favoritos (asignando probabilidades irreales del 95%). El shrinkage bayesiano contrae suavemente las probabilidades hacia un prior conservador ($\lambda = 0.75$), reflejando el hecho deportivo real de que cualquier equipo de élite puede perder en un día de bajo acierto exterior.
