import pathlib

def filepath_correct(directorio):
    if not pathlib.Path(directorio).isdir():
        return False
    return True

def create_dir(db_path): 
    try:
        path = pathlib.Path(db_path)
        path.parent.mkdir(parents=True, exist_ok=True) # parent crea los directorios padre y exist_ok evita error si ya existe el directorio
        return path
    except Exception as e:
        print(f"Error: {e}")