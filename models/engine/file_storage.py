#!/usr/bin/python3
"""File Storage Class"""

from models.base_model import BaseModel
import json
import os


class FileStorage:
    """
        Attributes:
            Private:
                __file_path (string) - path to JSON file
                __objects (dict) - empty but will store objects
                by <class name>.id
        Methods:
            all(self) - returns dictionary objects
            new(self, obj) - sets in __objects the obj with
            key <obj class name>.id
            save(self) - serializes __objects to JSON file (path: __file_path)
            reload(self) - deserializes JSON file to __objects only if path
            exists otherwise do nothing
    """
    def __init__(self):
        """Init method"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns object"""
        return (self.__objects)

    def new(self, obj):
        """
            Sets in __objects the obj with key <obj class name>.id
            Args:
                obj (dict) - object to set
        """
        key = (obj.__class__.__name__ + "." + str(obj.id))
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
            Serializes self.__object into string
        """
        with open(self.__file_path, "a") as file:
            # serialize and dump
            json.dump(self.__objects, file)

    def reload(self):
        """
            Deserialize string into self.__object
        """
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, "r") as file:
                    line = file.readline()
                    while line:
                        self.__objects = json.loads(line)
                        line = file.readline()
            else:
                pass
        except FileNotFoundError as e:
            pass


baseModel = BaseModel()
model = FileStorage()
model.new(baseModel)
print(model.all())
