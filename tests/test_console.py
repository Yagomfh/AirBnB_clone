#!/usr/bin/python3
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os.path
from os import path


