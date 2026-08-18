# Hub del Portfolio de Analítica de Baloncesto
## International Basketball Analytics (2005–2024)
### *De los Datos a la Evidencia para Apoyar Decisiones de Baloncesto*

Este directorio centraliza todos los activos de presentación, casos de estudio, perfiles de candidatura y guías de demostración del proyecto.

---

## 🧭 Itinerarios de Navegación Personalizados

### 1. START HERE (Por Dónde Empezar)
1. ⚡ **[La Idea en 30 Segundos](../README.md#el-proyecto-en-30-segundos)**: Resumen ejecutivo del problema y la solución.
2. ⏱️ **[Demostración en 5 Minutos](presentation/5_minute_project_demo.md)**: Guión ágil para entrevistas técnicas y deportivas.
3. 📊 **[Presentación Ejecutiva Completa (30 Slides)](presentation/README.md)**: Archivo PowerPoint editable y notas de orador para 25–35 min.
4. 🏀 **[Caso Flagship: Pekín 2008](flagship_case.md)**: Estudio prepartido de la final olímpica España vs. EE. UU.
5. 📘 **[Documentación Técnica](../docs/README.md)**: Índice de 12 documentos de arquitectura, datos y modelos.
6. 💻 **[Repositorio Principal en GitHub](../README.md)**: Código fuente, datos relacionales DuckDB y suite de pruebas.

---

### 2. FOR RECRUITERS & HIRING MANAGERS (Para Reclutadores y Recursos Humanos)
1. 👤 **[Perfil del Candidato (Candidate Profile)](job_search/candidate_profile.md)**: Resumen de habilidades, competencias día 1 y áreas de desarrollo.
2. 📄 **[Master de Entradas para CV](job_search/cv_master.md)** y **[Modelo de CV de 1 Página](job_search/cv_one_page.md)**: Bullets modulares y CV estandarizado.
3. ⏱️ **[Pitch Profesional de 60 Segundos](presentation/60_second_pitch.md)**: Guión oral de presentación ejecutiva.
4. 🌐 **[Ficha del Proyecto para LinkedIn](job_search/linkedin_profile.md)** y **[Publicación Destacada](job_search/linkedin_post.md)**.
5. 🤝 **[Estrategia de Outreach y Mensajes](job_search/outreach_strategy.md)**: Plantillas de contacto para clubes y empresas en `job_search/outreach/`.

---

### 3. FOR BASKETBALL PROFESSIONALS (Para Entrenadores y Directores Deportivos)
1. 📋 **[Pitch de Baloncesto y Pizarra](presentation/basketball_analyst_pitch.md)**: Enfoque táctico en Four Factors, P&R y espaciado.
2. 🏀 **[Caso Flagship: Pekín 2008](flagship_case.md)**: Cómo el analista detecta ventajas tácticas en drop coverage.
3. 📑 **[Soporte a Decisiones y Briefs Prepartido](../docs/soporte_decisiones.md)**: Estructura de informes de 1.5 páginas para el cuerpo técnico.
4. 🎥 **[Análisis Táctico y Vídeo](../docs/analisis_tactico.md)**: Protocolo de observación cualitativa con fiabilidad $\kappa = 0.80$.
5. 🏟️ **[Adaptación a un Club Profesional](../docs/real_club_adaptation.md)**: Cómo evoluciona el sistema con datos de tracking 25Hz y calendario semanal.

---

### 4. FOR TECHNICAL REVIEWERS (Para Data Scientists y Data Engineers)
1. 🏗️ **[Arquitectura del Sistema](../docs/arquitectura.md)**: Esquema de 9 capas y almacenamiento en DuckDB / Parquet.
2. 🗄️ **[Procedencia y Calidad de Datos](../docs/datos.md)**: 1.145 partidos, 2.124 entidades canónicas y firmas SHA-256.
3. 🤖 **[Machine Learning y Calibración](../docs/machine_learning.md)**: Validación walk-forward en 17 folds (Brier = 0.1967, ECE = 0.0314).
4. 🎲 **[Simulaciones Monte Carlo](../docs/metodologia.md)**: 180.000 iteraciones con shrinkage bayesiano ($\lambda = 0.75$).
5. 🧪 **[Marco de Testing (209 tests)](../docs/testing.md)**: Suite de pruebas unitarias y de integración con pytest (100% pass rate).
6. ⚙️ **[Guía de Reproducibilidad](../docs/reproducibilidad.md)**: Instrucciones deterministas de instalación y ejecución.

---

## Cómo Lanzar la Aplicación Interactiva (Streamlit Workspace)

```bash
streamlit run src/analytics/mvp10_analyst_workspace.py -- streamlit
```

Selecciona **"🎯 5–10 Min Flagship Live Demo"** en el menú lateral para iniciar la experiencia interactiva prepartido con aislamiento temporal anti-hindsight.
