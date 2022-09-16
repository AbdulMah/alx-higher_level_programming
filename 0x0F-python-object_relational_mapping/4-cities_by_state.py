#!/usr/bin/python3
""" This module lists all the cities from the
    database hbtn_0e_0_usa.
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
    cur.execute("SELECT cities.id,\
                cities.name, states.name FROM cities\
                INNER JOIN states ON\
                cities.state_id=states.id ORDER BY cities.id;")
    query_rows = cur.fetchall()
    for city in query_rows:
        print(city)
    cur.close()
    conn.close()



