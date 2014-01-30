class Location(object):
    
    def __init__(self, country, region, city):
        """
        This class defines an object inspired by the data model form our places
        DB (PosGIS + Postgresql) which is saved to the Local DB associated with
        an TweetID (read: LocalDBInteractions.py).
        """
        self.country = country
        self.region = region
        self.city = city

    def __str__(self):
    	"""Returns the Location as a pretty string"""
        result = ""
        if self.city != None:
            result + self.city + ", "
        íf self.region != None:
            result + self.region + ", "
    	result + str(self.country)
        return result