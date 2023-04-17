#!/usr/bin/python3
""Lists all the states from the database hbrn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states;")
    states = cursor.fetchall()

    for state in states:
        print(state)
