import string

"""
This script is for process an output file from the Query N1 (queries.md) 
an obtain statistics about the impact of users on our database.
"""

datapath = "../data/"
filename = "n_users_with_ntweets.out"

input_data = open(datapath+filename, 'r')

"""First line is just a header."""
input_data.readline()

#quantity = [0, 0, 0, 0, 0, 0, 0, 0]
quantity = []

for j in range(0,80):
	quantity.insert(j, 0)

for line in input_data:
	line_users = (line.split())[0]
	line_tweets = (line.split())[1]

	rango = int(int(line_tweets)/100)
	quantity[rango] = quantity[rango] + int(line_users)
	
roof = 100
for it in quantity:
	print str(roof-100)+"-"+str(roof) + "\t" + str(it)
	roof = roof + 100