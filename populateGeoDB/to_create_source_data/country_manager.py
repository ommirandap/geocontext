import csv, sys

def createCountriesPositionsCSV(source_folder, outcome_folder):
	original_file = open(source_folder + "cities5000.txt", "r")
	out_file = open(outcome_folder + "countriesPositions.csv", "w")

	# each line is defined by http://download.geonames.org/export/dump/ like this:
	# geonameid name asciiname alternatenames latitude longitude 
	# feature_class feature_code country_code cc2 admin1_code admin2_code admin3_code 
	# admin4_code population elevation dem timezone modification_date

	for line in original_file:
		row = line.lower().split("	")
		country_code = row[8]
		feature_code = row[7]
		lat = row[4]
		lon = row[5]

		# If it is a capital I get the location
		# feature codes descriptions are here http://www.geonames.org/export/codes.html

		if feature_code == 'pplc': 
			row = country_code + ',' + str(lat) + ',' + str(lon) + '\n'
			out_file.write(row)


	country_pos = getExtraCountryLocations()
	for (country_code, lat_lon) in country_pos.items():
		row = country_code + ',' + str(lat_lon[0]) + ',' + str(lat_lon[1]) + '\n'
		out_file.write(row)

	original_file.close()
	out_file.close()

def getExtraCountryLocations():

	# UGLY WAY TO NOT LOSE A COUPLE OF LOCATIONS
	# each item in country_pos is: {country_code : [lat, lon]}

	country_pos = {}
	country_pos['AQ'] = [-90.0000, 0.0000]
	country_pos['BV'] = [-54.4333,3.4000]
	country_pos['HM'] = [-53.1000,72.5167]
	country_pos['IL'] = [31.5000,34.7500]
	country_pos['IO'] = [-6.0000,71.5000]
	country_pos['NR'] = [-0.5333,166.9167]
	country_pos['PS'] = [32.0000,35.2500]
	country_pos['TK'] = [-9.0000,-172.0000]
	country_pos['UM'] = [19.2833,166.6000]
	country_pos['AN'] = [12.2500,-68.7500]
	return country_pos

def createCountriesCSV(source_folder, outcome_folder):

	country_pos = createCountryPosDictionary(outcome_folder)
	original_file = open(source_folder + "countryInfo.txt", "r")
	out_file = open(outcome_folder + "countries.csv", "w")
	process = False

	# each line is defined like:
	# ISO ISO3 ISO-Numeric fips Country Capital Area(in sq km) Population Continent tld 
	# CurrencyCode CurrencyName Phone Postal Code Format Postal Code Regex Languages 
	# geonameid neighbours EquivalentFipsCode

	for line in original_file:
		if process:
			row = line.lower().split("	")
			country_code = row[0]
			country_name = row[4]
			population = row[7]
			continent = row[8]
			lat_lon = getLatitudeLongitude(country_code, country_pos)
			row = country_code + ',' + country_name + ',' + population + ',' + continent
			if lat_lon is not None:
				row += ',' + str(lat_lon[0]) + ',' + str(lat_lon[1]) + '\n'
			else:
				row += ',,\n'
			out_file.write(row)
		# only start processing when the head of the file inds
		if "#ISO	ISO3	ISO-Numeric" in line:
			process = True
	original_file.close()
	out_file.close()

def createCountryPosDictionary(base_folder):
	reader = csv.reader(open(base_folder+'countriesPositions.csv', 'rb'))
	country_pos = {}
	# each row is: country_code, lat, lon
	for row in reader:
		country_pos[row[0]] = [row[1], row[2]]
	return country_pos

def createCountryDictionary(base_folder):
	reader = csv.reader(open(base_folder+'countries.csv', 'rb'))
	countries = {}
	# each row is: country_code, country_name, population, continent, lat, lon
	for row in reader:
		countries[row[0]] = row[1]
	return countries

def getLatitudeLongitude(country_code, country_pos):
	if country_code in country_pos:
		lat_long = country_pos[country_code]
		return (lat_long[0], lat_long[1])
	else:
		return None
