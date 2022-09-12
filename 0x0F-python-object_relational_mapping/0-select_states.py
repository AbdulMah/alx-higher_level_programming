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
    if len(argv) >= 4:
        db_connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM states ORDER BY id ASC;')
        results = cursor.fetchall()
        for result in results:
            print(result)
        db_connection.close()
