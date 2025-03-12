# => Data Collections ( Module Containers )

# => Counter (from collections module)
from collections import Counter

getcounts = Counter("Hello World")
print(getcounts) # Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})


# => Queues (from collections module)

from collections import deque

qpersons = deque(["Su Su","Nu Nu","Yu Yu"])

qpersons.append("Tun Tun") # Add to right end
qpersons.appendleft("Sai Sai") # Add to left start

# for person in qpersons:
#     print(person)


# Removing elements
qpersons.pop() # Remove from right end
qpersons.popleft() # Remove from left start

for person in qpersons:
    print(person)


# => defaultdict (from collections module)

from collections import defaultdict

items = defaultdict(list)

items["fruits"].append("apple")
items["fruits"].append("mango")
items["fruits"].append("banana")
items["colors"].append("orange")

print(items["fruits"]) # ['apple', 'mango', 'banana']
print(items["colors"]) # ['orange']
print(items["candy"]) # []


numitems = defaultdict(int)

numitems["val"] += 1

print(numitems) # defaultdict(<class 'int'>, {'val': 1})

print(numitems["val"]) # 1



# Grouping Items
groups = defaultdict(list)
foods = [("fruit","apple"),("fruit","orange"),("vegetable","carrot"),("fruit","mango")]

for key,value in foods:
    groups[key].append(value)

print(groups)



numitems = defaultdict(int)
print(numitems["val"]) # 0
numitems["val"] = 1
print(numitems["val"]) # 1



# Counting Elements
colorcounts = defaultdict(int)
candycolors = ["red","green","blue","green","red","black","green"]

for candycolor in candycolors:
    colorcounts[candycolor] += 1

print(colorcounts) # defaultdict(<class 'int'>, {'red': 2, 'green': 3, 'blue': 1, 'black': 1})


# => OrderedDict ( from collections module )

from collections import OrderedDict

myorders = OrderedDict()
myorders["num1"] = 100
myorders["num2"] = 200
myorders["num3"] = 300
myorders["num4"] = 400
myorders["num5"] = 500

print(myorders) # OrderedDict({'num1': 100, 'num2': 200, 'num3': 300, 'num4': 400, 'num5': 500})
print(myorders["num2"]) # 200

# Recording Item
myorders.move_to_end("num2")
print(myorders) # OrderedDict({'num1': 100, 'num3': 300, 'num4': 400, 'num5': 500, 'num2': 200})

# re-inserting
myorders["num1"] = 10
print(myorders) # OrderedDict({'num1': 10, 'num3': 300, 'num4': 400, 'num5': 500, 'num2': 200})

# Reordering Item
del myorders["num3"]
print(myorders) # OrderedDict({'num1': 10, 'num4': 400, 'num5': 500, 'num2': 200})


config = OrderedDict()
config['host'] = 'localhost'
config['port'] = 8080
config['debug'] = True

for key,value in config.items():
    print(f"{key} : {value}")



# => namedTuple (from collections module)

from collections import namedtuple

LuckyNumbers = namedtuple("LuckyNumbers",["num1","num2","num3"])

getnums = LuckyNumbers(33,66,99)
print(getnums.num1) # 33
print(getnums.num2) # 66
print(getnums.num3) # 99

# exercise with tuple , hard to remember what index number represents
staff = ("Yu Yu",20,"Developer")
print(staff[0]) # Yu Yu
print(staff[1]) # 20
print(staff[2]) # Developer

# namedtuple
Student = namedtuple('Student',['name',"age","profession"])
# pupil = Student("Su Su",30,"Engineer")
pupil = Student(name="Su Su",age=30,profession="Engineer")
print(pupil.name) # Su Su
print(pupil.profession) # Engineer
print(pupil.age) # 30




# => ChainMap (from collections module)

from collections import ChainMap

dict1 = {"name":"Aye Aye"}
dict2 = {"city":"Yangon"}
getdata = ChainMap(dict1,dict2)
print(getdata) # ChainMap({'name': 'Aye Aye'}, {'city': 'Yangon'})
print(getdata['name']) # Aye Aye
print(getdata['city']) # Yangon



# => array (from array module)

from array import array

myarrs = array('i',[10,20,30,40])
print(myarrs)




# => queue (from queue module)

from queue import Queue

qone = Queue()
qone.put(400)
qone.put(300)
qone.put(100)

print(qone.get())
print(qone.get())
print(qone.get())