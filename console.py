#!/usr/bin/python3
"""Interactive python console for Airbnb Project"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Defines commands for our console"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the command line"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the command line"""
        print()
        return True
    
    def emptyline(self):
       pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
