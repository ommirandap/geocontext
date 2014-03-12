COMPLETE SYSTEM
================

Input 	-> Data Base (Mauricio)

Output 	-> Tweet's Location related to an event

* Step 1 : Get event's info

	- Input: 	(Event Keywords, Datetime)
	- Output: ([{Coordenated Tweets -> GeoPoint Object}, {Coordenatedless Tweets -> Location Field cleaned}])
	- Do/ne:
		[X] Get the Tweet's ID of all the Events of the day
			* db-interactions::getLastEventDateTime
			* db-interactions::getEventsBetweenTwoDateTimes
			* db-interactions::getTweetsIDByEvent
