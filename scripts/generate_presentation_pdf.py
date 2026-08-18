"""
Script to generate high-resolution, publication-grade 30-slide PDF presentation
for 'International Basketball Analytics (2005-2024)'.
Uses ReportLab with 16:9 widescreen dimensions (960 x 540 pt).
"""
import os
import sys
from reportlab.lib.pagesizes import landscape
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

# Define 16:9 dimensions in points (width=960 pt, height=540 pt)
PAGE_WIDTH = 960.0
PAGE_HEIGHT = 540.0
PAGE_SIZE = (PAGE_WIDTH, PAGE_HEIGHT)

class NumberedCanvas(canvas.Canvas):
    """Canvas that performs two-pass numbering and adds header/footer banners."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        # Skip decorative header/footer on title slide (slide 1)
        if self._pageNumber == 1:
            # Title slide background accent
            self.saveState()
            self.setFillColor(colors.HexColor("#0f172a")) # Dark navy
            self.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
            self.setFillColor(colors.HexColor("#1e3a8a")) # Deep blue accent
            self.rect(0, 0, PAGE_WIDTH, 14, fill=1, stroke=0)
            self.rect(0, PAGE_HEIGHT - 14, PAGE_WIDTH, 14, fill=1, stroke=0)
            self.restoreState()
            return

        self.saveState()
        # Top banner
        self.setFillColor(colors.HexColor("#1e293b"))
        self.rect(0, PAGE_HEIGHT - 38, PAGE_WIDTH, 38, fill=1, stroke=0)
        self.setFillColor(colors.HexColor("#2563eb"))
        self.rect(0, PAGE_HEIGHT - 40, PAGE_WIDTH, 2, fill=1, stroke=0)

        # Header Title
        self.setFillColor(colors.HexColor("#ffffff"))
        self.setFont("Helvetica-Bold", 11)
        self.drawString(40, PAGE_HEIGHT - 24, "INTERNATIONAL BASKETBALL ANALYTICS (2005–2024)")

        self.setFont("Helvetica", 10)
        self.setFillColor(colors.HexColor("#94a3b8"))
        self.drawRightString(PAGE_WIDTH - 40, PAGE_HEIGHT - 24, "Decision Support & Sports Engineering Portfolio")

        # Bottom banner
        self.setFillColor(colors.HexColor("#f8fafc"))
        self.rect(0, 0, PAGE_WIDTH, 28, fill=1, stroke=0)
        self.setFillColor(colors.HexColor("#e2e8f0"))
        self.line(0, 28, PAGE_WIDTH, 28)

        # Footer Left: Author / Stack
        self.setFillColor(colors.HexColor("#64748b"))
        self.setFont("Helvetica", 9)
        self.drawString(40, 10, "Miguel — Basketball Data Analyst | Python • R • DuckDB • Parquet • Quarto • LightGBM")

        # Footer Right: Slide Page Number
        page_text = f"Slide {self._pageNumber} of {page_count}"
        self.drawRightString(PAGE_WIDTH - 40, 10, page_text)
        self.restoreState()


def create_presentation_pdf(output_path: str):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=PAGE_SIZE,
        leftMargin=40,
        rightMargin=40,
        topMargin=50,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_main = ParagraphStyle(
        'TitleMain',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=28,
        leading=34,
        textColor=colors.HexColor('#ffffff'),
        alignment=0
    )

    title_sub = ParagraphStyle(
        'TitleSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=15,
        leading=20,
        textColor=colors.HexColor('#93c5fd'),
        alignment=0
    )

    slide_title = ParagraphStyle(
        'SlideTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=4
    )

    slide_subtitle = ParagraphStyle(
        'SlideSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#475569'),
        spaceAfter=12
    )

    body_text = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#1e293b')
    )

    bullet_text = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#1e293b')
    )

    card_header = ParagraphStyle(
        'CardHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#1e3a8a')
    )

    card_body = ParagraphStyle(
        'CardBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#334155')
    )

    callout_text = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#0f172a')
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=12,
        textColor=colors.HexColor('#1e293b')
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=colors.HexColor('#ffffff')
    )

    story = []

    # Slide 1: Cover
    story.append(Spacer(1, 100))
    story.append(Paragraph("INTERNATIONAL BASKETBALL ANALYTICS (2005–2024)", title_main))
    story.append(Spacer(1, 10))
    story.append(Paragraph("De los Datos a la Evidencia para Apoyar Decisiones en Baloncesto de Élite", title_sub))
    story.append(Spacer(1, 40))

    meta_text = (
        "<font color='#cbd5e1' size=11>"
        "<b>Autor</b>: Miguel — Basketball Data Analyst<br/>"
        "<b>Stack Técnico</b>: Python • R • DuckDB • Apache Parquet • Quarto • LightGBM • Pytest (227 tests passing)<br/>"
        "<b>Alcance Histórico</b>: 18 Torneos Oficiales FIBA (EuroBasket, Mundiales, JJ.OO.) | 1.145 Partidos | 27.353 Actuaciones"
        "</font>"
    )
    story.append(Paragraph(meta_text, body_text))
    story.append(PageBreak())

    # Slides content definition (30 slides total)
    slides_data = [
        # Slide 2
        (
            "La Idea en 30 Segundos",
            "¿Cuál es la propuesta de valor fundamental del analista?",
            [
                ("Flujo Riguroso", "Conectamos datos brutos de partido con la pizarra táctica mediante un pipeline desacoplado: Datos ➔ Análisis ➔ Validación ➔ Contexto ➔ Decisión."),
                ("Filtrado de Ruido", "En el baloncesto profesional el problema no es la falta de datos, sino la saturación de ruido: varianza de tiro en torneos cortos y sesgo de resultado."),
                ("Apoyo al Entrenador", "No sustituimos al entrenador ni predecimos marcadores mágicos; transformamos datos heterogéneos en briefs prepartido ejecutivos de 1.5 páginas.")
            ],
            "<b>Propuesta Central</b>: Cuantificar la incertidumbre y dar al cuerpo técnico ventajas tácticas comprobables antes de entrar al vestuario."
        ),
        # Slide 3
        (
            "Qué Problema Resuelve un Analista",
            "¿Por qué los cuerpos técnicos necesitan analítica de rendimiento?",
            [
                ("Sesgo Retrospectivo", "Evaluar decisiones solo por si el tiro entró o no distorsiona el plan. La analítica evalúa la calidad del proceso y la generación del tiro."),
                ("Sobrerreacción a Rachas", "En muestras de 6–9 partidos, lanzadores del 33% parecen del 55%. La contracción bayesiana (λ=0.75) estabiliza la verdadera capacidad."),
                ("Ahorro de Tiempo", "Sintetizar 20 partidos de scout rival en 3 preguntas clave y 2 mapas de tiro listos para la sesión de vídeo semanal.")
            ],
            "<b>Impacto Operativo</b>: Menos tiempo procesando tablas dispersas, más tiempo preparando el plan de partido en pista."
        ),
        # Slide 4
        (
            "Qué Construí: Arquitectura en 9 Capas",
            "¿Cómo está estructurado el sistema desacoplado end-to-end?",
            [
                ("Ingeniería & OLAP", "Ingesta determinista de 18 torneos ➔ Almacén DuckDB de 12 tablas (28.5 MB) ➔ 11 Marts analíticos en Apache Parquet."),
                ("Estadística & ML", "Análisis longitudinal con R/tidyverse ➔ 6 Arquetipos (K-Means/PCA) ➔ LightGBM en 17 folds walk-forward (1.105 partidos test)."),
                ("Decisión & QA", "Simulación Monte Carlo (180k iteraciones) ➔ Briefs prepartido con detección de contradicciones P&R ➔ 227 tests en pytest.")
            ],
            "<b>Principio de Arquitectura</b>: Separación estricta entre almacenamiento (DuckDB/Parquet), modelado (Python/R) y entrega al usuario."
        ),
        # Slide 5
        (
            "Escala y Cifras Clave del Proyecto",
            "¿Qué volumen real y cobertura histórica tiene el sistema?",
            [
                ("Competiciones Oficiales", "18 Torneos FIBA (EuroBasket 2005–2022, Mundiales 2006–2023, JJ.OO. Pekín 2008–París 2024)."),
                ("Partidos y Jugadores", "1.145 partidos oficiales, 2.290 observaciones de equipo, 2.124 jugadores canónicos y 27.353 actuaciones registradas."),
                ("Rigor de Evaluación", "1.105 partidos evaluados out-of-sample sin data leakage, Brier Score 0.1967 (vs 0.2500 naive) y ECE 0.0314.")
            ],
            "<b>Verificación 100% Determinista</b>: Todas las cifras están respaldadas por hashes SHA-256 inmutables y 227 tests automáticos."
        ),
        # Slide 6
        (
            "Calidad de Datos y QA Determinista",
            "¿Cómo se garantiza que los datos son fiables y consistentes?",
            [
                ("Desduplicación de Entidades", "Resolución determinista de 2.124 jugadores a través de 20 años de torneos internacionales sin APIs de pago."),
                ("Validaciones Relacionales", "Comprobación automática de 200 minutos por encuentro reglamentario (más prórrogas) y cuadre estricto de actas."),
                ("Inmutabilidad Criptográfica", "Manifiesto de reproducibilidad con firmas SHA-256 para cada tabla DuckDB y archivo Parquet.")
            ],
            "<b>Regla de Oro</b>: Un modelo sofisticado construido sobre datos corruptos sigue siendo un modelo inservible."
        ),
        # Slide 7
        (
            "Más Allá de los Puntos por Partido (PPG)",
            "¿Por qué el volumen anotador tradicional es insuficiente?",
            [
                ("Distorsión del Ritmo", "Un equipo que anota 85 puntos a 80 posesiones es menos eficiente que uno que anota 78 puntos a 68 posesiones."),
                ("True Shooting Percentage", "Ponderamos el valor real del tiro de 3 puntos y los tiros libres: TS% = Puntos / (2 * (FGA + 0.44 * FTA))."),
                ("Normalización por 40 Minutos", "Permite comparar la productividad real de titulares y jugadores de rol sin distorsión de rotación.")
            ],
            "<b>Enfoque</b>: Evaluar eficiencia por posesión antes de juzgar el volumen absoluto de anotación."
        ),
        # Slide 8
        (
            "Four Factors y Contexto de Juego",
            "¿Cómo traducimos los números a preguntas tácticas?",
            [
                ("Effective Field Goal (eFG%)", "¿Cómo es la calidad de los tiros que generamos frente a los tiros que concedemos?"),
                ("Turnover Percentage (TOV%)", "¿Cuidamos el balón o regalamos puntos fáciles en transición defensiva?"),
                ("Offensive Rebounding (ORB%)", "¿Castigamos en segundas oportunidades o priorizamos el balance defensivo hacia atrás?"),
            ],
            "<b>Free Throw Rate (FTR)</b>: Mide la agresividad atacando la pintura y provocando faltas al rival."
        ),
        # Slide 9
        (
            "Player Analytics y Estabilidad Longitudinal",
            "¿Cómo evaluamos la función y consistencia de un jugador?",
            [
                ("3.767 Campañas Cualificadas", "Evaluamos a todo jugador con ≥40 minutos en un torneo para garantizar significación estadística."),
                ("Estabilidad Año a Año", "Comprobamos que las tasas de rebote y pérdidas son mucho más estables entre torneos que el % de triple."),
                ("Bandas de Confianza Bootstrap", "Calculamos intervalos de confianza con B=5.000 remuestreos para evitar conclusiones precipitadas.")
            ],
            "<b>Conclusión Analítica</b>: La varianza a corto plazo no debe confundirse con la capacidad estructural del jugador."
        ),
        # Slide 10
        (
            "Arquetipos Funcionales (Clustering K-Means/PCA)",
            "¿Qué 6 roles estadísticos objetivos emergen del juego real?",
            [
                ("Iniciadores & Directores", "Primary Initiators (generadores principales de P&R) y Floor Generals (bases organizadores de bajo error)."),
                ("Tiradores & Versátiles", "Floor Spacers (tiradores de volumen exterior) y Balanced Wings (aleros 'two-way' de impacto múltiple)."),
                ("Pintura & Defensa", "Interior Hubs (pívots pasadores y finalizadores interiores) y Defensive Anchors (protectores de aro y rebote).")
            ],
            "<b>Utilidad para Scouting</b>: Permite auditar la complementariedad de un quinteto antes de fichar o rotar."
        ),
        # Slide 11
        (
            "Del Número a la Pista: Puente Datos ➔ Cinta",
            "¿Cómo se conecta el análisis cuantitativo con la observación de vídeo?",
            [
                ("Fase 1: Detección Cuantitativa", "La analítica detecta una anomalía estadística (ej. rival permite 1.18 PPP en P&R cuando defienden en Drop)."),
                ("Fase 2: Hipótesis Táctica", "Formulamos la causa probable: el pívot rival hunde demasiado su posición y concede tiros cómodos tras bote."),
                ("Fase 3: Auditoría en Vídeo", "Comprobamos 20 posesiones en vídeo para verificar si la debilidad es estructural o fruto de la suerte.")
            ],
            "<b>Entrega Final</b>: Un clip de 45 segundos y una consigna clara para la pizarra del entrenador."
        ),
        # Slide 12
        (
            "Validación Táctica en Vídeo (420 Clips)",
            "¿Cómo medimos la fiabilidad del scouting cualitativo?",
            [
                ("Codificación Sistemática", "Analizamos 420 situaciones de pick-and-roll en torneos oficiales categorizando coberturas defensivas."),
                ("Fiabilidad Inter-Observador", "Alcanzamos un coeficiente Cohen's Kappa κ = 0.80, garantizando consistencia en el criterio de scouting."),
                ("Tipología de Coberturas", "Evaluamos Drop, Switch, Blitz/Trap y Hedge y su eficacia frente a diferentes perfiles de manejador.")
            ],
            "<b>Rigor Metodológico</b>: El vídeo deja de ser subjetivo cuando se audita con protocolos estructurados."
        ),
        # Slide 13
        (
            "Machine Learning Supervisado: LightGBM Calibrado",
            "¿Qué precisión probabilística out-of-sample logramos?",
            [
                ("Modelado Predictivo Calibrado", "Entrenamos árboles de decisión con gradient boosting regularizado L2 sobre diferenciales prepartido."),
                ("Brier Score: 0.1967", "Mejora del +21.3% frente al baseline no informativo (0.2500), con MAE de 11.73 puntos en margen final."),
                ("Expected Calibration Error (ECE)", "ECE = 0.0314, garantizando que un evento con 70% de probabilidad asignada ocurre 7 de cada 10 veces.")
            ],
            "<b>Honestidad Estadística</b>: No afirmamos predecir el futuro; estimamos probabilidades calibradas antes del salto inicial."
        ),
        # Slide 14
        (
            "Validación Walk-Forward en 17 Folds",
            "¿Por qué es inadmisible la fuga de datos del futuro?",
            [
                ("El Error del K-Fold Aleatorio", "Mezclar partidos de 2022 para predecir 2012 'filtra' el estilo de juego del futuro y produce métricas falsas."),
                ("Esquema Expansivo Real", "Entrenamos estrictamente con torneos hasta T-1 y evaluamos out-of-sample en el torneo T (1.105 partidos test)."),
                ("Robustez Temporal", "El modelo mantiene estabilidad predictiva a lo largo de 20 años de evolución táctica y cambios de regla.")
            ],
            "<b>Principio Técnico</b>: El modelo solo conoce lo que un analista conocía el día antes del partido."
        ),
        # Slide 15
        (
            "Incertidumbre y Calibración Probabilística",
            "¿Cuánto debemos confiar en las probabilidades del modelo?",
            [
                ("Reliability Diagram", "Las curvas de calibración se ajustan a la diagonal perfecta, evitando la sobreconfianza en favoritos."),
                ("Probabilidades, No Certezas", "Un 85% de probabilidad de victoria significa que el rival ganará 15 de cada 100 partidos si se juega el plan."),
                ("Gestión del Riesgo", "Permite al cuerpo técnico decidir si arriesgar con una defensa agresiva o mantener el plan conservador.")
            ],
            "<b>Aplicación al Juego</b>: La probabilidad cuantitativa dimensiona el riesgo real de las decisiones tácticas."
        ),
        # Slide 16
        (
            "Atribución TreeSHAP y Límites de Causalidad",
            "¿Por qué la atribución matemática no implica causalidad deportiva?",
            [
                ("Explicabilidad Local", "TreeSHAP descompone qué factores prepartido empujan la probabilidad hacia la victoria o derrota."),
                ("Factores Más Influyentes", "Diferencial de eFG% histórico, ratio de pérdidas/asistencias y rebote defensivo dominan el impacto."),
                ("Distinción Causal Crítica", "SHAP describe correlaciones en el espacio de características del modelo, NO recetas causales directas.")
            ],
            "<b>Humildad Intelectual</b>: Un valor SHAP positivo no 'provoca' la victoria; refleja la ventaja estructural acumulada."
        ),
        # Slide 17
        (
            "Simulación Monte Carlo (180.000 Iteraciones)",
            "¿Cómo proyectamos la varianza de un cuadro de torneo?",
            [
                ("Simulación Estocástica", "Ejecutamos 10.000 simulaciones por torneo modelando la varianza de posesiones y tiro con cópulas."),
                ("Contracción Bayesiana (λ=0.75)", "Ajustamos el rendimiento hacia la media histórica del equipo para evitar distorsiones de rachas cortas."),
                ("Distribución de Medallas", "Generamos probabilidades completas de podio, pase a cuartos y eliminación en fase de grupos.")
            ],
            "<b>Resultado</b>: Capturamos la incertidumbre completa del formato eliminatorio a partido único."
        ),
        # Slide 18
        (
            "Por Qué Simular un Torneo",
            "¿En qué se diferencia preparar un partido de planificar un campeonato?",
            [
                ("Dinámica de Cuadros", "Un cruce favorable en cuartos puede doblar la probabilidad de medalla sin que el equipo mejore su rating."),
                ("Gestión de Minutos y Cargas", "Identificar qué partidos de fase de grupos permiten rotaciones más amplias sin comprometer la clasificación."),
                ("Escenarios 'What-If'", "¿Cómo cambia la probabilidad de podio si el rival directo pierde a su base titular?")
            ],
            "<b>Aporte a la Dirección</b>: Visión probabilística de largo alcance para la dirección técnica y deportiva."
        ),
        # Slide 19
        (
            "Del Análisis a la Decisión: Integración Multicapa",
            "¿Cómo se integran las capas analíticas en una recomendación final?",
            [
                ("Capa 1: Base de Datos", "Almacén DuckDB unificado con estadísticas históricas y tendencias de tiro."),
                ("Capa 2: Modelado Probabilístico", "Calibración prepartido y simulación Monte Carlo para medir el contexto de riesgo."),
                ("Capa 3: Síntesis Táctica", "Traducción a un brief prepartido de 1.5 páginas con directrices visuales para el banquillo.")
            ],
            "<b>Objetivo Final</b>: Ningún dato llega a la pista sin haber pasado por el filtro del contexto baloncestístico."
        ),
        # Slide 20
        (
            "Detección de Contradicciones Tácticas",
            "¿Qué hacemos cuando la estadística y el vídeo discrepan?",
            [
                ("Ejemplo Real", "El dato dice: 'Rival concede 38% en triples'. El vídeo revela: 'Conceden triples punteados desde las esquinas a malos tiradores'."),
                ("Resolución del Conflicto", "La estadística alerta sobre el volumen; el vídeo contextualiza la calidad y ubicación del lanzamiento."),
                ("Regla de Trabajo", "Si el dato contradice el vídeo, no descartamos ninguno: auditamos la muestra para entender la discrepancia.")
            ],
            "<b>Valor del Analista Híbrido</b>: Saber programar en Python/R y al mismo tiempo entender una defensa en 'Next'."
        ),
        # Slide 21
        (
            "Caso Real: Final Pekín 2008 (España vs EE.UU.)",
            "¿Cómo aplicamos pensamiento probabilístico en la final olímpica?",
            [
                ("El Reto Táctico", "EE.UU. dominaba el torneo forzando pérdidas y corriendo al contraataque (1.25 PPP en transición)."),
                ("La Solución Cuantitativa", "Controlar el ritmo de posesiones (bajar a <72 pos), cargar el rebote ofensivo y forzar 5c5 en estático."),
                ("Resultado del Modelo", "El modelo prepartido estimaba un margen de -8.4 pts; el resultado final fue 107-118 (-11 pts) en un partido histórico.")
            ],
            "<b>Lección Táctica</b>: Maximizar la probabilidad de competir exige atacar las debilidades estructurales del favorito."
        ),
        # Slide 22
        (
            "Caso Real: EuroBasket 2015 (España vs Francia)",
            "¿Cómo evitamos sobrerreaccionar a rachas cortas de tiro?",
            [
                ("La Trampa de la Muestra Corta", "Francia llegaba invicta y con alto acierto exterior en los primeros 6 partidos en Lille."),
                ("Análisis de Estabilidad", "El modelo detectó que el 3P% francés estaba inflado por varianza y que su defensa interior sufría en P&R central."),
                ("Ejecución en Pista", "Ataque focalizado en el bloqueo directo central (Pau Gasol 40 pts) para forzar la prórroga y la victoria 80-75.")
            ],
            "<b>Impacto Analítico</b>: La contracción bayesiana previene diseñar defensas sobre varianza estadística pasajera."
        ),
        # Slide 23
        (
            "Qué Puede Hacer un Entrenador con Esta Información",
            "¿Qué 6 preguntas concretas responde el sistema en la pizarra?",
            [
                ("1. Selección de Tiro", "¿De dónde tira más eficiente el rival y qué zonas de la pista debemos negarle?"),
                ("2. Cobertura de Bloqueo Directo", "¿Debemos jugar Drop, Switch o Flash según el perfil del manejador rival?"),
                ("3. Balance Defensivo vs Rebote", "¿Compensa mandar a 2 jugadores al rebote ofensivo o replegar a los 5?")
            ],
            "<b>4. Rotaciones | 5. Gestión del Ritmo | 6. Distribución de Faltas Tácticas</b>."
        ),
        # Slide 24
        (
            "Ejemplo de Brief Prepartido (1.5 Páginas)",
            "¿Cómo se estructura un informe prepartido ejecutable?",
            [
                ("Sección 1: Identidad y Ritmo", "Gráfico de Four Factors frente a la media de la liga, ritmo de posesiones y eficiencia neta."),
                ("Sección 2: Perfiles Individuales", "Mapa de tiro de los 3 generadores principales, arquetipo funcional y alertas de mano dominante."),
                ("Sección 3: 3 Claves para el Vídeo", "Tres consignas directas para el scout de vídeo (ej. 'Castigar la defensa en Drop del #14').")
            ],
            "<b>Formato</b>: Diseñado para imprimirse o leerse en tablet en menos de 4 minutos."
        ),
        # Slide 25
        (
            "Qué Haría Diferente en un Club Profesional",
            "¿Cómo se adapta esta metodología al día a día de una liga?",
            [
                ("Ingesta de Tracking Óptico", "Integrar datos de tracking XY de jugadores y balón (Second Spectrum / Kinexon) si están disponibles."),
                ("Monitoreo de Cargas Físicas", "Cruzar datos de rendimiento táctico con telemetría GPS y carga neuromuscular del preparador físico."),
                ("Pipeline Semanal Automatizado", "Generación automática del brief del rival a las 6:00 AM del lunes tras la jornada del fin de semana.")
            ],
            "<b>Flexibilidad</b>: La arquitectura modular permite sustituir los datos FIBA por datos de ACB, EuroLeague o FEB."
        ),
        # Slide 26
        (
            "Qué Aportaría como Analista en un Staff",
            "¿En qué áreas clave sumaría valor desde el primer día?",
            [
                ("1. Rigor Cuantitativo", "Bases de datos limpias, sin duplicados y con control de calidad determinista."),
                ("2. Traducción al Baloncesto", "Capacidad de hablar el idioma del entrenador y entregar informes sin jerga matemática."),
                ("3. Automatización de Procesos", "Ahorrar 10–15 horas semanales al cuerpo técnico en preparación de datos y scouting.")
            ],
            "<b>4. Modelado Predictivo | 5. Scouting de Plantilla | 6. Trabajo Interdisciplinar con Vídeo y Físico</b>."
        ),
        # Slide 27
        (
            "Lo Que NO Haría (Líneas Rojas Profesionales)",
            "¿Qué límites metodológicos y de ética mantengo?",
            [
                ("NO Pretender Dirigir", "El analista aporta evidencia y contexto; las decisiones tácticas y de vestuario son del Head Coach."),
                ("NO Vender 'Magia Predictiva'", "Rechazo categórico a algoritmos de 'caja negra' que prometen adivinar resultados sin incertidumbre."),
                ("NO Ocultar la Varianza", "Siempre reportar intervalos de confianza y asumir que en 40 minutos cualquier resultado es posible.")
            ],
            "<b>Ética de Trabajo</b>: Humildad, rigor técnico y respeto absoluto por la experiencia del entrenador."
        ),
        # Slide 28
        (
            "Límites Metodológicos del Dataset",
            "¿Qué restricciones reales tiene este proyecto?",
            [
                ("Ausencia de Tracking Óptico", "El dataset utiliza boxscores oficiales y eventos, no coordenadas espaciales continuas a 25 fps."),
                ("Torneos de Muestra Corta", "Las competiciones de selecciones tienen 6–9 partidos; se requiere regularización bayesiana para inferir."),
                ("Datos Públicos Heterogéneos", "Los formatos de acta evolucionaron entre 2005 y 2024, requiriendo normalización determinista.")
            ],
            "<b>Transparencia</b>: Reconocer los límites del dato es el primer paso para no extraer conclusiones falsas."
        ),
        # Slide 29
        (
            "El Repositorio en GitHub: Auditoría en 2–30 Minutos",
            "¿Cómo puede un evaluador técnico auditar el código?",
            [
                ("2 Minutos (Overview)", "README con tabla canónica, diagramas de arquitectura y 227 tests automatizados en pytest."),
                ("5 Minutos (Reproducibilidad)", "Ejecución unificada con `python scripts/run_project.py` que valida el entorno y ejecuta los tests."),
                ("30 Minutos (Inspección Profunda)", "Revisión de módulos en `src/`, capa R/Quarto en `R/`, consultas DuckDB y manifiesto SHA-256.")
            ],
            "<b>Código Abierto y Certificado</b>: 0 credenciales, 0 secretos y 100% de reproducibilidad offline."
        ),
        # Slide 30
        (
            "Cierre y Filosofía del Analista de Baloncesto",
            "¿Cuál es la misión final de nuestro trabajo?",
            [
                ("La Misión Central", "Ayudar a entrenadores, directores deportivos y jugadores a tomar mejores decisiones bajo incertidumbre."),
                ("El Enfoque", "Combinar ingeniería de datos robusta, estadística rigurosa, machine learning calibrado y pasión por el baloncesto."),
                ("Contacto Profesional", "Miguel — Basketball Data Analyst | GitHub: github.com/miguel/basketball-analytics")
            ],
            "<b>Muchas Gracias</b>: Abierto a preguntas técnicas, metodológicas y de baloncesto."
        )
    ]

    # Build slides 2 to 30
    for idx, (title, subtitle, bullets, callout) in enumerate(slides_data, start=2):
        story.append(Paragraph(title, slide_title))
        story.append(Paragraph(subtitle, slide_subtitle))

        # Create 3 visual cards/boxes for bullets
        card_data = []
        for b_title, b_desc in bullets:
            cell_content = [
                Paragraph(b_title, card_header),
                Spacer(1, 4),
                Paragraph(b_desc, card_body)
            ]
            card_data.append(cell_content)

        # 3-column table for cards
        col_w = (PAGE_WIDTH - 80) / 3.0
        table_rows = [[card_data[0], card_data[1], card_data[2]]]

        card_table = Table(table_rows, colWidths=[col_w, col_w, col_w])
        card_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8fafc')),
            ('BOX', (0, 0), (0, 0), 1, colors.HexColor('#cbd5e1')),
            ('BOX', (1, 0), (1, 0), 1, colors.HexColor('#cbd5e1')),
            ('BOX', (2, 0), (2, 0), 1, colors.HexColor('#cbd5e1')),
            ('ROUNDEDCORNERS', [4, 4, 4, 4]),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        story.append(card_table)
        story.append(Spacer(1, 16))

        # Callout banner at bottom
        callout_p = Paragraph(callout, callout_text)
        callout_table = Table([[callout_p]], colWidths=[PAGE_WIDTH - 80])
        callout_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#eff6ff')), # Light blue tint
            ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#93c5fd')),
            ('LEFTPADDING', (0, 0), (-1, -1), 14),
            ('RIGHTPADDING', (0, 0), (-1, -1), 14),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
        ]))
        story.append(callout_table)

        if idx < 30:
            story.append(PageBreak())

    # Build the document using NumberedCanvas
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Presentation PDF successfully built at: {output_path}")

if __name__ == '__main__':
    out_pdf = os.path.abspath('presentation/International_Basketball_Analytics_Presentation.pdf')
    create_presentation_pdf(out_pdf)
