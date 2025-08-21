# Formatted Strings ex 1 ✅
name = "Dinuka"
age = 22

# normal way to print
print("my name is " , name , " and im " , age + 1 , " years old tomorrow")

try:
    print('my name is ' + name + ' and im ' + age + ' years old tomorrow')
except TypeError as e:
    print("Error: ", e)
    print("You can't concatenate string and integer directly. Convert age to string first.")
    
# correct way
print('my name is ' + name + ' and im ' + str(age + 1) + ' years old tomorrow')

# new way (f-strings) introduced in Python 3.6
print(f'my name is {name} and im {age+2} years old tomorrow')

###########################################################################################################################

# String Methods ✅
fn = "Hewasinghege Dinuka Pramod"

print(len(fn))  # space characters are also counted

print(fn.upper())
print(fn.lower())

print(fn[3])
print(fn[-1])  # last letter
print(fn[-3])  # 3 values from last letter(last one is -1)
print(fn[1:4]) # letter in index 4(5th letter) is excluded === (1 to 3)
print(fn[6:15]) # letter in index 15(16th letter) is excluded === (6 to 11)
print(fn[2:])  # if the 2nd param is empty, fetch till last value (-1st index)
print(fn[:5])  # if first param is empty, fetch from first value (0th index)


 
print('Dinuka' in fn)
print('dinuka' in fn)
print('Kavinda' in fn) 
 
print(fn.find('n'))     # index of first appearance if theres multiple
print(fn.find('nuka'))
print(fn.find('x'))  #no x in name, so will give -1

'''
Strings in Python are immutable, 
meaning any string method like .replace() does not change the original string — it returns a new string.

if needed to change the original string, reassign it to the same variable

fn = fn.replace('n','x')
print(fn)
'''
new_fn = fn.replace('n','x')
print("old name: " , fn)
print("new name: " , new_fn)

wrongFullName = "    Dinuka   Pramod   Kavinda  "
print(wrongFullName)
print(wrongFullName.strip())   # white spaces only in the start and end are removed
print(wrongFullName.lstrip())  # white spaces only in the start(left) are removed
print(wrongFullName.rstrip())  # white spaces only in the end(right) are removed

abc = "hello world"
print(abc.capitalize())  # Hello world
print(abc.title())       # Hello World
print(abc.swapcase())    # HELLO WORLD

s2 = "apple,banana,cherry"
fruits = s2.split(",")
print(fruits)         # ['apple','banana','cherry']
print(" & ".join(fruits))  # apple & banana & cherry

s3 = "Hello"
print(s3.center(10, "*"))  # **Hello***
print(s3.ljust(10, "-"))  # Hello-----
print(s3.rjust(10, "*"))  # *****Hello

# count(substring) → number of times substring appears
sentence = "Python is fun. Python is easy."
print(sentence.count("Python"))  # 2

# index(substring) → index of first occurrence (raises error if not found)
print(sentence.index("Python"))   # 0
print(sentence.index("fun"))      # 10



# python 5_string_methods.py
