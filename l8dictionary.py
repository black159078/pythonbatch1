# Method 1
student = {
    "name":"Su Su",
    "age":20,
    'city':"Yangon"
}

print(student) # {'name': 'Su Su', 'age': 20, 'city': 'Yangon'}
print(student["name"]) # Su Su
# print(student.city) # error
print(student.get("city"))


# Method 2 dict()

staff = dict(name="Aung Aung",age=30,city="Mandalay")

print(staff)
print(staff["age"])
print(staff.get('city'))

# print(student["country"]) # KeyError: 'country'
# print(staff["country"]) # KeyError: 'country'


print(student.get("country")) # None
print(staff.get("country")) # None

# .get(primary,secondary)
print(student.get("country","Myanmar")) # Myanmar
print(staff.get("country","Thailand")) # Thailand

print(student.get("age",40)) # 20
print(staff.get("age",50)) # 30


employee = {
    "name":"Aung Aung",
    "age":30,
    "city":"Mandalay"
}

print(employee) # {'name': 'Aung Aung', 'age': 30, 'city': 'Mandalay'}

employee["email"] = "aungaung@gmail.com"
print(employee) # {'name': 'Aung Aung', 'age': 30, 'city': 'Mandalay', 'email': 'aungaung@gmail.com'}

employee["age"] = 25
print(employee) # {'name': 'Aung Aung', 'age': 25, 'city': 'Mandalay', 'email': 'aungaung@gmail.com'}

del employee["city"]
print(employee) # {'name': 'Aung Aung', 'age': 25, 'email': 'aungaung@gmail.com'}



worker = dict(name="Nilar",age=20,city="Bago")

print(worker) # {'name': 'Nilar', 'age': 20, 'city': 'Bago'}

worker["email"] = "nilar@gmail.com"
print(worker) # {'name': 'Nilar', 'age': 20, 'city': 'Bago', 'email': 'nilar@gmail.com'}

worker["age"] = 25
print(worker) # {'name': 'Nilar', 'age': 25, 'city': 'Bago', 'email': 'nilar@gmail.com'}

del worker["city"]
print(worker) # {'name': 'Nilar', 'age': 25, 'email': 'nilar@gmail.com'}