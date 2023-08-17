"""
The print function is important, because beyond be the default contact with the computer
(default input data into the computer: keyboard;  default output from the computer: monitor),
it is helpful for you to DEBUG (solve logical coding problems) your code by inserting it 
in strategic points of your code.

It is simple to use, you just need to provide, as argument, what you want to be displayed.
If it is a text you must use ' or " (it is gonna be printed exactly what is between the quotes), 
if not just provide the info .
Possibilities:
"""

print("text message")
print("text using double quotes", 'text using single quotes')
print("text using both. Here I am using single quotes in 'this part', but if you have started the text with double quotes, you should finish with double quotes")
print('text using both. Here I am using double quotes in "this part", but if you have started the text with single quotes, you should finish with single quotes')
print(3)
print(2 + 3)
print('text1', 3)
print('text1' + 'text2')
print('this sequence of characteres will put the next text in the next row\n' + 'Hej! I am in the 2 line')

print(""" 
    when you have a loooooooooooooooooooooooooooooooooooooooooong text you can split in lines you message.
    And for that, you just need to do in the same way.
    It is worth saying that it is gonna be printed exactly what is between the quotes even the spaces from the left side!
    Could you see that the print function is not only HELLO WORLD?!
    :D
""")

print('text1' + 'text2', sep="####", end="@@@@")
print('')
print('text1', 3, sep="####", end="@@@@")
print("")

var = 'I love python classes'
print(var)

# formated print (used to insert external values into the text inside the print function)
number = 5
name = 'Ian'
print(f"the value of the variable given by {name} is {number}")