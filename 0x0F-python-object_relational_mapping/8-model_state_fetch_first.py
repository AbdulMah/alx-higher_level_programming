#!/usr/bin/python3
'''script for task 8'''

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
                           sys.argv[1], sys.argv[2], 'localhost', '3306', sys.argv[3]),
                           pool_pre_ping=True, poolclass=NullPool)
    Session = sessionmaker(bind=engine)
    local_session = Session()
    result = local_session.query(State).order_by(State.id).first()
    local_session.close()

    if result:
        print('{}: {}'.format(result.id, result.name))
    else:
        print('Nothing')
