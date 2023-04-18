#!/usr/bin/python3
"""
    lists all State objects, and corresponding City objects, contained
    from the database database hbtn_0e_100_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == '__main__':
    """Connection arguments"""
    user = sys.argv[1]
    pasword = sys.argv[2]
    dbname = sys.argv[3]

    """start the engine"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, pasword, dbname), pool_pre_ping=True)

    """create all tables stored in this metadata"""
    Base.metadata.create_all(engine)

    """create a configured session class"""
    Session = sessionmaker(bind=engine)

    """create a session instance"""
    session = Session()

    s = session.query(State).outerjoin(City).order_by(State.id, City.id).all()

    for state in s:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
