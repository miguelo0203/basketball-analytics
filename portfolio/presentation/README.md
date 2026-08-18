# Presentación Ejecutiva del Portfolio
## International Basketball Analytics (2005–2024)
### De los Datos a la Evidencia para Apoyar Decisiones de Baloncesto

Este directorio contiene el paquete completo de presentación profesional orientado a entrevistas de trabajo, reuniones con directores deportivos, cuerpos técnicos y responsables de analítica.

---

## Archivos del Paquete de Presentación

- **[International_Basketball_Analytics_Presentation.pptx](International_Basketball_Analytics_Presentation.pptx)**: Archivo PowerPoint editable en formato panorámico 16:9 con las 30 diapositivas diseñadas profesionalmente.
- **[Guión y Estructura Visual (presentation_outline.md)](presentation_outline.md)**: Estructura detallada de las 30 diapositivas con la pregunta concreta que responde cada slide.
- **[Notas del Orador (speaker_notes.md)](speaker_notes.md)**: Guía completa de exposición oral cronometrada para una presentación de 25 a 35 minutos.

---

## Resumen del Flujo Narrativo (30 Diapositivas)

$$\text{PROBLEMA} \longrightarrow \text{DATOS} \longrightarrow \text{CALIDAD} \longrightarrow \text{ANÁLISIS} \longrightarrow \text{TÁCTICA} \longrightarrow \text{VALIDACIÓN} \longrightarrow \text{DECISIÓN} \longrightarrow \text{VALOR}$$

1. **Slides 1–3**: Introducción, propuesta de valor en 30s y el problema real que resuelve un analista.
2. **Slides 4–6**: Arquitectura de 9 capas, escala verificada y pipeline determinista de calidad de datos.
3. **Slides 7–12**: Four Factors, analítica de jugadores, arquetipos funcionales y validación táctica en vídeo ($\kappa = 0.80$).
4. **Slides 13–18**: Machine Learning walk-forward, calibración isotónica ($\text{ECE} = 0.0314$), atribución SHAP y simulaciones Monte Carlo.
5. **Slides 19–24**: Síntesis de decisión, motor de contradicciones, casos reales (Pekín 2008, EuroBasket 2015) y brief para el entrenador.
6. **Slides 25–30**: Adaptación a club profesional, aportaciones del candidato, líneas rojas, límites y cierre.

---

## Cómo Reproducir o Regenerar la Presentación

La presentación se genera programáticamente de forma determinista mediante el script Python:

```bash
python -m src.analytics.generate_master_presentation
```
