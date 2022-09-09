#!/usr/bin/python3
""" This module lists all the states from the
    database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def main():
    """
        Function containing code to select all the states by id
        from the database.
    """

    # Create a database connection
    conn = MySQLdb.connect(
                hostname="localhost", port=3306, username=sys.argv[1],
                password=sys.argv[2], db_name=sys.argv[3], charset="utf8mb4"
            )
    cur = conn.cursor()
    # Select states
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
