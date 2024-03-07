#!/usr/bin/python3
"""
Review class, subclass of basemodel
"""

from models.base_model import BaseModel

class Review(BaseModels):
    """
    Represents review
    """
    place_id = ""
    user_id = ""
    text = ""
