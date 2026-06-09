---------------------------------
-- Distribución terremotos
---------------------------------
select zona , count(*) as total
from earthquakes_clean
where zona is not null
group by zona
order by total desc;
---------------------------------
-- Ranking por países
---------------------------------
select geo_country, count(*) as total
from earthquakes_clean
where geo_country is not null
and geo_country is not "Ocean"
group by geo_country
order by total desc
limit 10;
---------------------------------
-- Ranking por países >4 mag
---------------------------------
select geo_country, count(*) as total
from earthquakes_clean
where geo_country is not null
and mag > 4
and geo_country is not "Ocean"
group by geo_country
order by total desc
limit 10;
---------------------------------
-- Evolución temporal (anual)
---------------------------------
select year, count(*) as total
from earthquakes_clean
group by year
order by year;
---------------------------------
-- Clasificación por magnitud
---------------------------------
select 
    CASE 
        WHEN mag < 2 THEN 'Micro'
        WHEN mag >= 2 and mag < 4 THEN 'Menor'
        WHEN mag >= 4 and mag < 6 THEN 'Moderado'
        ELSE THEN 'Fuerte'
    END AS Category,
    count(*) as N_earthquakes
from earthquakes_clean
group by Category
order by mag;
---------------------------------
-- Validar datos (country vs geo_country)
---------------------------------
select 
    case 
        when country = geo_country then 'equal'
        else then 'not equal'
    end as Validation,
    count(*) as Total
from earthquakes_clean
group by Validation;