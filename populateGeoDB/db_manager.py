import psycopg2
import sys
import db_config

def getConnection():
	try:
		con = psycopg2.connect(host = db_config.host,
					database = db_config.database, 
				        user = db_config.user, 
				        password = db_config.password,
				        port = db_config.port)
		return con
	except psycopg2.DatabaseError, e:
		onDBErrorDo(e)

def onDBErrorDo(e):
	print 'Error %s' % e    
	sys.exit(1)

def executeScripts(con, sql_script_list):
	executeScriptsWithParam(con, sql_script_list, [])

def executeScriptsWithParam(con, sql_script_list, params_list):
	try:
		cur = con.cursor() 
		for i in range(0, len(sql_script_list)):
			if len(params_list) <= i:
				cur.execute(sql_script_list[i])
			else:
				cur.execute(sql_script_list[i], params_list[i])
		con.commit()
	except psycopg2.DatabaseError, e:
		onDBErrorDo(e)
