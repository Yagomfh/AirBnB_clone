#!/usr/bin/python3
"""Console module"""
import cmd
import sys
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
        all_objs = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            for obj_id in all_objs.keys():
                if all_objs[obj_id].id == args[1]:
                    if args[2] in all_objs[obj_id].__dict__:
                        t = type(all_objs[obj_id].__dict__[args[2]])
                        if t is int:
                            all_objs[obj_id].__dict__[args[2]] = int(args[3])
                        elif t is str:
                            all_objs[obj_id].__dict__[args[2]] = args[3]
                        else:
                            all_objs[obj_id].__dict__[args[2]] = float(args[3])
                        storage.save()
                        return
            print("** no instance found **")

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
