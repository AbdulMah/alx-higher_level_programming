#!/usr/bin/python3
"""task"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
                           sys.argv[1], sys.argv[2], 'localhost', '3306', sys.argv[3]),
                           pool_pre_ping=True)
    state_name = sys.argv[4]
    Session = sessionmaker(bind=engine)
    local_session = Session()
    result = local_session.query(State).filter(
        State.name.like(state_name)
    ).first()
    local_session.close()
    engine.dispose()

    if result:
        print(result.id)
    else:
        print('Not found')
