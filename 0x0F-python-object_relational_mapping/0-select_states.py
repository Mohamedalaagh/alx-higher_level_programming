#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_USA`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database and retrieve the states
    from the database.
    """
    connection = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()
