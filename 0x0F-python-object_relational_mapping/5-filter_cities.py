#!/usr/bin/python3
""" Takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa
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
                SELECT cities.name
                FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                WHERE states.name LIKE BINARY %s
                ORDER BY cities.id ASC""", (argv[4], ))

    result = ""

    for row in cur.fetchall():
        result += row[0] + ", "

    print(result[0:-2])

    cur.close()
    db_conn.close()


if __name__ == "__main__":
    main()
