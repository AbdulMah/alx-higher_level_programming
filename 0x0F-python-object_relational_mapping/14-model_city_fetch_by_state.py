#!/usr/bin/python3
""" kkkkkkkkkkkkkkkk
"""


if __name__ == '__main__':

    import sys
    from model_state import State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".format(
                           sys.argv[1], sys.argv[2], 'localhost', '3306', sys.argv[3]
                           ), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    local_session = Session()
    result = local_session.query(City, State).filter(
        City.state_id == State.id
    ).order_by(City.id).all()

    for row in result:
        print('{}: ({}) {}'.format(row[1].name, row[0].id, row[0].name))

    local_session.close()
    engine.dispose()
