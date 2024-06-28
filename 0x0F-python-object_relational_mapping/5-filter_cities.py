#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    db_connection = db.connect(host="localhost", port=3306,
                               user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connection.cursor()

    db_cursor.execute(
        "SELECT cities.name FROM cities JOIN states ON \
                cities.state_id = states.id\
                WHERE states.name = %s ORDER BY cities.id ASC", (argv[4],))
    cities = db_cursor.fetchall()

    print(", ".join([city[0] for city in cities]))

    db_cursor.close()
    db_connection.close()
