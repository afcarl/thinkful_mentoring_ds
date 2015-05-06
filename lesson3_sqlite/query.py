import pandas as pd
import sqlite3 as lite

con = lite.connect('getting_started.db')

with con:    

    cur = con.cursor()    
    cur.execute("SELECT * FROM cities")

    rows = cur.fetchall()
	
 	cols = [desc[0] for desc in cur.description]
  	df = pd.DataFrame(rows, columns=cols)

### Do stuff with df ####


