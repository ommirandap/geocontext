from datetime import datetime

FORMAT_DATETIME = "%Y-%m-%d %H:%M:%S"

class Event(object):
    
    def __init__(self, eventID, keywords, datetime):
        """
        An event is identified by 3 fields: his ID, a couple of keywords 
        (one string) and a datetime. 
        This schema comes from the DB and this was created only to manipulate 
        those records easily.
        """
        self.eventID = eventID
        self.keywords = keywords
        self.datetime = datetime

    def __str__(self):
    	"""Dump the event as a string."""
    	return (str(self.eventID)+ " - " 
                + str(self.keywords) + " - " 
                + str(self.datetime.strftime(FORMAT_DATETIME)))
    
    def getID(self):
        """
        Return the ID of the eventID.
        Type: long.
        """
        return self.eventID

    def getKeywords(self):
    	"""Returns the couple of keywords of the Event (1 string)."""
    	return self.keywords

    def getDatetime(self):
    	"""Returns the datetime when the Event was added to the DB (datetime)."""
    	return self.datetime