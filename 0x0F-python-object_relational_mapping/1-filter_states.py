#!/usr/bin/python3
"""
    lists all states with a name starting with N (upper N) from the
    database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    curr = db.cursor()
    curr.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    states = curr.fetchall()

    for state in states:
        print(state)
