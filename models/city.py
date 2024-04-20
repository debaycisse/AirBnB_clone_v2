#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'),
                      nullable=False)
    name = Column(String(128), nullable=False)

"""    def __init__(self, *args, **kwargs):
        #The constructor method for this class#######
        super().__init__(args, kwargs)
        self.state_id = Column(String(60), ForeignKey('states.id'),
                               nullable=False)
        self.name = Column(String(128), nullable=False)"""
