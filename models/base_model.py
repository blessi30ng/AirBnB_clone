#!/usr/bin/python3
"""
class basemodel defines all common attributes/methods for other classes
"""

from uuid import uuid4
from datetime import datetime

class BaseModel():
    """
    Represents basemodel
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization of basemodel class
        """
        format_for_date = %Y-%m-%dT%H:%M:%S.%f
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(value, format_for_date)
                elif "updated_at" == key:
                    self.updated_at == datetime.strptime(value, format_for_date)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Return class name, id , dict
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
