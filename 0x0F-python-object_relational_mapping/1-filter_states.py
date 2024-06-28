#!/usr/bin/python3
"""
This script lists all the states with
a `name` starting with  letter `N`
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Connect to the database, execute a query to retrieve all states
    with names starting with 'N', and print the results.
    """
    connection = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    connection.close()

