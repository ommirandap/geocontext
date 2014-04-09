import sys
sys.path.append('../src')
from datetime import date, datetime, time
import json, MySQLdb, re, pprint
from dstk import DSTK

import GeoDBInteractions as geoDB

def main():
	connection = geoDB.getConnection()
	file_name_base = "../data/coords_and_locations_"
	files_months = ["january", "february", "march"]
	file_name_end = "2014.csv"
	output_file_name_base = "../data/comparing_locations_"
	output_file_name_end = "2014.csv"

	print "DBSK:"
	d = DSTK()
	chicago = d.coordinates2politics((41.897314250000001,-87.619115649999998)), '\n' #Chicago  IL
	print chicago
	print getCountryCodeFromDSTK(connection,chicago)

	delcambre = d.coordinates2politics((29.952500000000001,-91.990399999999994)), '\n' #Delcambre Louisiana
	print delcambre
	print getCountryCodeFromDSTK(connection,delcambre)

	toronto = d.coordinates2politics((43.484849420000003,-79.704873370000001)), '\n' #Toronto
	print toronto
	print getCountryCodeFromDSTK(connection,toronto)

	print  d.coordinates2politics((0.0,0.0)) #something


	print "My DB:"
	print geoDB.getClosestCountry(connection,41.897314250000001,-87.619115649999998)#Chicago  IL
	print geoDB.getClosestCountry(connection,29.952500000000001,-91.990399999999994)#Delcambre Louisiana
	
	print geoDB.getClosestCountry(connection,43.484849420000003,-79.704873370000001)#Toronto
	print geoDB.getClosestCountry(connection,-33.46, -70.64), '\n' #Santiago

	print geoDB.getClosestCountry(connection,37.9044774,127.0651855) #korea
	print geoDB.getClosestCountry(connection,0.0,0.0) #something
			
	print connection

def getCountryCodeFromDSTK(connection,location):
	politics = location[0][0]['politics']
	for p in politics:
		if p['friendly_type'] == 'country':
			country = geoDB.searchCountryName(connection, p['name'])
			if country is None:
				return searchCountryCodeFromRegionNameDSTK(connection,location)
			else:
				return country[0][1]

def searchCountryCodeFromRegionNameDSTK(connection,location):
	politics = location[0][0]['politics']
	for p in politics:
		if p['type'] == 'admin4':
			country = geoDB.searchCountryNameByRegionName(connection, p['name'])
			if country is None:
				return None
			else:
				return country[0][1]

def getCountryCodeFromGeoDB(location):
#	firts_coma getClosestCountry location
	print 'joli0'
if __name__ == "__main__":
	main()
