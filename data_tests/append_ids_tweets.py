import sys
sys.path.append('../src')
from datetime import date, datetime, time
import json, MySQLdb, re, pprint
from dstk import DSTK
from os import listdir
from os.path import isfile, join
import GeoDBInteractions as geoDB
import re
def main():

	path_locations = '/home/vpena/Projects/Galean/geocontext/data/tweets/extracted_loc_test/'
	path_original = '/home/vpena/Projects/Galean/geocontext/data/tweets/ids_and_tweets_2013/'
	path_ids_locations = '/home/vpena/Projects/Galean/geocontext/data/tweets/ids_and_locations/'
	base_filename_locations = 'extracted_only_text_ids_and_tweets_'
	base_filename_original = 'ids_and_tweets_'
	base_filename_output = 'idstweets_and_locations_'

	only_files = [f for f in listdir(path_locations) if isfile(join(path_locations, f))]

	for f in only_files:
		date_and_year = f[len(base_filename_locations):]
		original_file_name = base_filename_original + date_and_year
		locations_file = open(path_locations + f)
		original_file = open(path_original + original_file_name)
		output_file = open(path_ids_locations + base_filename_output + date_and_year, 'w')
		for line in locations_file:
			ori_line = original_file.readline()
			id_tweet = ori_line.split('***,***')[0]
			output_file.write(id_tweet + '***,***' + line )
		

if __name__ == '__main__':
	main()
