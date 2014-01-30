from datetime import date, datetime, time
import json, MySQLdb, re, pprint
import settings as k
from Event import Event
from dstk import DSTK
from GeoPoint import GeoPoint
import CountryCodes as CD
import LocationCleaner

# >
# <
FORMAT_DATETIME = "%Y-%m-%d %H:%M:%S"
Q_LAST_EVENT 			= "SELECT datetime FROM event ORDER BY id DESC LIMIT 1"
Q_EVENTS_BETWEEN 		= "SELECT id, keywords, datetime FROM event WHERE datetime >= %s AND datetime <= %s"
Q_TWEETS_ID_FROM_EVENT 	= "SELECT tweet_id FROM tweet WHERE event_id_id = "
Q_USERS_ID_FROM_EVENT 	= "SELECT user_id_id FROM tweet WHERE event_id_id = "
Q_LOCATION_FROM_USER 	= "SELECT location FROM user WHERE user_id = "
Q_COORD_FROM_TWEET 		= "SELECT coordinates FROM tweet WHERE tweet_id = "
global lastEventDT
global Count_Dict

""" -------------------------- Funciones ------------------------------- """
def queryToDB(cursor, query):
	try:
		cursor.execute(query)
		return cursor.fetchall()
	except MySQLdb.Error:
		print "Error: unable to fetch data"
		return -1

def getLastEventDateTime(cursor):
	try:
		cursor.execute(Q_LAST_EVENT)
		data = cursor.fetchone()
		return datetime.strptime(str(data[0]), FORMAT_DATETIME)
	except MySQLdb.Error:
		print "Error: unable to fetch data"
		return -1

def getEventsBetweenTwoDateTimes(cursor):
	lastEventDT = getLastEventDateTime(cursor)
	if lastEventDT != -1:
		try:
			zeroTodayDT = datetime(lastEventDT.year, lastEventDT.month, lastEventDT.day, 0, 0, 0)
			cursor.execute(Q_EVENTS_BETWEEN, (zeroTodayDT.strftime(FORMAT_DATETIME), lastEventDT.strftime(FORMAT_DATETIME),)) 
			return cursor.fetchall()
		except MySQLdb.Error:
			print "Error: unable to fetch data"
			return -1

def getTweetsIDByEvent(cursor, ID_Event):
	try:
		cursor.execute(Q_TWEETS_ID_FROM_EVENT + str(ID_Event))
		return cursor.fetchall()
	except MySQLdb.Error:
		print "Error: unable to fetch data"
		return -1

def getUsersIDByEvent(cursor, ID_Event):
	try:
		cursor.execute(Q_USERS_ID_FROM_EVENT + str(ID_Event))
		return cursor.fetchall()
	except MySQLdb.Error:
		print "Error: unable to fetch data"
		return -1

def getLocationFromUserID(cursor, ID_User):
	try:
		cursor.execute(Q_LOCATION_FROM_USER + str(ID_User))
		return cursor.fetchone()
	except MySQLdb.Error:
		print "Error: unable to fetch data"
		return -1

def getCoordinatesFromTweetID(cursor, ID_tweet):
	try:
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
				# Due to that Twitter ALWAYS return the same when the tweet has a Location, this code should never be reached
				pass

	except MySQLdb.Error:
		print "Error: unable to fetch data"
		return -1
#TODO
def saveTweetIDAndLocation(cursor, IDTweet, Location):
	"""
	Take an IDTweet with a Location Object and record it to the Local DB.
	"""
	pass

def getLocationFromDSTK(cursor, anEvent, Count_Dict):
	
	List_Tweets_Coordenatesful  = []
	Dict_Tweets_Coordenatesful 	= {}
	List_Tweets_Coordenatesless = []

	List_Tweets = getTweetsIDByEvent(cursor, anEvent.getID())
	
	for tweetID in List_Tweets:
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
		geoPointForQuery = [geoPointFromID.getLatitude(), geoPointFromID.getLongitude()]
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
	


""" ----------------------------------------------------------------------- """

def main():
	db = MySQLdb.connect(k.DB_HOST, k.DB_USER, k.DB_KEY, k.DB_NAME)
	cursor = db.cursor()
	Array_ID_events = []
	Dict_ID_Keywords = {}
	Array_Events = []

	Count_Dict = {}
	for row in getEventsBetweenTwoDateTimes(cursor):
		event = Event(row[0], row[1], row[2])
		Array_Events.append(event)
		#Array_ID_events.append(row[0])
		#Dict_ID_Keywords[row[0]] = row[1]
	
	for everyEvent in Array_Events:
		#getLocationFromDSTK(cursor, everyEvent, Count_Dict)

		# ID de usuarios que twitearon en el evento[0]
		List_Users = getUsersIDByEvent(cursor, everyEvent.getID())
		for user in List_Users:
			locationOfUser = getLocationFromUserID(cursor, user[0])
			effectiveLoc = locationOfUser[0]
			cleanedLoc = LocationCleaner.cleanLocationField(effectiveLoc)
			if type(cleanedLoc) == str:
				print "Input: %s \t Result String: %s" % (effectiveLoc, cleanedLoc)
			if type(cleanedLoc) == GeoPoint:
				print "Input: %s \t Result GeoPoint: %s" % (effectiveLoc, str(cleanedLoc))
			if cleanedLoc == None:
				print "Input: Useless = %s \t Result None" % effectiveLoc
	db.close()


if __name__ == "__main__":
	main()
