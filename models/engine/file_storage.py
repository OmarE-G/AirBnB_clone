#!/usr/bin/python3
""" The file storage module """
from models.base_model import BaseModel
import json
import os


class FileStorage:
    """ file storage file """
    __file_path = 'file.json'
    __objects = dict()


    def __init__(self):
        """ constructor function """
        pass

    def new(self, obj):
        """ funcion to save objects with their ids """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ serilize objects in __objects
        (serialization cannot deal with class or instance. therefore, we converty them to a 
        familar data type like dict throught to_dict() function --implemented before--
        and path the dict to  a json file __file_path to save permenatly"""
        json_value = None
        for key, value in FileStorage.__objects:
            value = FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, 'w', encoding='UTF-8') as f:
            json.dump(FileStorage.__objects, f)

    def all(self):
        """ return __objects """
        return (FileStorage.__objects)

    def reload(self):
        if (os.path.exists(FileStorage.__file_path)):
            DictObjs = dict()
            with open(FileStorage.__file_path, 'r', encoding='UTF-8') as f:
                DictObjs = json.load(f)
                


