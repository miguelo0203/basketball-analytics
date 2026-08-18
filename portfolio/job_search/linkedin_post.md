# Publicación de Lanzamiento para LinkedIn (Project Post)
## Anuncio Profesional del Proyecto Finalizado

---

### Texto Listo para Publicar

🏀 **International Basketball Analytics (2005–2024)**  
*De los datos a la evidencia para apoyar decisiones de baloncesto.*

¿Cómo puede un analista de datos ayudar realmente a un cuerpo técnico de baloncesto a preparar un partido o evaluar una plantilla?

Para responder a esta pregunta con hechos y no con teoría, he dedicado los últimos meses a construir un sistema analítico integral sobre **20 años de torneos internacionales oficiales** (18 campeonatos FIBA y JJ.OO. entre 2005 y 2024, con 1.145 partidos y más de 27.000 actuaciones individuales de jugador).

Mi objetivo no era construir un modelo que pretenda "adivinar" resultados ni vender una caja negra mágica. Quería demostrar cómo cubrir toda la cadena de valor de un analista:

1. **Ingeniería y Calidad de Datos**: Almacén relacional en **DuckDB y Parquet** con verificación SHA-256 y unificación de 2.124 jugadores canónicos, con pipelines de QA que validan matemáticamente el 100% de los partidos.
2. **Analítica de Baloncesto y Pizarra**: Descomposición de posesiones mediante los **Four Factors de Dean Oliver**, minería de **6 arquetipos funcionales de jugador** (K-Means++/PCA sobre 3.767 campañas) y validación en vídeo de coberturas de pick-and-roll con fiabilidad inter-evaluador ($\text{Cohen's Kappa } \kappa = 0.80$).
3. **Machine Learning y Calibración**: Validación temporal walk-forward en 17 folds expansivos sin fuga de datos (*zero data leakage*), logrando con **LightGBM** un Brier Score de `0.1967`, un error de calibración medio de solo `3.14%` (ECE = 0.0314) y 180.000 simulaciones Monte Carlo.
4. **Soporte a Decisiones**: Generación de **briefs prepartido de 1.5 páginas** diseñados para leerse en 2.5 minutos antes del entrenamiento, traduciendo debilidades numéricas a preguntas concretas para la pizarra (ej. castigar drops defensivos profundos con pick-and-pop).

💡 **Lo que he aprendido**: En el baloncesto de alta competición, el valor del analista no reside en abrumar al entrenador con números, sino en **filtrar el ruido, cuantificar la incertidumbre y formular las preguntas correctas**.

🏀 **El siguiente paso**: En un entorno de club profesional (ACB, Euroliga o LEB), esta misma metodología se conecta de forma natural a datos de tracking 25Hz (Second Spectrum), play-by-play detallado (Synergy), datos biométricos (Catapult GPS) y al ritmo operativo diario del equipo.

Todo el código, la base de datos DuckDB, la documentación completa en español y los 209 tests automatizados (100% pass rate) son públicos y reproducibles:

👉 **Repositorio en GitHub**: [https://github.com/[usuario]/Espana2005-2025](https://github.com/[usuario]/Espana2005-2025)

Quedo a vuestra total disposición para conversar con entrenadores, analistas y directores deportivos interesados en analítica aplicada al juego.

---

#BasketballAnalytics #SportsAnalytics #DataEngineering #Python #DuckDB #MachineLearning #Baloncesto #Scouting #SportsData
