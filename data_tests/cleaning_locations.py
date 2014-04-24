import sys
sys.path.append('../src')
from datetime import date, datetime, time
import json, MySQLdb, re, pprint
from dstk import DSTK
import LocationCleaner

import GeoDBInteractions as geoDB

def main():
	locations = open("/home/vpena/Projects/Galean/geocontext/data/locations_users/locations_vanessa.txt", "r")
	words_locations = open("/home/vpena/Projects/Galean/geocontext/data/locations_users/words_locations.txt", "w")
	coords_locations = open("/home/vpena/Projects/Galean/geocontext/data/locations_users/coords_locations.txt", "w")
	n_line = 0
	for line in locations:
		n_line += 1
		clean_location = LocationCleaner.cleanLocationField(line)
		if isinstance(clean_location, str):
			words_locations.write(str(n_line) + ',' + line)
			print "yes"
		else:			
			coords_locations.write(str(n_line) + ',' + line)
			print "no!"

if __name__ == '__main__':
	main()
