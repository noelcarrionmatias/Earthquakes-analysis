from src import extract
from src import transform
from src import load
import sqlite3
import pathlib

data_csv = pathlib.Path(r"database\raw").resolve()
db_path = pathlib.Path(r"database\earthquakes_csv.db").resolve()


with open("sql/schema.sql", "r") as f: # Abre schema.sql en modo lectura
    conn = sqlite3.connect(db_path) # Connexión a mi .db
    conn.executescript(f.read()) # Ejecuta el comando
    

columns_schema = [
    "id", "time", "year", "month", "day",
    "latitude", "longitude", "depth", "mag",
    "country", "geo_country", "is_ocean", "place"
] # Seleccion de las mismas columnas que schema

total_records = 0

# Por cada archivo csv: 
for csv in data_csv.glob("*.csv"): # Devuelve exclusivamente archivos CSV
    print(f"Procesando {csv}") # Dime que archivo estas procesando       
    df = extract.load_csv(csv) # Lee el archivo .csv
    df = transform.add_time_features(df) # Añade las columnas year, month y day
    df = transform.add_country_column(df) # Extrae el país de la columna place. Margen de error
    df = transform.normalize_country(df) # Unifica el nombre de los países/regiones según la nueva columna creada en "add_country_column"
    df = transform.add_geospatial_features(df) # Spatial Join con la capa de limites adminsitrativos. Obtiene el nombre del país y si es Oceano/Tierra. Mayor precisión.
    df.columns = df.columns.str.lower()
    df = df[columns_schema]
    load.load_to_sql(df,conn) # Carga del dataframe en sql y asignamos el nombre de "earthquakes_clean". Por defecto tiene mode="append"
    print(f"{len(df)} filas cargadas") # Indica las filas que se han cargado 
    total_records += len(df)

# Imprime el total de registros
print(f"Total de registros cargados: {total_records}")

conn.close() # Cierra conexión