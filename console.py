#!/usr/bin/python3
<<<<<<< HEAD
=======
"""Hbnb console"""

>>>>>>> 194c0f62dc121bbc2201038227ad36df16fb5e3b
import cmd
import models

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()  # print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = models.classes[arg]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
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
            instance = models.storage.get(models.classes[arg_list[0]], arg_list[1])
            print(instance)
        except:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
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
            instance = models.storage.get(models.classes[arg_list[0]], arg_list[1])
            instance.delete()
            models.storage.save()
        except:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        arg_list = arg.split()
        if arg and arg_list[0] not in models.classes:
            print("** class doesn't exist **")
            return
        instances = models.storage.all()
        if arg:
            print([str(value) for key, value in instances.items() if type(value).__name__ == arg_list[0]])
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
            instance = models.storage.get(models.classes[arg_list[0]], arg_list[1])
            if len(arg_list) < 3:
                print("** attribute name missing **")
                return
            if len(arg_list) < 4:
                print("** value missing **")
                return
            setattr(instance, arg_list[2], eval(arg_list[3]))
            models.storage.save()
        except:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
