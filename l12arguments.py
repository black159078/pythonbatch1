# => Type of Argument in Python
# Positional Arguments
# Keyword Arguments
# Default Arguments
# Variable-length Arguments (*args)   (Non-keyword Variable Arguments)
# Variable-length Arguments (**kwargs)  (keyword Variable Arguments)

# Positional Arguments
def greet(name,age):
    print(f"Hello friend! my name is {name}, i am {age} years old.")

greet("Su Su",23)
greet(25,"Nu Nu")



# Keyword Arguments
def hifi(name,age):
    print(f"Hello friend! my name is {name}, i am {age} years old.")

hifi(name="Min Min",age=23)
hifi(age=30,name="Nyi Nyi")


# Default Arguments
def hime(name,age=18):
    print(f"Hello friend! my name is {name}, i am {age} years old.")

hime("Yamin")
hime("Thuzar",20)


# Variable-length Arguments (*args)   (Non-keyword Variable Arguments)
def boys(*args):
    print(args)

boys("aung aung")
boys("aung aung","kyaw kyaw")
boys("aung aung","kyaw kyaw","zaw zaw","tun tun")
# boys("aung aung",args="kyaw kyaw") # error when including keyword argument


def sumresults(*numbers):
    total = sum(numbers)
    print(f"Sum result is = {total}")

sumresults(1,2,3) # Sum result is = 6
sumresults(10,20,30,40,50) # Sum result is = 150


def myfunone(num,*nums):
    print(num) # 1
    print(nums) # (2,3,4,5)

myfunone(1,2,3,4,5)

# ERROR
# def myfuntwo(*nums,num):
#     print(num)
#     print(nums)

# myfuntwo(1,2,3,4,5)



# Variable-length Arguments (**kwargs)  (keyword Variable Arguments)


def personinfos(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} = {value}")

personinfos(name="Thuzar",age=25,city="Mandalay")
personinfos(name="Kaung Kaung",professional="Engineer",city="Mawlamyine")




# Exercise ( Combining Different Type of Arguments )

def emailsender(address,*messages,**files):
    print(f"Address = {address}")
    if messages:
        for message in messages:
            print(f"Message : {message}")
    if files:  
        for key,value in files.items():
            print(f"{key} = {value}")

emailsender("dataland@gmail.com","Hello admin","i want to request record video",lesson="Python Batch 1",classdate="25 / Nov / 2024")



def studentinfos(name,age=18,*hobbies,**infos):
    print(f"Name = {name}")
    print(f"Age = {age}")
    if hobbies:
        for hobbie in hobbies:
            print(f"Hobbies = {hobbie}")
    if infos:
        for key,value in infos.items():
            print(f"{key} = {value}")

studentinfos("Nandar")
studentinfos("Maung Maung",25)
studentinfos("Maung Maung",25,'reading','travelling')
studentinfos("Maung Maung",25,'reading','travelling',city="Bago",profession="Enginner")




def staffinfos(name,age=18,*hobbies,**infos):
    print(f"Name = {name}")
    print(f"Age = {age}")
    if hobbies:
            # print(f"Hobbies = {hobbies}") # Hobbies = ('reading', 'travelling')
            print(f"Hobbies = {','.join(hobbies)}") # Hobbies = reading,travelling
    if infos:
        for key,value in infos.items():
            print(f"{key} = {value}")

staffinfos("Ni Lar",25,'reading','travelling',city="Yangon",profession="Enginner")