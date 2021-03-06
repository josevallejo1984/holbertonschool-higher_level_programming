#!/usr/bin/python3
"""Show lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
from sys import argv

# connect to db
if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )

    # Getting a cursor in MySQLdb python
    cur = conn.cursor()

    # Executing db queries
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    # Obtaining all result of queries
    query_table = cur.fetchall()
    # Printing the result one to one
    for row in query_table:
        print(row)

    # Close conection to cursor and db
    cur.close()
    conn.close()
