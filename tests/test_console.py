#!/usr/bin/python3
"""Unittest for console.py"""
import unittest
from io import StringIO
from console import HBNBCommand
from models import storage
from unittest.mock import patch
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import re
import inspect
import console
import pep8
import os


class TestBaseDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")


class TestConsole(unittest.TestCase):
    """Tests for the console"""
    classes = {"Amenity": Amenity, "City": City, "BaseModel": BaseModel,
               "Place": Place, "Review": Review, "State": State, "User": User}

    def test_help_doc(self):
        """Tests helps doc exists"""
        cmds = ["create", "quit", "EOF", "show", "destroy",
                "all", "update", "count"]
        for cmd in cmds:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help {}".format(cmd))
                self.assertTrue(len(str(f.getvalue())) > 1)

    def test_class_missing_error(self):
        """Tests class missing error"""
        cmds = ["create", "show", "destroy",
                "update"]
        error_msg = "** class name missing **\n"
        for cmd in cmds:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{}".format(cmd))
                self.assertEqual(error_msg, f.getvalue())

    def test_class_doesnt_exist_error(self):
        """Tests class doesn't exist error"""
        cmds = ["create", "show", "destroy",
                "all", "update"]
        error_msg = "** class doesn't exist **\n"
        for cmd in cmds:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{} MyClass".format(cmd))
                self.assertEqual(error_msg, f.getvalue())

    def test_id_missing_error(self):
        """Tests id missing error"""
        cmds = ["show", "destroy",
                "update"]
        error_msg = "** instance id missing **\n"
        for cmd in cmds:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{} BaseModel".format(cmd))
                self.assertEqual(error_msg, f.getvalue())

    def test_no_instance_found_error(self):
        """Tests no instance found error"""
        cmds = ["show", "destroy", "update"]
        error_msg = "** no instance found **\n"
        for cmd in cmds:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{} BaseModel 1234".format(cmd))
                self.assertEqual(error_msg, f.getvalue())

    def test_update_errors(self):
        """Tests update errors"""
        mod = BaseModel()
        error_msg = "** attribute name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update BaseModel {}".format(mod.id))
                self.assertEqual(error_msg, f.getvalue())
        error_msg = "** value missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update BaseModel {} name".format(mod.id))
                self.assertEqual(error_msg, f.getvalue())

    def test_create(self):
        """Test create command"""
        for Class in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(Class))
                self.assertTrue(len(str(f.getvalue())) > 1)

    def test_show(self):
        """Test show command"""
        for key in self.classes.keys():
            inst = self.classes[key]()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show {} {}".format(key, inst.id))
                self.assertEqual((str(inst) + "\n"), f.getvalue())

    def test_destroy(self):
        """Test destroy command"""
        for key in self.classes.keys():
            inst = self.classes[key]()
            ID = inst.id
            HBNBCommand().onecmd("destroy {} {}".format(key, ID))
            error_msg = "** no instance found **\n"
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show {} {}".format(key, inst.id))
                self.assertEqual(error_msg, f.getvalue())

    def test_all(self):
        """Test all command"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        for key in self.classes.keys():
            inst = self.classes[key]()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("all {}".format(key))
                self.assertTrue(str(inst) in f.getvalue())

    def test_update(self):
        """Test update command"""
        for key in self.classes.keys():
            inst = self.classes[key]()
            inst.richest_man = "Jeff Bezos"
            HBNBCommand().onecmd("update {} {} \
richest_man 'Elon Musk'".format(key, inst.id))
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show {} {}".format(key, inst.id))
                for k in inst.__dict__.keys():
                    self.assertTrue(str(k) in f.getvalue())

    def test_count(self):
        """Test count command"""
        for key in self.classes.keys():
            count = 0
            for Class in storage.all():
                if key in Class:
                    count += 1
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{}.count()".format(key))
                self.assertEqual(int(f.getvalue()), count)

    def test_show_v2(self):
        """Test show command"""
        for key in self.classes.keys():
            inst = self.classes[key]()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{}.show({})".format(key, inst.id))
                self.assertEqual((str(inst) + "\n"), f.getvalue())

    def test_all_v2(self):
        """Test all command"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        for key in self.classes.keys():
            inst = self.classes[key]()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{}.all()".format(key))
                self.assertTrue(str(inst) in f.getvalue())

    def test_destroy_v2(self):
        """Test destroy command"""
        for key in self.classes.keys():
            inst = self.classes[key]()
            ID = inst.id
            HBNBCommand().onecmd("{}.destroy({})".format(key, ID))
            error_msg = "** no instance found **\n"
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show {} {}".format(key, inst.id))
                self.assertEqual(error_msg, f.getvalue())

    def test_update_v2(self):
        """Test update command"""
        for key in self.classes.keys():
            inst = self.classes[key]()
            inst.richest_man = "Jeff Bezos"
            HBNBCommand().onecmd("{}.update({}, \
richest_man, 'Elon Musk')".format(key, inst.id))
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show {} {}".format(key, inst.id))
                for k in inst.__dict__.keys():
                    self.assertTrue(str(k) in f.getvalue())
