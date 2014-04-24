import sys
sys.path.append('../src')
from datetime import date, datetime, time
import json, MySQLdb, re, pprint
from dstk import DSTK
import LocationCleaner
import GeoDBInteractions as geoDB

from os import listdir
from os.path import isfile, join



def main():
	path = '/home/vpena/Projects/Galean/geocontext/data/Coords_locations_tweets/'
	only_files = [f for f in listdir(path) if isfile(join(path, f))]
	for f in only_files:
		coords_tweets = open(path + f, 'r')
		only_idtweets_country_code = open(path + 'only_coords_tweets' + f, 'w')
		for line in coords_tweets:
			data = line.split(',')
			tweet_id = data[1]
			my_c_code = data[7]
#			print line
			only_idtweets_country_code.write(tweet_id + ',' + my_c_code + '\n')


if __name__ == '__main__':
	main()
