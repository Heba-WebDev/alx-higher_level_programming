#!/usr/bin/python3
"""
Prints all City objects from
the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine, Table, Column, Integer, String
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cty = session.query(State, City).join(City).order_by(City.id)
    for city, state in cty:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
