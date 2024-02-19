#!/usr/bin/python3
"""
Takes arg displays values in states
where `name` matches the arg
from the db `hbtn_0e_0_usa`.
Is safe frm MySQL injections!
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

    with db.cursor() as cus:
        cus.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, {
            'name': argv[4]
        })

        rows = cus.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
