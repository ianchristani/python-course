'''
Primitive Types of variables (data):

STR: strings are text in general terms
INT: integer are natural numbers: 1, 2, 3, 0, -1, -6, etc...
FLOAT: float are numbers with more precision (they have dot): 2.9 or 10.63 etc...
BOOL: booleans are logic values and we just have just 2 possibilities: True or False
None: it is used to represent "lack of value". There is nothing!

For us to check the nature of the variable we should use the function type() and provide the data as argument for this function.

note: this part will not be execute by the python interpreter
'''
simpleVariable = 3.1415
print(type(simpleVariable))


# how it is gonna be present to you on the command line (bash), note that this line will not be executed by the python interpreter
print('this is a string', type('this is a string'))
print(2, f' - this kind of variable is gonna be shown like that: {type(2)}')
print(3.14, f' - this kind of variable is gonna be shown like that: {type(3.14)}')
print(True, f' - this kind os variable is gonna be shown like that: {type(True)}')
print(None, f' - this kind of variable is gonna be shown like that: {type(None)}')

"""
It is worth saying that the inspection of variables is ESSENTIAL for deploy your code. Some mistakes are not visible when you analyse your code, it means
that, probably, your code is treating a data in a wrong way. For instance, the classic newbie mistake: making maths operations with inputed numbers by the user.
Once the input fuction, by default, it is a string, not a number (int or float). So in this case we will have a concatenation instead.
Keep in mind the data inspection using print and type functions is VERY IMPORTANT to avoid unexpected mistakes, save time and reputation... ;)

With that, we need to convert variables into ones we need... and it is simple! Check this out:
"""

anotherSimpleVariable = "5"
print(type(anotherSimpleVariable))

# converting into integer
anotherSimpleVariable = int(anotherSimpleVariable)
print(anotherSimpleVariable, type(anotherSimpleVariable))

# converting into float
anotherSimpleVariable = float(anotherSimpleVariable)
print(anotherSimpleVariable, type(anotherSimpleVariable))

# converting into boolean
anotherSimpleVariable = False
print(anotherSimpleVariable, type(anotherSimpleVariable))

# letting the variable without any value:
anotherSimpleVariable = None
print(anotherSimpleVariable, type(anotherSimpleVariable))

# be aware that not all convertions are ok!!! the first following example yes, but the second no...
var = '3.2'
var = float(var)
print(var)
