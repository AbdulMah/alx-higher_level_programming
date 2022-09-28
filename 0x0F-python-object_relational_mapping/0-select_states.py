#!/usr/bin/python3
"""script that lists all states from the
database hbtn_0e_0_usa
"""


from sys import argv
import MySQLdb


if __name__ == '__main__':

    conn = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host="localhost",
                         port=3306)
    cur = conn.cursor()
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
