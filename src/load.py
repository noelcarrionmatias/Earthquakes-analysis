import sqlite3
import pathlib

def create_dir(db_path): 
    try:
        path = pathlib.Path(db_path)
        path.parent.mkdir(parents=True, exist_ok=True) # parent crea los directorios padre y exist_ok evita error si ya existe el directorio
        return path
    except Exception as e:
        print(f"Error: {e}")


def load_to_sql(df, conn, mode="append"): # definimos mode="append" por si hay más de 1 df de carga y no lo borre con replace
    try:
        df.to_sql(name="earthquakes_clean", 
                  con=conn,
                  if_exists=mode, # append predefinido
                  index=False,
                  chunksize=1000) # bloques de 1000
        
    except Exception as e:
        print(f"Error en load_to_sql: {e}")