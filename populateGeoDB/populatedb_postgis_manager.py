import psycopg2

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
