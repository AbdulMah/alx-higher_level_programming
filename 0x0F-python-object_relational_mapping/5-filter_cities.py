#!/usr/bin/python3
"""
Lists all cities of a state on the DB hbtn_0e_4_usa
using the state as argument

"""


from sys import argv
import MySQLdb
if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host="localhost",
                         port=3306)
    state_name = argv[4]
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.name FROM cities WHERE state_id IN\
            (SELECT id FROM states WHERE name = %s)\
            ORDER BY cities.id;", (state_name, ))
    query_rows = cursor.fetchall()
    print(', '.join([x[0] for x in query_rows]))
    cursor.close()
    db.close()
