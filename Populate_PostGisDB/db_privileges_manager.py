import psycopg2
import sys
import db_config
import db_manager

def addPrivileges(con):
	try:
		cur = con.cursor() 
		cur.execute("GRANT USAGE ON SCHEMA public to " + db_config.user + ";")
		cur.execute("GRANT SELECT ON ALL TABLES IN SCHEMA public TO " + db_config.user + ";")
		cur.execute("ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO " + db_config.user + ";")
		cur.execute("CREATE EXTENSION IF NOT EXISTS postgis")
	except psycopg2.DatabaseError, e:
		db_manager.onDBErrorDo(e)
