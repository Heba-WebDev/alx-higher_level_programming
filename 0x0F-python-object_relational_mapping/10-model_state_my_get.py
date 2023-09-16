#!/usr/bin/python3
"""
Lists all State objects containing
the argument
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def list_arg_state_obj():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    rows = session.query(State).all()

    result = ""

    for i in rows:
        if sys.argv[4] in i.__dict__['name']:
            result = i.__dict__['id']

    if result != "":
        print(result)
    else:
        print("Not Found")

    session.close()


if __name__ == "__main__":
    list_arg_state_obj()
