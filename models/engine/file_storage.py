#!/usr/bin/python3
""" The file storage module """
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
        key = f"{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serilize objects in __objects
        (serialization cannot deal with class
        or instance. therefore, we converty them to a
        familar data type like dict throught to_dict()
        function --implemented before--
        and path the dict to  a json file __file_path to save permenatly"""
        json_dict = dict()
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='UTF-8') as f:
            json.dump(json_dict, f)

    def all(self):
        """ return __objects """
        return (self.__objects)

    def reload(self):
        from models.base_model import BaseModel

        if (os.path.exists(self.__file_path)):
            if os.path.getsize(self.__file_path) > 0:
                with open(self.__file_path, 'r', encoding='UTF-8') as f:
                    DictObjs = json.load(f)

                for value in DictObjs.values():
                    self.new(BaseModel(value))
