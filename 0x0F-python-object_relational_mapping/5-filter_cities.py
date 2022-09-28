#!/usr/bin/python3
"""
Lists all cities of a state on the DB hbtn_0e_4_usa
using the state as argument
Arguments:
    username - username to connect the mySQL
    mysql passwd - password to connect the mySQL
    DB name - Name of the database
    state name - name of the state to search
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
    cursor.execute("SELECT cities.name\
    FROM cities\
    JOIN states\
    ON state_id=states.id\
    WHERE states.name = %s\
    ORDER BY cities.id ASC", (argv[4],))

   lists = cursor.fetchall()
    cities = []
    for row in lists:
        if row[4] == state_name[0]:
            cities.append(row[2])
    print(', '.join(cities))

    cursor.close()
    db.close()
