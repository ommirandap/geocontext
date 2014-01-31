#!/usr/bin/env python

import csv, os, os.path
from geodict_lib import *
import psycopg2
import sys
import db_config
import db_manager
import db_country_manager
import db_region_manager
import db_city_manager
import db_privileges_manager


### MAIN ###
con = db_manager.getConnection()

### ADD NECESARY PRIVILEGES
db_privileges_manager.addPrivileges(con)

### CREATE AND  COUNTRY TABLE ###
db_country_manager.createCountriesTable(con)
db_country_manager.populateCountriesTable(con)

### CREATE AND  REGIOn TABLE ###
db_region_manager.createRegionsTable(con)
db_region_manager.populateRegionsTable(con)

### CREATE AND  COUNTRY TABLE ###
db_city_manager.createBigCitiesTable(con)
db_city_manager.createGeometryIndex(con)
db_city_manager.populateBigCitiesTable(con)
db_city_manager.createClosestcityFunction(con)
db_city_manager.runVacuum(con)
