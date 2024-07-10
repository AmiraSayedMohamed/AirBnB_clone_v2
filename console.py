#!/usr/bin/python3
""" Console Module """
import cmd
import sys
import uuid
import os
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
    """Console for the HBNB project"""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def preloop(self):
        """Pre-loop hook"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Pre-command hook"""
        if '.' in line and '(' in line and ')' in line:
            try:
                cls_cmd, remainder = line.split('.', 1)
                cmd_name, args = remainder.split('(', 1)
                args = args.strip(')')
                if cls_cmd in self.classes and cmd_name in self.dot_cmds:
                    cmd_str = f"{cmd_name} {cls_cmd} {args}"
                    return cmd_str
            except Exception:
                pass
        return line

    def postcmd(self, stop, line):
        """Post-command hook"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, arg):
        """Quit command to exit the console"""
        exit(0)

    def help_quit(self):
        """Help for the quit command"""
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """EOF command to exit the console"""
        exit(0)

    def help_EOF(self):
        """Help for the EOF command"""
        print("Exits the program without formatting\n")

    def emptyline(self):
        """Handle empty line input"""
        pass

    def do_create(self, arg):
        """Create an instance of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        cls_name = args[0]
        if cls_name not in self.classes:
            print("** class doesn't exist **")
            return

        attributes = {}
        for attr in args[1:]:
            key, value = self.parse_key_value(attr)
            if key and value:
                attributes[key] = value

        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            if 'id' not in attributes:
                attributes['id'] = str(uuid.uuid4())
            if 'created_at' not in attributes:
                attributes['created_at'] = str(datetime.now())
            if 'updated_at' not in attributes:
                attributes['updated_at'] = str(datetime.now())

            new_instance = self.classes[cls_name](**attributes)
        else:
            new_instance = self.classes[cls_name]()
            for key, value in attributes.items():
                if key not in ('id', 'created_at', 'updated_at', '__class__'):
                    setattr(new_instance, key, value)

        new_instance.save()
        print(new_instance.id)

    def help_create(self):
        """Help for the create command"""
        print("Creates a class of any type")
        print("[Usage]: create <className> <key=value> ...\n")

    def do_show(self, arg):
        """Show an instance of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        cls_name = args[0]
        if cls_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{cls_name}.{instance_id}"
        instance = storage.all().get(key)
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def help_show(self):
        """Help for the show command"""
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, arg):
        """Destroy an instance of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        cls_name = args[0]
        if cls_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{cls_name}.{instance_id}"
        if key in storage.all():
            storage.delete(storage.all()[key])
            storage.save()
        else:
            print("** no instance found **")

    def help_destroy(self):
        """Help for the destroy command"""
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, arg):
        """Show all instances of a class or all classes"""
        args = arg.split()
        objects = storage.all()
        if args:
            cls_name = args[0]
            if cls_name not in self.classes:
                print("** class doesn't exist **")
                return
            instances = [str(obj) for key, obj in objects.items() if key.startswith(cls_name)]
        else:
            instances = [str(obj) for obj in objects.values()]
        print(instances)

    def help_all(self):
        """Help for the all command"""
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, arg):
        """Count the number of instances of a class"""
        cls_name = arg.split()[0] if arg else None
        if cls_name in self.classes:
            count = sum(1 for key in storage.all() if key.startswith(cls_name))
            print(count)
        else:
            print("** class doesn't exist **")

    def help_count(self):
        """Help for the count command"""
        print("Usage: count <class_name>")

    def do_update(self, arg):
        """Update an instance of a class"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return

        cls_name = args[0]
        if cls_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{cls_name}.{instance_id}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return

        if len(args) == 3:
            attr_name, attr_value = self.parse_key_value(args[2])
            if attr_name and attr_value:
                setattr(instance, attr_name, attr_value)
        elif len(args) > 3:
            for key_value_pair in args[2:]:
                attr_name, attr_value = self.parse_key_value(key_value_pair)
                if attr_name and attr_value:
                    setattr(instance, attr_name, attr_value)

        instance.save()

    def help_update(self):
        """Help for the update command"""
        print("Updates an object with new information")
        print("Usage: update <className> <id> <key=value> ...\n")

    def parse_key_value(self, pair):
        """Parse key=value string"""
        if '=' not in pair:
            return None, None
        key, value = pair.split('=', 1)
        if value[0] == value[-1] == '"':
            value = value[1:-1].replace('_', ' ')
        elif '.' in value:
            try:
                value = float(value)
            except ValueError:
                return None, None
        else:
            try:
                value = int(value)
            except ValueError:
                return None, None
        return key, value


if __name__ == "__main__":
    HBNBCommand().cmdloop()
