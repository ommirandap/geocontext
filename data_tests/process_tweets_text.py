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

	getOnlytextfolder()

def getOnlytext():
	path = '/home/vpena/Projects/Galean/geocontext/data/tweets/'
	tweets = open(path + 'ids_and_tweets_august2013.csv', 'r')
	only_text_tweets = open(path + 'only_text_tweets_august2013.csv', 'w')

	for line in tweets:
		if line == '\n': continue
		data = line.split('***,***')
		#print data
		text = data[1]
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
		for u in urls:
			text = text.replace(u, " ")
		only_text_tweets.write(text )

def getOnlytextfolder():
	path_input = '/home/vpena/Projects/Galean/geocontext/data/tweets/ids_and_tweets_2013/'
	path_output = '/home/vpena/Projects/Galean/geocontext/data/tweets/only_tweets_2013/'

	only_files = [f for f in listdir(path_input) if isfile(join(path_input, f))]
	for f in only_files:
		tweets = open(path_input + f, 'r')
		only_text_tweets = open(path_output + 'only_text_' + f, 'w')

		for line in tweets:
			if line == '\n': continue
			data = line.split('***,***')
			#print line
			text = data[1]
			#urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
			#for u in urls:
			#	text = text.replace(u, " ")
			only_text_tweets.write(text )


def countLines(path, file_name):
	#path = '/home/vpena/Projects/Galean/geocontext/data/tweets/'
	tweets = open(path + file_name, 'r')
	n_lines = 0
	for l in tweets:
		n_lines += 1 
	print n_lines
		

if __name__ == '__main__':
	main()
