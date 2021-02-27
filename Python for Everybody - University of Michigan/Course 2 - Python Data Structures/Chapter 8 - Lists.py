# Chapter 8 - Lists Quiz


# 1.
# How are "collection" variables different from normal variables?


# Collection variables can store multiple values in a single variable


# 2.
# What are the Python keywords used to construct a loop to iterate through a list?


# for / in


# 3.
# For the following list, how would you print out 'Sally'?

friends = [ 'Joseph', 'Glenn', 'Sally' ]


# print(friends[2])


# 4.
# What would the following Python code print out?

fruit = 'Banana'
fruit[0] = 'b'
print(fruit)


# Nothing would print - the program fails with a traceback


# 5.
# Which of the following Python statements would print out the length of a list stored in the
# variable data?


# print(len(data))


# 6.
# What type of data is produced when you call the range() function?

x = range(5)


# A list of integers


# 7.
# What does the following Python code print out?

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))


# 6


# 8.
# Which of the following slicing operations will produce the list [12, 3]?


# t[2:4]


# 9.
# What list method adds a new item to the end of an existing list?


# append()


# 10.
# What will the following Python code print out?

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])


# Glenn


# ----------------------------------------------------------------------------------------------------------------------


# Chapter 8 - Lists Assignments


# Assignment 8.4


file_name = input("Enter file name: ")  # Enter romeo.txt
file_pointer = open(file_name)

res = []

for line in file_pointer:
    for word in line.split():
        if word not in res:
            res.append(word)

res.sort()
print(res)


# Assignment 8.5


file_name = input("Enter file name: ")  # Enter mbox-short.txt
file_pointer = open(file_name)
count = 0

for line in file_pointer:
    if not line.startswith("From "):
        continue
    sender = line.split()[1]
    print(sender)
    count += 1

print("There were", count, "lines in the file with From as the first word")
