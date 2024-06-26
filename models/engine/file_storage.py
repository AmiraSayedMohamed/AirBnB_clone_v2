#!/usr/bin/python3
"""Defines the FileStorage engine"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Represents a file storage engine"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects"""
        if cls:
            return {key: val for key, val in self.__objects.items() if isinstance(val, cls)}
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary"""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as f:
            json.dump({key: val.to_dict() for key, val in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
                for key, val in objs.items():
                    cls_name = val['__class__']
                    self.__objects[key] = eval(cls_name)(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from the storage dictionary"""
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Calls reload method for deserializing the JSON file"""
        self.reload()

