#!/usr/bin/python3
""" This module lists all the states from the
    database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv


def main(*args):
    # Create a database connection
    conn = MySQLdb.connect(
                 host = args[0],
                 port = args[1], 
                 user = args[2],
                 password = args[3], 
                 db = args[4], 
                 charset="utf8mb4"
             )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    conn.close()


if __name__ == "__main__":
    #main()
    if len(argv) >= 4:
        host, port, user, password, db = argv[1], argv[2], argv[3], argv[4]       
        main(host, port, user, password, db)
        #main(*argv)