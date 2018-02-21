# Chapter 11 Quiz


# 1.
# Which of the following best describes "Regular Expressions"?


# A small programming language unto itself


# 2.
# Which of the following is the way we match the "start of a line"
# in a regular expression?


# ^


# 3.
# What would the following mean in a regular expression? [a-z0-9]


# Match a lowercase letter or a digit


# 4.
# What is the type of the return value of the re.findall() method?


# A list of strings


# 5.
# What is the "wild card" character in a regular expression (i.e., the character that matches any
# character)?


# .


# 6.
# What is the difference between the "+" and "*" character in regular expressions?


# The "+" matches at least one character and the "*" matches zero or more characters


# 7.
# What does the "[0-9]+" match in a regular expression?


# One or more digits


# 8.
# What does the following Python sequence print out?

import re

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)


# ['From: Using the :']


# 9.
# What character do you add to the "+" or "*" to indicate that the match is to be done in a non-greedy
# manner?


# ?


# 10.
# Given the following line of text:

"From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

# What would the regular expression '\S+?@\S+' match?


# stephen.marquard@uct.ac.za


# ----------------------------------------------------------------------------------------------------------------------


# Chapter 11 Assignments


# Extracting Data with Regular Expressions


file_pointer = open('regex_sum_325328.txt')

text = file_pointer.readlines()

sum = 0

for line in text:
    numbers = re.findall('[0-9]+', line.strip())
    if len(numbers) > 0:
        for number in numbers:
            sum += int(number)

print(sum)








