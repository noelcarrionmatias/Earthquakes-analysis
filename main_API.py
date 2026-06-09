# Importación de modulos y funciones
from src import extract
from src import transform
from src import load
import sqlite3
import pathlib
import calendar
import time
import json

# Definición de la variable con la ruta de la db
db_path = pathlib.Path(r"database\processed\earthquakes_API.db").resolve()
db_path.parent.mkdir(parents=True, exist_ok=True)

# Genera una conexión a la db y ejecuta el schema
with open("sql/schema.sql", "r") as f: # Abre schema.sql en modo lectura
    conn = sqlite3.connect(db_path) # Connexión a mi .db
    conn.executescript(f.read()) # Ejecuta el comando

# Seleccion de las mismas columnas que schema
columns_schema = [
    "id", "time", "year", "month", "day",
    "latitude", "longitude", "depth", "mag", "tsunami",
    "country", "geo_country", "is_ocean", "place"
] 

# Variable para contar cuantos registros se han cargado
total_records = 0

# Cambio de fecha automaticamente con todo el proceso ETL
for year in range(2000, 2026): 
    for month in range(1, 13):

        last_day = calendar.monthrange(year, month)[1] # Devuelve el numero de dias del año y mes. [1] selecciona solo mes. Manejo automatico de años bisiestos

        start_date = f"{year}-{month:02d}-01" # month debe tener 2 digitos. Valor esperado 2023-01-01 no 2023-1-01
        end_date = f"{year}-{month:02d}-{last_day}"

        print(f"Procesando el rango de fechas: {start_date} a {end_date}")
        
        # Proceso de importación API, transformar datos, limpiar y cargar en db SQLite
        df = extract.get_earthquakes_from_api(start_date,end_date) # Petición a la API
        
        if df is None: # Evita el fallo de la API si la consulta ha fallado
            print(f"Saltando {start_date} → {end_date}")
            continue

        if "features" not in df: # validar estructura
            print(f"Error en {start_date} → {end_date}")
            continue
                
        if df is not None: # guardar en raw_API (copia de seguridad)
            raw_path = pathlib.Path(f"database/raw_api/{year}_{month:02d}.json")
            raw_path.parent.mkdir(parents=True, exist_ok=True)

            with open(raw_path, "w") as f:
                json.dump(df, f)
                print(f"Procesando {len(df['features'])} registros") # Salida esperada: Procesando xxxx registros
                df = transform.geojson_to_dataset(df) # Convierte el geojson a dataframe
                if df.empty or 'time' not in df.columns: # Valida si el DataFrame está vacío
                            print(f"DataFrame vacío/no válidos en {start_date} → {end_date}, se salta...")
                            continue

        df = transform.add_time_features(df) # Añade las columnas year, month y day
        df = transform.add_country_column(df) # Extrae el país de la columna place. Margen de error
        df = transform.normalize_country(df) # Unifica el nombre de los países/regiones según la nueva columna creada en "add_country_column"
        df = transform.add_geospatial_features(df) # Spatial Join con la capa de limites adminsitrativos. Obtiene el nombre del país y si es Oceano/Tierra. Mayor precisión.
        df.columns = df.columns.str.lower()
        df = df.reindex(columns=columns_schema)
        df["time"] = df["time"].astype(str) # cambio de formato a str al no aceptar datetime
        df["is_ocean"] = df["is_ocean"].astype(int) # Standarizar is_ocean a 0/1
        df["tsunami"] = df["tsunami"].fillna(0).astype(int) # Standarizar tsunami a 0/1
        load.load_to_sql(df,conn) # Carga del dataframe en sql y asignamos el nombre de "earthquakes_clean". Por defecto tiene mode="append"
        print(f"{len(df)} filas cargadas") # Indica las filas que se han cargado 
        total_records += len(df)
        
        time.sleep(1) # Pausa de 1s para no saturar.

# Imprime el total de registros
print(f"Total de registros cargados: {total_records}")

# Cierra conexión
conn.close() 