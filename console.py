#!/usr/bin/python3
"""This module contains console functions"""

from models.base_model import BaseModel
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
    def emptyline(self):
        """Does not execute anything wjen empty line is passed"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        if args:
            try:
                model_class = globals()[args]
                new = model_class()
                new.save()
                print(new.id)
            except KeyError:
                print("** class doesn't exist **")

        else:
            print("** class name missing **")
    
    def do_show(self, args):
        """
        Prints the string representation of an instance 
        based on the class name and id
        """
        if 



if __name__ == '__main__':
    HBNBCommand().cmdloop()
