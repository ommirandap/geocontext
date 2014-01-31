import csv, sys
import country_manager
import region_manager

def createCitiesCSV(source_folder, outcome_folder):
	# You can use cities1000, cities15000 or cities5000
	original_file = open(source_folder + "cities5000.txt", "r")
	out_file = open(outcome_folder + "cities.csv", "w")

	# each line is defined by http://download.geonames.org/export/dump/ like this:
	# geonameid name asciiname alternatenames latitude longitude 
	# feature_class feature_code country_code cc2 admin1_code admin2_code admin3_code 
	# admin4_code population elevation dem timezone modification_date


	for line in original_file:
		row = line.lower().split("	")
		country = row[8]
		city = row[2].replace(',', ' ')
		region_code = row[10]
		population = float(row[14])
		lat = row[4]
		lon = row[5]
		feature_code = row[7]
		
		# only cities, capitals and first-order administrative division
		if feature_code == 'ppl' or feature_code == 'ppla' or feature_code == 'pplc':
			row = country + ',' + city + ',' + region_code + ',' + str(population) + ',' + str(lat) + ',' + str(lon) + '\n'
			out_file.write(row)
	original_file.close()
	out_file.close()

def createBigCitiesCSV(source_folder, outcome_folder):
	# You can use cities1000, cities15000 or cities5000
	original_file = open(source_folder + "cities5000.txt", "r")
	out_file = open(outcome_folder + "cities.csv", "w")
	countries = country_manager.createCountryDictionary(outcome_folder)
	regions = region_manager.createRegionsDictionary(outcome_folder)

	# each line is defined by http://download.geonames.org/export/dump/ like this:
	# geonameid name asciiname alternatenames latitude longitude 
	# feature_class feature_code country_code cc2 admin1_code admin2_code admin3_code 
	# admin4_code population elevation dem timezone modification_date

	for line in original_file:
		row = line.lower().split("	")
		country_code = row[8]
		country_name = countries[country_code]
		city = row[2].replace(',', ' ')
		if city == '':
			city = row[3].replace(',', ' ')
		region_code = row[10]
		if country_code in regions and region_code in regions[country_code]:
			region_name = regions[country_code][region_code]
		else: 
			region_name = ''
		population = float(row[14])
		lat = row[4]
		lon = row[5]
		feature_code = row[7]

		# only cities, capitals and first-order administrative division
		if feature_code == 'ppl' or feature_code == 'ppla' or feature_code == 'pplc':
			#print line
			#break
			row = city + ',' + country_code + ','  + country_name + ',' + region_code + ',' + region_name + ',' + str(population) + ',' + str(lat) + ',' + str(lon) + ',' + feature_code + '\n'
			out_file.write(row)

	original_file.close()
	out_file.close()

