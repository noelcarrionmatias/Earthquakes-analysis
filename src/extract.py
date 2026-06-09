import pandas as pd
import requests

def get_earthquakes_from_api(start_date, end_date):
    
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query" # Base de la API
    
    params = { # Definidos los parametros necesarios según la docu de API
        "format": "geojson",
        "starttime": start_date,
        "endtime": end_date,
        "minmagnitude": 0,
        "orderby": "time"
    }
    try:
        response = requests.get(url, params=params, timeout=30) # Devuelve la url + parametros

        # comprobar status
        if response.status_code != 200:
            print(f"Error API ({response.status_code}) en {start_date}")
            return None

        # comprobar contenido vacío
        if not response.text:
            print(f"Respuesta vacía en {start_date}")
            return None

        # intentar parsear JSON seguro
        return response.json()

    except Exception as e:
        print(f"Error en request en {start_date}: {e}")
        return None


def load_csv(filepath):
        df = pd.read_csv(filepath)
        return df