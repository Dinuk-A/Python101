#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

print(len(thisdict))
print(type(thisdict))

thisdict2 = dict(name = "John", age = 36, country = "Norway")
print(thisdict2)

mydict = thisdict.copy()

# get values
print(thisdict["brand"])
print(thisdict.get("model"))

print(thisdict.keys())  # get keys
print(thisdict.values())  # get values
print(thisdict.items())  # get key-value pairs

#check if key exists
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  
#change values
thisdict["year"] = 2020
thisdict.update({"year": 2021})

#add items
thisdict["color"] = "red"
thisdict.update({"price": 50000})  #only if the key does not exist

#remove items
thisdict.pop("model") #removes item with specified key
thisdict.popitem() #removes the last inserted item
#del thisdict["year"] #removes item with specified key
#thisdict.clear() #empties the dictionary
#del thisdict #deletes the dictionary completely

#setdefault
# if "color" key exists, returns its value; otherwise, adds "color": "white" and returns "white"
x = car.setdefault("color", "white")
print(x)  


# python day2/5_dict_ops.py