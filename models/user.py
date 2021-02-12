#!/usr/bin/python3
"""Module User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class defining a User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
