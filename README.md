# Earthquakes-analysis

Análisis de los terremotos superiores a 2.5 en la escala de Richter en todo el mundo. Generar estadísticas sobre los terremotos (cantidad por país, rangos, evolución en el tiempo, etc.). El proyecto se realizará integrando Python, SQLite y Power BI.

Se utiliza SQLite porque no necesita instalar nada. Genera un archivo local .db, perfecto para proyectos como éste.

## Tecnologías utilizadas

- Python 3.13
- Librerías estándar:

    - pathlib
    - pandas
    - geopandas
    - sqlite3
    
# Preguntas a responder

- Número de terremotos por país.
- Qué país tiene mayor actividad sísmica.
- Top 10 terremotos.
- Evolución de terremotos temporal.
- Relación magnitud vs profundidad.
- Distribución geográfica (mapa).
- Frecuencia de terremotos > 6 por año.
- Clustering por zonas sísmicas.

# Modelado de procesamiento

- Descarga de datos en https://earthquake.usgs.gov/ en formato CSV
- Inspección de la estructura de datos en Python
- CLEAN layer mediante Python (funciones en transform.py)
    - Dar formato date a la fecha del terremoto
    - Extraer el país y normalizarlo
- Cargar datos, crear tablas y vistas con SQLite
- Generar gráficas en Power BI y Python

# Estructura

earthquakes-analysis/

- data/
    - raw/
    - processed/

- sql/
    - schema.sql
    - queries.sql

- src/
    - extract.py
    - transform.py
    - load.py

- notebooks/

- README.md

# Requisitos

- Respetar la estructura organizativa del proyecto
