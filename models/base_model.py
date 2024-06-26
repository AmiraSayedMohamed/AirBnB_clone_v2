import json
from models import storage

class FileStorage:
    """A file-based storage engine for AirBnB clone data."""

    def __init__(self, file_path="file.json"):
        self.file_path = file_path

    def all(self, cls=None):
        """Retrieves all objects from storage."""
        objects = []
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                for obj_val in data.values():
                    obj = cls(**obj_val) if cls else BaseModel(**obj_val)
                    objects.append(obj)
        except FileNotFoundError:
            pass
        return objects

    # ... other storage methods (save, new, delete, etc.)

