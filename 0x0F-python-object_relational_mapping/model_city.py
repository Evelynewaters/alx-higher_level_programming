#!/usr/bin/python3
"""
This script defs a City cls
to work with MySQLAlchemy ORM.
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City cls
    Attr:
        __tablename__ (str): The table name of cls
        id (int): The id of the cls
        name (str): The name of the cls
        state_id (int): The state the city belongs
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
