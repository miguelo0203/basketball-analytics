# AUDITORÍA DE EXPERIENCIA DEL REVISOR EXTERNO (README AUDIT - MVP-17)
## International Basketball Analytics (2005–2024)

> **Objetivo**: Evaluar la claridad, velocidad de comprensión y utilidad del `README.md` ante tres perfiles reales de evaluadores externos.

---

## 1. Evaluación por Perfiles de Usuario

### 👤 Persona A — Hiring Manager / Recruiter Técnico (< 60 Segundos)

| Pregunta Clave | ¿Se responde en el README? | Ubicación y Calidad de la Respuesta | Veredicto |
|---|:---:|---|:---:|
| **¿Qué ha construido el candidato?** | SÍ | Bloque inicial "El proyecto en 30 segundos" y tabla resumen de hechos canónicos. | **GREEN** |
| **¿Qué sabe hacer técnicamente?** | SÍ | Insignias activas, matriz de tecnologías (Python, R, DuckDB, ML, Quarto) y tabla de componentes. | **GREEN** |
| **¿Qué nivel de rigor demuestra?** | SÍ | 227 tests automatizados en pytest con 100% de éxito y validación walk-forward out-of-sample en 17 folds. | **GREEN** |
| **¿Dónde están los materiales de contratación?** | SÍ | Enlace directo y destacado al [Portfolio Hub](../portfolio/README.md) con rutas específicas por perfil. | **GREEN** |

---

### 👤 Persona B — Basketball Analyst / Entrenador / Director Deportivo

| Pregunta Clave | ¿Se responde en el README? | Ubicación y Calidad de la Respuesta | Veredicto |
|---|:---:|---|:---:|
| **¿Qué problema real de baloncesto aborda?** | SÍ | Explica la distorsión de la muestra pequeña en torneos de 6–9 partidos y la sobrecarga de datos del staff. | **GREEN** |
| **¿Cómo traduce datos en información útil?** | SÍ | Detalla la entrega de briefs prepartido de 1.5 páginas con preguntas accionables para el cuerpo técnico. | **GREEN** |
| **¿Qué tipo de outputs deportivos genera?** | SÍ | Arquetipos funcionales, análisis de cobertura P&R en vídeo y simulaciones Monte Carlo con contracción bayesiana. | **GREEN** |
| **¿Reconoce los límites del dato en pista?** | SÍ | Sección explícita de "Qué NO pretende hacer": no predice certezas absolutas ni sustituye la autoridad del entrenador. | **GREEN** |

---

### 👤 Persona C — Technical Data Engineer / Analytics Lead

| Pregunta Clave | ¿Se responde en el README? | Ubicación y Calidad de la Respuesta | Veredicto |
|---|:---:|---|:---:|
| **¿Cómo se ingieren y validan los datos?** | SÍ | Diagrama de flujo de datos, almacén relacional DuckDB (12 tablas) y motor de QA determinista. | **GREEN** |
| **¿Cómo se divide Python y R?** | SÍ | Sección de arquitectura dual: Python para ETL/ML/QA, R para EDA/Longitudinal/Quarto. | **GREEN** |
| **¿Cómo se ejecuta el proyecto en local?** | SÍ | Instrucciones claras de "Inicio Rápido en 3 Pasos" (`python scripts/run_project.py`). | **GREEN** |
| **¿Cómo se verifican los tests?** | SÍ | Comando `python -m pytest tests` documentado y enlazado a [docs/testing.md](../docs/testing.md). | **GREEN** |

---

## 2. Puntos Fuertes Identificados en el README

1. **Estructura Piramidal**: Va de lo conceptual (30 segundos) a lo cuantitativo (cifras auditadas), arquitectónico y operativo.
2. **Navegación Modular por Audiencias**: Rutas diferenciadas para directores deportivos, analistas de datos e ingenieros de software.
3. **Honestidad Intelectual**: Ausencia total de sobreventa, claims de omnisciencia o predicciones mágicas.

---

## 3. Veredicto del README

> **VEREDICTO**: **GREEN (EXCELENTE)**.  
> El documento cumple con los estándares más exigentes de presentación técnica en GitHub, permitiendo una comprensión integral del proyecto en menos de 2 minutos.
