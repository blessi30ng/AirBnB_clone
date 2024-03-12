#!/usr/bin/python3
"""
class basemodel defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """
    Represents basemodel
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization of basemodel class
        """
        format_for_date = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(value, 
                            format_for_date)
                elif "updated_at" == key:
                    self.updated_at == datetime.strptime(value, 
                            format_for_date)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return class name, id , dict
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, 
                self.id, self.__dict__)

    def __repr__(self):
        """
        Returns string representation of basemodel
        """
        return (self.__str__())

    def save(self):
        """
        Updates updated_at property with current time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        representation of dictionary of basemodel with str formats of times
        """
        t_dict = self.__dict__.copy()
        t_dict["created_at"] = self.created_at.isformat()
        t_dict["updated_at"] = self.updated_at.isformat()
        t_dict["__class__"] = self.__class.__name__
        return t_dict
