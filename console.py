#!/usr/bin/python3
"""Defines the HBNBCommand class"""
import cmd
import os
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Represent HBNBCommand class"""
    prompt = "(hbnb) "
    __classes = {
            "BaseModel"
    }
    def do_EOF(self, line):
        """Exit the program"""
        return True

    def do_quit(self, line):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing if line is empty"""
        pass

    def do_create(self, line):
        """Create an instance of Class and prints the id.
        Usage: Create <class name>"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        print(eval(args[0])().id)
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances.
        Usage: all <class name>"""
        args = line.split()
        if len(args) != 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        objs = []
        for obj in storage.all().values():
            if len(args) == 0:
                objs.append(obj.__str__())
            elif obj.__class__.__name__ == args[0]:
                objs.append(obj.__str__())
        print (objs)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
