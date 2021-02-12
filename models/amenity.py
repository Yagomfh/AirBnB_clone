#!/usr/bin/python3
"""Module Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class defining a Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
