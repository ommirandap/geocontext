from datetime import date, datetime, time
import json, MySQLdb, re, pprint
import settings as k
from Event import Event
from dstk import DSTK
from GeoPoint import GeoPoint
import CountryCodes as CD
import LocationCleaner
import BreaknewsDBInteractions as bnews

def main():
	connection = bnews.getConnection()
	
	array_events = bnews.getTodayEvents(connection)
	an_event = array_events[0]
	event_id = an_event.eventID
	event_tweets = bnews.getTweetsIDByEvent(connection, event_id)
	for tweet in event_tweets:
		coords = bnews.getCoordinatesFromTweetID(connection, tweet[0])
		if coords is not None:
			user_id = bnews.getUserIDFromTweetID(connection, tweet[0])
			location = bnews.getLocationFromUserID(connection, user_id)
			print tweet[0], ";", coords, ";" , user_id, ";", location, "\n"
	
if __name__ == "__main__":
	main()
