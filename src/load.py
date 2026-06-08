import sqlite3
import pathlib

def create_dir(db_path): 
    try:
        path = pathlib.Path(db_path)
        path.parent.mkdir(parents=True, exist_ok=True) # parent crea los directorios padre y exist_ok evita error si ya existe el directorio
        return path
    except Exception as e:
        print(f"Error: {e}")


def load_to_sql(df, db_path, mode="append"): # definimos mode="append" por si hay más de 1 df de carga y no lo borre con replace
    try:
        create_dir(db_path)
        with sqlite3.connect(db_path) as conn:
            df.to_sql(name="earthquakes_clean", con=conn,if_exists=mode, index=False)
        
    except Exception as e:
        print(f"Error en la conexión al .db: {e}")