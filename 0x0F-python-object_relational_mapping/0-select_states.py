#!/usr/bin/python3
""" This module lists all the states from the
    database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv



    # Create a database connection
    # conn = MySQLdb.connect(
    #             host="localhost", port=3306, user=argv[1],
    #             password=argv[2], db=argv[3], charset="utf8mb4"
    #         )
    # cur = conn.cursor()
    # cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    # query_rows = cur.fetchall()
    # for row in query_rows:
    #     print(row)
    # cur.close()
    # conn.close()


if __name__ == "__main__":
    #main()
    db = MySQLdb.connect(host="localhost:3306",
                         port = 3306,
                         user=str(argv[1]),
                         password=str(argv[2]),
                         database=str(argv[3])
                         )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")
    for i in cursor.fetchall():
        print(i)

    db.close()
