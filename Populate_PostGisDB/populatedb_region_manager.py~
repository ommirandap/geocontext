import csv, sys
import populate_db_config
import populatedb_postgis_manager
from geodict_lib import *

def createRegionsTable(con):
	populatedb_postgis_manager.executeScripts(con, [populate_db_config.create_regions])

def populateRegionsTable(con):
	reader = csv.reader(open(populate_db_config.source_folder+'regions.csv', 'rb'))
	for row in reader:
		try:
			country_code = row[0]
			region_code = row[1]
			region_name = row[2]
		except:
	    		continue
		last_word, index, skipped = pull_word_from_end(region_name, len(region_name)-1, False)
		params = [region_name, country_code, region_code, last_word, country_code, region_code]
		populatedb_postgis_manager.executeScriptsWithParam(con, [populate_db_config.insert_values_regions], [params])
