# 05 — Debilidades, Límites y Honestidad Metodológica (Weaknesses & Limits)
## Autocrítica Rigurosa y Madurez Profesional

---

### 1. ¿Cuáles son las mayores limitaciones o debilidades de este proyecto?
> **Respuesta**: Las reconozco con total transparencia:
> 1. **Muestras Pequeñas en Torneos de Selecciones**: Con 6 a 9 partidos por campeonato, la varianza natural en el porcentaje de tiro de tres puntos es muy alta.
> 2. **Ausencia de Tracking Óptico 25Hz en Datos Históricos**: El proyecto se apoya en actas oficiales y codificación de vídeo, no en coordenadas continuas XYZ de cámaras en pista.
> 3. **Rotación de Plantillas (*Roster Turnover*)**: Las selecciones cambian de convocatoria cada verano, a diferencia de los clubes que mantienen plantillas más estables durante 9 meses.

---

### 2. ¿Qué mejorarías en este sistema si dispusieras de más datos?
> **Respuesta**: 
> 1. Con datos de **tracking espacial (Second Spectrum)**, calcularía la métrica de *Shot Quality* (probabilidad esperada de enceste en función de la distancia al defensor más cercano y la velocidad de desplazamiento) para aislar la calidad de generación de la varianza de acierto.
> 2. Con datos de **carga física (Catapult GPS)**, cruzaría la fatiga acumulada con la caída en la eficiencia defensiva en los minutos finales de partido.
> 3. Con secuencias largas de liga regular (34+ jornadas), implementaría modelos de **Adjusted Plus/Minus Regularizado (RAPM)**.

---

### 3. ¿El sistema garantiza que siguiendo sus recomendaciones se ganan más partidos?
> **Respuesta**: Absolutamente no. Ningún sistema analítico honesto puede garantizar victorias en un deporte dinámico de alta varianza. El sistema garantiza que las decisiones del cuerpo técnico estarán respaldadas por **evidencia rigurosa, de calidad controlada y con cuantificación honesta de la incertidumbre**, mejorando la calidad del proceso de toma de decisiones.
