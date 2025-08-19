#OPERATORS
# Arithmetic Operators ✅
a = 10
b = 5
x =34
y=10
print("Addition:", a + b)         # Addition
print("Subtraction:", a - b)      # Subtraction
print("Multiplication:", a * b)    # Multiplication
print("Division:", a / b)          # Division (float result)
print("Exponentiation:", a ** b)    # Exponentiation (a raised to the power of b)
print("Floor Division:", x // y)    # Floor Division (integer result)
print("Modulus:", x % y)            # Modulus (remainder)

# logical operators ✅
print("True and True =", True and True)      # True
print("True and False =", True and False)    # False
print("True or False =", True or False)      # True
print("False or False =", False or False)    # False
print("not True =", not True)                # False
print("not False =", not False)           # True

# Comparison Operators ✅
print("Is 10 equal to 5?", a == b)          # Equal to
print("Is 10 not equal to 5?", a != b)      # Not equal to
print("Is 10 greater than 5?", a > b)       # Greater than
print("Is 10 less than 5?", a < b)          # Less than
print("Is 10 greater than or equal to 5?", a >= b)  # Greater than or equal to
print("Is 10 less than or equal to 5?", a <= b)      # Less than or equal to
c = 10
d = 25
print(c<d and d <35)

# identity operators ✅
var1 = "abc"
var2 = "abc"
var3 = "xyz"
print("Is var1 identical to var2?", var1 is var2)  # Identity (same object)
print("Is var1 identical to var3?", var1 is not var3)  # Identity (not same object)
'''
Python automatically interns (caches) small strings and commonly used strings to save memory. 
When you create two identical small strings, Python often reuses the same object in memory
'''

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("Is list1 identical to list2?", list1 is list2)  # Identity (not same object, ids are different) 
#Lists are mutable objects, so Python creates a new object in memory each time, even if they contain the same values:
print(list1 == list2)  # This checks if the contents are the same, which is True in this case

# Membership Operators ✅
my_list = [1, 2, 3, 4, 5]
print("Is 3 in my_list?", 3 in my_list)       # True (3 is an element of my_list)
print("Is 6 not in my_list?", 6 not in my_list)  # True (6 is not an element of my_list)

# python 3_operators.py
