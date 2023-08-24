'''
Primitive Types os variables (data):

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

'''
var = "3.2"
var = int(var)
print(var)
'''

'''
So far you cold see we are changing the values to be used, by interacting directly with the source code. It is a problem
since it is not safe for our code and the user might have no knowledge where to change.
Regarding this, we need another function that allows the user, in a safe way, to insert data into our program.
Here comes the function input()
This function has one argument and it is the text that is gonna be shown to the user.
It is worth to remembering that:
1. as default, all data provided from input is a STRING, so if you need a different type you need to convert it as describled before.
2. you need to keep the entered value into a variable, or you will not be able to use it.

let's take a look:
'''

# using the default type
anyData = input("Type anything you wan't to: ")
print(anyData)
print(type(anyData))

# changing the type to integer (INT)
yourAge = int(input("How old are you: "))
print(yourAge)
print(type(yourAge))

# WARNING: in the last example, the code is waiting a INT number, if you enter any other kind, we will have an ERROR.
