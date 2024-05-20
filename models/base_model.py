#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from os import getenv

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model

        Args:
            args - is a list non-keyword arguments
            kwargs - is a list of keyword arguments
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for k, v in kwargs.items():
                not_cls = (k != '__class__')
                not_upd = (k != 'updated_at')
                not_crd = (k != 'created_at')
                if (not_cls and not_upd and not_crd):
                    setattr(self, k, v)
            time_f = '%Y-%m-%dT%H:%M:%S.%f'
            if kwargs['created_at']:
                self.created_at = datetime.strptime(kwargs['created_at'], time_f)
            if kwargs['updated_at']:
                self.updated_at = datetime.strptime(kwargs['updated_at'], time_f)
            if ('id' not in kwargs) or (kwargs['id'] is None):
                self.id = str(uuid.uuid4())
            if '__class__' in kwargs:
                del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models.__init__ import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            dictionary.pop('_sa_instance_state')
        return dictionary

    def delete(self):
        """Deletes the current instance or object of this class"""
        from models.__init__ import storage
        storage.delete(self)
