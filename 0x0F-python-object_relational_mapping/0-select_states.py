#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':
    import sys 
    import MySQLdb
    
    #user, password, database = argv[1], argv[2], argv[3]
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    conn.close()
