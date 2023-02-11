#!/usr/bin/python3
"""
Custom base class for the entire project
"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Custom base for all the classes in the AirBnb console project
    Arttributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime
    Methods:
        __str__: prints the class name, id, and creates dictionary
        representations of the input values
        save(self): updates instance arttributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj
    """
    
    def __init__(self,*args,**kwargs):
        
        """Public instance artributes initialization
        after creation
        Args:
            *args(args): arguments
            **kwargs(dict): attrubute values
        """
        "Define the date format"
        DATE_FORMAT= '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            
            models.storage.new(self)
        "How to treat dictionary models loop through" 
        for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value) 
                
        "Returning a string instance"
        
        def __str__(self):
            return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)
            
            
        def save(self):
            """
            updates the public instance attribute
            updated_at with the current datetime
            """
            self.updated_at = datetime.now()
            models.storage.save()
            
            
        def to_dic(self):
            "returns dic of all the keys and values of _dic__"
            
            "unpacking the content of the __dic__ to new dic"
            dic = {**self.__dic__}
            
            "creating the class with 'key and changing the format of classes objects'"
            dic["__class__"] = type(self).__name__
            dic["created_at"] = dic["created_at"].isoformat()
            dic['updated_at'] = dic['updated_at'].isoformat()
            
            
            return dic
            
            
            
            
        