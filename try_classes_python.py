'''create classes in python '''
class Person:   #class name
    def __init__(self, name, age):  #constructor
        self.name = name
        self.age = age
    def myfunc(self):   #method
        print("Hello my name is " + self.name  +  "\t and I am " + str(self.age) + " years old")
        

p1 = Person("John", 36)
p1.myfunc()

'''create database connection in python  mysql'''


