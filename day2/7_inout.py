#to get an input, use 'input' keyword ✅
#fullName = input("Enter your full name: ")
#print("Your name is",fullName)

#python automatically adds a space around the inputted value when printing ✅
#fname = input("Enter first name: ")
#lname = input("Enter last name: ")
#print("Your first name is",fname,"and last name is",lname)

#default type is String, but can be convereted later ✅
#age = int(input("How old are you: "))
#print(f'you are {age}')
#print(type(age)) 
 # this will give 'class str' if removed the 'int' part ✅
#print("You will be",age+1,"years old next year")

#what happens when a user entered a wrong typed input here? 
# will gives a valueError ,  so use inside a try-except , use 'except ValueError'

#output by print
#also discussed in day1 > 5_string_methods  ✅

#placeholders with .format ✅
a = 123
b= "cat"
print('value of a is {} and b is {}'.format(a,b))
print('value of a is {} and b is {}'.format(b,a))

#print sevaral vars ✅
name = "cat"
age = 25
print(-123.0,name,25*3,age)

#change default separator ✅
print(-123.0,name,25*3,age, sep="X")
print(-123.0,name,25*3,age, sep="--")

#end = what gets printed at the end of the output. ✅
#by default its a new line( \n) , using this will print the next print in same line
print(-123.0,name,25*3,age, sep="--",end="$")

#star patterns ❌


# python 7_inout.py












#python 7_inout.py