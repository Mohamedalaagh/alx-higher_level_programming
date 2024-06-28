#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    # Connect to the MySQL database
    db_connection = db.connect(host="localhost", port=3306,
                               user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connection.cursor()

    # Formulate the SQL query
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
            ORDER BY states.id ASC".format(argv[4])
    db_cursor.execute(query)
    states = db_cursor.fetchall()

    # Print each state found
    for state in states:
        print(state)
