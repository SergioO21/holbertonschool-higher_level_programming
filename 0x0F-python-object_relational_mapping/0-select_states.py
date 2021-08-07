#!/usr/bin/python3

from sys import argv
import MySQLdb


def main():

    db_conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8")

    cur = db_conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db_conn.close()


if __name__ == "__main__":
    main()
