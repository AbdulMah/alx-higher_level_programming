#!/usr/bin/python3
""" This module filters all the states from the
    database hbtn_0e_0_usa that start with upper N.
"""


if __name__ == "__main__":
    from sys import argv 
    import MySQLdb
    
    user, password, database = argv[1], argv[2], argv[3]
    conn = MySQLdb.connect(host='localhost', 
                           port=3306, 
                           user=user,
                           passwd=password, 
                           db=database)
    cur = conn.cursor()
    cur.execute('SELECT * FROM states ORDER BY states.id ASC;')
    query_rows = cur.fetchall()
    [print(state) for state in query_rows if state[1][0] == "N"]
    conn.close()