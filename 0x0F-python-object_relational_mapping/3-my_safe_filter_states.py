#!/usr/bin/python3
"""
Display all values in the states table of hbtn_0e_0_usa
where name matches the argument
SQL injections
Arguments:
    username - username to connect the mySQL
    mysql passwd - password to connect the mySQL
    DB name - Name of the database
    name - state name searched
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
    query = """SELECT * FROM states WHERE name = %s ORDER BY states.id ASC;"""
    cursor.execute(query, (argv[4],))
    lists = cursor.fetchall()
    for row in lists:
        print(row)

    cursor.close()
    db.close()
