import pandas as pd
import sqlite3 as lite


def query(connection):
	with connection as con:    
		cur = con.cursor()    
		cur.execute("SELECT * FROM cities")
		rows = cur.fetchall()
		cols = [desc[0] for desc in cur.description]
		print rows
		df = pd.DataFrame(rows, columns=cols)

	### Do stuff with df ####



