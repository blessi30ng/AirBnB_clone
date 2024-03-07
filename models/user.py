#!/usr/bin/python3
"""
class user, subclass of BaseModel
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    Represents user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
