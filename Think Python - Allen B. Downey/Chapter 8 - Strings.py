# Chapter Eight Exercises



# Exercise 8.1
# Question:

# Write a function that takes a string as an argument and displays the letters backward, one per line.

# Answer:


def print_backwards(s):
    for i in range(len(s) - 1, -1, -1):
        print(s[int(i)])


print_backwards("print backwards")



# Exercise 8.2
# Question:

prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    print(letter + suffix)

# Of course, that's not quite right because "Ouack" and "Quack" are misspelled.
# Modify the program to fix this error.

# Answer:

for letter in prefixes:
    if letter in ["O","Q"]:
        suffix = "u" + suffix
    print(letter + suffix)
    suffix = "ack"



# Exercise 8.3
# Question:

# Given that a fruit is a string, what does fruit[:] mean?

# Answer:

fruit = "banana"
print(fruit[:])  # The entire string



# Exercise 8.4
# Question:

# Modify find so that it has a third parameter, the index in word where it should start looking.

# Answer:


def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1



# Exercise 8.5
# Question:

# Encapsulate this code in a function named count, and generalize it
# so that it accepts the string and the letter as arguments.

# Answer:

def count(word, letter):
    counter = 0
    for i in word:
        if i == letter:
            counter += 1
    return counter



# Exercise 8.6
# Question:

# Rewrite this function so that instead of traversing the string, it uses the three-parameter
# version of find from the previous section.

# Answer:

def count_find(word, letter):
    counter = 0
    start_index = 0

    while start_index < len(word):
      next_letter_position = find(word, letter, start_index)
      if next_letter_position != -1:
        counter += 1
        start_index = next_letter_position + 1
      else:
        break
    return counter


print(count_find("banana","a"))



# Exercise 8.7
# Question:

# There is a string method called count that is similar to the function in the previous exercise.
# Read the documentation of this method and write an invocation that counts the number of as in 'banana'.


# Answer:

print("banana".count("a"))



# Exercise 8.9
# Question:

# Starting with this diagram, execute the program on paper, changing the values of i and j during each iteration.
# Find and fix the second error in this function.


# Answer:

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2) - 1

    while j > -1:  # Mistake was here. It should be j > -1 instead of j > 0.
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1

    return True

print(is_reverse("pots", "stop"))



# Exercise 8.10
# Question:

# A string slice can take a third index that specifies the "step size;" that is, the number of spaces
# between successive characters. A step size of 2 means every other character; 3 means every third, etc.
# A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string.
# Use this idiom to write a one-line version of is_palindrome from Exercise 6.6.


# Answer


def is_palindrome(s):
    return s == s[::-1]



# Exercise 8.11
# Question:

# The following functions are all intended to check whether a string contains any lowercase letters,
# but at least some of them are wrong. For each function, describe what the function actually does.


# Answer


# Returns True or False depending on the first letter. Doesn't check the rest of the string.
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


# This will always return True because it checks the string 'c'.
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return "True"
        else:
            return 'False'

# Returns True or False depending on the last letter. flag will always change during iteration.
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

# If c.islower() becomes True at least 1 time, the flag will be True.
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# This will return False as soon as an uppercase letter is found.
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True



# Exercise 8.12
# Question:

# Write a function called rotate_word that takes a string and an integer as parameters, and that returns a new
# string that contains the letters from the original string "rotated" by the given amount.

# Answer


def rotate_letter(letter, n):

    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):

    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res

