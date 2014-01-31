import csv, sys

def createRegionsCSV(source_folder, outcome_folder):
	original_file = open(source_folder + "admin1CodesASCII.txt", "r")
	out_file = open(outcome_folder + "regions.csv", "w")

	# each line is: country_code.regoin_code region_name region_name_ascii population
	for line in original_file:
		row = line.lower().split("	")
		country_regionCode = row[0]
		region = row[2].replace(',', ' ')
		country = country_regionCode[0:2]
		region_code = country_regionCode[3:]
		row = country + ',' + region_code + ',' + region + '\n'
		out_file.write(row)
	original_file.close()
	out_file.close()

def createRegionsDictionary(base_folder):
	reader = csv.reader(open(base_folder+'regions.csv', 'rb'))
	regions = {}

	# each row is: country_code, region_code, region name
	for row in reader:
		if row[0] not in regions:
			regions[row[0]] = {}
		regions[row[0]][row[1]] = row[2]
	return regions
