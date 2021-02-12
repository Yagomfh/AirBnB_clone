#!/usr/bin/python3
"""Module City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class defining a City"""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """initializes City"""
        super().__init__(*args, **kwargs)
