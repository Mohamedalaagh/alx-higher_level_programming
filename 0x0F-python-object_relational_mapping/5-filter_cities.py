#!/usr/bin/python3
"""
This script takes in the name of a state as an argument
and lists all cities of that state,
using the database `hbtn_0e_4_usa`.
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    Connect to the MySQL database and fetch cities for a given state.
    """

    connection = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {'state_name': argv[4]})
        result = cursor.fetchall()

    if result is not None:
        print(", ".join([city[1] for city in result]))
