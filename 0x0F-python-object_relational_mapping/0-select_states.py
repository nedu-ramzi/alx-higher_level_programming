#!/usr/bin/python3
"""Lists all the states from the database hbrn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], \
            db=sys.argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states;")
    states = curr.fetchall()

    for state in states:
        print(state)
