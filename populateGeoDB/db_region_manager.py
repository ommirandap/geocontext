import csv, sys
import db_config
import db_manager
import sqlscripts

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
		params = [region_name, country_code, region_code, country_code, region_code]
		db_manager.executeScriptsWithParam(con, [sqlscripts.insert_values_regions], [params])
