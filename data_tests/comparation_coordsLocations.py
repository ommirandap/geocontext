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
	print d.coordinates2politics((41.897314250000001,-87.619115649999998)), '\n' #Chicago  IL
	print d.coordinates2politics((29.952500000000001,-91.990399999999994)), '\n' #Delcambre Louisiana
	print d.coordinates2politics((43.484849420000003,-79.704873370000001)), '\n' #Toronto

	print "mi tontera:"
	print geoDB.getClosestCity(connection,41.897314250000001,-87.619115649999998)
	print geoDB.getClosestCity(connection,29.952500000000001,-91.990399999999994)
	print geoDB.getClosestCity(connection,43.484849420000003,-79.704873370000001)
			
	print connection
	
if __name__ == "__main__":
	main()
