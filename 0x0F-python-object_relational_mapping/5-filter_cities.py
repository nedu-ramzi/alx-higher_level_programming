#!/usr/bin/python3
"""script that takes in the name of a state as an argument
    and lists all cities of that state,
    using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    
    curr = db.cursor()
        curr.execute("SELECT cities.name FROM cities JOIN states ON 
                     cities.state_id = states.id 
                     WHERE states.name = '{}';".format(sys.argv[4]))
        states = curr.fetchall()

        print(", ".join(city[0] for city in states))
