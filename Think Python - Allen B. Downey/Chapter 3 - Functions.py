# Chapter Three Exercises

# Exercise 3.1
# Question:


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()

# Move the last line of this program to the top, so the function call appears before the definitions.
# Run the program and see what error message you get.

# Answer:

# NameError: name 'repeat_lyrics()' is not defined

# Exercise 3.2
# Question:

# Move the function call back to the bottom and move the definition of print_lyrics after the repeat_lyrics definition.
# What happens when you run this program?

# Answer:

# Program works fine.

# Exercise 3.3
# Question:

# Python provides a built-in function called len that returns the length of a string.
# The value of len('allen') is 5.
# Write a function named right_justify that takes a string named s as a parameter
# and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.

# right_justify('allen')
#                                                                allen

# Answer:


def right_justify(s):
    space_required = 70 - len(s)
    spaces = ' ' * space_required
    print(spaces + s)

# Exercise 3.4
# Question:

# A function object is a value you can assign to a variable or pass as an argument.
# For example, do_twice is a function that takes a function object as an argument and calls it twice:


def do_twice(f):
    f()
    f()

# Here’s an example that uses do_twice to call a function named print_spam twice.


def print_spam():
    print('spam')


do_twice(print_spam)

# Answer:

# 1. Type this example into a script and test it.

# It is already in a script.

# 2. Modify do_twice so that it takes a function object and a value,
#    and calls the function twice, passing the value as an argument.


def do_twice(f, v):
    f(v)
    f(v)

# 3. Write a more general version of print_spam, called print_twice,
#    that takes a string as a parameter and prints it twice.


def print_twice(s):
    do_twice(print, s)

# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.


do_twice(print_twice, "spam")

# 5. Define a function called do_four that takes a function object and a value
#    and calls the function four times, passing the value as a parameter.
#    There should be only two statements in the body of this function, not four.
#    Solution: http://thinkpython.com/code/do_four.py.


def do_four(f, val):
    do_twice(f, val)
    do_twice(f, val)

# Exercise 3.5
# Question:

# This exercise can be done using only the statements and other features we have learned so far.

# 1. Write a function that draws a grid like the following:

# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a comma-separated sequence:
# print('+', '-')
# If the sequence ends with a comma, Python leaves the line unfinished,
# so the value printed next appears on the same line.
# print('+',)
# print('-')
# The output of these statements is '+ -'.
#  A print function all by itself ends the current line and goes to the next line.

# Answer:


def draw_grid():
    column = '+ - - - - + - - - - +'
    row = '|         |         |'
    print(column)
    do_twice(print_twice, row)
    print(column)
    do_twice(print_twice, row)
    print(column)


draw_grid()

# 2. Write a function that draws a similar grid with four rows and four columns.

# Answer:


def draw_grid2():
    column = '+ - - - - + - - - - + - - - - + - - - - +'
    row = '|         |         |         |         |'
    print(column)
    do_twice(print_twice, row)
    print(column)
    do_twice(print_twice, row)
    print(column)
    do_twice(print_twice, row)
    print(column)
    do_twice(print_twice, row)
    print(column)


draw_grid2()
