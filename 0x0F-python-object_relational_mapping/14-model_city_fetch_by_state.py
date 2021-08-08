#!/usr/bin/python3
""" Prints all City objects from the database hbtn_0e_14_usa """

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

    for state, city in session.query(State, City).filter(
            City.state_id == State.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()

    session.close()


if __name__ == "__main__":
    main()
