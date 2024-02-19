#!/usr/bin/python3
"""
This script defines a State class and
base cls to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State cls
    Attr:
        __tablename__ (str): The table name of the cls
        id (int): The State id of the cls
        name (str): The State name of the cls
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
