import sqlite3 as lite

con = lite.connect('getting_started.db')

cities = (('Las Vegas', 'NV'), ('Atlanta', 'GA'), ("Washington", "DC"), ("Houston", "TX"))

weather = (('Las Vegas', 2013, 'July', 'December'), ('Atlanta', 2013, 'July', 'January'))

# Inserting rows by passing values directly to `execute()`
with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS cities")
    cur.execute("DROP TABLE IF EXISTS weather")

    cur.execute("CREATE TABLE cities (name text, state text)")
    cur.execute(
    	"CREATE TABLE weather (\
    		city text, \
    		year integer, \
    		warm_month text, \
    		cold_month text, \
    		average_high integer)"
    	)

