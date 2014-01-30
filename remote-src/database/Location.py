class Location(object):
    
    def __init__(self, countryName, countryCode, regionName, regionCode, cityName):
        """
        This class defines an object inspired by the data model form our places
        DB (PosGIS + Postgresql) which is saved to the Local DB associated with
        an TweetID (read: LocalDBInteractions.py).
        """
        self.countryName = countryName
        self.countryCode = countryCode
        self.regionName = regionName
        self.regionCode = regionCode
        self.cityName = cityName

    def __str__(self):
    	"""Returns the Location as a pretty string."""
        result = ""
        if self.cityName != None:
            result = result + str(self.cityName) + ", "
        if self.regionName != None:
            result = result + str(self.regionName) + ", "
        
        result = result + str(self.countryName)
        return result
        
    def getCountryName(self):
        """Returns the countryName."""
        return self.countryName
        
    def getCountryCode(self):
        """Returns the countryCode."""
        return self.countryCode
        
    def getRegionName(self):
        """Returns the regionName."""
        return self.regionName
        
    def getRegionCode(self):
        """Returns the regionCode."""
        return self.regionCode
        
    def getCityName(self):
        """Returns the cityName."""
        return self.cityName

    def setCountryName(self, countryName):
        """Set the value of countryName for the given value."""
        self.countryName = countryName
        
    def setCountryCode(self, countryCode):
        """Set the value of countryCode for the given value."""
        self.countryCode = countryCode
        
    def setRegionName(self, regionName):
        """Set the value of regionName for the given value."""
        self.regionName = regionName
        
    def setRegionCode(self, regionCode):
        """Set the value of regionCode for the given value."""
        self.regionCode = regionCode
        
    def setCity(self, cityName):
        """Set the value of cityName for the given value."""
        self.cityName = cityName