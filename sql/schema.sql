drop table if exists earthquakes_clean;

create table earthquakes_clean (
    id text primary key,
    time text, -- no acepta el tipo de dato datetime, por lo que se almacena como texto
    year int,
    month int,
    day int,
    latitude real, -- real en vez de float al ser el tipo de dato recomendado para números de punto flotante en SQLite
    longitude real,
    depth real,
    mag real,
    tsunami text,
    country text,
    geo_country text,
    is_ocean text,
    place text
);