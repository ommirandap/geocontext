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
        """Method docstring."""
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
        return cls([longitude_value, latitude_value])

    def toStringForDSTK(self):
        """Method docstring."""
        return str(self.latitude)+ ", " + str(self.longitude)

    def toArray(self):
        """ Return the object as an array [Longitude, Latitude] """
        points = [0.0, 0.0]
        points[0] = self.longitude
        points[1] = self.latitude
        return points

    def toGeoJSON(self):
        """ """
        defaultDict = {"type": "Point"}
        defaultDict["coordinates"]=self.toArray()
        return json.dumps(defaultDict)

    def getLatitude(self):
        """ Returns the Latitude of the point """
        return self.latitude

    def getLongitude(self):
    	""" Returns the Longitude of the point """
    	return self.longitude

    def setLatitude(self, latitude):
        """ Returns the Latitude of the point """
        self.latitude = latitude

    def setLongitude(self, longitude):
        """ Returns the Longitude of the point """
        self.longitude = longitude


"""
def main():

    a = GeoPoint.from_values(23.14123,-82.12343)
    a = GeoPoint.__init__from_string("23.14123 -82.12343")
    print str(a)
    ble = json.loads(a.toGeoJSON())
    print ble["type"]
    print a.toArray()
    print a.getLatitude()
    print a.getLongitude()

if __name__ == "__main__":
    main()
"""