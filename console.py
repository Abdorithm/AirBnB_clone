#!/usr/bin/python3
"""Defines the HBNBCommand class"""
import cmd
import os

class HBNBCommand(cmd.Cmd):
    """Represent HBNBCommand class"""
    prompt = "(hbnb) "
    def do_EOF(self, line):
        """Exit the program"""
        return True

    def do_quit(self, line):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing if line is empty"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
