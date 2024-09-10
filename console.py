#!/usr/bin/python3
"""
This module defines the entry point for the command interpreter.
"""
import cmd
import json
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()  # To print a newline when EOF is entered (Ctrl+D)
        return True

    def emptyline(self):
        """Do nothing on empty input."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id."""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg
        if class_name not in ["BaseModel"]:  # Add other classes here if needed
            print("** class doesn't exist **")
            return

        obj = eval(f"{class_name}()")
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel"]:  # Add other classes here if needed
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return

        print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel"]:  # Add other classes here if needed
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        obj = storage.all().pop(key, None)
        if not obj:
            print("** no instance found **")
            return

        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        args = arg.split()
        if len(args) == 0:
            objs = storage.all()
        else:
            class_name = args[0]
            if class_name not in ["BaseModel"]:  # Add other classes here if needed
                print("** class doesn't exist **")
                return
            objs = {k: v for k, v in storage.all().items() if k.startswith(class_name)}

        print([str(obj) for obj in objs.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = arg.split()
        if len(args) < 3:
            print("** class name missing **" if len(args) < 1 else "** instance id missing **" if len(args) < 2 else "** attribute name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel"]:  # Add other classes here if needed
            print("** class doesn't exist **")
            return

        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3].strip('"')
        setattr(obj, attr_name, attr_value)
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
