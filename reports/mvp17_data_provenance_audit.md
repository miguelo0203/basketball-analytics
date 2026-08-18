# AUDITORÍA DE PROCEDENCIA DE DATOS, LICENCIAS Y DERECHOS (MVP-17)
## International Basketball Analytics (2005–2024)

> **Propósito**: Evaluar la legalidad, atribución y transparencia de las fuentes de datos utilizadas en el proyecto.

---

## 1. Fuentes de Datos y Procedencia

| Categoría de Datos | Fuente Primaria | Acceso / Protocolo | Almacenamiento Local | Atribución y Licencia | Veredicto |
|---|---|---|---|---|:---:|
| **Resultados y Boxscores Oficiales FIBA** | Archivo Oficial FIBA / Documentación Pública de Torneos | Consulta pública / Archivo local estructurado | `data/01_raw/SRC_WIKI_ARCHIVE/` | Hechos deportivos públicos de dominio general. Uso estrictamente educativo y de investigación no comercial. | **GREEN** |
| **Plantillas y Metadatos de Jugadores** | Registros federativos públicos y anuarios de torneos | Hechos deportivos oficiales | `dim_player`, `dim_tournament` | Datos fácticos de eventos públicos internacionales. | **GREEN** |
| **Codificación Táctica de Vídeo (P&R)** | Muestreo de vídeo de partidos emitidos en abierto (2008–2024) | Visionado y anotación manual propia | `data/04_analytics/mvp5_video_validation.parquet` | Creación propia del autor siguiendo rúbrica estandarizada (`config/mvp5_video_observation_rubric.yaml`). | **GREEN** |
| **Código Fuente del Proyecto** | Desarrollado íntegramente para este repositorio | Repositorio GitHub | `src/`, `R/`, `scripts/`, `tests/` | Licencia MIT / Open Source para demostración de portfolio profesional. | **GREEN** |

---

## 2. Declaración de Limitaciones de Redistribución y Ética

1. **Uso No Comercial**: Todos los datos procesados corresponden a competiciones de selecciones nacionales absolutas masculinas disputadas entre 2005 y 2024. El proyecto tiene fines exclusivamente analíticos, metodológicos y de demostración de competencias profesionales.
2. **Ausencia de Scraping Agresivo en Vivo**: Los datos brutos están archivados localmente en `data/01_raw/`, por lo que el repositorio no ejecuta ataques de scraping automatizados contra servidores de federaciones deportivas.
3. **Privacidad y Datos Sensibles**: No se recopilan ni almacenan datos médicos privados, biometría invasiva ni telemetría confidencial de los atletas.

---

## 3. Veredicto de Procedencia

> **VEREDICTO**: **GREEN (CUMPLIMIENTO ÉTICO Y LEGAL COMPLETO)**.  
> La procedencia de los datos está documentada en [config/sources.yaml](config/sources.yaml) y [docs/execution_lineage.md](docs/execution_lineage.md), sin infringir derechos propietarios ni utilizar datos corporativos restringidos.
