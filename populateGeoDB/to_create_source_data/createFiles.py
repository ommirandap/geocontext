import csv, sys
import country_manager
import region_manager
import city_manager

# This program creates the csv files for the gazetteer from http://download.geonames.org/export/dump/

csv.field_size_limit(sys.maxsize)

source_folder = 'original_source_data/'
outcome_folder = '../source_data/'

country_manager.createCountriesPositionsCSV(source_folder, outcome_folder)
country_manager.createCountriesCSV(source_folder, outcome_folder)
region_manager.createRegionsCSV(source_folder, outcome_folder)
city_manager.createBigCitiesCSV(source_folder, outcome_folder)
