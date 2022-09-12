#!/usr/bin/python3
"""lists the first State objects from the database hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

def main():
    """_summary_
    """
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(argv[1], 
                    argv[2], 
                    argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).first()
    if state is None:
        print("Nothing")
    print('{}: {}'.format(state.id, state.name))

if __name__ == "__main__":
    main()