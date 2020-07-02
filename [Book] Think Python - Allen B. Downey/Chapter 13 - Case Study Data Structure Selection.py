# Chapter Thirteen Exercises



# Exercise 13.1
# Write a program that reads a file, breaks each line into words, strips whitespace and
# punctuation from the words, and converts them to lowercase.
# Hint: The string module provides strings named whitespace, which contains space,
# tab, newline, etc., and punctuation which contains the punctuation characters.



from string import punctuation, whitespace

def word_splitter(f):

    text = ""
    fin = open(f)

    for c in fin.read():
        if c in punctuation or c in whitespace:
            continue
        else:
            text += c.lower()
    return text



# Exercise 13.2
# Go to Project Gutenberg (gutenberg.org) and download your favorite out-of-copyright book in plain text format.
# Modify your program from the previous exercise to read the book you downloaded,
# skip over the header information at the beginning of the file, and process the rest of the words as before.
# Then modify the program to count the total number of words in the book, and the number of times each word is used.
# Print the number of different words used in the book. Compare different books by
# different authors, written in different eras. Which author uses the most extensive vocabulary?



def skip_header(file):
    for line in file:
        if line.startswith('Produced by'):
            break


def process_line(line, words):
    for word in line.split():
        word = word.lower().strip(punctuation)
        if word.isalpha():
            words[word] = words.get(word, 0) + 1


def process_file(filename):

    words_used = {}
    fp = open(filename, encoding="utf-8")

    skip_header(fp)  # This sets the file pointer to the end of the header.

    for line in fp:
        process_line(line, words_used)  # This loop will start from just after the header.

    return words_used


pride_and_prejudice = process_file("Pride and Prejudice.txt")
heart_of_darkness = process_file("Heart of Darkness.txt")

# print(pride_and_prejudice)
# print(heart_of_darkness)



# Exercise 13.3
# Modify the program from the previous exercise to print the 20 most frequently-used
# words in the book.



def show_words_ascending(words_used, n):
    freqs = []
    for v in sorted(words_used.values(), reverse=True):
        freqs.append(v)

    freqs = freqs[:n]

    top_words = []
    for k,v in words_used.items():
        if v in freqs:
            top_words.append((v, k))

    top_words.sort(reverse=True)

    return top_words


# print(show_words_ascending(pride_and_prejudice, 20))



# Exercise 13.4
# Modify the previous program to read a word list and then print all the words in the book
# that are not in the word list. How many of them are typos? How many of them
# are common words that should be in the word list, and how many of them are really obscure?



def not_in_word_list(book_file, words_file):

    word_list_pointer = open(words_file)
    word_list = []

    for line in word_list_pointer:
        word_list.append(line.strip())  # Having a word list filled with given words_file

    book_words = process_file(book_file)  # Having a histogram of words from the book_file

    for k in book_words.keys():
        if k not in word_list:  # Printing the words that are in the book but not in the word list
            print(k)


#  not_in_word_list("Heart of Darkness.txt", "words.txt")



# Exercise 13.5
# Write a function named choose_from_hist that takes a histogram and returns a random value from the histogram,
# chosen with probability in proportion to frequency. For example, for this histogram:
# >>> t = ['a', 'a', 'b']
# >>> hist = histogram(t)
# >>> print(hist)
# {'a': 2, 'b': 1}
# your function should return ’a’ with probability 2/3 and ’b’ with probability 1/3.



from random import choice

t = ['a', 'a', 'b']


def histogram(t):
    hist = {}
    for item in t:
        hist[item] = hist.get(item, 0) + 1
    return hist


hist = histogram(t)
print(hist)


def choose_from_hist(hist):
    temp = []
    for k,v in hist.items():
        for i in range(v):
            temp.append(k)  # Adding a key value times to the list.

    return choice(temp)


def test_probability(sample):
    test = []
    for i in range(sample):
        test.append(choose_from_hist(hist))  # Choosing items from the histogram given sample times

    a_count = test.count("a")
    b_count = test.count("b")
    print("In a sample of %d iterations, %d items are chosen a and %d items are chosen b. "
          "The ratio of a/b is %f" % (sample, a_count, b_count, a_count / b_count))


print(test_probability(1000))



# Exercise 13.6
# Python provides a data structure called set that provides many common set operations.
# Read the documentation at docs.python.org/lib/types-set.html and write a program
# that uses set subtraction to find words in the book that are not in the word list.



def subtract_words(book_words, words_list):
    return set(book_words) - set(words_list)  # They are both dictionaries casted to sets



# Exercise 13.7
# This algorithm works, but it is not very efficient; each time you choose a random,
# it rebuils the list, which is as big as the original book. An obvious improvement is to
# build the list once and then make multiple selections, but the list is still big.
# An alternative is:
# 1. Use keys to get a list of the words in the book.
# 2. Build a list that contains the cumulative sum of the word frequencies.
#    The last item in the list is the total number of words in the book, n.
# 3. Choose a random number from 1 to n. Use a bisection search to find the index
#    where the random number would be inserted in the cumulative sum.
# 4. Use the index to find the corresponding word in the word list.



from random import randint
from bisect import bisect


def random_word(hist):
    words = []
    freqs = []
    total_freq = 0

    for word, freq in hist.items():
        total_freq += freq
        words.append(word)
        freqs.append(total_freq)  # Adding the cumulative sum of the frequency

    target = randint(0, total_freq - 1)  # Searching the cumulative frequency
    index = bisect(freqs, target)
    return words[index]



# Exercise 13.8
# Markov analysis:
# 1. Write a program to read a text from a file and perform Markov analysis. The result
#    should be a dictionary that maps from prefixes to a collection of possible suffixes.
#    The collection might be a list, tuple, or dictionary; it is up to you to make an
#    appropriate choice. You can test your program with prefix length two, but you should
#    write the program in a way that makes it easy to try other lengths.



suffix_map = {}  # Prefix mapping to a list suffixes
prefix = ()      # Tuple of words

def process_file(filename, order=2):

    file_pointer = open(filename)
    skip_header(file_pointer)  # Skipping the header with defined function in 13.2

    for line in file_pointer:
        for word in line.rstrip().split():
            process_word(word, order)



def shift(t, word):
    return t[1:] + (word,)  # Removing tuples first word and adding the given word to the end


def process_word(word, order=2):

    global prefix

    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        suffix_map[prefix].append(word)  # Appending the word to the suffix list mapped to a prefix
    except KeyError:
        suffix_map[prefix] = [word]  # If prefix doesn't exist, creating it

    prefix = shift(prefix, word)



# 2. Add a function to the previous program to generate random text based on the
#    Markov analysis.



def random_text(num_words):

    start = choice(suffix_map.keys())  # Starting with a random prefix

    for i in range(num_words):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            random_text(num_words - i)
            return

        word = choice(suffixes)  # Choosing a random suffix
        start = shift(start, word)