# Metodología Analítica y Estadística

## 1. Los Four Factors de Dean Oliver

En lugar de evaluar a los equipos por estadísticas acumuladas simples, el sistema descompone la eficiencia del juego en los cuatro factores fundamentales del baloncesto ajustados por posesión:

1. **Effective Field Goal % ($\text{eFG}\%$)**:
   $$\text{eFG}\% = \frac{\text{FGM} + 0.5 \times \text{3PM}}{\text{FGA}}$$
   *Pregunta*: ¿Con qué eficiencia convierte el equipo sus lanzamientos ponderando el valor del triple?
2. **Turnover Rate ($\text{TOV}\%$)**:
   $$\text{TOV}\% = \frac{\text{TOV}}{\text{FGA} + 0.44 \times \text{FTA} + \text{TOV}}$$
   *Pregunta*: ¿Cuántas posesiones pierde el equipo por pérdidas de balón antes de lograr un lanzamiento?
3. **Offensive Rebound % ($\text{ORB}\%$)**:
   $$\text{ORB}\% = \frac{\text{ORB}}{\text{ORB} + \text{Opp DRB}}$$
   *Pregunta*: ¿Qué porcentaje de los propios tiros errados es capaz de capturar en segunda oportunidad?
4. **Free Throw Rate ($\text{FTR}$)**:
   $$\text{FTR} = \frac{\text{FTA}}{\text{FGA}}$$
   *Pregunta*: ¿Con qué frecuencia el equipo genera viajes a la línea de tiros libres atacando el aro?

---

## 2. Ajuste de Ritmo y Net Rating

El cálculo de posesiones por 40 minutos permite neutralizar las diferencias de ritmo entre estilos de juego:
$$\text{Pace} = 40 \times \frac{\text{Posesiones}}{\text{Minutos}}$$
$$\text{Net Rating} = \text{Offensive Rating} - \text{Defensive Rating}$$

---

## 3. Econometría Longitudinal: Interrupted Time Series (ITS)

Para evaluar el impacto estructural del retraso de la línea de tres puntos de FIBA de 6.25m a 6.75m en octubre de 2010, se implementó una regresión segmentada de series temporales interrumpidas:
$$Y_t = \beta_0 + \beta_1 \cdot T_t + \beta_2 \cdot D_t + \beta_3 \cdot P_t + \epsilon_t$$
*Hallazgo*: Se detectó una caída inmediata en el acierto exterior seguida de una expansión sostenida en el volumen de triples por partido ($\text{3PAr}$ subió del $27.4\%$ al $38.6\%$).

---

## 4. Minería de Roles Funcionales (K-Means++ y PCA)

A partir de 3.767 campañas de jugador cualificadas ($\ge 40$ minutos jugados), se identificaron 6 arquetipos estadísticos mediante K-Means++ optimizado con K=6 y proyectado sobre 2 componentes principales (PCA):
1. **Iniciador Principal (Primary Initiator)**: Alto uso de balón, generación tras bote.
2. **Espaciador Móvil (Movement Spacer)**: Alta frecuencia de triples tras recepción y bloqueos indirectos.
3. **Eje Interior (Interior Hub)**: Postes con volumen de rebote y juego al poste alto/bajo.
4. **Director de Juego (Floor General)**: Control de tempo, ratio asistencia/pérdida élite.
5. **Ancla Defensiva (Defensive Anchor)**: Protección de aro, rebote defensivo y bloqueos directos.
6. **Alero Equilibrado (Balanced Wing)**: Producción multidimensional sin sobrecarga de balón.

*Límite*: La clusterización es una herramienta de agrupación descriptiva; no sustituye la evaluación del scouting visual.

---

## 5. Inferencia No Paramétrica y Bootstrap Agrupado ($B=5.000$)

Dada la estructura jerárquica de los torneos cortos (partidos agrupados dentro de un mismo campeonato), las aproximaciones normales clásicas infraestiman la varianza de tiro. El sistema aplica remuestreo bootstrap por conglomerados ($B=5.000$) para calcular intervalos de confianza empíricos al $95\%$ en márgenes de puntos e índices Four Factors.
