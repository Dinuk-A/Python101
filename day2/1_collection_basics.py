#collection types are data structures that can store multiple values in a single variable
#4 major types

# List ✅
# Ordered  === have a fixed sequence (index positions) . can access elements by their position, order which insert items is preserved
# Mutable  === can change later (add new ones/remove existing ones)
# Allow duplications

fruits = ["apple","banana","guava","apple","orange"]
print(fruits[2])
fruits.append("tomato")
print("New fruits: ", fruits)

# Tuple ✅
# Ordered
# Immutable === cannot change later (cannot add new ones/remove existing ones)
# Allow duplications
fruits_tuple = ("apple","banana","guava","apple","orange")
print(fruits_tuple[2]) 

try:
    fruits_tuple[2] = "kiwi"  # This will raise an error because tuples are immutable
except TypeError as e:
    print("Error: ", e)

try:
    fruits_tuple.append("tomato")  # This will also raise an error
except AttributeError as e:
    print("Error: ", e)    
 
print("Fruits tuple: ", fruits_tuple)   


# Set ✅
# Unordered === no fixed sequence (index positions) . cannot access elements by their position like [n], order which insert items is not preserved
# Mutable === can change later (add new ones/remove existing ones) || BUT ELEMENTS MUST BE IMMUTABLE LIKE STRINGS, TUPLES, NUMBERS
# No duplications === no repeated items
# good for fast lookups
fruits_set = {"apple","banana","guava","apple","orange"}     # 'apple' will be stored only once
fruits_set.add("tomato")
print("New fruits set: ", fruits_set) 

# different results will come for different runs
for f in fruits_set:
    print(f)
    
    
# Dictionary ✅
# Ordered by insertion (Python 3.7+) === preserves the order items were added
# order of keys is preserved, so if you iterate over the dictionary, items will come out in the order you added them.
# Mutable === can change later (add new ones/remove existing ones)
# Key-Value Pairs === each item is stored as a pair of key and value, keys must be unique
student = {"name":"john","age":20,"major":"computer science"}
print(student["name"])
student["age"] = 22
# Add a new key-value pair
student["city"] = "Colombo"

# more methods per each will be discussed separately ✅

# python 1_collection_basics.py