# Chapter 9 Quiz


# 1.
# How are Python dictionaries different from Python lists?


# Python lists maintain order and dictionaries do not maintain order


# 2.
# What is a term commonly used to describe the Python dictionary feature in other
# programming languages?


# Associative arrays


# 3.
# What would the following Python code print out?

stuff = dict()
print(stuff['candy'])


# The program would fail with a traceback


# 4.
# What would the following Python code print out?

stuff = dict()
print(stuff.get('candy',-1))


# -1


# 5.
# (T/F) When you add items to a dictionary they remain in the order in which you added
# them.


# False


# 6.
# What is a common use of Python dictionaries in a program?


# Building a histogram counting the occurrences of various strings in a file


# 7.
# Which of the following lines of Python is equivalent to the following sequence of
# statements assuming that counts is a dictionary?

if key in counts:
    counts[key] = counts[key] + 1
else:
    counts[key] = 1


# counts[key] = counts.get(key,0) + 1


# 8.
# In the following Python, what does the for loop iterate through?

x = dict()
...
for y in x :
     ...


# It loops through the keys in the dictionary


# 9.
# Which method in a dictionary object gives you a list of the values in the dictionary?


# values()


# 10.
# What is the purpose of the second parameter of the get() method for Python dictionaries?


# To provide a default value if the key is not found


# ----------------------------------------------------------------------------------------------------------------------


# Chapter 9 Assignments


# Assignment 9.4


file_name = input("Enter file name:")  # Enter mbox-short.txt
file_pointer = open(file_name)

email_histogram = {}

for line in file_pointer:
    if not line.startswith("From "):
        continue

    sender = line.split()[1]
    email_histogram[sender] = email_histogram.get(sender, 0) + 1

max_count = None
max_email = None

for email, count in email_histogram.items():
    if max_count is None or count > max_count:
        max_email = email
        max_count = count
print (max_email, max_count)