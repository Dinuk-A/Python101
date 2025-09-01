#function is a block of organized code that is used to perform a single task or action

#Anatomy of a function ✅ ❌

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

#use '*' if the number of args that will be passed into the function are not known  ❌

# python 1_fns.py