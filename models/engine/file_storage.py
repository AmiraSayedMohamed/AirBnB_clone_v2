import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects by class."""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        else:
            return self.__objects

    def delete(self, obj=None):
        """Deletes an object from __objects if it exists."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def new(self, obj):
        """Adds a new object to __objects."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file."""
        serialized = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        cls_name, obj_id = key.split('.')
                        cls = eval(cls_name)
                        self.__objects[key] = cls(**value)
                except Exception:
                    pass

