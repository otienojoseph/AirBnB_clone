from models.engine.file_storage import FileStorage
import json
import unittest


class TestFileStorage(unittest.TestCase):

    # FileStorage can be initialized without any errors
    def test_initialize_without_errors(self):
        storage = FileStorage()
        self.assertIsNotNone(storage)

    # all() method returns an empty dictionary when no objects have been added
    def test_all_returns_empty_dictionary(self):
        storage = FileStorage()
        objects = storage.all()
        self.assertEqual(objects, {})

    # new() method adds an object to __objects dictionary with the correct key
    def test_new_adds_object_to_dictionary(self):
        storage = FileStorage()

        class TestObject:

            def __init__(self, id, name):
                self.id = id
                self.name = name

            def to_dict(self):
                return {'id': self.id, 'name': self.name}

        obj = TestObject(1, 'object')
        storage.new(obj)
        objects = storage.all()
        self.assertEqual(objects, {'TestObject.1': obj.to_dict()})

    # new() and all() methods can be used together to add and retrieve
    # objects from __objects dictionary
    def test_new_and_all_methods(self):
        storage = FileStorage()

        class Object1:
            def __init__(self, id, name):
                self.id = id
                self.name = name

            def to_dict(self):
                return {'id': self.id, 'name': self.name}

        class Object2:
            def __init__(self, id, name):
                self.id = id
                self.name = name

            def to_dict(self):
                return {'id': self.id, 'name': self.name}

        obj1 = Object1(1, 'object1')
        obj2 = Object2(2, 'object2')
        storage.new(obj1)
        storage.new(obj2)
        objects = storage.all()
        self.assertEqual(objects, {'Object1.1': obj1.to_dict(),
                                   'Object2.2': obj2.to_dict()})

    # save() method is called when __objects dictionary is empty
    def test_save_with_empty_dictionary(self):
        storage = FileStorage()
        storage.save()
        with open(storage._FileStorage__file_path, 'r') as file:
            data = json.load(file)
        self.assertEqual(data, {})

    # reload() method is called when file path does not exist
    def test_reload_with_nonexistent_file_path(self):
        storage = FileStorage()
        storage._FileStorage__file_path = "nonexistent_file.json"
        storage.reload()

    # save() and reload() methods can be used together to save and load
    # objects from a JSON file
    def test_save_and_reload_methods(self):
        storage = FileStorage()

        class Object:
            def __init__(self, id, name):
                self.id = id
                self.name = name

            def to_dict(self):
                return {'id': self.id, 'name': self.name}

        obj = Object(1, 'object')
        storage.new(obj)
        storage.save()
        storage.reload()
        objects = storage.all()
        self.assertEqual(objects, {'Object.1': obj.to_dict()})

    # new() method overwrites an existing object in __objects dictionary
    # with the same key
    def test_new_overwrites_existing_object(self):
        storage = FileStorage()

        class Object:
            def __init__(self, id, name):
                self.id = id
                self.name = name

            def to_dict(self):
                return {'id': self.id, 'name': self.name}

        obj1 = Object(1, 'object1')
        obj2 = Object(1, 'object2')
        storage.new(obj1)
        storage.new(obj2)
        objects = storage.all()
        self.assertEqual(objects, {'Object.1': obj2.to_dict()})
