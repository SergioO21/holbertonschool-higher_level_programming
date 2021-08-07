#!/usr/bin/python3
""" Takes in arguments and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument. But this time,
    write one that is safe from MySQL injections!
"""

from sys import argv
import MySQLdb


def main():
    """ Main Function """

    db_conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8")

    cur = db_conn.cursor()

    cur.execute("""
                SELECT *
                FROM states
                WHERE name LIKE BINARY %s
                ORDER BY id ASC""", (argv[4], ))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db_conn.close()


if __name__ == "__main__":
    main()
