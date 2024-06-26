from models.base_model import BaseModel

class Amenity(BaseModel):
    name = str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

