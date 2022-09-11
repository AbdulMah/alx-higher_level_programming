#!/usr/bin/python3
""" Lists all States and corresponding Cities in the database hbtn_0e_101_usa.
     Usage: ./101-relationship_states_cities_list.py <mysql username> /
                                                 <mysql password> /
                                                 <database name>
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

def main():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], 
                                   argv[2], 
                                   argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))


if __name__ == "__main__":
    main()