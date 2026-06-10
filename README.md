# Earthquakes-analysis

Análisis de la actividad sísmica global entre 2000 y 2025 utilizando datos de la API de USGS.

El objetivo del proyecto es estudiar la frecuencia, distribución geográfica y evolución de los terremotos.

## Descripción del proyecto

En el proyecto se construye un pipeline completo de datos (ETL) para analizar la actividad sísmica global:

- Extracción de datos desde la API oficial de USGS
- Transformación y limpieza de datos
- Enriquecimiento geoespacial con GeoPandas
- Almacenamiento en SQLite
- Análisis y visualización en Python

El dataset final contiene más de 3 millones de registros oficiales, incluyendo los terremotos de magnitud 0 a 10.

Se utiliza SQLite al no necesitar instalar nada. Genera un archivo local .db, perfecto para proyectos como éste y mejora su portabilidad.

## Tecnologías utilizadas

- Python 3.13
- Librerías estándar:

    - pathlib: manejo de carpetas y archivos
    - pandas: manipulación de datos
    - geopandas: análisis geoespacial
    - sqlite3: almacenamiento
    - seaborn: visualización de datos
    - matplotlib: visualización de datos
    - time: soporte ETL
    - calendar: soporte ETL
    - json: soporte ETL
    - requests: consumo de API
    
## Pipeline de datos (ETL)

1. Extracción:
    - Descarga de datos desde la API de USGS
    - División de consultar por meses/semanas para evitar límites de API

2. Transformación:
    - Conversion de fechas
    - Creación de nuevas variables
    - Extracción y normalización del nombre de países
    - Enriquecimiento geoespacial con GeoPandas

3. Carga:
    - Carga de datos en SQLite
    - Control de errores y recuperación de datos fallidos en consulta de API
    - Dataset final completo

# Estructura

earthquakes-analysis/

- database/
    - geoespatial/ # Limites administrativos
    - processed/ # Base de datos final
    - raw/ # Muestra de datos sin procesar CSV
    - raw_api/ # Datos sin procesar API

- images/ # Gráficos generados

- notebooks/ # Análisis exploratorio

- sql/ # Schema y queries utilizadas

- src/ # Lógica ETL

- main_API.py # Pipeline principal API
- main_CSV.py # Pipeline con datos CSV
- main_failer_range_API.py # Pipeline secundario API
- README.md

## Análisis realizado

### 1. Distribución por magnitud
images/numero de terremotos por categoria.png

## Preguntas a responder

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


# Requisitos

- Respetar la estructura organizativa del proyecto
