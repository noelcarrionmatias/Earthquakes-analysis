from src import extract
from src import transform
from src import load
import sqlite3
import pathlib
import pandas as pd

conn = sqlite3.connect(r"C:\Users\BICAMANO\Documents\Earthquakes-analysis\database\earthquakes.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS earthquakes_clean")

data_csv = input(r"Introduce la ruta donde estan los archivos .CSV: ")
data_csv = pathlib.Path(data_csv).resolve()
db_path = input(r"Introduce la ruta de la base de datos SQLite: ")
db_path = pathlib.Path(db_path).resolve()

# Por cada archivo csv: 
for csv in data_csv.glob("*.csv"): # Devuelve exclusivamente archivos CSV
    print(f"Procesando {csv}") # Dime que archivo estas procesando
    df = extract.load_csv(csv) # Lee el archivo .csv
    df = transform.add_time_features(df) # Añade las columnas year, month
    #df = transform.extract_site_from_place(df)
    df = transform.add_country_column(df)
    df = transform.normalize_country(df)
    transform.add_geospatial_features
    load.load_to_sql(df,db_path)
