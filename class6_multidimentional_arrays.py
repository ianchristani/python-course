"""
As we can have different contents within a LIST (array), we might have an array as well.
And the good news is: the basic concepts we had in our previous classes related with lists, still remain.
But for you to recognize how many dimentions the array has, just count 'the amount of list layers' we have within the first one.

Lets consider the example:
"""
# two dimentional array - structure:
my2DArray = [1, 'someString', 3.14, ['I am the secound list']]
# remember, you can represent it as:
my2DArray = [1,
             'someString',
             3.14,
             ['I am the secound list']
             ]

other2Darray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# or
other2Darray = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# as you could see, we just have a list inside a list 1x, so it is 2D

# let's add one more dimention
my3DArray = [1, 'someString', 3.14, ['I am the secound list', ['I am the third list']]]
#or
my3DArray = [1,
             'someString',
             3.14,
             ['I am the secound list',
              ['I am the third list'],
              ]
            ]
# now, we have a list inside a list and this last one is inside my3DArray, so for you to get how many dimentions
# take the innest one and count how many layers we have till the main one!

"""
as it was told, the things we've learned about lists before are still valid! Just a little bit more complex, but not difficult
Let's take a look:
"""
# Accessing
# itens in a 2D List:
my2DArray = [1, 'someString', 3.14, ['I am the secound list', 10, False]]
# indexes:   0,      1      ,   2 ,        3/0              ,3/1,  3/2 

myArrayInsideOtherArray = my2DArray[3]
print(myArrayInsideOtherArray)

theSecoundListContent = my2DArray[3][1]
print(theSecoundListContent)

# itens in a 3D List:
my3DArray = [1, 'someString', 3.14, ['I am the secound list', ['I am the third list']]]
# indexes:   0,      1      ,   2 ,        3/0              ,     3/1/0

myArrayInsideOtherArray = my3DArray[3][1]
print(myArrayInsideOtherArray)

theThirdListContent = my3DArray[3][1][0]
print(theThirdListContent)


# Slicing
# itens in a 2D List:
my2DArray = [1, 'someString', 3.14, ['I am the secound list', 10, False, 'ian']]
content = my2DArray[3][1:3]
print(content)


# itens in a 3D List:
my3DArray = [1, 'someString', 3.14, ['I am the secound list', ['I am the third list', 1, 2, 3, 4, 5]]]
content = my3DArray[3][1][1:]
print(content)

# Appending
# itens in a 2D List:
my2DArray = [1, 'someString', 3.14, ['I am the secound list', 10, False]]
my2DArray[3].append('uhuuuu')

myArrayInsideOtherArray = my2DArray[3]
print(myArrayInsideOtherArray)

# itens in a 3D List:
my3DArray = [1, 'someString', 3.14, ['I am the secound list', ['I am the third list']]]
my3DArray[3][1].append('uhuuu again!')
print(my3DArray[3][1])

