#!/usr/bin/python3
""" Prints the first State object from the database hbtn_0e_6_usa """

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """ Main function """

    db_conn = {
            "host": "localhost",
            "port": 3306,
            "user": argv[1],
            "pass": argv[2],
            "db": argv[3],
            "charset": "utf8"
            }

    conn_format = 'mysql+mysqldb://{user}:{pass}@{host}:{port}/{db}'

    engine = create_engine(conn_format.format(**db_conn), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))

    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    main()
