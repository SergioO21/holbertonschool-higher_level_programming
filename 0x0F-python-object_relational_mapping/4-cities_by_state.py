#!/usr/bin/python3
""" Lists all cities from the database hbtn_0e_4_usa. """

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
                SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY id ASC""")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db_conn.close()


if __name__ == "__main__":
    main()
