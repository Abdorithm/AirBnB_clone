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

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id.
        Usage: show BaseModel 1234-1234-1234."""
        args = line.split()
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
            return
        print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (saves the change into the JSON file).
        Usage: destroy BaseModel 1234-1234-1234."""
        args = line.split()
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
            return
        del obj_dict["{}.{}".format(args[0], args[1])]
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances.
        Usage: all <class name>"""
        args = line.split()
        if len(args) != 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        all_obj = []
        for obj in storage.all().values():
            if len(args) == 0:
                all_obj.append(obj.__str__())
            elif obj.__class__.__name__ == args[0]:
                all_obj.append(obj.__str__())
        if all_obj:
            print(all_obj)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id.
        Usage: update <class name> <id> <attribute name> \"<attribute value>\"
        """
        args = line.split()
        obj_dict = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            attribute_type = type(getattr(obj, args[2]))
            setattr(obj, args[2], attribute_type(args[3]))
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
