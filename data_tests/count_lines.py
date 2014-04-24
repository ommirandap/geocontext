import sys
sys.path.append('../src')
from datetime import date, datetime, time
import json, MySQLdb, re, pprint
from dstk import DSTK
from os import listdir
from os.path import isfile, join
import GeoDBInteractions as geoDB

def main():

	countLines("/home/vpena/Projects/Galean/geocontext/data/tweets/extracted_locs_2013/", "extracted_only_text_ids_and_tweets_april2014.csv")

def countLines(path, file_name):
	tweets = open(path + file_name, 'r')
	n_lines = 0
	for l in tweets:
		n_lines += 1 
	print n_lines
def countAll():
	path = '/home/vpena/Projects/Galean/geocontext/data/tweets/ids_and_tweets_2013/'
	only_files = [f for f in listdir(path) if isfile(join(path, f))]
	n_lines_total = 0
	for f in only_files:
		n_lines = 0
		file_tweets = open(path + f, 'r')
		for line in file_tweets:
			n_lines += 1
		print f , ' n_lines =' , str(n_lines)
		n_lines_total += n_lines	
		
if __name__ == '__main__':
	main()
