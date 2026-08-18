# Límites Metodológicos y Alcance Profesional

## 1. Límites de Datos y Tamaño de Muestra
- **Formato de Torneo Corto**: Las competiciones internacionales constan de 6 a 9 partidos en 15 días. Las estadísticas de tiro acumuladas en un único torneo presentan una elevada varianza estocástica.
- **Sin Tracking Óptico 25Hz en Vivo**: El sistema utiliza actas oficiales y codificación de vídeo cualitativa; no incorpora coordenadas cartesianas continuas (Second Spectrum XYZ) al no disponer de licencias propietarias de clubes privados.

---

## 2. Límites Estadísticos y del Modelo Predictivo
- **Asociación vs. Causalidad**: Los árboles de decisión (LightGBM) y los valores TreeSHAP identifican correlaciones estadísticas condicionales históricas. No garantizan relaciones causales directas tras una intervención táctica.
- **Incertidumbre Irreducible**: El baloncesto es un juego dinámico con rebotes fortuitos, faltas arbitrales y rachas individuales de tiro que escapan a cualquier modelo prepartido.

---

## 3. Límites de la Capa de Vídeo
- **Muestra Observacional ($N=420$)**: La codificación de 420 posesiones en 36 partidos clave sirve para ilustrar cómo se contrastan números con vídeo; no pretende constituir un censo de cada jugada disputada en 20 años.

---

## 4. Requisitos para el Despliegue en un Club Profesional Real
Para transferir esta arquitectura a la operativa diaria de un club de élite (Liga Endesa / EuroLeague / NBA), se requeriría:
1. Conexión directa a APIs de proveedores en vivo (Synergy Sports, Second Spectrum).
2. Integración con datos de carga física y biometría (Catapult GPS / Firstbeat).
3. Base de datos de contratos y mercado de fichajes para modelar restricciones salariales.
