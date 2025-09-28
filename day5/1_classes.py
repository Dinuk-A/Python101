#use the class kw to create a class ✅
class MyClass:
    x = 10
    y = "Hello World"

# use the class to crate objects, using objects we can access the properties of the class ✅
c1 = MyClass()
print(c1.y)

c2 = MyClass()
print(c2.x)

#use kw pass to create an empty class
class MyEmptyClass:
    pass

# __init__() method is a constructor  ✅
# it is automatically called when an object is created
# we can use it to assign values to object attributes

class Car:
    
    #class variables, belongs to class and all the objects will be shared the same value
    wheels = 4
    
    #__init__() method . 'self' refers to the OBJECT itself (THE CURRENT INSTANCE)
    def __init__(self,brand,clr):
        self.brand = brand   #these are called instance variables
        self.clr = clr
    
    #other cusom methods 1 ✅
    def start(self):
        print(f'{self.brand} is now started')
    
    #other cusom methods 2 ✅
    def paintNewClr(self,new_clr):
        self.clr = new_clr
        print(f'car is now {self.clr}')

car1 = Car("Toyota", "Blue") # SELF REFERS TO THIS
car2 = Car("Volvo", "red")

print(car2.wheels)
print(car1.brand)
print(car2.clr)

car1.start()
car2.paintNewClr("Green")

# modify class variables
Car.wheels = 5
print(car2.wheels)

# change a value of a object (modify an object's property)  ✅
car1.brand = "BMW"
print("new car1 brand: " + car1.brand)

# __str()__ method defines what (how) should be displayed when an object of the class is printed ✅
class Person:
    
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'{self.name} is {self.age}'

p1 = Person("Dinuka",27)
print(p1)

#delete object properties ✅ and entire object ✅
p2 = Person("cat",2)
del p2.age   #now 'print(p2.age)' will give an error

del p2 #now 'print(p2)' will give an error


        

# python 1_classes.py