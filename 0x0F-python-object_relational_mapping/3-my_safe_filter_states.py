#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument,
safe from SQL injection.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    db_connection = db.connect(host="localhost", port=3306,
                               user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connection.cursor()

    db_cursor.execute("SELECT * FROM states WHERE name = %s\
            ORDER BY states.id ASC", (argv[4],))
    states = db_cursor.fetchall()

    for state in states:
        print(state)
