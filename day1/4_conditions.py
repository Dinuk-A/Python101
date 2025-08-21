# IF ex 1 ✅
time = 10

if time < 12:
    print("its morning")
if time>12:
    print("its afternoon")
    
# IF ex 2 ✅
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# IF ex 3 ✅
marks = 158

if marks >= 75:
    print("Grade A")
elif 60 <= marks <= 75:
     print("Grade B")
elif 40 <= marks <= 60:
     print("Grade c")  
else:
     print("Grade D")  

# series of 'if' statements could do the same but then python interpreter will check all the statemens == resource waste
# in above version when a true statement is found it doesnt go further

# IF ex 4 ✅
has_good_credit_score = True
has_criminal_record = True

if has_good_credit_score and not has_criminal_record :
    print("Eligible for loan")
elif not has_good_credit_score and has_criminal_record:
       print("Not eligible for loan")
else:
     print("Not eligible for loan")

# IF ex 5 ✅
num = 12

if num % 2 == 0 and num > 10:
    print("Even number greater than 10")

# IF ex 6 ✅
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")


# WHILE EX 1 ✅
number = 1
while number <= 5:
    print(number)
    number += 1
print("Done")

# WHILE EX 2(break) ✅
num = 5
while num <= 15:  
    if num == 13:
        print("execution stopped at: ", num)
        break    #break stops the loop execution
    print(num)  
    num += 1
print("Done")

# WHILE EX 3(continue) ✅
n = 3
while n<=20:
    if n%5 == 0 :
        print("skipped: " , n)
        n += 1  
        continue
    print(n)
    n += 1
print("Done")

#In while loops, always make sure your loop variable updates even if you continue, 
#otherwise you’ll get stuck in an infinite loop.

# WHILE EX 4 ✅
correct_pin = "1234"
attempts = 0

while attempts<3:
    pin = input("Enter your ATM PIN: ")
    attempts += 1
    
    if pin != correct_pin:
        print("Wrong pin, try again")
        continue
    else:
        print("Access granted")
        break
else:
    print("Too many attempts.Access Blocked")



#  python 4_conditions.py