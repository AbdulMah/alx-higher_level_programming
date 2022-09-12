#!/usr/bin/python3
""" This module lists all the states from the
    database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv


def main():
    """
        Function containing code to filter all the states
        from the database.
    """

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
    conn = MySQLdb.connect(
                host="localhost", port=3306, user=argv[1],
                password=argv[2], db=argv[3], charset="utf8mb4"
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    #cur.close()
    conn.close()
