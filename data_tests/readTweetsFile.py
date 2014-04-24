import sys
sys.path.append('../src')
from datetime import date, datetime, time
import json, MySQLdb, re, pprint
from dstk import DSTK

import GeoDBInteractions as geoDB

def main():

	path = '../data/'
	file_tweets = open(path + 'tweets_users_coords_and_locations_august2013.csv', 'r')
	line_anterior = 'asdf'
	for line in file_tweets:
		if line == '\n' or (line[0].isdigit() == False): 
			print 'Esta linea la ignoro: ' +  line.encode('utf8') 
			print 'Esta es la anterior' +  line_anterior.encode('utf8') 
			continue
		line_anterior = line		
		
if __name__ == '__main__':
	main()
