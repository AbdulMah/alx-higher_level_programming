#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host="localhost",
                         port=3306)

    cursor = db.cursor()
    query = """SELECT * FROM states WHERE name = '%s' ORDER BY states.id ASC;"""
    cursor.execute(query,argv[4])
    lists = cursor.fetchall()
    for row in lists:
        if row[1] == argv[4]:
            print(row)

    cursor.close()
    db.close()
