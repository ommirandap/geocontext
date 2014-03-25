from datetime import date, datetime, time
import json, MySQLdb, re, pprint
import settings as k
from Event import Event
from dstk import DSTK
from GeoPoint import GeoPoint
import CountryCodes as CD
import LocationCleaner
import sys

FORMAT_DATETIME = "%Y-%m-%d %H:%M:%S"
Q_LAST_EVENT 			= "SELECT datetime FROM event ORDER BY id DESC LIMIT 1"
Q_EVENTS_BETWEEN 		= """SELECT id, keywords, datetime FROM event 
							WHERE datetime >= %s AND datetime <= %s"""
Q_TWEETS_ID_FROM_EVENT 	= "SELECT tweet_id FROM tweet WHERE event_id_id = "
Q_USERS_ID_FROM_EVENT 	= "SELECT user_id_id FROM tweet WHERE event_id_id = "
Q_LOCATION_FROM_USER 	= "SELECT location FROM user WHERE user_id = "
Q_COORD_FROM_TWEET 		= "SELECT coordinates FROM tweet WHERE tweet_id = "
Q_USER_FROM_TWEET 		= "SELECT user_id_id FROM tweet WHERE tweet_id = "
global lastEventDT
global Count_Dict

def getConnection():
	"""
	Returns a connection object whom will be given to any DB Query function.
	"""
	try:
		connection = MySQLdb.connect(host=k.MYSQLDB_HOST, port=3306, user=k.MYSQLDB_USER, 
							passwd=k.MYSQLDB_KEY, db=k.MYSQLDB_NAME)
		return connection	
	except MySQLdb.DatabaseError, e:
		print 'Error %s' % e    
		sys.exit(1)

def getLastEventDateTime(connection):
	"""
	Returns a string with the Datetime of the lastEvent registered on the DB.
	"""
	try:
		cursor = connection.cursor()
		cursor.execute(Q_LAST_EVENT)
		data = cursor.fetchone()
		return datetime.strptime(str(data[0]), FORMAT_DATETIME)
	except MySQLdb.Error:
		print "Error: unable to fetch data"
		return -1

def getTodayEvents(connection):
	"""
	Returns all the events (as an Array of Events Objects) added to the DB, 
	between the 00:00hrs and the time of the last event added (on the same day).
	"""
	lastEventDT = getLastEventDateTime(connection)
	if lastEventDT != -1:
		try:
			zeroTodayDT = datetime(lastEventDT.year, lastEventDT.month, 
									lastEventDT.day, 0, 0, 0)
			cursor = connection.cursor()
			cursor.execute(Q_EVENTS_BETWEEN, 
							(zeroTodayDT.strftime(FORMAT_DATETIME), 
							lastEventDT.strftime(FORMAT_DATETIME),)) 
			internalEvents = []
			for row in cursor.fetchall():
				event = Event(row[0], row[1], row[2])
				internalEvents.append(event)
			return internalEvents
		except MySQLdb.Error:
			print "Error: unable to fetch data"
			return -1
	else:
		print "Something went wrong with getting the last event of today"
		sys.exit(1)

def getTweetsIDByEvent(connection, ID_Event):
	"""
	Returns all the ID of the Tweets from an specified EventID.
	"""
	try:
		cursor = connection.cursor()
		cursor.execute(Q_TWEETS_ID_FROM_EVENT + str(ID_Event))
		return cursor.fetchall()
	except MySQLdb.Error:
		print "Error: unable to fetch data"
		return -1

def getUsersIDByEvent(connection, ID_Event):
	"""
	Returns all the users that tweeted on a certain event (given the Event ID).
	"""
	try:
		cursor = connection.cursor()
		cursor.execute(Q_USERS_ID_FROM_EVENT + str(ID_Event))
		return cursor.fetchall()
	except MySQLdb.Error:
		print "Error: unable to fetch data"
		return -1

def getLocationFromUserID(connection, ID_User):
	"""
	Returns the Location field from a user's profile (of a specific User ID).
	"""
	try:
		cursor = connection.cursor()
		cursor.execute(Q_LOCATION_FROM_USER + str(ID_User))
		return  (cursor.fetchone())[0]
	except MySQLdb.Error:
		print "Error: unable to fetch data"
		return -1

