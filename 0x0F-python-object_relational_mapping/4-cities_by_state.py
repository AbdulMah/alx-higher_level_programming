#!/usr/bin/python3
"""
Display all cities from hbtn_0e_4_usa
Arguments:
    username - username to connect the mySQL
    mysql passwd - password to connect the mySQL
    DB name - Name of the database
"""


import MySQLdb
from sys import argv
if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host="localhost",
                         port=3306)
    """Connect to a MySQL server."""

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
    FROM cities\
    JOIN states\
    ON state_id=states.id\
    ORDER BY cities.id ASC")

    lists = cursor.fetchall()
    for row in lists:
        print(row)

    cursor.close()
    db.close()
