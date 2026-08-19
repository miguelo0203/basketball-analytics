# Índice de Documentación Técnica

Bienvenido a la documentación técnica y metodológica completa del sistema de **Análisis de Baloncesto Internacional y Soporte a Decisiones (2005–2024)**.

---

## 1. Fundamentos del Sistema
- **[Arquitectura del Sistema](arquitectura.md)**: Flujo de datos, capas de almacenamiento, almacén DuckDB y componentes modulares.
- **[Datos y Procedencia](datos.md)**: Fuentes oficiales, cobertura temporal (18 torneos, 1.145 partidos), validación SHA-256 y esquemas relacionales.
- **[Metodología Analítica](metodologia.md)**: Four Factors de Dean Oliver, ajuste de posesiones, econometría y taxonomía de roles.

---

## 2. Modelado y Análisis Avanzado
- **[Machine Learning y Calibración](machine_learning.md)**: Validación temporal walk-forward en 17 folds, calibración isotónica ($\text{ECE} = 0.0314$), TreeSHAP e inferencia.
- **[Análisis Táctico y Toma de Decisiones](analisis_tactico.md)**: Integración de Four Factors, mapas de tiro y formulación de consignas prepartido.
- **[Sistema de Soporte a Decisiones](soporte_decisiones.md)**: Matriz de evidencia analítica, motor de contradicciones, briefs prepartido y aislamiento anti-hindsight.

---

## 3. Calidad, Testing y Reproducibilidad
- **[Guía de Reproducibilidad](reproducibilidad.md)**: Instrucciones deterministas de instalación, inicialización de datos y ejecución local.
- **[Marco de Testing y Calidad](testing.md)**: Detalle de los 227 tests automatizados con pytest ($100\%$ de tasa de éxito).

---

## 4. Transparencia, Gobernanza y Límites
- **[Límites y Alcance Profesional](limitaciones.md)**: Qué demuestra este proyecto, qué está modelado y qué requiere datos de tracking en vivo.
- **[Gobernanza de Claims y Lenguaje](claims_y_limitaciones.md)**: Clasificación de métricas públicas en VERDE, AMARILLO y ROJO.
- **[Guía del Revisor de GitHub](github_reviewer_journey.md)**: Itinerario de lectura optimizado para 2, 5, 15, 30 y 60 minutos.

---

> [!NOTE]
> **Nota de Contexto y Metodología Data-First**:
> El proyecto publicado sigue estrictamente una metodología **Data-First** basada en actas oficiales, eventos estructurados, Four Factors neutralizados al ritmo y modelado probabilístico calibrado.
> Los informes en `reports/` contienen artefactos históricos del proceso iterativo de desarrollo; la documentación pública en este índice, el `README.md` principal, la presentación y los casos de estudio en `portfolio/case_studies/` constituyen la fuente autoritativa actual.
