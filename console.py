import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.place import Place
import shlex

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to JSON file and prints the id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "State", "Place"]:  # Adjust as per your supported classes
            print("** class doesn't exist **")
            return
        
        # Prepare kwargs for object creation
        kwargs = {}
        for pair in args[1:]:
            if '=' not in pair:
                continue
            key, value = pair.split('=', 1)
            key = key.strip()
            value = value.strip()
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1].replace('_', ' ')
            elif '.' in value:
                try:
                    value = float(value)
                except ValueError:
                    continue
            else:
                try:
                    value = int(value)
                except ValueError:
                    continue
            kwargs[key] = value

        # Create the object
        new_instance = eval(class_name)(**kwargs)
        new_instance.save()
        print(new_instance.id)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

