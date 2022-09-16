#!/usr/bin/python3
"""lists all city objects from the database hbtn_0e_6_usa"""


if __name__ == "__main__":
    from sys import argv
    from model_state import State
    from model_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(argv[1], argv[2], argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State) \
            .filter(City.state_id == State.id) \
            .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
