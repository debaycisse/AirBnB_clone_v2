#!/usr/bin/python3
"""This module houses the definition of a class that
processes data when the db storage engine"""
from sqlalchemy import (create_engine)
from models.base_model import Base
from os import getenv
from sqlalchemy.orm import sessionmaker
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class DBStorage:
    """Defines the class for the db storage engine type"""
    __engine =  None
    __session = None

    def __init__(self):
        """Defines the constructor class for the DBStorage class"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Fetches a given class' instances or all instances
        if no specific class is given.

        Args:
            cls - the given class name

        Returns:
            a dictionary that contains both a key and value
            of the specific or all instances
        """
        classes = {'Amenity': Amenity, 'City': City, 'Place': Place,
                   'Review': Review, 'State': State, 'User':  User}
        dictionary = {}
        if  cls is None:
            for obj in self.__session.query(Amenity, City, Place,
                                            Review, State, User).all():
                key = obj.to_dict()['__class__'] + '.' + obj.id
                dictionary.update({key: obj})
        else cls in classes:
            for obj in self.__session.query(cls).all():
                key = obj.to_dict()['__class__'] + '.' + obj.id
                dictionary.update({key: obj})
        else:
            print("The passed class does not exist")
            return
        return dictionary

    def new(self, obj):
        """Adds a given object to the current database session

        Args:
            obj - object to be added to the current database session
        """
        self.__session.add(obj)
