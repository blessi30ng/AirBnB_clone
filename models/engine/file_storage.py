#!/usr/bin/python3
"""file storage for the airbnb clone project"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.state import State

class FileStorage:
    """
    represebtation for storage engine for airbnb clone project
    """
    __file_path = 'file.json'
    __object = {}
    class_dict = {"BaseModel": BaseModel, "User": User,
            "State": State, "City": City, "Amenity": Amenity, "Place": Place, 
            "Review": Review}

    def all(self):
        """
        Returns dictionary
        """
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        dic_storage = {}

        for key, obj in self.__objects.items():
            dic_storage[key] = obj.to_dict
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(dic_storage, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_dic_storage = json.load(f)
            for key, value in new_dic_storage.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            return
