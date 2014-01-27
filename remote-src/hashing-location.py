#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import string, re
from string import maketrans
from operator import itemgetter

""" Function declarations """
""""""""""""""""""""""""""""""""""""""""""""""""""""""

COORD_REGEX = re.compile('([-+]?)([\d]{1,2})(((\.)(\d+)(,)))(\s*)(([-+]?)([\d]{1,3})((\.)(\d+))?)')
STRICT_COORD_REGEX = re.compile('^(([-+]?[\d]{1,2}(\.)(\d+))((,)(\s*))(([-+]?)([\d]{1,3})(\.)(\d+)))')

def punctuationToSpace(word):
	before_table = string.punctuation
	after_table =  "                                " # 32 spaces
	translation_table = maketrans(before_table, after_table)
	return word.translate(translation_table)

def reduceSpaces(word):
	return re.sub('\s+', ' ', word)

def normalize(word):
	str1 = punctuationToSpace(word)
	str2 = reduceSpaces(str1)
	str3 = string.lower(str2)
	str4 = str3.strip()
	return str4

def onlyNumbers(word):
	match = re.search('[a-zA-Z]', word)
	if match:	return False
	else:		return True

def isCoordinates(word):
	match = COORD_REGEX.search(word)
	if match:	return True
	else:		return False

def deleteTextFromWord(word):
	ret_list = []
	word = string.lower(word)
	""" punctuation_filter = string.punctuation - {',','.','-'} """
	punctuation_filter = '!"#$%&\'()*+/:;<=>?@[\\]^_`{|}~'
	ascii_punctuation_filter = string.ascii_lowercase + punctuation_filter
	for letter in list(word):
		if letter in ascii_punctuation_filter:
			continue
		else:
			ret_list.append(letter)
	return ("".join(ret_list)).strip()

def getCoordinatesFromCleanText(word):
	match = STRICT_COORD_REGEX.search(word)
	if match:	return STRICT_COORD_REGEX.search(word).group(0)
	else:		return ''

def normalizeGeocoordenates(word):
	str1 = deleteTextFromWord(word)
	if str1 != '':
		almostClean = getCoordinatesFromCleanText(str1)
		cleaned = almostClean.replace(" ","")
		return cleaned
	else: 
		return ''

def sbv6(d,reverse=False):
    return sorted(d.iteritems(), key=itemgetter(1), reverse=True)

""""""""""""""""""""""""""""""""""""""""""""""""""""""

#filepath = '/home/vpena/Omar/geocontext/data/'
#filename = 'sorted-locations.out'
filepath = '../data/'
infilename = 'sorted-locations.out'
outfilename = 'processed-sorted-locations.out'
out_filename_location = 'location-ocurrences.out'
#out_filename_gcoord = 'geolocation-data.out'
out_filename_gcoord = 'geoclean.out'

input_data  = open(filepath + infilename, 'r')
output_data = open(filepath + outfilename, 'w')

n_useless = 0
n_useful = 0
location_dict = {}
rawGeoCoord = []
validGeoCoord = []

line = input_data.readline()
copyline = line

while line:
	
	if isCoordinates(line):
		rawGeoCoord.append(line)
		n_useful = n_useful + 1
		line = input_data.readline()
		copyline = line
		continue

	norm_word = normalize(line)
	
	if norm_word == '':
		#output_data.write("Original: " + copyline.strip()+" \t\tResult: nothing to retreive\n")
		n_useless = n_useless + 1
		line = input_data.readline()
		copyline = line
		continue

	#output_data.write("Original: " + copyline.strip()+" \t\tResult: "+norm_word+'\n')
	n_useful = n_useful + 1
	
	if (norm_word in location_dict):
		location_dict[norm_word] = location_dict[norm_word] + 1
	else:
		location_dict[norm_word] = 1
	# For debug we print the next line to visualize the process of the script
	if (n_useful%100000 == 0):
		print str(n_useful)

	line = input_data.readline()
	copyline = line

input_data.close()
output_data.close()

output_geocoord = open(filepath + out_filename_gcoord, 'w')
for i in rawGeoCoord:
	cleaned = normalizeGeocoordenates(i)
	if cleaned != '':
		validGeoCoord.append(cleaned)
		output_geocoord.write(cleaned + '\n')
	else:	continue
output_geocoord.close()

location_dict['GEOCOORDENATES'] = len(validGeoCoord)

sortedLocationDict = sbv6(location_dict, reverse=False)

output_locations = open(filepath + out_filename_location, 'w')
n_diff_locations = len(sortedLocationDict)
output_locations.write("Total number of diff Locations: " + str(n_diff_locations)+"\n")

acc_percent = 0.0
specific_percent = 0.0
n_total_locations = n_useless + n_useful

for k,v in sortedLocationDict:
	specific_percent = float(v)*100.0/n_useful
	acc_percent = acc_percent + specific_percent
	output_locations.write(k + "\t" + str(v) + "\t"+ str(specific_percent) + "\t"+ str(acc_percent) + "\n")
#	output_locations.write(k + "\t" + str(v) + "\n")
output_locations.close()


""" Print statistics to the stdout """
""""""""""""""""""""""""""""""""""""""""""""""""""""""
print "Number of total Locations: " + str(n_total_locations)
print "Number of useless Locations (only punctuation): " + str(n_useless) + " - " + str(float(n_useless*100.0/n_total_locations)) + "%" 
print "Number of \"userful\" Locations (Numbers OR text): " + str(n_useful) + " - " + str(float(n_useful*100.0/n_total_locations)) + "%"
print "Amount of Location in Coordenates form: " + str(len(rawGeoCoord))
print "Amount of Location in Coordenates form (VALID): " + str(len(validGeoCoord))
print "------------------------------------------------------"