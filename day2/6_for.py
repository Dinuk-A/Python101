#ex 1
fruits = ["apple", "banana", "mango"]
for f in fruits:
    print(f)   # prints each fruit one by one

#ex 2
name = "Dinuka"
for ch in name:
    print(ch)  # prints each character separately

#ex 3
for i in range(5):
    print(i)   # 0 1 2 3 4

# ex 4 start and end
for i in range(2, 6):
    print(i)   # 2 3 4 5

# ex 5 steps
for i in range(0, 10, 2):
    print(i)   # 0 2 4 6 8

# ex 6 enumeate
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)

# ex 7 break
for i in range(10):
    if i == 5:
        break   # stop the loop
    print(i)

#ex 8 continue
for i in range(6):
    if i == 3:
        continue   # skip 3
    print(i)

# ex 9 pass
for i in range(5):
    if i == 2:
        pass   # do nothing
    else:
        print(i)
        
        
# WHILE LOOPS ARE EXPLAINED IN DAY 1 too> day1/4_conditions_if_while.py ✅

# ex 1 basic while loop
count = 0
while count < 5:
    print(count)   # 0 1 2 3 4
    count += 1

# ex 2 using break
count = 0
while True:
    print(count)
    count += 1
    if count == 5:
        break   # exit loop when count reaches 5

# ex 3 using continue
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue   # skip printing 3
    print(count)   # prints 1, 2, 4, 5

# ex 4 using else with while
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop completed normally")  # runs only if loop was not broken

# ex 5 looping until user stops
user_input = ""
while user_input.lower() != "quit":
    user_input = input("Type 'quit' to exit: ")
    print("You typed:", user_input)


# python day2/6_for.py