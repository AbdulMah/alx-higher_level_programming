#!/usr/bin/python3
'''script for task 12'''

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
                           sys.argv[1], sys.argv[2], 'localhost', '3306', sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    local_session = Session()
    state = local_session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    local_session.commit()

    local_session.close()
    engine.dispose()
