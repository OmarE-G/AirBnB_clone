#!/usr/bin/python3
"""Interactive python console for Airbnb Project"""
import cmd
from models import base_model

class HBNBCommand(cmd.Cmd):
    """Defines commands for our console"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the command line"""
        return True

    def do_EOF(self, line):
        """Signal    to exit the command line"""
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, name):
        """Creates an instance of the passed class name"""
        if name:
            if name != "BaseModel":
                print("** class doesn't exist **")
            else:
                print(base_model.BaseModel().id)
        else:
            print("** class name missing **")                             
       

if __name__ == '__main__':
    HBNBCommand().cmdloop()
