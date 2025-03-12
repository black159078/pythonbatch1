# Function

# 1. Simple Function with No Parameters
# 2. Function with Parameter
#         (i) Single Parameter Function
#         (ii) Multi Parameter Function
# 3. Function with Default Parameter
# 4. Function with a Return Value
# 5. Function with multi Return Values
# 6. Lambda Function ( Anonymous Function )


def sayname():
    print("Hello Aung Aung")

sayname()
sayname()


# 2. Function with Parameter
#           (i) Single Parameter Function

def saycity(city):
    print("Hello " + city)


saycity("Yangon")
saycity("Mandalay")


# 3. Function with Default Parameter

def country(country="Thailand"):
    print(f'Hello {country}')

country()
country("Myanmar")
country("Indonesia")



# 4. Function with a Return Value

def sayage():
    return "I am 25 years old"


print(sayage())


def saynickname():
    result = "Daw Pu"
    return result

print(saynickname())


def saynum(num1=20):
    return num1

print(saynum(100))
print(saynum())


def greeting(value="ya min"):
    return f"Hello {value}"

print(greeting("Su Su"))
print(greeting())



def funone(num1,num2):
    result = num1 + num2
    return result

print(funone(10,20))



def funtwo(num1,num2=200):
    result = num1 + num2
    return f"Total value is = {result}"

print(funtwo(10))
print(funone(10,20))



# 5. Function with multi Return Values

def saynameandage():
    name = "Honey"
    age = 26
    city = "mawlamyine"
    return name,age,city

print(saynameandage()) # ('Honey',26)

name,age,city = saynameandage()
print(name) # Honey
print(age) # 26
print(city)


#6. Lanbda Function ( Anonymous Functin )

addresult = lambda num1,num2,num3:num1+num2+num3
print(addresult(200,300,400))


sumresult = lambda num1,num2=200,num3=500:num1+num2+num3
print(sumresult(200,300))
print(sumresult(100))


# inputval = input("Enter your name = ")
# msg = "Hello "+inputval
# msg = "Hello %s" % inputval # v2 (useless)
# msg = f"Hello {inputval}" # v3
# print(msg)


# firstname = input("Enter First Name = ")
# lastname = input("Enter Last Name = ")
# # fullname = "Hello %s%s" % (firstname,lastname) #v2
# # fullname = "Hello %s %s" % (firstname,lastname) #v2
# fullname = f"Hello {firstname} {lastname}"
# print(fullname)



# => Generator Function

def genfun():
    yield 1
    yield 2
    yield 3

print(genfun()) # <generator object genfun at 0x7da4db384930>
print(list(genfun())) # [1, 2, 3]

for value in genfun():
    print(value) # 1 2 3



# => Multi Comment

"""
print("hello sir")
print("hello sir")
print("hello sir")
"""