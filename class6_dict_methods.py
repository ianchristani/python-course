"""
Dictionaries
As dictionaries don't work with indexes, there is a sequence, but we cannot say it is ordered, unless we sort it.
we can access the dictionaries's values and keys using the following ways. 
Let's consider the following example:
"""

myDict = {"name": "ian christani", "bankAccountBalance": 1.00, "hasCats": 3, "work": True}
# displaying the full dictionary keys + values
print(myDict)
# display a tuple that contains just the keys within a list
print(myDict.keys())
# display a tuple that contains just the values within a list
print(myDict.values())
# display a tuple that contains a list of each key-value pair within its tuple
print(myDict.items())
# displaying one specific value: The way is similar than we use when we have lists and tuples
print(myDict['name'])

# Dictionaries' methods
# changing a key's value - sintax: dictName["keyName"] = newValue
print(f"The original dict: {myDict}")
myDict["name"] = "teacher"
print(f"The modified dict: {myDict}")
# we can perform the same task in a different way even add a new pair - sintax: dictName.update({keyName:newValue})
print(f"The original dict: {myDict}")
myDict.update({"teacher":"ian christani"})
print(f"The modified dict: {myDict}")

# sorting the dictionary
print(f"The original dict: {myDict}")
sortedDict = sorted(myDict)
print(f"The modified dict: {sortedDict}")

# making a copy of your dict - sintax: newDictName = refDictName.copy()
newD = myDict.copy()
print(newD)

# deleting the last pair - sintax: dictName.popitem()
print(f"The original dict: {newD}")
newD.popitem()
print(f"The modified dict: {newD}")

# deleting a specific pair key-value. This method works in the same way than the lists and tuples one - sintax: del dictName["keyName"]
print(f"The original dict: {newD}")
del newD["name"]
print(f"The modified dict: {newD}")

# cleaning a dictionary- sintax: dictName.clear()
print(f"The original dict: {newD}")
newD.clear()
print(f"The modified dict: {newD}")