from models.base_model import BaseModel
from datetime import datetime


import unittest

class Test__Init__(unittest.TestCase):

    # Initializes a new instance of the BaseModel class.
    def test_initialization(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)

    # Generates a unique id for the instance using uuid4.
    def test_unique_id(self):
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    # None.
    def test_none(self):
        base_model = BaseModel()
        self.assertIsNone(base_model.__init__())

    # The generated id should be unique across multiple instances of the BaseModel class.
    def test_unique_id_across_instances(self):
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    # The created_at and updated_at attributes should be set to the same datetime value when the instance is created.
    def test_same_datetime_value(self):
        base_model = BaseModel()
        self.assertEqual(base_model.created_at, base_model.updated_at)