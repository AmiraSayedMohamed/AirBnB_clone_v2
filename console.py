#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = '(hbnb) '
    
    # Class dictionary for easy access to model classes
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        
        # Create a dictionary to hold the attributes and their values
        new_instance = self.classes[class_name]()
        for param in args[1:]:
            if '=' in param:
                key, value = param.split('=', 1)
                value = value.replace('_', ' ')
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1].replace('\\"', '"')
                else:
                    try:
                        if '.' in value:
                            value = float(value)
                        else:
                            value = int(value)
                    except ValueError:
                        continue
                setattr(new_instance, key, value)
        
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        storage.delete(storage.all()[key])
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        args = shlex.split(arg)
        if len(args) == 0:
            print([str(instance) for instance in storage.all().values()])
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        print([str(instance) for key, instance in storage.all().items() if key.startswith(class_name)])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        instance = storage.all()[key]
        if attr_value.startswith('"') and attr_value.endswith('"'):
            attr_value = attr_value[1:-1].replace('\\"', '"')
        else:
            try:
                if '.' in attr_value:
                    attr_value = float(attr_value)
                else:
                    attr_value = int(attr_value)
            except ValueError:
                pass
        setattr(instance, attr_name, attr_value)
        instance.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

