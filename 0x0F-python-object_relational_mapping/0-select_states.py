#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    user, password, database = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db.close()
