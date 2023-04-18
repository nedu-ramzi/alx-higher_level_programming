#!/usr/bin/python3
"""Class definition of a State and an instance Base"""
from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Represents a state class that inherits a declarative base"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
