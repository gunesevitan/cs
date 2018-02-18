# Chapter Eleven Exercises



# Exercise 11.1
# Write a function that reads the words in words.txt and stores them as keys in a
# dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast
# way to check whether a string is in the dictionary.



def create_word_dict():
    fin = open('words.txt')

    words = {}
    for line in fin:
        word = line.strip()
        words[word] = word
    return words



# Exercise 11.2
# Use get to write histogram more concisely.
# You should be able to eliminate the if statement



def histogram(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1  # get will return given key's value and add +1 to the value
								# if the key doesn't exist, it will create it with value 0 and add +1
    return d


h = histogram("brontosaurus")
print(h)



# Exercise 11.3
# Modify print_hist to print the keys and their values in alphabetical order.



def print_hist(h):
    hist_keys = sorted(h.keys())
    for key in hist_keys:
        print(key, h.get(key))

print_hist(h)



# Exercise 11.4
# Modify reverse_lookup so that it builds and returns a list of all keys that map to v, or
# an empty list if there are none.



def reverse_lookup(d, v):
    temp = []
    for k in d:
        if d[k] == v:
            temp.append(k)
    return temp



# Exercise 11.5
# Read the documentation of the dictionary method setdefault and use it to write a
# more concise version of invert_dict.



def invert_dict(d):
    inverse = {}
    for key, val in d.items():
        inverse.setdefault(val, []).append(key)
    return inverse



# Exercise 11.6
# Run this version of fibonacci and the original with a range of parameters and compare
# their run times.



import time

known = {0:0, 1:1}  # Cache for the computed values

def fibonacci(n):
    if n in known:  # Checking the cache first in order to save time
        return known[n]

    res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res

def fibonacci_old(n):
    if n < 2:
        return n
    return fibonacci_old(n - 2) + fibonacci_old(n - 1)


# Fibonacci

start_time_fib = time.time()
print(fibonacci(30))
print("Fibonacci with memoization takes %s seconds" % (time.time() - start_time_fib))

# Fibonacci Old

start_time_fib_old = time.time()
print(fibonacci_old(30))
print("Fibonacci without memoization takes %s seconds" % (time.time() - start_time_fib_old))

# Memoized fibonacci takes constant time to finish the call because it doesn't need to compute values
# every time. Old fibonacci function is probably growing linearly.



# Exercise 11.7
# Memoize the Ackermann function from Exercise 6.5 and see if memoization makes it
# possible to evaluate the function with bigger arguments.



cache = {}

def ackermann(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m-1, 1)
    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ackermann(m - 1, ackermann(m, n - 1))
        return cache[m, n]

print(ackermann(3, 4))
print(ackermann(3, 6))



# Exercise 11.9
# If you did Exercise 10.8, you already have a function named has_duplicates that takes
# a list as a parameter and returns True if there is any object that appears more than once
# in the list.
# Use a dictionary to write a faster, simpler version of has_duplicates.



def has_duplicates(l):
    seen = {}
    for i in l:
        if i in seen:
            return True
        seen[i] = True
    return False



# Exercise 11.10
# Two words are "rotate pairs" if you can rotate one of them and get the other.
# Write a program that reads a wordlist and finds all the rotate pairs.



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



def word_dict():
    d = {}
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    return d


def rotate_pairs(word, word_dict):
    for i in range(1, 14):
        rotated_word = rotate_word(word, i)
        if rotated_word in word_dict:
            print(word, i, rotated_word)



# Exercise 11.11
# Write a program that lists all the words that solve the Puzzler.



def make_word_dict():
    d = {}
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    return d


def are_homophones(a, b, phonetic):
    if a not in phonetic or b not in phonetic:
        return False

    return phonetic[a] == phonetic[b]  # Comparing the given words' phonetics'
