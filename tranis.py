# a={1:'tom', 2:'man'}
# b={4:'jone'}
# a.update(b)
# print(a)

 
# class C:

#     # def __init__(self,a,b,c):
#     #     self.a=a
#     #     self.b=b
#     #     self.c=c
#     def set_salery(self, value):
#         self.salery = value
# e = C()     
# e.set_salery(200)  
# print(e.salery) 

# tom1=C('tman','tman1','tman2')
# print(tom1.__dict__)
# di= tom1.__dict__.copy()
# print(di)
# di['a']='maniga'
# print(di)
# dic = self.__dict__.copy()
# print(dic)





# #Creating dictionaries
# dict1 = {'color': 'blue', 'shape': 'square', 'volume':40}
# dict2 = {'color': 'red', 'edges': 4, 'perimeter':15}

# #Creating new pairs and updating old ones
# dict1['area'] = 25 #{'color': 'blue', 'shape': 'square', 'volume': 40, 'area': 25}
# dict2['perimeter'] = 20 #{'color': 'red', 'edges': 4, 'perimeter': 20}

# #Accessing values through keys
# print(dict1['shape'])

# #You can also use get, which doesn't cause an exception when the key is not found
# dict1.get('false_key') #returns None
# dict1.get('false_key', "key not found") #returns the custom message that you wrote 

# #Deleting pairs
# dict1.pop('volume')

# #Merging two dictionaries
# dict1.update(dict2) #if a key exists in both, it takes the value of the second dict
# dict1 #{'color': 'red', 'shape': 'square', 'area': 25, 'edges': 4, 'perimeter': 20}

# #Getting only the values, keys or both (can be used in loops)
# dict1.values() #dict_values(['red', 'square', 25, 4, 20])
# dict1.keys() #dict_keys(['color', 'shape', 'area', 'edges', 'perimeter'])
# dict1.items() 
# #dict_items([('color', 'red'), ('shape', 'square'), ('area', 25), ('edges', 4), ('perimeter', 20)])


# import json
# from dataclasses import dataclass

# @dataclass

# class Person:
#     name: str
#     age: int

# p=Person(name='jone', age=40)


# def encoder(Person):
#     # if isinstance(Person, Person):
#         return {'name':Person.name,'age': Person.age}
#     # raise TypeError(f'object{Person} is not type person')    

# encoded = json.dumps(p,default=encoder)
# print(encoded)




# import cmd

# class Hello(cmd.Cmd):
#     """ simple example"""
#     def do_greet(self,line):
#         """great the line gigaa"""
#         if line:
#             print('hi ',line)
#         else:
#             print("hi ")    

#     def do_EOF(self,line):
#         return True  
#     def post(self):
#         print    
# if __name__ == "__main__":
#     Hello().cmdloop()          

# import pprint

# a={"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "My_First_Model", "my_number": 89}}
# for key, value in a.items():
#     new_obj = a[key]["id"]
#     # self.new(new_obj)
#     print(new_obj)
#     l= a[key]
#     print(l)


# print(eval('BaseModel'))

#     # Basemodel(**BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2)





# a= [BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}

# for obj in a.values():

#  print(a.obj)
from models import storage
from models.base_model import BaseModel
import datetime as dt

# y = dt.datetime.now()
# print(y)
# print(type(y))
# x= y.isoformat()
# print(x)
# print(type(x))
# z=y.strftime("%Y-%m-%dT%H:%M:%S.%f")
# print(z)
# print(type(z))

# b= dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.%f")
# print(b)
# print(type(b))


# all_obj = storage.all()
# a=BaseModel()
# print(a)
# print(all_obj)


# for  obj in storage.all().values():
#   ob1=str(obj)
#   a=type(ob1).__name__ 
# print(a)



 
# def classes(self):
#         """Returns a dictionary of valid classes and their references"""
#         from models.base_model import BaseModel
#         from models.user import User
#         from models.state import State
#         from models.city import City
#         from models.amenity import Amenity
#         from models.place import Place
#         from models.review import Review

#         classes = {"BaseModel": BaseModel,
#                    "User": User,
#                    "State": State,
#                    "City": City,
#                    "Amenity": Amenity,
#                    "Place": Place,
#                    "Review": Review}
#         return classes

# def reload(self):
#         """Reloads the stored objects"""
#         if not os.path.isfile(FileStorage.__file_path):
#             return
#         with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
#             obj_dict = json.load(f)
#             obj_dict = {k: self.classes()[v["__class__"]](**v)
#                         for k, v in obj_dict.items()}
            # TODO: should this overwrite or insert?
#             FileStorage.__objects = obj_dict

txt = ",,,,,11222.3....banana....444"
x = txt.strip(",1425.")
print(x)

lol = "     lol    " 
print(lol.strip())


# txt = "  test    "

# txt.strip()
# #Output: "test"

# txt.lstrip()
# #Output: "test    "

# txt.rstrip()
# #Output: "  test"
line = """User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68", "fn", "kebede")"""
my_list = line.split('.')
print(my_list)
a= my_list[1][:4]
print(a)

new_li = []
new_li.append(my_list[0])
print(new_li)
# idd = my_list[1][6:42]
# print(idd)
new_st = my_list[1][my_list[1].find('(')+1:my_list[1].find(')')]
print(new_st)
new_li.append(" ".join(new_st.split(", ")))
print(new_li)
b= " ".join(i for i in new_li)
print(b)
c =b.split(" ")
try:
    c[1]= c[1].strip('"')
    c[2]= c[2].strip('"')
    
except IndexError:
    pass


g= " ".join(i for i in c)
print(g)



 
lis =[]
line ="""User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89}) """
y_list = line.split('.')
print(y_list)
lis.append(y_list[0])
my_dict = eval(
                y_list[1][y_list[1].find('{'):y_list[1].find('}')+1])
print(my_dict)  

new_r = y_list[1][y_list[1].find('(')+1:y_list[1].find(')')]
print(new_r)

lis.append(((new_r.split(", "))[0]).strip('"'))


lis.append(my_dict)

print(lis)
key =lis[0] + ' ' + lis[1]
for k, v in lis[2].items():
        m= (key + ' {} "{}"'.format(k, v))
        print(m)





# print(new_list[1])
# print(new_list[0])

# b= eval(Show my_list[0] my_list[1][6:42])
# User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})



