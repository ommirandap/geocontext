PopulateGeoDB
==========

Module to populate the database containing the information about the cities, regions and countries in the world using PostgreSQL and PostGIS.


##### 0.- Install PostgreSQL and PostGIS
##### 1.- (OPTIONAL) Create the places files

This step is only necesary if you wan to populate the geoDB with the latest information from geonames.org. This module provides the information of cities, regions and countries by the date of January, 2014.

To accomplish this step, download the following files:

- http://download.geonames.org/export/dump/admin1CodesASCII.txt 
- http://download.geonames.org/export/dump/countryInfo.txt
- http://download.geonames.org/export/dump/cities5000.zip, extracting the cities5000.txt file

And replace those in the to_create_source_data/original_source_data

Finally, execute the createFiles.py script in the to_create_source_data folder.

##### 2.- Create a database in PostgreSQL. By default we use the "geoDB" name for the database
##### 3.- Update the information of your postgres configuration in the db_config.py file
##### 4.- Execute the populate_db_postgis.py script. This process takes some time, make yourself a coffee in the meantime

And you are done!


Developed by Omar Miranda (Undergrad Student) & Vanessa Peña (PhD Student)

KDW-PRISMA Lab, CS Department, Universidad de Chile
