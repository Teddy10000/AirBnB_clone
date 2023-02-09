#!/usr/bin/python3
import datetime
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
        
    """ This the storage engine for the project
        Class Methods involve:
            all: Returns the object
            new: updates the dictionary id
            save: Serializes, or converts Python objects into JSON strings
            reload: Deserializes, or converts JSON strings into Python objects.
        Class Attributes:
            __file_path (str): The name of the file to save objects to.
            __objects (dict): A dictionary of instantiated objects.
            class_dict (dict): A dictionary of all the classes.
        """
    __file_path = ""
    __objects = ""
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}
    
    
    def all(self):
        "Return the objects"
        return self.__objects
    
    def new(self,instance):
        "create a new dictionary of the object instances"
        
        if instance:
            
            key = f"{instance._class_._name}.{instance.id}"
            "Turning the instance into dictionary"
            self.__objects[key] = instance
        
        
    def save(self):
            
        "turn into a dictionary first"
        dic = {}
            
        for key ,obj in self.__objects.items():
            dic[key] = obj.to_dict()
                
        with open(self.file_path, 'w',encoding='utf8') as f:
            json.dump(dic, f)
            
    def reload(self):
        
        "how to deserialise json strings into python objects"
        "from json turn into dictionary and then into objects using th"
        "First access the json data"
        with open(self.file_path, 'r',encoding='utf8') as f:
            new_data = json.load(f)
            
        for key , value in new_data.items(): 
            obj_class = self.class_dict[value['__class__']]
            obj_args = {k: v for k, v in value.items() if k != '__class__'}
            obj = obj_class(**obj_args)
            self.__objects[key] = obj
            
        
        
        
            
                