#!/usr/bin/python3
'''script for task 9'''

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
                           sys.argv[1], sys.argv[2], 'localhost', '3306', sys.argv[3]),
                           pool_pre_ping=True, poolclass=NullPool)
    Session = sessionmaker(bind=engine)
    local_session = Session()
    a_states = local_session.query(State).filter(
        State.name.op('regexp')('.*a+.*')
    ).order_by(State.id)
    local_session.close()
    engine.dispose()

    if a_states:
        for state in a_states:
            print('{}: {}'.format(state.id, state.name))
