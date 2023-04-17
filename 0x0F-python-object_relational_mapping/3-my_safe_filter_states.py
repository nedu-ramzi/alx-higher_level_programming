#!/usr/bin/python3
"""
    script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where
    name matches the argument
    and safe from SQL injection
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], 
                         db=sys.argv[3], port=3306)

    curr = db.cursor()
    curr.execute("SELECT * FROM states WHERE name = %s;", (sys.argv[4]))
    states = curr.fetchall()

    for state in states:
        print(state)
