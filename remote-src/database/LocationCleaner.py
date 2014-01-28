#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import string, re, sys
from string import maketrans
from GeoPoint import GeoPoint
from operator import itemgetter

COORD_REGEX = re.compile(
	'([-+]?)([\d]{1,2})(((\.)(\d+)(,)))(\s*)(([-+]?)([\d]{1,3})((\.)(\d+))?)'
	)
STRICT_COORD_REGEX = re.compile(
	'^(([-+]?[\d]{1,2}(\.)(\d+))((,)(\s*))(([-+]?)([\d]{1,3})(\.)(\d+)))'
	)

"""Functions to clean a typical User's Location field."""

def punctuationToSpace(word):
	"""Returns the word with every punctuation symbol replaced for a space."""
	input_table = string.punctuation
	output_table =  "                                "
	translation_table = maketrans(input_table, output_table)
	translated_word = word.translate(translation_table)
	return translated_word

def reduceSpaces(word):
	"""Return the word with all the spaces reduced to 1."""
	return re.sub('\s+', ' ', word)

def normalizeString(word):
	"""
	Return the same word without punctuation, all 1+ spaces to 1 spaces, 
	lowercased and stripped. After this function, a useless word will be: ''.
	"""
	word_stage1 = punctuationToSpace(word)
	word_stage2 = reduceSpaces(word_stage1)
	word_stage3 = string.lower(word_stage2)
	word_stage4 = word_stage3.strip()
	if word_stage4 == '':
		return None
	else:
		return word_stage4

"""Functions to clean a User's Location field that contains geoCoordinates."""

def hasCoordinates(word):
	"""Returns True if the word has coordinates on it, otherwise False."""
	match = COORD_REGEX.search(word)
	if match:	return True
	else:		return False

def deleteTextFromWord(word):
	"""
	Returns the word without any symbol, except for Numbers and (,.-).
	"""
	non_filtered = []
	word = string.lower(word)
	punctuation_filter = '!"#$%&\'()*+/:;<=>?@[\\]^_`{|}~'
	ascii_punctuation_filter = string.ascii_lowercase + punctuation_filter
	for char in list(word):
		if char in ascii_punctuation_filter:
			continue
		else:
			non_filtered.append(char)
	if non_filtered[0] == '.':
		non_filtered[0] = ' '
	return ("".join(non_filtered)).strip()

def getCoordinatesFromCleanText(word):
	"""Returns the coordinates from an only {number,.-} string."""
	match = STRICT_COORD_REGEX.search(word)
	if match:	return STRICT_COORD_REGEX.search(word).group(0)
	else:		return ''

def normalizeGeocoordenates(word):
	"""Returns GeoCoordinate as a text from a GeoCoordinate-style word."""
	word = word.replace("U.T:", "")
	word = word.replace("i12T:", "")
	word_wout_text = deleteTextFromWord(word)
	if word_wout_text != '':
		almostClean = getCoordinatesFromCleanText(word_wout_text)
		cleaned = almostClean.replace(" ","")
		return cleaned
	else: 
		return None

def getAsGeoPoint(word):
	"""Returns a GeoPoint object from a text."""
	return GeoPoint.initFromString(word, True)

def cleanLocationField(LocationFieldFromUser):
	"""
	If LocationFromUser is a String without any possible geoCoordinate
	information, then returns a cleaned Location string. Otherwise, if the 
	string contains any possible geoCoordinate information, returns a GeoPoint 
	object.
	If the LocationField is useless, returns None.
	"""
	result = None
	if hasCoordinates(LocationFieldFromUser):
		resultAsString = normalizeGeocoordenates(LocationFieldFromUser)
		result = getAsGeoPoint(resultAsString)
	else:
		result = normalizeString(LocationFieldFromUser)
	return result


def main():
	ble = sys.argv[1]
	if hasCoordinates(ble):
		print normalizeGeocoordenates(ble)
		print type(getAsGeoPoint(normalizeGeocoordenates(ble)))
	else:
		print "ble"


if __name__ == "__main__":
	main()