#Ordered, immutable, allows duplicates
#created using parentheses ()

my_tuple = (10, 20, 30, 40, 50)
# Tuple with one element (MUST use a comma!)
single_tuple = (10,)

from_list = tuple([1, 2, 3])

print(len(my_tuple))
print(type(my_tuple))

print(my_tuple[0])   # 10 (first element)
print(my_tuple[-1])  # 50 (last element)
print(my_tuple[1:4]) # (20, 30, 40) 

#Tuples are immutable → you cannot directly append, remove, or pop.
#But you can convert to a list, modify, and convert back.
temp_list = list(my_tuple)
temp_list.append(60)
my_tuple = tuple(temp_list)
print(my_tuple)  # (10, 20, 30, 40, 50, 60)

print(my_tuple.count(20))  # 3

print(my_tuple.index(30))  # 2

nested = (1, (2, 3), 4)
print(nested[1][0])  # 2

#Concatenation and Repetition
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)   # (1, 2, 3, 4)
print(t1 * 3)    # (1, 2, 1, 2, 1, 2)

#packing and unpacking
#creating a tuple means 'packing' a tuple, === assign values to it
#extract values from a tuplr and assign them to vars means 'unpacking'

fruits = ("apple","banana","cherry")
(green,yel,red) = fruits
print(green)
print(yel)
print(red)

#The number of variables must match the number of values in the tuple, 
# if not, you must use an asterisk to collect the remaining values as a list.
fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits2

print(green)
print(yellow)
print(red)




# python day2/3_tuple_ops.py