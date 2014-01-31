import csv, sys
import db_config
import db_manager
import sqlscripts
from geodict_lib import *

def createRegionsTable(con):
	db_manager.executeScripts(con, [sqlscripts.create_regions])

def populateRegionsTable(con):
	reader = csv.reader(open(db_config.source_folder+'regions.csv', 'rb'))
	for row in reader:
		try:
			country_code = row[0]
			region_code = row[1]
			region_name = row[2]
		except:
	    		continue
		last_word, index, skipped = pull_word_from_end(region_name, len(region_name)-1, False)
		params = [region_name, country_code, region_code, last_word, country_code, region_code]
		db_manager.executeScriptsWithParam(con, [sqlscripts.insert_values_regions], [params])
