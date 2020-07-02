# Chapter Twelve Exercises



# Exercise 12.1
# Write a function called sumall that takes any number of arguments and returns their sum.



def sumall(*args):
    return sum(args)



# Exercise 12.2
# In this example, ties are broken by comparing words, so words with the same length
# appear in reverse alphabetical order. For other applications you might want to break ties
# at random. Modify this example so that words with the same length appear in random order.
# Hint: see the random function in the random module.



from random import random

def sort_by_length_random(words):
    l = []
    for word in words:
       l.append((len(word), random.random(), word))

    l.sort(reverse=True)  # List will be sorted by length first, then by a random number between 0 and 1.

    res = []
    for length, _, word in l:
        res.append(word)
    return res



# Exercise 12.3
# Write a function called most_frequent that takes a string and prints the letters in
# decreasing order of frequency. Find text samples from several different languages and see
# how letter frequency varies between languages.



def most_frequent(s):

    hist = make_histogram(s)

    temp = []
    for word, freq in hist.items():
        temp.append((freq, word))

    temp.sort(reverse=True)  # Sorting the words by their frequency in descending order

    res = []
    for freq, x in temp:
        res.append(x)

    return res


def make_histogram(s):
    hist = {}
    for c in s:
        hist[c] = hist.get(c, 0) + 1
    return hist



# Exercise 12.4



# 1. Write a program that reads a word list from a file (see Section 9.1)
#    and prints all the sets of words that are anagrams.
#    Here is an example of what the output might look like:
#    ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
#    ['retainers', 'ternaries']
#    ['generating', 'greatening']
#    ['resmelts', 'smelters', 'termless']
#    Hint: you might want to build a dictionary that maps from a set of letters
#    to a list of words that can be spelled with those letters. The question is,
#    how can you represent the set of letters in a way that can be used as a key?



def sort_string(s):
    temp = list(s)
    temp.sort()
    temp = ''.join(temp)
    return temp


def find_anagrams(file):
    d = {}

    for line in open(file):
        word = line.strip().lower()
        sorted_string = sort_string(word)

        if sorted_string not in d:
            d[sorted_string] = [word]
        else:
            d[sorted_string].append(word)
    return d


def print_anagrams(d):
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)



# 2. Modify the previous program so that it prints the largest set of anagrams first,
#    followed by the second largest set, and so on.



def print_anagrams_descending(d):
    temp = []
    for v in d.values():
        if len(v) > 1:
            temp.append((len(v), v))

    temp.sort(reverse=True)

    # print the sorted list
    for anagram in temp:
        print(anagram)



# 3. In Scrabble a "bingo" is when you play all seven tiles in your rack, along
#    with a letter on the board, to form an eight-letter word. What set of 8
#    letters forms the most possible bingos? Answer: 'aeginrst'
#    Hint: there are seven.



def filter_length(d, length):
    temp = {}
    for word, anagrams in d.iteritems():
        if len(word) == length:
            temp[word] = anagrams
    return temp



# Exercise 12.5
# Two words form a "metathesis pair" if you can transform one into the other by swapping
# two letters; for example, "converse" and "conserve." Write a program that finds all of the
# metathesis pairs in the dictionary. Hint: don't test all pairs of words, and don't test all
# possible swaps.



def metathesis_pairs(d):
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if letter_difference(word1, word2) == 2:  # Looking for 2 different letters in both words
                    print(word1, word2)


def letter_difference(word1, word2):
    count = 0
    for letter_word1, letter_word2 in zip(word1, word2):
        if letter_word1 != letter_word2:  # Computing the different letters in 2 words
            count += 1

    return count
