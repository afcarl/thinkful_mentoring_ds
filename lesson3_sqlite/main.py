import sqlite3 as lite

from lib.populate_db import populate
from lib.query import query


def main():

	con = lite.connect('getting_started.db')
	populate(con)
	query(con)
	print "complete"

if __name__ == "__main__":
	main()


