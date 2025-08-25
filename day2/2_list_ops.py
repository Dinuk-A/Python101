#lists are created using square brackets === []
# ordered, changeable, and allow duplicate values.


myList = ["apple","cat",12345.00,True,"cat",-100]
print(myList)

print(len(myList)) #length of the list
print(myList[1]) #accessing elements in a list
print(type(myList)) #type of the list === <class 'list'>

# accessing as a range
#in a range, last index is excluded
print(myList[1:4]) #from index 1 to index 3
print(myList[:4]) #from start to index 3
print(myList[2:]) #from index 2 to end
print(myList[-1]) #accessing the last element
print(myList[-3:-1]) #from the third last to the second last element
print(myList.index("cat")) #gives the index of the first matching value

#check if an item is exists in the list
if "apple" in myList:
    print("Yes, apple is in the list")

print("apple" in myList) #True

#change the value of a list item
myList[4] = "new value"

#change value of a range
myList[1:3] = ["a","b","c"]
print(myList)

# changing two indexes with a single value
myList[1:3] = ["single value for two indexes"]
print(myList)

#use the list() constructor to make a list
#double brackets
myList2 = list(("dog","banana",67890.00,False,"banana",200))

#add items to a list
myList2.append("new item") #add to the end of the list
myList2.insert(3,"inserted item") #add to a specific index

#add an entire new list to an existing list
#can add any iterable (tuple, set, dictionary)
myList2.extend(["item1","item2","item3"])
print(myList2)

myList2.extend(myList) #adding myList to myList2

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#remove a specific item
myList2.remove("banana") #removes the first matching value
myList2.pop() #removes the last item
myList2.pop(2) #removes the item at the specified index
del myList2[0] #removes the item at the specified index

newList = myList2.copy() #copy a list
newList.clear() #clear the entire list
del newList #delete the entire list

#list comprehension
nums = [5,54,3,8,1,2]
evenNums = [x for x in nums if x % 2 == 0]
print(evenNums) # [54, 8, 2]

#manipulate values while iterating
newNums =[x*100 for x in range(25) if x %5 == 0]
print(newNums) # [0, 500, 1000, 1500, 2000, 2500]

fruits = ["apple","banana","cherry","kiwi","mango"]
newFruits = [x.upper() for x in fruits]

#sort a list
newFruits.sort() #ascending order alphabetical
print(newFruits)

newFruits.sort(reverse=True) #descending order alphabetical
print(newFruits)

#case sensitive sorting - all uppercase letters come before lowercase letters
fruits2 = ["apple","Banana","cherry","Kiwi","mango"]
fruits2.sort()
print(fruits2)

#to perform a case insensitive sort, use str.lower as the key function
fruits2.sort(key=str.lower)
print(fruits2)

nums = [5,54,3,8,1,2]
nums.sort() #ascending order numerical
print(nums)

nums.sort(reverse=True) #descending order numerical
print(nums)

#just reverse order
nums.reverse()

# python day2/2_list_ops.py