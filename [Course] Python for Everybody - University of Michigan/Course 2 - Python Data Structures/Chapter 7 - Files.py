# Chapter 7 Quiz


# 1.
# Given the architecture and terminology we introduced in Chapter 1, where are files
# stored?


# Secondary memory


# 2.
# What is stored in a "file handle" that is returned from a successful open() call?


# The handle is a connection to the file's data


# 3.
# What do we use the second parameter of the open() call to indicate?


# Whether we want to read data from the file or write data to the file


# 4.
# What Python function would you use if you wanted to prompt the user for a file name to
# open?


# input()


# 5.
# What is the purpose of the newline character in text files?


# It indicates the end of one line of text and the beginning of another line of text


# 6.
# If we open a file as follows:

xfile = open('mbox.txt')

# What statement would we use to read the file one line at a time?


# for line in xfile:


# 7.
# What is the purpose of the following Python code?

fhand = open('mbox.txt')
x = 0
for line in fhand:
       x = x + 1
print(x)


# Count the lines in the file 'mbox.txt'


# 8.
# If you write a Python program to read a text file and you see extra blank lines in the
# output that are not present in the file input as shown below, what Python string function
# will likely solve the problem?

# From: stephen.marquard@uct.ac.za

# From: louis@media.berkeley.edu

# From: zqian@umich.edu

# From: rjlowe@iupui.edu

# ...


# rstrip()


# 9.
# The following code sequence fails with a traceback when the user enters a file that does
# not exist. How would you avoid the traceback and make it so you could print out your
# own error message when a bad file name was entered?

fname = input('Enter the file name: ')
fhand = open(fname)


# try / except


# 10.
# What does the following Python code do?

fhand = open('mbox-short.txt')
inp = fhand.read()


# Reads the entire file into the variable inp as a string


# ----------------------------------------------------------------------------------------------------------------------


# Chapter 7 Assignments


# Assignment 7.1


file_name = input("Enter file name: ")  # Enter words.txt
file_pointer = open(file_name)
for line in file_pointer:
    print(line.upper().strip())


# Assignment 7.2


file_name = input("Enter file name: ")  # Enter mbox-short.txt
file_pointer = open(file_name)

res = []

for line in file_pointer:
    if line.startswith("X-DSPAM-Confidence:"):
        line.replace(" ", "")
        colon_location = line.find(":")
        res.append(float(line[colon_location + 1:]))

print("Average spam confidence:", sum(res) / len(res))