# Chapter Seven Exercises



# Exercise 7.1
# Question:

# Rewrite the function print_n from "Recursion" using iteration instead of recursion.

# Answer:


def print_n(n):
    for i in range(n, 0, -1):
        print(i)
        if i == 1:
            print("Blastoff!")


print_n(5)



# Exercise 7.2
# Question:

# Encapsulate this loop in a function called square_root that takes a as a parameter,
# chooses a reasonable values of x, and returns an estimate of the square root of a.

# Answer:


def square_root(a, x):
    while True:
        y = (x + a / x) / 2
        if y == x:
            return y
        x = y



# Exercise 7.3
# Question:

# Write a function called test_square_root that prints a table like this.

# Answer:

from math import sqrt


def test_square_root(n):
    for i in range(1, n + 1):
        print(i, square_root(i, i / 2), sqrt(i), abs(square_root(i, i / 2) - sqrt(i)))


test_square_root(9)



# Exercise 7.4
# Question:

# The built-in function eval takes a string and evaluates it using the Python interpreter.
# Write a function called eval_loop that iteratively prompts the user, takes the resulting input
# and evaluates it using eval, and prints the result.

# Answer:


def eval_loop():
    while True:
        user_input = input('>>>')
        if user_input == 'done':
            break
        value = eval(user_input)
        print(value)


eval_loop()



# Exercise 7.5
# Question:

# Write a function called estimate_pi that uses this formula to compute and return an estimate of pi.
# It should use a while loop to compute terms of the summation until the last term is smaller than 1e - 15 (10^-15).
# You can check the results by comparing it to math.pi.

# Answer:

import math


def factorial(n):
    if n == 0:
        return 1
    else:
        fact = factorial(n - 1)
        result = n * fact
        return result


def estimate_pi():
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4 * k) * (1103 + 26390 * k)
        den = factorial(k) ** 4 * 396 ** (4 * k)
        term = factor * num / den
        total += term

        if abs(term) < 1e-15:
            break
        k += 1

    return 1 / total


print(estimate_pi())
