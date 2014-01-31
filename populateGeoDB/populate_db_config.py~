#CONSIDER POSTGIS USE (longitude, latitude) ORDER TO CREATE GEOMETRY POINTS

# The location of the source data to be loaded into your database
source_folder = 'source_data/'

# Your MySQL user credentials
user = 'galean'
password = '1234'

# The address and port number of your database server
host = 'localhost'
port = 0

# The name of the database to create
database = 'geodict2'

###### SQL scripts ######
# Countries
create_countries = "CREATE TABLE IF NOT EXISTS countries( country VARCHAR(64), PRIMARY KEY(country), country_code CHAR(2), population INT, continent CHAR(2), last_word VARCHAR(32));"
create_geom_countries = "SELECT AddGeometryColumn ('public', 'countries','lon_lat',4326,'POINT',2);"
insert_values_countries = "INSERT INTO countries (country, country_code, population, continent, last_word, lon_lat) values (%s, %s, %s, %s, %s, ST_GeomFromText(%s, 4326))"

# Regions

create_regions = """CREATE TABLE IF NOT EXISTS regions (
			        region VARCHAR(500),
				region_code char(15),
			        country CHAR(2),
			        PRIMARY KEY(region_code, country),
			        last_word VARCHAR(250)); """

insert_values_regions = """INSERT INTO regions (region, country, region_code,last_word)
				 SELECT %s, %s, %s, %s WHERE NOT EXISTS 
				 (SELECT region FROM regions WHERE country=%s and region_code = %s); """

# Cities
create_cities = """CREATE TABLE IF NOT EXISTS cities (city VARCHAR(500),
					country CHAR(2), 
					PRIMARY KEY(city, country), 
					region_code CHAR(15),     
					population INT, 
					last_word VARCHAR(250)); """

create_cities_2 = """CREATE TABLE IF NOT EXISTS cities (city VARCHAR(500),
					country_code CHAR(2),
					country_name varchar(64),  
					PRIMARY KEY(city, country_code), 
					region_code CHAR(15),    
				        region VARCHAR(500), 
					population INT, 
					last_word VARCHAR(250)); """

create_geom_cities = "SELECT AddGeometryColumn ('public', 'cities','lon_lat',4326,'POINT',2);"

insert_values_cities = """INSERT INTO cities (city, country, region_code, population, last_word, lon_lat)
				 SELECT %s, %s, %s, %s, %s, ST_GeomFromText(%s, 4326) WHERE NOT EXISTS 
				 (SELECT city FROM cities WHERE city=%s and country = %s); """

insert_values_cities_2 = """INSERT INTO cities (city, country_code, country_name, region_code, region, population, last_word, lon_lat)
				 SELECT %s, %s, %s, %s, %s, %s, %s, ST_GeomFromText(%s, 4326) WHERE NOT EXISTS 
				 (SELECT city FROM cities WHERE city=%s and country_code = %s); """

closest_city = """CREATE OR REPLACE FUNCTION closestcity(double precision, double precision, double precision, integer DEFAULT 10)
				RETURNS TABLE ( city varchar(500), country char(2), region_code char(15), distance  float ) AS
				$BODY$;
				SELECT city, country, region_code, ST_Distance_Sphere(cities.lon_lat, ST_MakePoint($1, $2)) as distance
				FROM "cities"
				WHERE ST_Distance_Sphere(cities.lon_lat, ST_MakePoint($1, $2)) <= $3 * 1609.34
				ORDER by distance
				LIMIT $4;
				$BODY$
				LANGUAGE sql VOLATILE
				COST 100
				ROWS 1000;
				ALTER FUNCTION closestcity(double precision, double precision, double precision, integer)
				OWNER TO galean;"""

create_geom_index_cities = "CREATE INDEX lon_lat_index ON cities USING GIST (lon_lat);"

vacuum_analyze_cities = "VACUUM ANALYZE cities;"



