import psycopg2 as PG
import settings as k
import Location
from operator import itemgetter
import sys

"""
This file contains the main interactions with the local DB, which stores the
relation TweetID-Location
"""
Q_ALL_COUNTRIES = 	"SELECT country, country_code FROM countries;"
Q_ALL_REGIONS	=	"SELECT region, region_code, country FROM regions;"
Q_ALL_CITIES 	=	"SELECT city, country, region_code FROM cities;"
Q_COUNTRY_BY_NAME = "SELECT country, country_code FROM countries WHERE country LIKE %s;"
Q_CITIES_BY_NAME = "SELECT city, country, region_code FROM cities WHERE city LIKE %s;"

def getConnection():
	try:
		connection = PG.connect(database=k.PGSQLDB_NAME, host=k.PGSQLDB_HOST, 
								user=k.PGSQLDB_USER, password=k.PGSQLDB_KEY)
		return connection	
	except PG.DatabaseError, e:
		print 'Error %s' % e    
		sys.exit(1)

def getCountries(connection):
	"""Returns all the countries in the DB."""
	cursor = connection.cursor()
	cursor.execute(Q_ALL_COUNTRIES)
	return cursor.fetchall()

def getRegions(connection):
	cursor = connection.cursor()
	cursor.execute(Q_ALL_REGIONS)
	return cursor.fetchall()

def getCities(connection):
	cursor = connection.cursor()
	cursor.execute(Q_ALL_CITIES)
	return cursor.fetchall()

def searchCountryName(connection, name):
	cursor = connection.cursor()
	param = [name]
	cursor.execute(Q_COUNTRY_BY_NAME, param)
	return cursor.fetchall()

def searchCityName(connection, name):
	cursor = connection.cursor()
	param = [name]
	cursor.execute(Q_CITIES_BY_NAME, param)
	return cursor.fetchall()

def getClosestCity(con, lat, lon):
	try:
		cur = con.cursor() 
		sql = "select closestcity(%s,%s, 10)"
		params = [lon, lat]
		cur.execute(sql, params)
		rows = cur.fetchall()
		if len(rows) > 0:
			return rows[0]
		else:
			return None
	except psycopg2.DatabaseError, e:
		print 'Error %s' % e    
		sys.exit(1)

def sbv6(d,reverse=False):
    return sorted(d.iteritems(), key=itemgetter(1), reverse=False)

def main():
	connection = getConnection()
	dump = getCities(connection)
	CityList = []
	index = {}
	for i in dump:
		CityList.append(i[0])

	for cityName in CityList:
		for word in cityName.split(" "):
			if word in index.keys():
				index[word] = index[word] + 1
			else:
				index[word] = 1
	
	sortedIndex = sbv6(index, reverse=False)
	for k,v in sortedIndex:
		if v > 3:
			print k + " " + str(v)

	print len(index)

	#for i in sal:
	#	iLocation = Location.Location(i[0],i[1], None, None, None)
	#	LocationList.append(iLocation)

if __name__ == "__main__":
	main()
