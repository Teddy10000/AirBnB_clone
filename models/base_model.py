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
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)