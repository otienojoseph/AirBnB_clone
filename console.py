#!/usr/bin/python3
"""This module contains console functions"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Program that contains entry point for the command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Command to quit/exit the program"""
        return True

    def do_EOF(self, arg):
         """Command to quit/exit the program"""
         print()
         return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
