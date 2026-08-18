# Pitch Técnico (2–3 Minutos)
## Orientado a: Data Scientists, Data Engineers, Analytics Engineers y Technical Hiring Managers

**Duración**: 2.5 Minutos  
**Foco**: Arquitectura de software, integridad de datos, esquemas de validación, calibración y testing.

---

### Guión de Exposición Técnica

> "A nivel técnico, el proyecto está concebido como una infraestructura analítica integral desacoplada en 9 capas, diseñada bajo principios estrictos de reproducibilidad, modularidad y aislamiento temporal.
> 
> En la **capa de datos e ingeniería**, la fuente original proviene de actas oficiales de FIBA congeladas con hashes criptográficos SHA-256. Implementé un pipeline determinista de resolución de identidades que unificó 2.124 jugadores canónicos y normalizó las entidades en un almacén relacional **DuckDB** de 12 tablas, optimizado para analítica OLAP columnar y exportado a marts en **Parquet**.
> 
> En la **capa de feature engineering y modelado no supervisado**, procesamos 3.767 campañas cualificadas de jugador ($\ge 40$ min) extrayendo métricas normalizadas per-40, Four Factors de Dean Oliver y ratios de eficiencia. Aplicamos **K-Means++ y PCA** para descubrir 6 arquetipos funcionales independientes de la posición tradicional.
> 
> Para la **capa predictiva supervisada**, evité intencionadamente cualquier partición aleatoria estándar (*k-fold shuffle*) que generaría *data leakage* temporal masivo. En su lugar, construí **17 folds temporales walk-forward expansivos**, evaluando 1.105 partidos estrictamente fuera de muestra. Nuestro modelo principal con **LightGBM** obtuvo un Brier Score de `0.1967`, un ROC-AUC de `0.7613` y un MAE de margen de `11.739 puntos`.
> 
> Evaluamos la **calibración probabilística** con reliability curves sobre 10 bins, logrando un Expected Calibration Error (ECE) de `0.0314` (3.14%), lo que garantiza que las probabilidades estimadas son estadísticamente seguras para propagar a nuestro motor de **simulación Monte Carlo** (180.000 iteraciones con shrinkage $\lambda = 0.75$).
> 
> Para la **interpretabilidad**, calculamos la importancia por permutación en pliegues test y medimos la estabilidad temporal de los rankings con correlación de Spearman ($\rho = 0.854$).
> 
> Finalmente, todo el repositorio está respaldado por **201 tests automatizados con pytest**, con una tasa de éxito del 100% en menos de 90 segundos, garantizando que cada transformación matemática y esquema relacional es determinísticamente reproducible."
