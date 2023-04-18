#!/usr/bin/python3
"""
    script that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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

    """define the new state"""
    newState = State(name='Louisiana')

    """add the new state"""
    session.add(newState)

    """save the changes"""
    session.commit()

    print(newState.id)
