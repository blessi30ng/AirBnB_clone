#!/usr/bin/python3
"""
Module for console
"""
"""Hbnb console"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Amenity",
                     "Place", "Review", "State", "City"]
    """console class"""
    prompt = '(hbnb)'
    storage = models.storage

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program.
        """
        """Exit the program"""
        print()
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def help_quit(self):
        """
        Quit command to exit the program
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        EOF command to exit the program
        """
        print("EOF (Ctrl+D) signal to exit the program.")

    def do_create(self, arg):
        """
        Create a new instance of BaseModel or User
        and save it to the JSON file.
        """
        if not arg:
            print("**no class**")
            return

        if arg not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(f"{arg}()")
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance
        based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
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

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
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

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")
        try:
            instance = models.storage.get(models.classes[arg_list[0]], arg_list[1])
            instance.delete()
            models.storage.save()
        except Exception as e:
            print("** instance not  found **")

    def do_all(self, arg):
        """
        Prints all instances of a class.
        """
        if not arg:
            print([str(obj) for obj in storage.all().values()])
            return

        if arg not in self.valid_classes:
            print("** class doesn't exist **")
            return

        objects = storage.all()
        instances = [str(obj) for key, obj in objects.items()
                     if key.startswith(arg + '.')]
        print(instances)
        instances = models.storage.all()
        if arg:
            print([str(value) for key, value in instances.items() i
                f type(value).__name__ == arg_list[0]])
        else:
            print([str(value) for value in instances.values()])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = objects[key]
        attribute_name = args[2]
        attribute_value = args[3]
        try:
            attribute_value = eval(attribute_value)
        except (NameError, SyntaxError):
            pass

        setattr(obj, attribute_name, attribute_value)
        obj.save()

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
