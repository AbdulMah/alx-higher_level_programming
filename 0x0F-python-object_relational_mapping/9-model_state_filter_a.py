#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa that contain 'a'"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

def main():
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(argv[1], 
                    argv[2], 
                    argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id)
    for state in result:
        if "a" in state.name:
            print('{}: {}'.format(state.id, state.name))

if __name__ == "__main__":
    main()