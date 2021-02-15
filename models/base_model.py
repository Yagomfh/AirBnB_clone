#!/usr/bin/python3
"""Class BaseModel that defines all common
attributes/methods for other classes"""
import uuid
from datetime import datetime
import models


time_f = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Init method"""
        if len(kwargs) != 0:
            for key in kwargs.keys():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        kwargs[key] = datetime.strptime(kwargs[key], time_f)
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Str method"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        res = self.__dict__.copy()
        res["__class__"] = self.__class__.__name__
        res["created_at"] = res["created_at"].isoformat("T")
        res["updated_at"] = res["updated_at"].isoformat("T")
        return res
