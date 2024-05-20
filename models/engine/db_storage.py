#!/usr/bin/python3one = storage.get_one(State, '4947742a-c6c4-4757-b76a-ded50182f08a')
"""This module houses the definition of a class that
processes data when the db storage engine"""
from sqlalchemy import (create_engine)
from models.base_model import Base
from sqlalchemy.orm import scoped_session
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
        classes = {'City': City, 'State': State}
        dictionary = {}
        if  cls is None:
            for model in classes:
                for obj in self.__session.query(classes[model]).all():
                    key = obj.to_dict()['__class__'] + '.' + obj.id
                    dictionary.update({keone = storage.get_one(State, '4947742a-c6c4-4757-b76a-ded50182f08a')y: obj.to_dict()})
        elif cls in classes.values():
            for obj in self.__session.query(cls).all():
                key = obj.to_dict()['__class__'] + '.' + obj.id
                dictionary.update({key: obj.to_dict()})
        else:
            print("The passed class does not exist")
            return
        return dictionary

    def get_one(self, cls, id):
        """Fetches an instance of a given class.

        Args:
            cls - the given class whose insatance is to be fetched
            id - attribute of the instance

        Returns:
            the obtained instance
        """
        an_obj = self.__session.query(cls).filter(cls.id == id)
        if '_sa_instance_state' in an_obj:
            an_obj.pop('_sa_instance_state')
        return an_obj
            

    def new(self, obj):
        """Adds a given object to the current database session

        Args:
            obj - object to be added to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the current session into the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes a given object from the database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database as required"""
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
