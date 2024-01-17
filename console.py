#!/usr/bin/python3
"""This module contains console functions"""

from models.base_model import BaseModel
from models import storage
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

    def do_create(self, arg):
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

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if arg:
            args = arg.split()
            try:
                cls = globals()[args[0]]
                if (len(args) < 2):
                    print("** instance id missing **")
                else:
                    storage.reload()
                    data_dict = storage.all()
                    key_id = args[0] + "." + args[1]

                    if data_dict.get(key_id) is not None:
                        print(data_dict[key_id])
                    else:
                        print("** no instance found **")
            except KeyError:
                print("** class doesn't exist **")           
        else:
            print("** class name missing **")

    def do_all(self, arg):
            """
            Prints string representation of all instances based on class name
            """
            if arg:
                args = arg.split()
            try:
                cls = globals()[args[0]]

                storage.reload()
                data_dict = storage.all()

                if isinstance(data_dict.get(args[0]), cls):
                    model = cls(data_dict)
                    model.__str__
            except KeyError:
                print("** class doesn't exist **")           
            else:
                print(data_dict)

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and id
        Save changes to JSON file
        """
        if arg:
            args = arg.split()
            try:
                cls = globals()[args[0]]
                if (len(args) < 2):
                    print("** instance id missing **")
                else:
                    storage.reload()
                    data_dict = storage.all()
                    key_id = args[0] + "." + args[1]

                    if data_dict.get(key_id) is not None:
                        del(data_dict[key_id])
                        storage.save()
                    else:
                        print("** no instance found **")
            except KeyError:
                print("** class doesn't exist **")           
        else:
            print("** class name missing **")




if __name__ == "__main__":
    HBNBCommand().cmdloop()
