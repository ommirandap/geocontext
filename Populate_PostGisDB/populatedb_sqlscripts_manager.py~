import populate_db_config

# Countries
create_countries = "CREATE TABLE IF NOT EXISTS countries( country_name VARCHAR(64), PRIMARY KEY(country), country_code CHAR(2), population INT, continent CHAR(2), last_word VARCHAR(32));"
create_geom_countries = "SELECT AddGeometryColumn ('public', 'countries','lon_lat',4326,'POINT',2);"
insert_values_countries = "INSERT INTO countries (country_name, country_code, population, continent, last_word, lon_lat) values (%s, %s, %s, %s, %s, ST_GeomFromText(%s, 4326))"

# Regions

create_regions = """CREATE TABLE IF NOT EXISTS regions (
			        region_name VARCHAR(500),
				region_code char(15),
			        country_code CHAR(2),
			        PRIMARY KEY(region_code, country_code),
			        last_word VARCHAR(250)); """

insert_values_regions = """INSERT INTO regions (region_name, country_code, region_code,last_word)
				 SELECT %s, %s, %s, %s WHERE NOT EXISTS 
				 (SELECT region_name FROM regions WHERE country_code=%s and region_code = %s); """

# Cities
create_cities = """CREATE TABLE IF NOT EXISTS cities (city VARCHAR(500),
					country_code CHAR(2), 
					PRIMARY KEY(city, country_code), 
					region_code CHAR(15),     
					population INT, 
					last_word VARCHAR(250)); """

create_big_cities = """CREATE TABLE IF NOT EXISTS cities (city_name VARCHAR(500),
					country_code CHAR(2),
					country_name varchar(64),  
					PRIMARY KEY(city, country_code), 
					region_code CHAR(15),    
				        region_name VARCHAR(500), 
					population INT, 
					last_word VARCHAR(250)); """

create_geom_cities = "SELECT AddGeometryColumn ('public', 'cities','lon_lat',4326,'POINT',2);"

insert_values_cities = """INSERT INTO cities (city_name, country_code, region_code, population, last_word, lon_lat)
				 SELECT %s, %s, %s, %s, %s, ST_GeomFromText(%s, 4326) WHERE NOT EXISTS 
				 (SELECT city_name FROM cities WHERE city_name=%s and country_code = %s); """

insert_values_big_cities_ = """INSERT INTO cities (city_name, country_code, country_name, region_code, region_name, population, last_word, lon_lat)
				 SELECT %s, %s, %s, %s, %s, %s, %s, ST_GeomFromText(%s, 4326) WHERE NOT EXISTS 
				 (SELECT city_name FROM cities WHERE city_name=%s and country_code = %s); """

closest_city = """CREATE OR REPLACE FUNCTION closestcity(double precision, double precision, double precision, integer DEFAULT 10)
				RETURNS TABLE ( city_name varchar(500), country_code char(2), region_code char(15), distance  float ) AS
				$BODY$;
				SELECT city_name, country_code, region_code, ST_Distance_Sphere(cities.lon_lat, ST_MakePoint($1, $2)) as distance
				FROM "cities"
				WHERE ST_Distance_Sphere(cities.lon_lat, ST_MakePoint($1, $2)) <= $3 * 1609.34
				ORDER by distance
				LIMIT $4;
				$BODY$
				LANGUAGE sql VOLATILE
				COST 100
				ROWS 1000;
				ALTER FUNCTION closestcity(double precision, double precision, double precision, integer)
				OWNER TO """ + populate_db_config.user + ";"

create_geom_index_cities = "CREATE INDEX lon_lat_index ON cities USING GIST (lon_lat);"

vacuum_analyze_cities = "VACUUM ANALYZE cities;"



