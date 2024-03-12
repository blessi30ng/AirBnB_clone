#!/usr/bin/python3
"""Hbnb console"""

import cmd
import models

import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """console class"""
    prompt = '(hbnb)'
    storage = models.storage

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("**no class**")
            return
        try:
            new_instance = models.classes[arg]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("**no class**")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** no class name **")
            return
        arg_list = arg.split()
        if arg_list[0] not in models.classes:
            print("** no class  **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        try:
            instance = models.storage.get(models.classes[arg_list[0]], arg_list[1])
            print(instance)
        except Exception as e:
            print("** instance not found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** no class name **")
            return
        arg_list = arg.split()
        if arg_list[0] not in models.classes:
            print("** no  class **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        try:
            instance = models.storage.get(models.classes[arg_list[0]], arg_list[1])
            instance.delete()
            models.storage.save()
        except Exception as e:
            print("** instance not  found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        arg_list = arg.split()
        if arg and arg_list[0] not in models.classes:
            print("** class doesn't exist **")
            return
        instances = models.storage.all()
        if arg:
            print([str(value) for key, value in instances.items() i
                f type(value).__name__ == arg_list[0]])
        else:
            print([str(value) for value in instances.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        if arg_list[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        try:
            instance = models.storage.get(models.classes[arg_list[0]], 
                    arg_list[1])
            if len(arg_list) < 3:
                print("** no attribute name **")
                return
            if len(arg_list) < 4:
                print("** value not found **")
                return
            setattr(instance, arg_list[2], eval(arg_list[3]))
            models.storage.save()
        except Exception as e:
            print("**  instance not  found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
