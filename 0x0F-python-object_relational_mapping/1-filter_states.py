#!/usr/bin/python3
""" This module filters all the states from the
    database hbtn_0e_0_usa that start with upper N.
"""

import MySQLdb
import sys


def main():
    """
        Function containing code to filter all the states by id
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
    [print(state) for state in query_rows if state[1][0] == "N"]
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
