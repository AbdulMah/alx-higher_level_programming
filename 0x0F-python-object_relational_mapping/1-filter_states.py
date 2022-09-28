#!/usr/bin/python3
"""List all states with a name starting with upper N."""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host="localhost",
                         port=3306)
    cursor = db.cursor()
    cursor.execute(
        """SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC;""")
    lists = cursor.fetchall()
    for row in lists:
        if row[1][0] == 'N':
            print(row)

    cursor.close()
    db.close()
