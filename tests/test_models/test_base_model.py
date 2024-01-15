#!/usr/bin/python3

from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4
import unittest
from models import storage


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

    # The generated id should be unique across multiple
    # instances of the BaseModel class.
    def test_unique_id_across_instances(self):
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    # The created_at and updated_at attributes should be set
    # to the same datetime value when the instance is created.
    def test_same_datetime_value(self):
        base_model = BaseModel()
        self.assertEqual(base_model.created_at, base_model.updated_at)

    # The created_at and updated at attributes are different
    # when instance is saved
    def test_base_model_save(self):
        base_model = BaseModel()
        original_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(base_model.updated_at, original_updated_at)

    # BaseModel is created with no kwargs
    def test_init_with_no_arguments(self):
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

    # BaseModel instance createed with kwargs
    def test_init_with_keyword_arguments(self):
        obj = BaseModel(id=uuid4(), created_at="2022-12-01T12:00:00.000000",
                        updated_at="2022-12-01T12:00:00.000000")
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

    # Raise error when given invalid datetime string
    def test_init_with_invalid_datetime_string(self):
        with self.assertRaises(ValueError):
            BaseModel(created_at="2022-13-01T12:00:00.000000",
                      updated_at="2022-13-01T12:00:00.000000")

    # BaseModel object is reloaded successfully
    def test_base_model_reload(self):
        storage.reload()
        self.assertIsNotNone(storage)
