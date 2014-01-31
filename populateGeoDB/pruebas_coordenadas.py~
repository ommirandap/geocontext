#!/usr/bin/env python

import csv, os, os.path
#import geodict_config
from geodict_lib import *
import psycopg2
import sys

db_user = 'galean'
db_pass = '1234'

def getConnection():
	try:
		con = psycopg2.connect(database='geodict2', user=db_user, password=db_pass)
		return con	
	except psycopg2.DatabaseError, e:
		print 'Error %s' % e    
		sys.exit(1)

def getClosestCity(con, lat, lon):
	try:
		cur = con.cursor() 
		sql = "select closestcity(%s,%s, 10)"
		params = [lon, lat]
		cur.execute(sql, params)
		rows = cur.fetchall()
		if len(rows) > 0:
			return rows[0]
		else:
			return None
	except psycopg2.DatabaseError, e:
		print 'Error %s' % e    
		sys.exit(1)

def leerArchivo(con):
	coordenadas_test = open("../Data pruebas/geoloc-dstk-codedict.out")
	local_compute = open("../Data pruebas/postgis-codedict.out", "w")
	for line in coordenadas_test:
		t = line[:-2].split("	 ")
		coord = t[1][12:-2].split(",")
		lat = coord[0]
		lon = coord[1]
		closestCity = getClosestCity(con, lat, lon)
		local_compute.write(line[:-1] + '	 ')
		if closestCity is not None:
			columns_closestCity = closestCity[0].replace(' ', '').split(",")
			local_compute.write('(local compute) from = ' + columns_closestCity[1] + ' code = ' + columns_closestCity[2])
		local_compute.write('\n')

con = getConnection()
leerArchivo(con)
