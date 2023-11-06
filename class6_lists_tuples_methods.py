"""
LISTS (arrays)

we can access the list's elements using indexes, let's consider the following list
note that when we start the index from the left, the first one is ZERO
"""
aboutIan = ["ian", 1.00, 3, True]
#the indexes: 0  ,  1  , 2,  3     

print(aboutIan[0])
print(aboutIan[1], aboutIan[3])

"""
We might use negative indexes:
note that when we start the index from the right, the first one is -1
"""
aboutIan = ["ian", 1.00, 3, True]
#the indexes: -4  , -3, -2,  -1 

print((aboutIan[-1]), aboutIan[-4])


"""
We can switch the place os the elements:
"""
print(f'the list before switch: {aboutIan}')
aboutIan[0], aboutIan[3] = aboutIan[3], aboutIan[0]
print(f'the list after switch: {aboutIan}\n')


"""
slicing Lists
we can take part of the list if we need, for this we will consider 2 positions and separate them with :
"""
# sintaxe: nameOfTheList[startingElementIndex : endingElementIndex]
print(f'the complete list now: {aboutIan}')
# let's take the full list using this sintaxe:
print(f"the full list using slicing list notation aboutIan[:]")
print(aboutIan[:])

print(f"taking from the element with index equal to 1 till the end using slicing list notation: aboutIan[1:]")
print(aboutIan[1:])

print(f"taking the element with index equal to 2 (ONLY) using slicing list notation: aboutIan[2:3]")
print(aboutIan[2:3])

print(f"taking from the element with index equal to 0 till the one with index equal to 2 using slicing list notation: aboutIan[0:3]")
print(aboutIan[0:3])

print(f"now slicing with negative index: aboutIan[:-2]")
print(aboutIan[:-2])

# ********** as you could see the endingElementIndex is used as a reference only, not providing the last element from the index that was included.. *********
#____________________________________________________________________________________________________________

"""
List Methods

Here we have the most used list methods
"""

# deleting the last element -sintax: nameOfTheList.pop()
print(f'the list before pop it: {aboutIan}')
aboutIan.pop()
print(f'the list after pop it: {aboutIan}\n')

# deleting an element from the list - sintax: del nameOfTheList[elementIndex]
print(f'the list before delete: {aboutIan}')
del aboutIan[0]
print(f'the list after delete: {aboutIan}\n')
# ******** WARNING: if you wan't to clear your list: del[:]
# ******** WARNING: if you wan't to DELETE your list: del nameOfTheList

# cleaning the list - sintax: nameOfTheList.clear()
print(f'the list before clean it: {aboutIan}')
aboutIan.clear()
print(f'the list after clean it: {aboutIan}\n')

aboutIan = ["ian", 1.00, 3, True]

# adding element in the end of the list: sintax: nameOfTheList.append[elementToBeAdded]
print(f'the list before add element: {aboutIan}')
aboutIan.append("ooops, I just got in")
print(f'the list after add the element: {aboutIan}\n')
"""
the APPEND method ALWAYS will add the element in the end of the list!
If you need to add in a specific place in the list, we shoud use the INSERT method
"""
# adding element in a specifc position sintax: nameOfTheList.insert[position, elementToBeAdded]
print(f'the list before insert the element: {aboutIan}')
aboutIan.insert(0, "HERE!!!!")
print(f'the list after insert the element: {aboutIan}\n')

# sorting one list - sintax: nameOfTheList.sort()
listOfLetters = ["c", "d", "a", "b"]

print(f'the list before sorting it: {listOfLetters}')
listOfLetters.sort()
print(f'the list after sorting it: {listOfLetters}\n')

# reversing the list - sintax: nameOfTheList.reverse()
print(f'the list before reversing it: {listOfLetters}')
listOfLetters.reverse()
print(f'the list after reversing it: {listOfLetters}\n')

# concatenating the list's elements (strings only) - sintax: "joinCharacter".join(nameOfTheList)
print(f'the list before join: {listOfLetters}')
listOfLetters = "#".join(listOfLetters)
print(f'the list after join: {listOfLetters}\n')

# make a copy from a list (resulting in INDEPENDENT lists) - sintax: nameNewList = nameSourceList[:]
newList = aboutIan[:]

# working with derived lists (resulting in NOT INDEPENDENT lists) - sintax: nameNewList = nameSourceList
# IDENTITY
sourceList = ["cats", "dogs", "birds"]
# making the atributions
list2 = sourceList
list3 = list2
# We will still have the list3 with elements
del sourceList[2]
del list2
print(list3)

# second test
sourceList = ["cats", "dogs", "birds"]
# making the atributions
list2 = sourceList
list3 = list2
# now we have an empty list as result
del sourceList[2]
del list2[:]
print(list3)