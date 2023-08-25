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

"""
we can convert between the type of datas we have in python, but if we convert FLOAT into INT we migh lose precision
"""

number = 2.3
number = int(number)
print(number, type(number))