import csv, sys

# This program creates the csv files from the gazetteer from http://download.geonames.org/export/dump/


csv.field_size_limit(sys.maxsize)

source_folder = 'original_source_data/'
outcome_folder = 'source_data/'

def createCitiesCSV_ori():
	# You can use cities1000, cities15000 or cities5000
	original_file = open(source_folder + "cities5000.txt", "r")
	out_file = open(outcome_folder + "cities.csv", "w")

	for line in original_file:
		row = line.lower().split("	")
		country = row[8]
		city = row[2].replace(',', ' ')
		region_code = row[10]
		population = float(row[14])
		lat = row[4]
		lon = row[5]
		feature = row[7]
		row = country + ',' + city + ',' + region_code + ',' + str(population) + ',' + str(lat) + ',' + str(lon) + '\n'
		out_file.write(row)
	original_file.close()
	out_file.close()

def createCitiesCSV():
	# You can use cities1000, cities15000 or cities5000
	original_file = open(source_folder + "cities5000.txt", "r")
	out_file = open(outcome_folder + "cities.csv", "w")
	countries = createCountryDictionary()

	for line in original_file:
		row = line.lower().split("	")
		country_code = row[8]
		country_name = countries[country_code]
		city = row[2].replace(',', ' ')
		region_code = row[10]
		population = float(row[14])
		lat = row[4]
		lon = row[5]
		feature = row[7]
		row = city + ',' + country_code + ','  + country_name + ',' + region_code + ',' + str(population) + ',' + str(lat) + ',' + str(lon) + '\n'
		out_file.write(row)
	original_file.close()
	out_file.close()


def createCountriesPositionsCSV():
	original_file = open(source_folder + "cities5000.txt", "r")
	out_file = open(outcome_folder + "countriesPositions.csv", "w")
	for line in original_file:
		row = line.lower().split("	")
		country = row[8]
		feature_code = row[7]
		lat = row[4]
		lon = row[5]
		# If it is a capital I get the location
		if feature_code == 'pplc': 
			row = country + ',' + str(lat) + ',' + str(lon) + '\n'
			out_file.write(row)

	# UGLY WAY TO NOT LOSE A COUPLE OF LOCATIONS
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
	
	for (key, value) in country_pos.items():
		row = key + ',' + str(value[0]) + ',' + str(value[1]) + '\n'
		out_file.write(row)

	original_file.close()
	out_file.close()
	

def createCountryPosDictionary():
	reader = csv.reader(open(outcome_folder+'countriesPositions.csv', 'rb'))
	country_pos = {}
	for row in reader:
		country_pos[row[0]] = [row[1], row[2]]
	return country_pos

def createCountryDictionary():
	reader = csv.reader(open(outcome_folder+'countries.csv', 'rb'))
	countries = {}
	for row in reader:
		countries[row[0]] = row[1]
	return countries

def createRegionsCSV():
	original_file = open(source_folder + "admin1CodesASCII.txt", "r")
	out_file = open(outcome_folder + "regions.csv", "w")

	for line in original_file:
		row = line.lower().split("	")
		country_regionCode = row[0]
		region = row[2].replace(',', ' ')
		country = country_regionCode[0:2]
		region_code = country_regionCode[3:]
		row = country + ',' + region_code + ',' + region + '\n'
		out_file.write(row)
	original_file.close()
	out_file.close()


def createCountriesCSV():
	country_pos = createCountryPosDictionary()
	original_file = open(source_folder + "countryInfo.txt", "r")
	out_file = open(outcome_folder + "countries.csv", "w")
	process = False

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
		if "#ISO	ISO3	ISO-Numeric" in line:
			process = True
	original_file.close()
	out_file.close()


def getLatitudeLongitude(country_code, country_pos):
	if country_code in country_pos:
		lat_long = country_pos[country_code]
		return (lat_long[0], lat_long[1])
	else:
		return None

	
createRegionsCSV()
createCountriesPositionsCSV()
createCountriesCSV()
createCitiesCSV()
