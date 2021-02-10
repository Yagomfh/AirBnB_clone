#!/usr/bin/python3
"""Console module"""
import cmd, sys
from models import storage
from models.base_model import BaseModel


classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, s):
        """Quits the console.\n"""
        return True

    def do_EOF(self, s):
        """EOF quits the console.\n"""
        return True

    def emptyline(self):
        pass

    def do_create(self, model=""):
        """Creates a new instance of BaseModel \
saves it (to the JSON file) and prints the id.\n\
Usage: create <Class Name>\n"""
        if model == "":
            print("** class name missing **")
        elif model not in classes:
            print("** class doesn't exist **")
        else:
            new_model = classes[model]()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        """Prints the string representation of an \
instance based on the class name and id.\n\
Usage: show <Class Name> <Object ID>\n"""
        args = arg.split()
        all_objs = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            for obj_id in all_objs.keys():
                if all_objs[obj_id].id == args[1]:
                    print(all_objs[obj_id])
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class \
name and id (save the change into the JSON file)\n\
Usage: destroy <Class Name> <Object ID>\n"""
        args = arg.split()
        all_objs = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            for obj_id in all_objs.keys():
                if all_objs[obj_id].id == args[1]:
                    del all_objs[obj_id]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances \
based or not on the class name.\n\
Usage: all OR all <Class Name>\n"""
        args = arg.split()
        all_objs = storage.all()
        res = []
        if len(args) == 1 and args[0] not in classes:
            print("** class doesn't exist **")
        else:
            for obj_id in all_objs.keys():
                res.append(all_objs[obj_id].__str__())
            print(res)

if __name__ == '__main__':
        prompt = HBNBCommand()
        prompt.prompt = "(hbnb) "
        prompt.cmdloop()
