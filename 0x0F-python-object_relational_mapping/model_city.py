#!/usr/bin/python3
"""Class definition of a city"""
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """Represents a city class that inherits a declarative base" from states"""

    __tablename__ = 'cities'

    id = Column(Integer, unique=True, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
