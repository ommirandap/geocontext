import psycopg2 as PG
import settings as k
import Location

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

def main():
	con = getConnection()
	sal = searchCityName(con, "santiago")
	#LocationList = []
	for i in sal:
		print i
	#for i in sal:
	#	iLocation = Location.Location(i[0],i[1], None, None, None)
	#	LocationList.append(iLocation)

if __name__ == "__main__":
	main()