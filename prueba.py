import geopandas as gpd
from src import transform

transform.add_geospatial_features()

world = gpd.read_file(r"C:\Users\BICAMANO\Documents\Earthquakes-analysis\database\geoespatial\ne_10m_admin_0_countries\ne_10m_admin_0_countries.shp",crs="epsg=4326") # Lee la capa del mundo con proyecion epsg=3857
