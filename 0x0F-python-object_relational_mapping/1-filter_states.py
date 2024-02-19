#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the db `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the db and get the states
    from the db.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cus = db.cursor()
    cus.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    rows = cus.fetchall()

    for row in rows:
        print(row)
