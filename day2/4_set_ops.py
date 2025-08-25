# unordered, no duplicates , mutable
# written using curly braces {}
#Duplicate values will be ignored

thisset = {"apple", "banana", "cherry"}
print(thisset)

print(len(thisset))
print(type(thisset))

thisset2 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset2)

#Unordered means that the items in a set do not have a defined order.
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# thisset[0]  # This will raise an error
# thisset[1] = "mango"  # This will also raise an error

thisset.add("orange")
print(thisset)

thisset.remove("banana") # raises an error if item not found
thisset.discard("banana") # does not raise an error if item not found

#can use pop() to remove a random item

#Duplicate values will be ignored
#The values True and 1 are considered the same value in sets, and are treated as duplicates
#same with False and 0

#update === can be any iterable object (tuples, lists, dictionaries etc.).
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset.clear() #empties the set
del thisset #deletes the set completely

set_a = {1, 2, 3, 4, 5}
set_copy = set_a.copy()
print(set_copy)  # {1, 2, 3, 4, 5}

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7}

#union === combines all unique elements from both sets
print(set_a.union(set_b))        # {1, 2, 3, 4, 5, 6, 7}
print(set_a | set_b)             # same as union

#intersection === elements common to both sets
print(set_a.intersection(set_b)) # {4, 5}
print(set_a & set_b)             # same as intersection

# difference === elements in set_a but not in set_b
print(set_a.difference(set_b))        # {1, 2, 3}
print(set_a - set_b)                  # same as difference

#elements in set_b but not in set_a
print(set_b.difference(set_a))        # {6, 7}

# symmetric_difference === elements in either set_a or set_b but not in both
print(set_a.symmetric_difference(set_b)) # {1, 2, 3, 6, 7}
print(set_a ^ set_b)                     # same as symmetric_difference

# intersection_update === keeps only elements found in both sets
set_a = {1, 2, 3}
set_a.intersection_update({2, 3, 4})
print(set_a)                                # {2, 3}

# symmetric_difference_update === keeps only elements not found in both sets
set_a = {1, 2, 3}
set_a.symmetric_difference_update({2, 3, 4})
print(set_a)                        # {1, 4}

# Subset / Superset / Disjoint
set_x = {1, 2}
set_y = {1, 2, 3, 4}
set_z = {5, 6}

# issubset === True if all elements of set_x are in set_y
print(set_x.issubset(set_y))   # True

# issuperset === True if all elements of set_x are in set_y (but reversed check)
print(set_y.issuperset(set_x)) # True

# isdisjoint === True if no common elements exist between the sets
print(set_x.isdisjoint(set_z))# True
