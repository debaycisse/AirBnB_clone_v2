#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class definition """
    __tablename__ = 'states'
    """id = Column(String(60), primary_key=True)"""
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City', backref='state',
            cascade='all, delete-orphan')

        def __init__(self, *args, **kwargs):
            """The contsructor method for this class"""
            super().__init__(*args, **kwargs)
    else:
        @property
        def cities(self):
            """Gets a list of city instances whose state_id is as equal
            as this current instance or self"""
            from models.city import City
            from models.__init__ import storage

            matched_cities = []
            for v in storage.all(City).__dict__.values():
                if v.state_id == self.id:
                    matched_cities.append(v)
            return matched_cities
