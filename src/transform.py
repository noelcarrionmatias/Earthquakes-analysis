import pandas as pd
import geopandas as gpd


def add_time_features(df):
    df['dates'] = pd.to_datetime(df["time"],errors='coerce',utc=True) # to_datetime devuelve el string en un formato fecha.
    df["year"] = df["dates"].dt.year
    df["month"] = df["dates"].dt.month
    df["day"] = df["dates"].dt.day
    df["hour"] = df["dates"].dt.hour
    return df

def extract_country_from_place(place):
    if pd.isna(place): # pd.isna(value) si es nulo o no
        return "Unknown"
    if "," in place:
        return place.split(",")[-1].strip()
    return place

def add_country_column(df):
    df["country"] = df["place"].apply(extract_country_from_place) # apply es un loop automatico: por cada fila de df["place"] aplica la formula extract_country_from_place 
    return df

def normalize_country(df):
    mapping = {
        "Alaska": "United States",
        "Hawaii": "United States",
        "CA": "United States",
        "Puerto Rico": "United States"
    }
    df["country"] = df["country"].replace(mapping) # Itera sobre df["country"] y si es igual que mapping lo reemplaza
    return df

def add_geospatial_features(df):
    gdf = gpd.GeoDataFrame(df, gpd.points_from_xy(df["longitude"],df["latitude"]),crs="EPSG=4326") # Crear un geodataframe a partir de lon y lat del df con proyeccion epsg=3857
    world = gpd.read_file(r"C:\Users\BICAMANO\Documents\Earthquakes-analysis\database\geoespatial\ne_10m_admin_0_countries\ne_10m_admin_0_countries.shp") # Lee la capa del mundo con proyecion epsg=3857
    gdf = gdf.to_crs(epsg=3857) # Reproyectar capa al 3857
    world = world.to_crs(epsg=3857) # Reproyectar capa al 3857
    result = gpd.sjoin(gdf, world,how='left',predicate="within") # Creamos un espatial join de gdf y world
    return result






