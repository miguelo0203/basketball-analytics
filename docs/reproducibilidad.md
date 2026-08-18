# Guía de Reproducibilidad Técnica

## 1. Requisitos del Entorno
- **Python**: Versión 3.10 o superior (certificado y probado en Python 3.14 de 64 bits en Windows, Linux y macOS).
- **Almacén Analítico**: DuckDB integrado en proceso (no requiere servidores externos).

---

## 2. Instalación Paso a Paso

```bash
# 1. Clonar el repositorio
git clone https://github.com/[usuario]/Espana2005-2025.git
cd Espana2005-2025

# 2. Crear y activar el entorno virtual
python -m venv .venv
# En Linux/macOS:
source .venv/bin/activate
# En Windows:
.venv\Scripts\activate

# 3. Instalar las dependencias fijadas
pip install -r requirements.txt
```

---

## 3. Verificación de la Base de Datos DuckDB

La base de datos analítica está pre-compilada y validada en el repositorio:
- **Ruta**: `data/03_validated/basketball_analytics.duckdb`
- **Marts Parquet**: `data/04_marts/analytics/`

Comprobación rápida en terminal de Python:
```python
import duckdb
con = duckdb.connect("data/03_validated/basketball_analytics.duckdb", read_only=True)
print(con.execute("SELECT count(*) AS total_partidos FROM fact_game;").df())
con.close()
```

---

## 4. Ejecución del Workspace del Analista (Streamlit)

Inicia la aplicación interactiva localmente:

```bash
streamlit run src/analytics/mvp10_analyst_workspace.py -- streamlit
```
- **Navegador**: Abre automáticamente en `http://localhost:8501`.
- **Modo Demo Rápido**: Selecciona **"🎯 5–10 Min Flagship Live Demo"** en la barra lateral para explorar el caso de estudio de la Final Olímpica de Pekín 2008.

---

## 5. Ejecución de la Suite Completa de Tests

Ejecuta los 195 tests automatizados de la suite de regresión:

```bash
python -m pytest tests -q
```
*Resultado esperado: `195 passed in ~80-100s (100% pass rate)`.*
