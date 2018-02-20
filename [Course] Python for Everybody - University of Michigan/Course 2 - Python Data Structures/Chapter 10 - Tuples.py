# Chapter 10 Quiz


# 1.
# What is the difference between a Python tuple and Python list?


# Lists are mutable and tuples are not mutable


# 2.
# Which of the following methods work both in Python lists and Python tuples?


# index()


# 3.
# What will end up in the variable y after this code is executed?

x , y = 3, 4


# 4


# 4.
# In the following Python code, what will end up in the variable y?

x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()


# A list of tuples


# 5.
# Which of the following tuples is greater than x in the following Python sequence?

x = (5, 1, 3)
if ??? > x :
   ...


# (6, 0, 0)


# 6.
# What does the following Python code accomplish, assuming the c is a non-empty
# dictionary?

tmp = list()
for k, v in c.items() :
    tmp.append( (v, k) )


# It creates a list of tuples where each tuple is a value, key pair


# 7.
# If the variable data is a Python list, how do we sort it in reverse order?

if key in counts:
    counts[key] = counts[key] + 1
else:
    counts[key] = 1


# data.sort(reverse=True)


# 8.
# Using the following tuple, how would you print 'Wed'?

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')


# print(days[2])


# 9.
# In the following Python loop, why are there two iteration variables (k and v)?

c = {'a':10, 'b':1, 'c':22}
for k, v in c.items() :
    ...


# Because the items() method in dictionaries returns a list of tuples


# 10.
# Given that Python lists and Python tuples are quite similar - when might you prefer to use
# a tuple over a list?


# For a temporary variable that you will use and discard without modifying


# ----------------------------------------------------------------------------------------------------------------------


# Chapter 10 Assignments


# Assignment 10.2


file_name = input("Enter file name:")  # Enter mbox-short.txt
file_pointer = open(file_name)

email_hours_histogram = {}

for line in file_pointer:
    if not line.startswith("From "):
        continue

    time = line.split()[5].split(':')
    hour = time[0]
    email_hours_histogram[hour] = email_hours_histogram.get(hour, 0) + 1

hours = list()

for k, v in email_hours_histogram.items():
    hours.append((k, v))

hours.sort()

for key, val in hours:
    print(key, val)





