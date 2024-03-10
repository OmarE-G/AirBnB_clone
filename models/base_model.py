#!/usr/bin/python3
""" base class file """


from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """ basemodel class for common attr """
    def __init__(self, *args, **kwargs):
        """ constructor """
        if (kwargs):
            for key, value in kwargs.items():
                if (key != '__class__'):
                    setattr(self, key, value)
                if (key == 'created_at' or key == 'updated_at'):
                    value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ str function """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ updates the datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ return dictionary of object in addition to class
        name with created_at and updated_at convested to string
        through iso format """
        dic = self.__dict__.copy()
        dic['id'] = self.id
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
