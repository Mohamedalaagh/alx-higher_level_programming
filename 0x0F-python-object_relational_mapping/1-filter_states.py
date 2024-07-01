#!/usr/bin/python3
"""
This script lists all states with a name starting with the letter 'N'
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    db_connection = db.connect(host="localhost", port=3306,
                               user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connection.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
        ORDER BY states.id ASC")

    states = db_cursor.fetchall()

    for state in states:
        print(state)
