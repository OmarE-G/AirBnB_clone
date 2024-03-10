#!/usr/bin/python3
"""Interactive python console for Airbnb Project"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


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

    def do_create(self, line):
        """Creates an instance of the passed class name"""
        if not self.check_errors(line, class_only=1):
            cls = globals()[line]
            obj = cls()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """print instance based on class name and id"""
        if not self.check_errors(line):
            line = line.split()
            print(storage.all()[line[1]])

    def do_destroy(self, line):
        if not self.check_errors(line):
            line = line.split()
            del storage.all()[line[1]]
            storage.save()

    def do_all(self, line):
        if not line or not self.check_errors(line, class_only=1):
            print('[', end='')
            storage_items = storage.all().values()
            for i, obj in enumerate(storage_items):
                if (not line) or (obj.__class__.__name__ == line):
                    print(f"\"{obj}\"", end='')
                    if i < len(storage_items) - 1:
                        print(',', end=' ')
            print(']')

    def do_update(self, line):
        """update or add an attribute to instance"""
        if not self.check_errors(line, attr=1):
            line = line.split()
            print(line[1])
            obj = storage.all()[line[1]]  # get obj by its id as key
            att_type = type(line[2])
            new_att = att_type(line[3].strip('"'))
            setattr(obj, line[2], new_att)

    def check_errors(self, line, class_only=0, attr=0):
        """check for input errors - return False if no errors"""
        full_string = line
        line = line.split()

        if not line:
            print("** class name missing **")
            return True

        try:
            name = line[0] if not class_only else full_string
            globals()[name]
        except KeyError:
            print("** class doesn't exist **")
            return True

        if class_only:
            return False

        if len(line) < 2:
            print("** instance id missing **")
            return True
        try:
            storage.all()[line[1]]
        except KeyError:
            print("** no instance found **")
            return True

        if attr:
            if len(line) < 3:
                print("** attribute name missing **")
                return True
            if len(line) < 4:
                print("** value missing **")
                return True

        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
