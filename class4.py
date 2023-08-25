"""
Here go the maths operations in python. They are simple:

SUM: + 
SUBTRACTION: -
DIVISION: /
DIVISION (considering just the integer part): //
MULTIPLICATION: *
EXPONENTIAL: **
REST OF THE DIVISION: %


Other signals:
value attribution: =        it is used to say that one thing is equal to other thing
comparing values: ==        it is used to compare is one value is equal to another one, and the answer is a Boolean value (True or False)
"""
print("lets check some examples:")
print(10 + 3)
print(21 - 1)
print(25 / 6)
print(25 // 6)
print(2 * 5)
print(3 ** 2)
print(25 % 6)
print(2 == 2.0)         # different than in JavaScript, python doesn't recognize this such kind of detail, it is gonna RETURN the answer: True

print('some details:')
# if you want to limit the number of decimal digits, for example 2 digits:
print(round((25 / 6), 2))
# it is worth to saying that the above sentence is the same than the following sentence:
numberToBeRounded = 25 / 6
print(round(numberToBeRounded, 2))
# and both are the same than this one:
numberToBeRounded = round(25 / 6, 2)
print(numberToBeRounded)

"""
As you could see, in programming languages we don't use {} and [] for maths operations like we did in the school, we use sequences of () intead
"""
print('about the sequences:')
# the sequence of importance is very similar than we used in the real life:
# first: exponentials
# second: multiplications and division
# third: subtractions and sums
print(8/2**3+2)
# when we have exponentials sequences we need to remember: EXPONENTIALS FOLLOWS THE REVERSAL SEQUENCE (from right to the left)
# we first solve the first exponential from left to right and then the second one, but using the result from the first
print(2 ** 2 ** 3)