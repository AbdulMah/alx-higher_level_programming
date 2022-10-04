#!/usr/bin/python3
'''script for task 13'''

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
    states = local_session.query(State).filter(
                           State.name.op('regexp')('.*a+.*')
                           )

    for state in states:
        local_session.delete(state)
    local_session.commit()

    local_session.close()
    engine.dispose()
