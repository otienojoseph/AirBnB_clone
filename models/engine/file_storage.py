#!/usr/bin/python3
"""File Storage Class"""

from base_model import BaseModel


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


baseModel = BaseModel()
model = FileStorage()
model.new(baseModel)
print(model.all())
