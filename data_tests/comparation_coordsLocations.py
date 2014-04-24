import sys
sys.path.append('../src')
from datetime import date, datetime, time
import json, MySQLdb, re, pprint
from dstk import DSTK

import GeoDBInteractions as geoDB

def main():
	connection = geoDB.getConnection()
	#files_months = ['january', 'february', 'march']
	#files_months = ['february']
	files_months = ['september', 'october', 'november', 'december']
	path = '../data/'
	coords_locations_name_base = 'coords_and_locations_'
	coords_locations_name_end = '2013.csv'
	
	extracted_locations_name_base = 'ext_locations_fromcoords_and_locations_'
	extracted_locations_name_end = '2013.csv'
	
	output_file_name_base = 'comparing_locations_try_2'
	output_file_name_end = '2013.csv'

	d = DSTK()

	for month in files_months:
		print 'estoy procesando ' + month
		coords_locations = open(path + coords_locations_name_base + month + coords_locations_name_end, 'r')
		extracted_locations = open(path + extracted_locations_name_base + month + extracted_locations_name_end, 'r')
		output = open(path + output_file_name_base + month + output_file_name_end, 'w')
		for line in coords_locations:
			extracted_country_code = extracted_locations.readline()
			if line == '\n' or (line[0].isdigit() == False): 
				print 'Esta linea la ignore: ' +  line.encode('utf8') 
				continue			
			
			last_comma = line.rfind(',')
			location = line[last_comma+1:]
			data = line.split(',')
			lat = float(data[3])
			lon = float(data[2])
			dstk_location = d.coordinates2politics((lat,lon))
			dstk_c_code = getCountryCodeFromDSTK(connection, dstk_location)


			my_c_code = geoDB.getClosestCountry(connection, lat, lon)

			output.write(line[:-1] + ',' + str(dstk_c_code) + ',' + str(my_c_code) + ',' +  extracted_country_code)
	
def getCountryCodeFromDSTK(connection,location):
	#print 'location 01: ', location
	politics = location[0]['politics']
	if politics is None: return None
	for p in politics:
		if p['friendly_type'] == 'country':
			country = geoDB.searchCountryName(connection, p['name'])
			if country is None or len(country) == 0:
				country_by_region = geoDB.searchCountryNameByRegionCode(connection, p['code'])
				if country_by_region is None or len(country_by_region) == 0:
					return searchCountryCodeFromRegionNameDSTK(connection,location)
				else:
					return country_by_region[0][1]
			else:
				return country[0][1]

def searchCountryCodeFromRegionNameDSTK(connection,location):
	politics = location[0]['politics']
	for p in politics:
		if p['type'] == 'admin4':
			country = geoDB.searchCountryNameByRegionName(connection, p['name'])
			if country is None or len(country) == 0:
				return searchCountryCodeFromCityNameDSTK(connection,location)
			else:
				return country[0][1]

def searchCountryCodeFromCityNameDSTK(connection,location):
	politics = location[0]['politics']
	for p in politics:
		if p['friendly_type'] == 'city':
			country = geoDB.searchCountryNameByCityName(connection, p['name'])
			if country is None or len(country) == 0:
				return None
			else:
				return country[0][1]
if __name__ == '__main__':
	main()
