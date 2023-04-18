#!/usr/bin/python3
"""
    Lists all City objects from the database hbtn_0e_101_usai
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

    s = session.query(State).join(City).order_by(City.id).all()

    for state in s:
        for city in state.cities:
            print('{}: {} -> {}'.format(city.id, city.name, state.name))
