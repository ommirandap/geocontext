import sys
sys.path.append('../src')
from datetime import date, datetime, time
import json, MySQLdb, re, pprint
from dstk import DSTK

import GeoDBInteractions as geoDB

def main():
	connection = geoDB.getConnection()
	#files_months = ['january', 'february', 'march']
	files_months = ['september']
	path = '../data/'
	comparing_locations_name_base = 'comparing_locations_try_2'
	comparing_locations_name_end = '2013.csv'

	output_file_name_base = 'compared_statistics_try_2_september2013.txt'
	total_records = 0
	equals_mydb_dstk = 0
	equals_extracted_mydb = 0
	equals_extracted_dstk = 0
	empty_locations = 0
	nulls_locations = 0

	for month in files_months:
		compared_locations = open(path + comparing_locations_name_base + month + comparing_locations_name_end, 'r')
		for line in compared_locations:
			data = line[:-1].split(',')

			code_dstk = data[6]			
			code_mydb = data[7]
			code_extracted = data[8]
			if code_mydb == code_dstk:
				equals_mydb_dstk += 1

			if code_mydb == code_extracted:
				equals_extracted_mydb += 1

			if code_dstk == code_extracted:
				equals_extracted_dstk += 1
			if code_extracted == 'null' or code_extracted == 'NONE' or code_extracted == 'None':
				nulls_locations += 1

			if data[5] == "":
				empty_locations += 1

			total_records += 1

	output = open(path + output_file_name_base, 'w')
	output.write('Total records: ' + str(total_records) + '\n')
	output.write('equals_mydb_dstk: ' + str(equals_mydb_dstk) + '\n')
	output.write('equals_extracted_mydb: ' + str(equals_extracted_mydb) + '\n')
	output.write('equals_extracted_dstk: ' + str(equals_extracted_dstk) + '\n')
	output.write('Empty locations: ' + str(empty_locations) + '\n')
	output.write('Null locations: ' + str(nulls_locations) + '\n')
if __name__ == '__main__':
	main()
