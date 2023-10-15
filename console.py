#!/usr/bin/python3
"""Defines the HBNBCommand class"""
import cmd
import os
import shlex
import models


class HBNBCommand(cmd.Cmd):
    """Represent HBNBCommand class"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing if line is empty"""
        pass

    def do_create(self, line):
        """Create an instance of Class and prints the id.
        Usage: Create <class name>"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            cls = models.classes_dict[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return

        print(cls().id)
        models.storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id.
        Usage: show <class name> <id>"""
        args = shlex.split(line)
        obj_dict = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in models.classes_dict:
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
        Usage: destroy <class name> <id>"""
        args = shlex.split(line)
        obj_dict = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in models.classes_dict:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
            return
        del obj_dict["{}.{}".format(args[0], args[1])]
        models.storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances.
        Usage: all <class name>"""
        args = shlex.split(line)
        if len(args) != 0 and args[0] not in models.classes_dict:
            print("** class doesn't exist **")
            return
        all_obj = []
        for obj in models.storage.all().values():
            if len(args) == 0:
                all_obj.append(obj.__str__())
            elif obj.__class__.__name__ == args[0]:
                all_obj.append(obj.__str__())
        print(all_obj)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id.
        Usage: update <class name> <id> <attribute name> \"<attribute value>\"
        """
        args = shlex.split(line)
        obj_dict = models.storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in models.classes_dict:
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
            attribute_type = type(getattr(obj, args[2], ''))
            setattr(obj, args[2], attribute_type(args[3]))
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
