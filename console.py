import re
import cmd, sys
from models.base_model import BaseModel
from shlex import split
from models.user import User
from models.amenity import Amenity
from models.city import City




class HBNBCommand(cmd.Cmd):
    intro = ""
    prompt = ' (hbnb) '
    
    
    
    def my_errors(self,line, num_args):
        classes = [Amenity , User , City , Amenity]
        messages = [
            "** class name missing **",
               "** class doesn't exist **",
               "** instance id missing **",
               "** no instance found **",
               "** attribute name missing **",
               "** value missing **"
                ]
        "splitting the line arguments"
        arg = line.split()  
        "checking if the class is present"
        if not line:
            print(f'{messages[1]}')
        
        "checking if the class exist and contains more than 1 argument"   
        if num_args >= 1 and arg[0] not in classes:
            print(messages[1])
            
        "check if the id isintance not missing"
            
        
    def do_quit(self , line):
        """This code quits the shell"""
        return True
    
    def do_EOF(self, line):
        """This code quits the shell"""
        return True
    
    def do_help(self,line):
        """Shows the various commands"""
        print("quit - Quit the program")
        print("EOF - Quit the program")
        print("  - Quit the program")
        
    def emptyline(self):
        "Nothing happens when you don't give it a command "
        pass
    
    def do_create(self,line):
        arg = line.split()
        if arg[1] == 0:
            print("class name missing")
      
    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
    
    
        
        
    
    
    



