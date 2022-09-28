#!/usr/bin/python3
"""List all states from the database.
Arguments:
    username - username to connect the mySQL
    mysql passwd - password to connect the mySQL
    DB name - Name of the database

"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host="localhost",
                         port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    query = cursor.fetchall()
    for row in query:
        print(row)
    db.close()
