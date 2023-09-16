#!/usr/bin/python3
"""
Lists all cities of a state
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                    JOIN states ON cities.state_id = states.id\
                    AND states.name = '{:s}'\
                    ORDER BY cities.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    res = []
    for i in rows:
        res.append(i[0])
    print(", ".join(res))

    cur.close()
    db.close()
