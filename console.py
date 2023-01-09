"""cmd module"""
import cmd
from models import storage
from models.base_model import BaseModel
import re
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class with sub coustom class cmd"""

    prompt = "(hbnb)"

    class_file = {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}

    def do_quit(self, line):
        """ "Quit command to exit the program"""
        return True

    def emptyline(self):
        """If this method is overriddes, the built in emptyline
        function which repeats the last nonempty command entered.
        """
        return

    def do_EOF(self, line):
        """ " end of file"""
        return True

    def do_create(self, args):
        """creat new instance and print its id"""

        if args == "" or args == None:
            print("** class name missing **")
        elif args not in HBNBCommand.class_file:
            print("** class doesn't exist **")
        else:
            print(eval(args)().id)
            storage.save()

    def do_show(self, args):
        """
        Prints the string representation of an instance.
        """
        if args == "" or args is None:
            print("** class name missing **")
        else:
            words = args.split(" ")
            if words[0] not in HBNBCommand.class_file:
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""

        if args == "" or args is None:
            print("** class name missing **")
        else:
            words = args.split(" ")
            if words[0] not in HBNBCommand.class_file:
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name."""
       
        if args != "":
            words = args.split(" ")
            if words[0] not in HBNBCommand.class_file:
                print("** class doesn't exist **")
            else:
                list1 = [
                    str(obj)
                    for obj in storage.all().values()
                    if obj.__class__.__name__ == words[0]
                ]
                print(list1)
        else:
            list2 = list1 = [str(obj) for obj in storage.all().values()]
            print(list2)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
       
        if args == "" or args is None:
            print("** class name missing **")
        else:
            words = args.split(" ")
            if words[0] not in HBNBCommand.class_file:
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            elif "{}.{}".format(words[0], words[1]) not in storage.all().keys():
                print("** no instance found **")
            elif len(words) < 3 and words[3] != [
                i for i in ("id", "created_at", "updated_at")
            ]:
                print("** attribute name missing **")
            elif len(words) < 4:
                print("** value missing **")
            else:
                if len(words) == 4:
                    cast = None
                    if not re.search('^".*"$', words[3]):
                        if "." in words[3]:
                            cast = float
                        else:
                            words[3]= int(words[3])
                    else:
                        words[3] = words[3].replace('"', "")
                    obj = storage.all()["{}.{}".format(words[0], words[1])]
                    obj.__dict__[words[2]] = words[3]
            storage.save()

    
    def strip_clean(self,args):

        new_list = []
        new_list.append(args[0])
        try:
            my_dict= eval(args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            new_list.append(((new_str.split(", "))[0]).strip('"'))
            new_list.append(my_dict)
            return new_list 

        str_new = args[1][args[1].find('(')+1:args[1].find(')')]
        new_list.append(" ".join(str_new.split(", ")))
        
        b= " ".join(i for i in new_list)
        c =b.split(" ")
        try:
            c[1]= c[1].strip('"')
            c[2]= c[2].strip('"')
    
        except IndexError:
          pass
        return " ".join(i for i in c)
        


    def do_count(self, args):
        """Counts the instances of a class.
        """
        words = args.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in HBNBCommand.class_file:
            print("** class doesn't exist **")
        else:
                count = 0
                for obj in storage.all().values():
                    if words[0] == obj.__class__.__name__:
                        count += 1
        print(count)

    
    def default(self,args):

        arg_list =args.split(".")
        if len(arg_list) >=2:
            if arg_list[1]== "all()":
                self.do_all(arg_list[0])
            elif arg_list[1]== "count()":
                self.do_count(arg_list[0])
            elif arg_list[1][:4] == "show":
                self.do_show(self.strip_clean(arg_list))   
            elif arg_list[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(arg_list))   
            elif arg_list[1][:6] == "update":
                args1=self.strip_clean(arg_list)
                if isinstance(args1, list):
                    key = args1[0] + " " + args1[1]
                    for k, v in args1[2].items():
                        self.do_update(key + ' {} "{}"'.format(k, v))
                else:
                    self.do_update(args1)
        else:
            cmd.Cmd.default(self, args)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
