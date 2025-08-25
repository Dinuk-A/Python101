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

# python day2/6_for.py