# Earthquakes-analysis

Análisis de los terremotos superiores a 2.5 en la escala de Richter en todo el mundo. Generar estadísticas sobre los terremotos (cantidad por país, rangos, evolución en el tiempo, etc.). El proyecto se realizará integrando Python, SQLite y Power BI.

Se utiliza SQLite al no necesitar instalar nada. Genera un archivo local .db, perfecto para proyectos como éste y mejora su portabilidad.

## Tecnologías utilizadas

- Python 3.13
- Librerías estándar:

    - pathlib
    - pandas
    - geopandas
    - sqlite3
    - seaborn
    - matplotlib
    - time
    - calendar
    - json
    
# Preguntas a responder

- Número de terremotos por país.
- Qué país tiene mayor actividad sísmica.
- Top 10 terremotos.
- Evolución temporal de terremotos.
- Relación magnitud vs profundidad.
- Distribución geográfica (mapa).
- Frecuencia de terremotos > 6 por año.
- Clustering por zonas sísmicas.

# Modelado de procesamiento

- ETL:
    - Descarga de datos de terremotos en https://earthquake.usgs.gov/ en formato CSV y capa de países (1:10m Cultural Vectors - Admin 0 - countries) en https://www.naturalearthdata.com/
    - Inspección de la estructura de datos en Python
    - CLEAN data mediante Python
        - Dar formato de fecha a la fecha del terremoto
        - Crear columnas necesarias para su posterior análisis
        - Extraer el país y normalizarlo a través de un spatial join con geopandas y la capa de países de naturalearthdata.
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
