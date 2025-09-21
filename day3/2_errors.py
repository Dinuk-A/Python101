#major error types in PY✅
'''
Syntax errors = mistakes in keywords/language
Runtime errors = errors found when the script is executed
Logical errors = these will not generate any errors, but will result unexpected outputs
'''

'''
Major runtime errors
    1.NameError = when trying to access an undefined var 
    2.IndexError = when trying to access an element of array which is out of range
    3.TypeError = when an invalid operation is applied to a var/object of inappropriate type (adding + 1 to a String)
    4.ValueError = when an inbuilt function recieves a parameter of correct type but invalid value( print(int('abc')))
    5. Module not found errors = when try to import non existing modules/funtion
'''

#to prevent these and more, use try-except blocks ✅
try:
    x = 100/0
except:
    print("deviding by 0 is not allowed")
    
#instead of looking for all the errors, we can catch a specific error ✅
try:
    y = 10/0
except ZeroDivisionError :
    print("deviding by 0 is not allowed")
    
    
#we can handle different errors in different ways ✅
try:
    num = int("hello")  
    result = 10 / num
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Division by zero!")
    
#if no errors occur, the code in the else block is executed ✅
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print("Success! Result is:", x)
    

#finally block is always executed ✅
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Division by zero!")
finally:
    print("Execution completed.")

    
# python 2_errors.py