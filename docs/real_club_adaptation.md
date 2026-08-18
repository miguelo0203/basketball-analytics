# Adaptación del Sistema a un Entorno de Club Profesional
## Hoja de Ruta Operativa: De Datos Históricos FIBA a Datos en Vivo de Competición

> [!IMPORTANT]
> Este documento reconoce con total transparencia que el proyecto actual se ha desarrollado sobre un corpus histórico de selecciones nacionales (2005–2024). A continuación se detalla cómo evolucionaría esta infraestructura analítica al integrarse en el día a día de un club profesional (ACB, Euroliga, LEB Oro o NBA G-League).

---

## 1. Integración de Nuevas Fuentes de Datos de Club

```
+----------------------------------------------------------------------------------------------------+
| FUENTE DE DATOS PROFESIONAL      | PROVEEDOR / ORIGEN               | CASO DE USO OPERATIVO        |
+----------------------------------------------------------------------------------------------------+
| **Tracking Óptico 25Hz (XYZ)**   | Second Spectrum / SportVU        | Calidad de tiro y closeouts. |
| **Play-by-Play Etiquetado**      | Synergy Sports / InStat          | Rendimiento por tipo de P&R. |
| **Coordenadas de Tiro (Shot-XY)**| Proveedores oficiales de liga    | Shot charts y zonas de valor.|
| **Lineup Stints (On/Off 5v5)**   | Datos de acta digital de liga    | Adjusted Plus/Minus (RAPM).  |
| **Carga Física y Biometría**     | Catapult GPS / Firstbeat         | Gestión de minutos y fatiga. |
| **Contratos y Mercado Salarial** | Base de datos interna de club    | Scouting de fichajes y CAP.  |
| **Vídeo Indexado en Directo**    | Nacsport / Hudl Sportscode       | Clips vinculados a posesión. |
| **Informes Médicos / Lesiones**  | Departamento médico interno      | Disponibilidad prepartido.   |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. Lo Que Ya Sé Hacer (Competencias Demostradas en este Portfolio)

1. **Modelado Relacional e Ingeniería de Almacenes**:
   - Diseño de esquemas normalizados en DuckDB y Parquet capaces de procesar millones de eventos con consultas subsegundo.
2. **Control de Calidad Determinista (QA)**:
   - Verificación matemática de cuadre de tiempos (200 minutos), identidades de jugadores y suma exacta de puntuaciones.
3. **Analítica Cuantitativa y Four Factors**:
   - Normalización de métricas por posesión y cálculo riguroso de Offensive/Defensive/Net Rating.
4. **Validación Temporal sin Fuga de Datos**:
   - Construcción de pipelines walk-forward que impiden cualquier contaminación con información del futuro.
5. **Calibración Probabilística e Incertidumbre**:
   - Evaluación mediante Brier Score, reliability diagrams, Expected Calibration Error (ECE) e inferencia bootstrap.
6. **Integración Cuantitativa-Cualitativa y Briefs**:
   - Detección de contradicciones entre números y vídeo, traduciéndolas a informes prepartido concisos de 1.5 páginas para entrenadores.
7. **Calidad de Software y Testing**:
   - Automatización de suites de pruebas con pytest (201 tests, 100% de éxito).

---

## 3. Lo Que Tendría que Aprender y Adaptar (Madurez y Humildad Profesional)

1. **Procesamiento de Tracking Óptico Continuo (Spatiotemporal Data)**:
   - *Adaptación*: Aprender a manejar flujos de coordenadas 2D/3D a 25Hz para calcular métricas espaciales como el *Shot Quality* (probabilidad esperada de enceste según la distancia del defensor más cercano) y la velocidad de desplazamiento defensivo.
2. **Ritmo de Calendario Profesional (2–3 Partidos por Semana)**:
   - *Adaptación*: En selecciones los torneos duran 15 días cada verano; en un club de Euroliga/ACB se juegan 60–80 partidos al año. Es imprescindible automatizar la ingesta post-partido nocturna para que el cuerpo técnico tenga el brief a primera hora de la mañana.
3. **Modelos de Regularized Adjusted Plus-Minus (RAPM)**:
   - *Adaptación*: Implementar regresiones Ridge con regularización bayesiana sobre secuencias de quintetos (*stints*) con muestras largas de temporada regular (34+ jornadas).
4. **Coordinación con el Departamento Médico y de Preparación Física**:
   - *Adaptación*: Aprender a cruzar los datos de rendimiento táctico con las métricas de carga física y fatiga neuromuscular (Catapult/Firstbeat) para sugerir alertas de descanso en rotaciones.
5. **Integración con Software Especializado de Vídeo (Hudl / Nacsport)**:
   - *Adaptación*: Conectar las consultas SQL de eventos con los archivos XML/JSON de corte de vídeo para que los entrenadores puedan saltar directamente al clip correspondiente con un clic.

---

## 4. Conclusión

Este portfolio demuestra que **la base matemática, analítica, de ingeniería de software y de entendimiento del juego de baloncesto está plenamente consolidada**. La transición a un entorno de club consistirá en conectar estos mismos principios metodológicos a fuentes de datos más granulares y al ritmo operativo diario del equipo.
