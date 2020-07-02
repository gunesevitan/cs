# Chapter Ten Exercises



# Exercise 10.1
# Write a function called nested_sum that takes a nested list of integers and add up the elements from all of the
# nested lists.



def nested_sum(nested_list):
    total = 0
    for item in nested_list:
        if type(item) == list:
            total += nested_sum(item)  # If item's type is list, calling the nested_sum on the item
        else:
            total += item
    return total


nest = [[1, 2, 3], [4, 5, 6], [1, [6, [3, 23]], 7], 5]
print(nested_sum(nest))



# Exercise 10.2
# Use capitalize_all to write a function named capitalize_nested that takes a nested list of strings and
# returns a new nested list with all strings capitalized.



def capitalize_all(list):
    result = []
    for string in list:
        result.append(string.capitalize())
    return result


def capitalize_nested(nested_list):
    result = []
    for item in nested_list:
        if type(item) == list:
            result.append(capitalize_all(item))
        else:
            result.append(item.capitalize())
    return result


print(capitalize_nested(["string", ["asd"], "hello", "world", ["hi", "worldd"]]))



# Exercise 10.3
# Write a function that takes a list of numbers and returns the cumulative sum;
# that is, a new list where the ith element is the sum of the first i+1 elements from the original list.
# For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].



def cumulative_sum(numbers):
    result = []
    total = 0
    for number in numbers:
        total += number
        result.append(total)  # Adding the total to the result every iteration
    return result


print(cumulative_sum([1, 2, 3, 4, 7, 12]))



# Exercise 10.4
# Write a function called middle that takes a list and returns a new list that contains all
# but the first and last elements. So middle([1,2,3,4]) should return [2,3].



def middle(l):
    return l[1:len(l) - 1]



# Exercise 10.5
# Write a function called chop that takes a list,
# modifies it by removing the first and last elements, and returns None.



def chop(l):
    del l[0]
    del l[(len(l)-1)]
    return None


list_going_to_be_chopped = [1, 2, 3, 4, 5, 6]
chop(list_going_to_be_chopped)
print(list_going_to_be_chopped)



# Exercise 10.6
# Write a function called is_sorted that takes a list as a parameter and returns True
# if the list is sorted in ascending order and False otherwise. You can assume (as a precondition)
# that the elements of the list can be compared with the relational operators <, >, etc.



def is_sorted(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False

    return True



# Exercise 10.7
# Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function called is_anagram that takes two strings and returns True if they are anagrams.



def is_anagram(s1, s2):
    t1 = list(s1)
    t2 = list(s2)
    t1.sort()
    t2.sort()

    return t1 == t2



# Exercise 10.8
# The (so-called) Birthday Paradox:

# 1. Write a function called has_duplicates that takes a list and returns True if there is any
#    element that appears more than once. It should not modify the original list.

# 2. If there are 23 students in your class, what are the chances that two of you have the same
#    birthday? You can estimate this probability by generating random samples of 23 birthdays and
#    checking for matches. Hint: you can generate random birthdays with the randint function
#    in the random module.



import random

def has_duplicates(l):
    sorted_l = l[:]
    sorted_l.sort()
    for i in range(len(sorted_l) - 1):
        if sorted_l[i] == sorted_l[i + 1]:
            return True


def birthday_generator(n):
    birthdays = []
    for i in range(n):
        birthday = random.randint(1, 365)
        birthdays.append(birthday)

    return birthdays


def count_matches(students, samples):
    count = 0
    for i in range(samples):
        birthdays = birthday_generator(students)
        if has_duplicates(birthdays):
            count += 1
    return count


students = 23
simulations = 1000
count = count_matches(students, simulations)

print('In %d simulations' % simulations)
print ('with %d students' % students)
print ('there were %d simulations with at least one match' % count)



# Exercise 10.9
# Write a function called remove_duplicates that takes a list and returns a new
# list with only the unique elements from the original.
# Hint: they don’t have to be in the same order.



def remove_duplicates(l):
    l_copy = []
    for i in l:
        if i not in l_copy:
            l_copy.append(i)

    return l_copy



# Exercise 10.10
# Write a function that reads the file words.txt and builds a list with one element
# per word. Write two versions of this function, one using the append method and the other using
# the idiom t = t + [x]. Which one takes longer to run? Why?



import time


def list_appender():
    words = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        words.append(word)

    return words


def list_concatter():
    words = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        words += word

    return  words


# Append
start_time_append = time.time()
appended_list = list_appender()
print("Appending a list takes %s seconds" % (time.time() - start_time_append))

# +=
start_time_concat = time.time()
concatted_list = list_concatter()
print("Concatting a list takes %s seconds" % (time.time() - start_time_concat))

print("Append / Concat ratio is:", start_time_append / start_time_concat)

# Append is faster because it will add one item to the list,
# while += will copy all elements of right-hand-side list into the left-hand-side list.



# Exercise 10.11
# Write a function called bisect that takes a sorted list and a target value and returns
# the index of the value in the list, if it’s there, or None if it’s not.



def bisect(l, target):
    start = 0
    end = len(l) - 1
    while True:
        if end < start:
            return -1
        mid = (start + end) // 2

        if l[mid] < target:
            start = mid + 1
        elif l[mid] > target:
            end = mid -1
        else:
            return mid



# Exercise 10.12
# Two words are a “reverse pair” if each is the reverse of the other.
# Write a program that finds all the reverse pairs in the word list.



def reverse_pair(words, word):
    reverse_word = word[::-1]
    return bisect(words, reverse_word)



# Exercise 10.13
# Two words “interlock” if taking alternating letters from each forms a new word. For
# example, “shoe” and “cold” interlock to form “schooled.”



def interlock(words, interlocked_word):
    first_word = interlocked_word[::2]  # Extracting the first word from the interlocked word
    second_word = interlocked_word[1::2]  # Extracting the second word from the interlocked word
    return bisect(words, first_word) and bisect(words, second_word)  # If both words exist in the list, they can interlock
