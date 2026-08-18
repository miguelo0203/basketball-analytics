# Análisis Táctico y Capa de Vídeo Cualitativo

## 1. Integración de Scouting Visual y Estadística

Las estadísticas cuantitativas tradicionales no capturan la geometría espacial de las defensas. Para cerrar esta brecha, el sistema incorpora un mart de datos de vídeo (`mart_tactical_video.parquet`) con posesiones codificadas bajo un protocolo estandarizado.

---

## 2. Protocolo de Observación y Variables Registradas

Se evaluaron dos comportamientos defensivos críticos:
1. **Profundidad de Drop Coverage en Pick-and-Roll**:
   - Posición del pívot defensor respecto a la línea de tiros libres y el aro (Drop profundo, a nivel de bloqueo, step out o cambio).
   - Concesión de espacios a tiradores exteriores en pick-and-pop.
2. **Velocidad de Recuperación en Closeouts**:
   - Tiempo de respuesta y ángulo de contestación ante pases abiertos a la esquina o cabecera.

---

## 3. Protocolo de Doble Codificación y Fiabilidad Inter-Evaluador

Para evitar la subjetividad de un único analista, se aplicó un protocolo de doble codificación independiente:
- **Muestra Observacional**: **420 posesiones** seleccionadas a través de 36 partidos internacionales de alta tensión.
- **Fiabilidad en Tipo de Acción Táctica**: **Cohen's Kappa $\kappa = 1.00$** (concordancia perfecta).
- **Fiabilidad en Calificación de Ejecución Defensiva**: **Cohen's Kappa $\kappa = 0.80$** (concordancia sustancial / casi perfecta).

---

## 4. Interpretación Correcta de la Capa de Vídeo

```
+----------------------------------------------------------------------------------------------------+
| QUÉ SIGNIFICA κ = 0.80                       | QUÉ NO SIGNIFICA                                    |
+----------------------------------------------------------------------------------------------------+
| • El protocolo de etiquetado táctico es      | • NO convierte 420 posesiones en un censo universal |
|   consistente, objetivo y reproducible.      |   de todo el baloncesto internacional.              |
| • Permite cruzar la estadística con la cinta | • NO sustituye la sesión diaria de vídeo del cuerpo|
|   para detectar contradicciones reales.      |   técnico antes de cada partido.                    |
+----------------------------------------------------------------------------------------------------+
```

*Definición Metodológica*: La capa de vídeo constituye una **muestra cualitativa exploratoria para generar hipótesis tácticas** y contextualizar las predicciones del modelo numérico.
