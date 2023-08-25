"""
Data
piece of information that can be processed, stored, or manipulated by a computer program. Data can be
since a simple single value, like a number or a character (within a variable), or it can be more complex, such as a 
collection of values or structured information (within a data structure).

examples (within a variable):
"""
name = "ian christani"
bankAccountBalanceInPLN = 1.00
hasCats = 3
workInAccenture = True

#_______________________________________________________________________________________________________________________

"""
Data Structures
They are used to store and organize amounts of data. 
We have 3 different ones:

Lists:

    A list is an ORDERED collection of items, where each item can be of any data type.
    Lists are mutable, which means you can modify, add, or remove elements while the code is running.
    Lists are defined using square brackets [].
    
    example:
"""
myList = ["ian christani", 1.00, 3, True]
# to declare a empty list:
nameOfTheList = []



"""
Tuples:

    A tuple is an ORDERED collection of items, similar to a list, but tuples are immutable, meaning once created, 
        their elements cannot be changed while the code is running.
    Tuples are defined using parentheses ().
    Tuples are often used when you want to group related data together and ensure that it remains constant.
    
    example:
"""
myTuple = ("ian christani", 1.00, 3, True)
# to declare a empty tuple:
nameOfTheTuple = ()


"""
Dictionaries:

    A dictionary is an UNORDERED collection of key-value pairs.
    Each key in a dictionary is unique, and it is used to access its corresponding value.
    Dictionaries are mutable.
    Dictionaries are defined using curly braces {}. Each key-value pair is separated by a colon :
    
    example:
"""
myDict = {"name": "ian christani", "bankAccountBalance": 1.00, "hasCats": 3, "workInAccenture": True}
# to declare a empty dictionary:
nameOfTheDict = {}


#_______________________________________________________________________________________________________________________
"""
JSON (JavaScript Object Notation) declaration language:

It is a lightweight data interchange format that is easy for humans to read and write and easy 
for machines to read (technical term: parse) and generate. JSON is often used to transmit data between a server and a web application, 
but it's also commonly used for configuration files (AWS, Azure and Google Cloud), data storage, and communication between 
different parts of a software system.

JSON is a text-based format and is structured as a collection of key-value pairs (dictionary), where the keys are strings and
the values can be strings, numbers, booleans, arrays, or nested objects (dictionary within dictionary). 

example:
"""

aboutIan = {"name": "ian christani",
          "bankAccountBalance": 1.00,
          "hasCats": 3,
          "workInAccenture": true,
          "address":{
              "street": "Rakowicka",
              "number":83,
              "city": "Krakow",
              "updated": true,
            }
          }

"""
more details:

1. the booleans values (true and false) in JSON don't start with capital letters as in python
2. as we have dictionaries within a JSON, we might have the other ones: lists and tuples
3. could you see in just one data structure I would have all the INFORMATION I needed? Now it is easier to store datas related to one thing only.
    Here we have the begining of Object-Oriented Programming (OOP), that we will study later.
"""