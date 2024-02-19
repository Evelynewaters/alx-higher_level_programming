#!/usr/bin/python3
"""
This script takes in an arg and
displays all values in the states
where `name` matches the arg
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
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))
    rows = cus.fetchall()

    for row in rows:
        print(row)
