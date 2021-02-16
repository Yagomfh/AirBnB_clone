#!/usr/bin/python3
"""Console module"""
import cmd
import re
import sys
import json
from models.engine.file_storage import FileStorage
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex


classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, s):
        """Quits the console.\n"""
        return True

    def do_EOF(self, s):
        """EOF quits the console.\n"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel \
saves it (to the JSON file) and prints the id.\n\
Usage: create <Class Name>\n"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_model = eval(args[0] + '()')
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
        elif len(args) == 0:
            for obj_id in all_objs.keys():
                res.append(all_objs[obj_id].__str__())
            print(res)
        else:
            for obj_id in all_objs.keys():
                if all_objs[obj_id].__class__.__name__ == args[0]:
                    res.append(all_objs[obj_id].__str__())
            print(res)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by \
adding or updating attribute (save the change into the JSON file).\n\
Usage: update <class name> <id> <attribute name> "<attribute value>"\n"""
        args = shlex.split(arg)
        intatt = ["number_rooms", "number_bathrooms", "max_guest",
                  "price_by_night"]
        floatatt = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif (args[0] + "." + args[1]) not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj = args[0] + "." + args[1]
            inst = storage.all()[obj]
            if args[0] == "Place":
                if args[2] in intatt:
                    try:
                        args[3] = int(args[3])
                    except:
                        args[3] = 0
                if args[2] in floatatt:
                    try:
                        args[3] = floatatt(args[3])
                    except:
                        args[3] = 0
            setattr(inst, args[2], str(args[3]))
            inst.save()

    def do_count(self, arg):
        """Counts the number of elements in a class"""
        args = arg.split()
        all_objs = storage.all()
        count = 0
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            for obj in all_objs.keys():
                if all_objs[obj].__class__.__name__ == args[0]:
                    count += 1
            print(count)

    def default(self, line):
        """Default cmd method"""
        fnct = {"all": self.do_all, "count": self.do_count,
                "show": self.do_show, "destroy": self.do_destroy,
                "update": self.do_update}
        args = line.replace(".", " ").replace("(", " ").replace(",\
 ", " ", 1).replace("{", "\'{").replace("}", "}\'")
        args = shlex.split(args, 1)
        if len(args) == 4 and args[1] == "update":
            Dict = line.split(" ", 1)[1].replace(")", "")
            Dict = eval(Dict)
            for key in Dict.keys():
                cmd_args = "" + args[0] + " " + args[2] + "\
 " + key + " " + str(Dict[key])
                try:
                    self.do_update(cmd_args)
                except:
                    print("*** Unknown syntax:", args[0])
        else:
            args = (line.replace("(", ".").replace(")", ".")
                    .replace('"', "").replace(",", "").split("."))
            cmd_args = ""
            for i in range(len(args)):
                if i != 1:
                    cmd_args += args[i]
                cmd_args += " "
            try:
                fnct[args[1]](cmd_args)
            except:
                print("*** Unknown syntax:", args[0])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
