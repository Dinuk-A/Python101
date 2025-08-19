#DATA TYPES ✅
# int
x = 42
print(type(x))  # <class 'int'>

# float
y = 3.14
print(type(y))  # <class 'float'>

# complex
z = 2 + 5j
print(type(z))  # <class 'complex'>

is_active = True
print(type(is_active))  # <class 'bool'>

name = "Dinuka"
print(type(name))  # <class 'str'>

value = None
print(type(value))  # None

#other types are List, Tuple, Set, Dictionary
# discussed in future files

# in python, an object is a collection of attributes and methods.
#every object has a type, identity, and value.

#ID ✅
# The id() function returns the unique identifier for an object, which is its memory address
print(id(x))  # Unique identifier for the object x
print(id(y))  # Unique identifier for the object y

newObj = x
print(id(newObj))  # Unique identifier for the object newObj, which is the same as x

print(x is newObj)  # True, because newObj is a reference to the same object as x

x = 100  # Changing the value of x
print(id(x))  # Unique identifier for the new object x, not the same as before

#CONSTRUCTORS ✅
weight = 55.5
print(int(weight))  # Converts weight to an integer (55)

# python 2_datatypes.py
