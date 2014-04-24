import sys
sys.path.append('../src')
from datetime import date, datetime, time
import json, MySQLdb, re, pprint
from dstk import DSTK
from os import listdir
from os.path import isfile, join
import GeoDBInteractions as geoDB

def main():

	path = '/home/vpena/Projects/Galean/geocontext/data/locations_users/'
	merged = open(path + 'proc_locations_vanessa.txt', 'r')
	n_lines = 0
	for l in merged:
		n_lines += 1 
	print n_lines
		

def joinLocations():
	path = '/home/vpena/Projects/Galean/geocontext/data/locations_users/locations/'
	only_files = [f for f in listdir(path) if isfile(join(path, f))]
	only_files.sort()
	print only_files
	big_locations = open(path + 'proc_words_locations.txt', 'w')
	for f in only_files:
		splitted_loc = open(path + f, 'r')
		for line in splitted_loc:
			big_locations.write(line)

def mergeFiles():
	path = '/home/vpena/Projects/Galean/geocontext/data/locations_users/'
	proc_w_loc = open(path + 'proc_words_locations.txt', 'r')
	proc_c_loc = open(path + 'proc_coords_locations.txt', 'r')
	ori_loc = open(path + 'locations_vanessa.txt', 'r')
	merged = open(path + 'proc_locations_vanessa.txt', 'w')
	n_line = 0
	for l in ori_loc:
		n_line += 1

	print n_line
	n_line_c = 1
	w_line = proc_w_loc.readline()
	c_line = proc_c_loc.readline()
	while n_line_c <= 1656419:
		while(w_line == 'NONE\n'):
			w_line = proc_w_loc.readline()		
		while(c_line == 'NONE\n'):
			c_line = proc_c_loc.readline()
		#print w_line
		#print c_line
		if w_line != '':
			w_coma = w_line.index(',')
			w_n_line = float(w_line[:w_coma])
		if c_line != '':
			c_coma = c_line.index(',')	
			c_n_line = float(c_line[:c_coma])

		if (w_n_line == n_line_c):
			merged.write(w_line)
			w_line = proc_w_loc.readline()
		elif (c_n_line == n_line_c):
			merged.write(c_line)
			c_line = proc_c_loc.readline()
		else:
			merged.write(str(n_line_c) + ',NONE\n')
		n_line_c += 1
if __name__ == '__main__':
	main()
