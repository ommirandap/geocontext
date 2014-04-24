import sys
sys.path.append('../src')
from datetime import date, datetime, time
import json, MySQLdb, re, pprint
from dstk import DSTK
import LocationCleaner
from GeoPoint import GeoPoint

import GeoDBInteractions as geoDB

def main():

	connection = geoDB.getConnection()
	coords_locations = open("/home/vpena/Projects/Galean/geocontext/data/locations_users/coords_locations.txt", "r")
	proc_coords_locations = open("/home/vpena/Projects/Galean/geocontext/data/locations_users/proc_coords_locations.txt", "w")
	for line in coords_locations:
		coma = line.index(',')
		n_line = line[:coma]
		coords = line[coma+1:]
		clean_location = LocationCleaner.cleanLocationField(coords)
		print coords
		print clean_location
		#if isinstance(clean_location, GeoPoint()):
		if type(clean_location) == type(GeoPoint((0,0))):
			lat = clean_location.getLatitude()
			lon = clean_location.getLongitude()
			my_c_code = geoDB.getClosestCountry(connection, lat, lon)
			proc_coords_locations.write(n_line + ',' + str(my_c_code) + '\n')
		else:
			proc_coords_locations.write(n_line + ',NONE\n')

if __name__ == '__main__':
	main()
