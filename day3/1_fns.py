#function is a block of organized code that is used to perform a single task or action

#Anatomy of a function ✅ 
def calc_total_bill(amount:float, service_chg: float = 10) -> float:
    
    '''
    This function will calculate the total bill amount
    
    Args: 
        amount (float): original bill amount
        service_chg (float, optional): service charge percentage. Defaults to 10.
    Returns:
        float: total bill amount including service charge
    '''
    total_service_chg = amount * (service_chg / 100)
    total_bill = amount + total_service_chg
    return total_bill

print(calc_total_bill(1000,15))
print(calc_total_bill(2000))

# Anatomy explained: 
# def = keyword to define a function
# calc_total_bill = function name
# (amount:float, service_chg: float = 10) = parameters >>> with type hints and default value for service_chg (optional)
# -> float = return type hint (optional)
# '''...''' = docstring to explain the function (optional but recommended)
# function body = indented block of code that performs the task
# return = keyword to return a value from the function
# calc_total_bill(1000,15) = function call with arguments (custom value for service_chg)
# calc_total_bill(2000) = function call with default service_chg

# # simple functions works without parameters, return, or docstring — extra anatomy is optional.


#ex 1 ✅
#defining a function
def greet(name):
    print("Hello",name)

#invoking a defined function
greet("dinuka")

#ex 2 ✅
def multiply():
    value = int(input("enter value: "))
    multiplier = int(input("enter multiplier: "))
    answer =  value * multiplier
    print(f'{value}*{multiplier} is {answer}')

multiply()

#ex 3 ✅ , with returned value
def findMax(val1,val2):
    if val1 > val2:
        return val1
    else:
        return val2 

print(findMax(10,-20))
print(findMax(1000,20))
print(findMax(10,20500))
print(findMax(10,-20500))

#ex 4 ✅
def findSum(a,b):
    return(a+b)

print(findSum(10,-20))
print(findSum(1000,20))
print(findSum(10,20500))
print(findSum(10,-20500))

# parameters vs arguments ✅
# parameters are the variables listed in the function definition
# arguments are the actual values passed to the function when it is called
'''greet(name) -> name is the parameter
   when calling the function elsewhere>  greet("dinuka") -> "dinuka" is the argument
'''
#if a function definition has 2 parameters, 2 arguments must be passed when calling the function, otherqwise an error will occur 

#Arbitrary Arguments ✅
# 2 types , *args and **kwargs

#if in advance we didnt know how many arguments will be passed into the function, we can use '*' before the parameter name in the function definition
# term 'args' is used by convention, we can use any name after '*'
def addNumbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(addNumbers(1,2,3))
print(addNumbers(10,20,30,40,50))

# **kwargs (keyword arguments) allows us to pass a variable number of keyword arguments (key-value pairs) to a function
def displayInfo(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
displayInfo(name="Alice", age=30, city="New York")
displayInfo(product="Laptop", price=1200, brand="Dell")

#pass statement ✅
# when a function is defined but not yet implemented, we can use 'pass' to avoid errors
def placeholderFunction():
    pass

#more advanced function topics (not covered here) ✅
#positional vs keyword arguments
#recursion fns
#decorators

#lambda functions (in day 4)  ✅

# python 1_fns.py