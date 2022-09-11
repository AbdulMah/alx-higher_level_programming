#!/usr/bin/python3
""" This module takes an argument and displays all values states
    database hbtn_0e_0_usa WHERE name matches the argument.
"""

import MySQLdb
from sys import argv


def main():
    """
        Function containing code to select the state provided
        in the argument and is implemented in a safe way to prevent
        an SQL injection.
    """

    # Create a database connection
    conn = MySQLdb.connect(
                host="localhost", port=3306, user=argv[1],
                password=argv[2], db=argv[3], charset="utf8mb4"
            )
    cur = conn.cursor()
    # Select states
    state_name = argv[4]
    cur.execute(
            "SELECT * FROM states WHERE\
                    name = %s ORDER BY states.id ASC;", (state_name, ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
