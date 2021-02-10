#!/usr/bin/python3
"""Contains the FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        all_objs = {}
        for key in self.__objects:
            all_objs[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(all_objs, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
            for key in data:
                self.__objects[key] = BaseModel(**data[key])
        except:
            pass
