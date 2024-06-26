#!/usr/bin/python3
""" Console Module """
import cmd
from datetime import datetime
import re

from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit(0)

    def help_quit(self):
        """ Prints the help documentation for quit """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        exit(0)

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        return False

    def do_create(self, args):
        """ Creates an object of any class"""

        # Check for missing class name
        if not args:
            print("** class name missing **")
            return

        # Validate class name
        class_name = args.split()[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        # Extract arguments (if any)
        args = args.split(maxsplit=1)[1] if ' ' in args else ''

        # Create the object with appropriate arguments
        try:
            new_instance = self.classes[class_name]()
            # Use dictionary comprehension for flexible attribute handling
            new_instance.__dict__ = {key: value for key, value in parse_args(args)}
            new_instance.save()
            print(f"{class_name} created: {new_instance.id}")
        except ValueError as e:
            print(f"** {e} **")

    def do_show(self, args):
        """ Method to show an individual object """

        # Extract class and id
        class_name, obj_id = parse_args(args)

        # Validate class name and object existence
        if not class_name or class_name not in self.classes:
            print("** class doesn't exist **")
            return
        key = f"{class_name}.{obj_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        # Print the object
        print(storage.all()[key])

    def do_destroy(self, args):
        """ Destroys a specified object """

        # Extract class and id
        class_name, obj_id = parse_args(args)

        # Validate class name and object existence
        if not class_name or class_name not in self.classes:
            print("** class doesn't exist **")
            return
        key = f"{class_name}.{obj_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        # Delete and save
        del storage.all()[key]
        storage.save()
        print(f"{class_name} deleted")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""

        # Filter objects based on class name (if provided)
        objects = [str(obj) for obj in storage.all().values() if not args or obj.__class__.__name__ == args]
        print(objects)

    def do_count(self, args):
        """Count current number of class instances"""

        # Count objects matching the class name (if provided)
        count = sum(1 for obj in storage.all().values() if not args or obj.__class__.__name__ == args)
        print(count)

