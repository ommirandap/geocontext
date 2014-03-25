from datetime import date, datetime, time
import json, MySQLdb, re, pprint
import settings as k
from Event import Event
from dstk import DSTK
from GeoPoint import GeoPoint
import CountryCodes as CD
import LocationCleaner
import BreaknewsDBInteractions as cuboid

def main():
	connection = cuboid.getConnection()
	
	array_events = cuboid.getTodayEvents(connection)

	an_event = array_events[0]
	print an_event
	
if __name__ == "__main__":
	main()
