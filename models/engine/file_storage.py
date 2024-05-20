#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage

        Args:
            cls - this is the class name whose
            instances are to be returned

        Returns:
            all instances of the passed class name
        """
        if cls is None:
            return FileStorage.__objects
        classes = {'Amenity': Amenity, 'BaseModel': BaseModel,
                   'City': City, 'Place': Place, 'Review': Review,
                   'State': State, 'User': User}
        if cls not in classes.values():
            print('Invalid class')
            return
        all_cls = {}
        cls_key = None
        for k in classes.keys():
            if classes[k] is cls:
                cls_key = k
                break
        for obj in FileStorage.__objects:
            if obj.split('.')[0] == cls_key:
                all_cls.update({obj: FileStorage.__objects[obj]})
        return all_cls

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def _update(self, obj):
        """updates an existing instance on the __objects"""
        key = obj.to_dict()['__class__'] + '.' + obj.id
        if key in FileStorage.__objects.keys():
            FileStorage.__objects[key] = obj

    def delete(self, obj=None):
        """deletes an existing instance that is stored in __objects

        Args:
            obj - the object or class instance that should be deleted
        """
        if obj is not None:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()

    def close(self):
        """closes an instance by reloading all exisitng instances"""
        self.reload()
