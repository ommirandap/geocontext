import csv, sys
import db_config
import db_manager
import sqlscripts

def createCitiesTable(con):
	db_manager.executeScripts(con, [sqlscripts.create_cities, sqlscripts.create_geom_cities])

def populateCitiesTable(con):
	reader = csv.reader(open(db_config.source_folder+'cities.csv', 'rb'))
	for row in reader:
		try:
			country_code = row[0]
			city_name = row[1]
			region_code = row[2]
			population = float(row[3])
			lat = row[4]
			lon = row[5]
		except:
			continue
		params = [city_name, country_code, region_code, population, 'POINT(' + lon + ' ' + lat + ')', city_name, country_code]
		db_manager.executeScriptsWithParam(con, [sqlscripts.insert_values_cities], [params])

def createBigCitiesTable(con):
	db_manager.executeScripts(con, [sqlscripts.create_big_cities, sqlscripts.create_geom_cities])

def populateBigCitiesTable(con):
	reader = csv.reader(open(db_config.source_folder+'cities.csv', 'rb'))
	for row in reader:
		try:
			city_name = row[0]
			country_code = row[1]
			country_name = row[2]
			region_code = row[3]
			region_name = row[4]
			population = float(row[5])
			lat = row[6]
			lon = row[7]
			feature_code = row[8]
		except:
			continue
		params = [city_name, country_code, country_name, region_code, region_name, population, 'POINT(' + lon + ' ' + lat + ')', city_name, country_code]
		db_manager.executeScriptsWithParam(con, [sqlscripts.insert_values_big_cities], [params])

def createClosestcityFunction(con):
	db_manager.executeScripts(con, [sqlscripts.closest_city])

def createGeometryIndex(con):
	db_manager.executeScripts(con, [sqlscripts.create_geom_index_cities])

def runVacuum(con):
	old_isolation_level = con.isolation_level
    	con.set_isolation_level(0)
	db_manager.executeScripts(con, [ sqlscripts.vacuum_analyze_cities])
	con.set_isolation_level(old_isolation_level)
