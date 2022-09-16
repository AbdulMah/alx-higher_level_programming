#!/usr/bin/python3
""" This module takes the name of a state as argument and displays all cities
    of that state, using the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    user, password, database, state_name = argv[1], argv[2], argv[3], argv[4]

    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=user,
                           passwd=password,
                           db=database)
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.name FROM cities WHERE state_id IN\
            (SELECT id FROM states WHERE name = %s)\
            ORDER BY cities.id;", (state_name, ))
    query_rows = cur.fetchall()
    print(', '.join([x[0] for x in query_rows]))
    conn.close()
