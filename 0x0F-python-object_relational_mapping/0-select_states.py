#!/usr/bin/python3
"""script that lists all states from the
database hbtn_0e_0_usa
"""


if __name__=='__main__':
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host="localhost",
                         port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    conn.close()
