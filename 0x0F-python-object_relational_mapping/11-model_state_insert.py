#!/usr/bin/python3
'''script for task 11'''

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
                           sys.argv[1], sys.argv[2], 'localhost', '3306', sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    local_session = Session()
    new_state = State(name='Louisiana')
    local_session.add(new_state)
    local_session.commit()

    print(new_state.id)
    local_session.close()
    engine.dispose()
