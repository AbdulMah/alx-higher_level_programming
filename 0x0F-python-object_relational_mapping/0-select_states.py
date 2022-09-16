#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    user, password, database = argv[1], argv[2], argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    cur.query("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
