import json, re

class GeoPoint(object):
    """ This class was made for give a representation for GeoPoints, acording to the GeoJSON information (Due to the discondance on using [Long,Lat] or [Lat,Long]"""
    
    defaultPoint = 0.0 

    def __init__(self, constructor=()):
        self.longitude  = constructor[0]
        self.latitude   = constructor[1]

    def __str__(self):
        """Method docstring."""
        return str(self.longitude)+ "," + str(self.latitude)
    
    @classmethod
    def from_string(cls, str):
        regx = re.compile('(.+)(\,)(.+)')
        match = regx.search(str)
        if match:
            constr = [float(regx.search(str).group(1)),float(regx.search(str).group(3))]
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

    def toArrayForDSTK(self):
        """ Return the object as an array [Longitude, Latitude] """
        points = [0.0, 0.0]
        points[0] = self.latitude
        points[1] = self.longitude
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


def main():

    a = GeoPoint.from_values(23.14123,-82.12343)
    a = GeoPoint.from_string("23.14123 -82.12343")
    print str(a)
    ble = json.loads(a.toGeoJSON())
    print ble["type"]
    print a.toArray()
    print a.getLatitude()
    print a.getLongitude()

if __name__ == "__main__":
    main()