def getCoordinatesFromTweetID(connection, ID_tweet):
	"""
	If a certain tweet contains the "coordinates" field activated, then returns 
	it. Otherwise, returns None.
	"""
	try:
		cursor = connection.cursor()
		cursor.execute(Q_COORD_FROM_TWEET + str(ID_tweet))
		result = (cursor.fetchone())[0]
		if result == "None":
			return None
		else:
			extractCordRegex = re.compile("('coordinates':) (\[)(.+)(\])")
			match = extractCordRegex.search(result)
			if match:	
				return extractCordRegex.search(result).group(3)
			else:
				#Due to that Twitter ALWAYS return the same when the tweet has
				#a Location, this code should never be reached.
				pass

	except MySQLdb.Error:
		print "Error: unable to fetch data"
		return -1

def getUserIDFromTweetID(connection, ID_tweet):
	"""
	Returns the user id for a tweet
	"""
	try:
		cursor = connection.cursor()
		cursor.execute(Q_USER_FROM_TWEET + str(ID_tweet))
		return (cursor.fetchone())[0]
	except MySQLdb.Error:
		print "Error: unable to fetch data"
		return -1

def getLocationFromDSTK(connection, anEvent, Count_Dict):
	"""
	Deprecated, since we use now a local DB for match the closer GeoCoordenate.
	"""
	List_Tweets_Coordenatesful  = []
	Dict_Tweets_Coordenatesful 	= {}
	List_Tweets_Coordenatesless = []

	List_Tweets = getTweetsIDByEvent(connection, anEvent.getID())
	
	for tweetID in List_Tweets:
		cursor = connection.cursor()
		probableCoord = getCoordinatesFromTweetID(cursor, tweetID[0])
		
		if probableCoord == None:
			List_Tweets_Coordenatesless.append(tweetID[0])
		else:
			geoPointFromCoord = GeoPoint.initFromString(probableCoord)
			List_Tweets_Coordenatesful.append(tweetID[0])
			Dict_Tweets_Coordenatesful[tweetID[0]] = geoPointFromCoord

	dstk = DSTK()
	for ID in Dict_Tweets_Coordenatesful.keys():
		geoPointFromID = Dict_Tweets_Coordenatesful[ID]
		geoPointForQuery = [geoPointFromID.getLatitude(), 
							geoPointFromID.getLongitude()]
		coordinates_dstk = dstk.coordinates2politics(geoPointForQuery)
		if coordinates_dstk[0]["politics"] is not None:
			result = coordinates_dstk[0]["politics"][0]["name"]
		else:
			result = "N/A"
		
		code = CD.searchByName(result)
		
		if code in Count_Dict:
			Count_Dict[code] = Count_Dict[code] + 1
		else:
			Count_Dict[code] = 1 
		
		print "Event: %s\t analizing: %s \t from = %s code = %s" % (anEvent.getKeywords(), str(geoPointForQuery), result, code) 

def main():
	connection = getConnection()
	
	Array_ID_events = []
	Dict_ID_Keywords = {}
	Array_Events = []

	Count_Dict = {}

	Array_Events = getTodayEvents(connection)
	
	for everyEvent in Array_Events:
		#getLocationFromDSTK(connection, everyEvent, Count_Dict)

		# ID de usuarios que twitearon en el evento[0]
		List_Users = getUsersIDByEvent(connection, everyEvent.getID())
		for user in List_Users:
			locationOfUser = getLocationFromUserID(connection, user[0])
			effectiveLoc = locationOfUser[0]
			cleanedLoc = LocationCleaner.cleanLocationField(effectiveLoc)
			if type(cleanedLoc) == str:
				print "Input: %s \t Result String: %s" % (effectiveLoc, cleanedLoc)
			if type(cleanedLoc) == GeoPoint:
				print "Input: %s \t Result GeoPoint: %s" % (effectiveLoc, str(cleanedLoc))
			if cleanedLoc == None:
				print "Input: Useless = %s \t Result None" % effectiveLoc
	connection.close()

if __name__ == "__main__":
	main()
