#!/usr/bin/python3
""" This module takes an argument and displays all values states
    database hbtn_0e_0_usa WHERE name matches the argument.
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
            "SELECT * FROM states WHERE\
                    name = %s ORDER BY states.id ASC;", (state_name, ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    conn.close()

