#!/usr/bin/python3
"""Lists all city objects from the database hbtn_0e_14_usa"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_city import City

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

    """query all state objects and order by state id"""
    st_cy = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in st_cy:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
