#!/usr/bin/python3
"""Module Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class defining a Review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
