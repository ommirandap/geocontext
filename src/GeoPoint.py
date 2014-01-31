import json, re

class GeoPoint(object):
    """
    This class was made for give a representation for GeoPoints, 
    according to the GeoJSON information 
    (Due to the differences on using [Long,Lat] or [Lat,Long]).
    """
    
    def __init__(self, constructor=()):
        if constructor == None:
            self.longitude = 0.0
            self.latitude  = 0.0
        else:
            self.longitude  = constructor[0]
            self.latitude   = constructor[1]

    def __str__(self):
        """Returns the GeoPoint as a String \"longitude,latitude\"."""
        return str(self.longitude)+ "," + str(self.latitude)
    
    @classmethod
    def initFromString(cls, stringLikeCoord, LatLongStyle = False):
        """
        Calls the constructor of GeoPoint, giving an array of [Long,Lat] 
        from a string with the same form. 
        If the string it's of the [Lat, Long] (like DataScienceToolkit API), 
        then LatLongStyle must be set as True.
        """
        regx = re.compile('(.+)(\,)(.+)')
        match = regx.search(stringLikeCoord)
        if match:
            if LatLongStyle:
                constr = [
                    float(regx.search(stringLikeCoord).group(3)),
                    float(regx.search(stringLikeCoord).group(1))
                    ]
            else:
                constr = [
                    float(regx.search(stringLikeCoord).group(1)),
                    float(regx.search(stringLikeCoord).group(3))
                    ]                
        else:
            constr = None
        return cls(constr)

    @classmethod
    def from_values(cls, longitude_value, latitude_value):
        """
        Calls the constructor of GeoPoint, giving an array of [Long,Lat] 
        from two parameters as values.
        """
        return cls([longitude_value, latitude_value])

    def toGeoJSON(self):
        """Dumps the GeoPoint object to a JSON on GeoJSON's style."""
        defaultDict = {"type": "Point"}
        defaultDict["coordinates"]=self.toArray()
        return json.dumps(defaultDict)

    def getLatitude(self):
        """Returns the Latitude of the GeoPoint."""
        return self.latitude

    def getLongitude(self):
        """Returns the Longitude of the GeoPoint."""
    	return self.longitude

    def setLatitude(self, latitude):
        """Set the Longitude of a GeoPoint."""
        self.latitude = latitude

    def setLongitude(self, longitude):
        """Set the Latitude of a GeoPoint."""
        self.longitude = longitude