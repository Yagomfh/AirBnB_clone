#!/usr/bin/python3
"""Unit tests for base model"""
import unittest
import pep8
import inspect
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from io import StringIO
import os
from datetime import datetime


class TestBaseDocs(unittest.TestCase):
    """Tests to check the documentation and style of FileStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """Test that models/base.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

class TestFileStorage(unittest.TestCase):
    """Class to test FileStorage class"""
    def test_all_returns_dict(self):
        """Test that all returns the FileStorage.__objects attr"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

    def test_save_and_load(self):
        os.remove("file.json")
        with self.assertRaises(Exception):
            with open("file.json", "r") as f:
                self.assertEqual(0, len(f.read()))
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        with open("file.json", "r") as f:
            self.assertNotEqual(0, len(f.read()))
