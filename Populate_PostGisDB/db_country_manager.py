import csv, sys
import db_config
import db_manager
import sqlscripts
from geodict_lib import *

def createCountriesTable(con):
	db_manager.executeScripts(con, [sqlscripts.create_countries, sqlscripts.create_geom_countries])

def populateCountriesTable(con):
	reader = csv.reader(open(db_config.source_folder+'countries.csv', 'rb'))
	for row in reader:
		try:
			country_code = row[0]
			country_name = row[1]
			population = float(row[2])
			continent = row[3]
			lat = row[4]
			lon = row[5]
		except:
			continue

		country_name = country_name.strip()            
		last_word, index, skipped = pull_word_from_end(country_name, len(country_name)-1, False)
		params = [country_name, country_code, population, continent, last_word]
		if lat == '':
			params.append(None)
		else:
			params.append('POINT(' + lon + ' ' + lat + ')')
		db_manager.executeScriptsWithParam(con, [sqlscripts.insert_values_countries], [params])
