# ESTRATEGIA DE DIFUSIÓN SOSTENIBLE DEL PROYECTO (MVP-21)
## International Basketball Analytics (2005–2024)

> **Regla de Oro**: *Compartir para aportar conocimiento y pedir crítica técnica, NUNCA con mensajes desesperados de "miren mi portfolio".*

---

## 1. El Repositorio de GitHub como Centro Inmutable

El repositorio [github.com/miguel/basketball-analytics] está estructurado para que cualquier visitante técnico o deportivo valide el trabajo en 3 niveles de profundidad:

```text
[NIVEL 1: 30 Segundos]    README.md
                          ├── Badges oficiales (227 tests passing, DuckDB, Python 3.14, R 4.6)
                          ├── Tabla de hechos canónicos (1.145 partidos, 18 torneos)
                          └── Gráfico de arquitectura de datos

[NIVEL 2: 2 Minutos]      Resultados y Soporte Táctico
                          ├── Brief Prepartido de 1.5 páginas (Pekín 2008 / EuroBasket 2022)
                          ├── Informe Quarto interactivo (.html)
                          └── Curvas de calibración y Brier Score (0.1967)

[NIVEL 3: 5 Minutos]      Ingeniería y Reproducibilidad
                          ├── Ejecución unificada: `python scripts/run_project.py`
                          ├── Manifiesto criptográfico SHA-256 (docs/reproducibility_manifest.md)
                          └── Suite de 227 tests en pytest (100% de éxito)
```

---

## 2. Pautas de Difusión en Comunidades (Showcase sin Spam)

1. **Compartir Fragmentos Autónomos (Micro-Casos de Estudio)**: En lugar de compartir el enlace global al repositorio, compartir la solución a un problema concreto (por ejemplo, cómo evitar *data leakage* en competiciones deportivas mediante *walk-forward*).
2. **Pedir Feedback Específico**: Cerrar siempre las publicaciones con una pregunta técnica abierta (*"¿Habéis experimentado problemas de calibración similares al modelar ligas cortas con LightGBM?"* o *"¿Cómo gestionáis en vuestros clubes el cuadre de minutos en actas con prórroga?"*).
3. **Ofrecer Código Limpio y Gráficos Nítidos**: Incluir bloques de código comentados en Markdown y figuras exportadas a 300 DPI con `theme_basketball_analytics()`.
