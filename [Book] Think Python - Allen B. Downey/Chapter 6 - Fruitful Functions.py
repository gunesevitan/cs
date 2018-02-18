# Chapter Six Exercises



# Exercise 6.1
# Write a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y.



def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1



# Exercise 6.2
# Use incremental development to write a function called hypotenuse that
# returns the length of the hypotenuse of a right triangle
# given the lengths of the two legs as arguments.



from math import sqrt

def hypotenuse(a, b):

    h = (a ** 2) + (b ** 2)
    h = sqrt(h)
    return h



# Exercise 6.3
# Write a function is_between(x, y, z) that returns True if x <= y <= z or False otherwise.



def is_between(x, y, z):
    return x <= y <= z



# Exercise 6.4
# Draw a stack diagram for the following program. What does the program print?

# def b(z):
#     prod = a(z, z)
#     print z, prod
#     return prod

# def a(x, y):
#     x = x + 1
#     return x * y

# def c(x, y, z):
#     total = x + y + z
#     square = b(total) ** 2
#     return square

# x = 1
# y = x + 1
# print c(x, y + 3, x + y)



# from swampy.Lumpy import Lumpy

# def b(z):
#     prod = a(z, z)
#     print(z, prod)
#     return prod

# def a(x, y):
#     x = x + 1
#     lumpy.object_diagram()
#     return x * y

# def c(x, y, z):
#     total = x + y + z
#     square = b(total) ** 2
#     return square

# lumpy = Lumpy()
# lumpy.make_reference()

# x = 1
# y = x + 1
# print(c(x, y + 3, x + y))



# Exercise 6.5
# The Ackermann function, A(m, n) is defined:

#           { n + 1                     if m = 0
# A(m, n) = { A(m - 1,1)                if m > 0 and n = 0
#           { A(m - 1, A(m, n - 1))     if m > 0 and n > 0

# Write a function named ack that evaluates Ackermann's function.
# Use your function to evaluate ack(3, 4), which should be 125.
# What happens for larger values of m and n?



def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    if m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))

		
print(ack(3, 4))

# For larger values RecursionError is yield because maximum recursion depth is reached.



# Exercise 6.6
# A palindrome is a word that is spelled the same backward and forward, like "noon" and "redivider".
# Recursively, a word is a palindrome if the first and last letters are the same and the middle is palindrome.

# The following are functions that take a string argument and return the first, last, and middle letters.

def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]



# 1. Type these functions into a file named palindrome.py and test them out.
#    What happens if you call middle with a string with two letters? One letter? What about the empty string?

print(middle("ab"))  # Returns an empty string
print(middle("a"))   # Returns an empty string
print(middle(""))    # Returns an empty string

# 2. Write a function called is_palindrome that takes a string argument and returns True if it a palindrome
#    and False otherwise. Remember that you can use the built-in function len to check the length of a string.

def is_palindrome(word):

    if first(word) != last(word):
        return False
    elif first(word) == last(word) and (len(word) == 3 or len(word) == 2):
        return True
    elif first(word) == last(word):
        word = middle(word)
        return is_palindrome(word)
    else:
        return False



# Exercise 6.7
# A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function
# called is_power that takes parameters a and b and returns True if a is a power of b.



def is_power(a, b):
    if a == b:
        return True
    elif a % b == 0:
        return is_power(a / b, b)
    else:
        return False



# Exercise 6.8
# Write a function called gcd that takes parameters a and b and returns their greatest common divisor.



def gcd(a, b):
    if a == b:
        return a
    else:
        values = sorted([a, b])
        return gcd(values[1] - values[0], values[0])
