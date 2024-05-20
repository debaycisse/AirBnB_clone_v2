#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'),
                      nullable=False)
    name = Column(String(128), nullable=False)
    """id = Column(String(60), primary_key=True)"""

    def __init__(self, *args, **kwargs):
        """The constructor method for this class"""
        super().__init__(*args, **kwargs)
