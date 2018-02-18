# Chapter Nine Exercises



# Exercise 9.1
# Write a program that reads words.txt and prints only the words with more than 20 characters (not counting whitespace).



def print_words():
    fin = open("words.txt")
    for line in fin:
        if len(line.strip()) > 20:  
            print(line.strip())  # Stripping the whitespace


print_words()



# Exercise 9.2
# Modify your program from the previous section to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e".



def has_no_e(word):
    for c in word:
        if c == "e":
            return False
    return True

def has_no_e_words():
    fin = open("words.txt")
    no_e_words = 0
    words = 0
    for line in fin:
        words += 1
        if has_no_e(line):
            print(line)
            no_e_words += 1
			
    print((no_e_words / words) * 100)  # The ratio of no_e_words in total words



# Exercise 9.3
# Write a function named avoids that takes a word and a string of forbidden letters, and
# returns True if the word doesn't use any of the forbidden letters.

# Modify your program to prompt the user to enter a string of forbidden letters and then
# print the number of words that don't contain any of them. Can you find a combination
# of 5 forbidden letters that excludes the smallest number of words?



def avoids(word, forbidden_letters):
    i = 0
    while i < len(word):
        if word[i] in forbidden_letters:
            return False
        else:
            i += 1
    return True


def avoids_prompt():

    forbidden_letters = input('Enter forbidden letters without spaces:')
    fin = open("words.txt")

    word_count = 0
    for line in fin:
        if avoids(line.strip(), forbidden_letters):
            print(line.strip())
            word_count += 1
    return word_count



# Exercise 9.4
# Write a function named uses_only that takes a word and a string of letters, and that returns True
# if the word contains only letters in the list.



def uses_only(word, letters):
    i = 0
    while i < len(word):
        if word[i] in letters:
            i += 1
        else:
            return False
    return True



# Exercise 9.5
# Write a function named uses_all that takes a word and a string of required letters, and that returns
# True if the word uses all the required letters at least once.



def uses_all(word, required_letters):
    for letter in required_letters:
        if letter not in word:
            return False
    return True



# Exercise 9.6
# Write a function called is_abercedarian that returns True if the letters in a word appear
# in alphabetical order (double letters are ok). How many abercedarian words are there?



def is_abcedarian(word):
    word = list(word)
    temp = word[:]  # Need slice operator to clone the list otherwise they will point to the same object
    temp.sort()
    return temp == word



# Exercise 9.7
# A word with three consecutive double letters.



def is_triple_double(word):
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:  # Checking a letter is same with the letter comes after itself
            count = count + 1
            if count == 3:
                return True
            i = i + 2  # Jumping to next index after the letter pair
        else:
            count = 0
            i = i + 1
    return False



# Exercise 9.8
# Palindromic odometer.



def has_palindrome(i, start, len):
    s = str(i)[start:start + len]
    return s[::-1] == s


def check(i):
    return (has_palindrome(i, 2, 4) and
            has_palindrome(i + 1, 1, 5) and
            has_palindrome(i + 2, 1, 4) and
            has_palindrome(i + 3, 0, 6))


def check_all():
    i = 100000
    while i <= 999996:
        if check(i):
            print(i)
        i = i + 1


check_all()



# Exercise 9.9



def str_fill(i, len):
    return str(i).zfill(len)


def are_reversed(i, j):
    return str_fill(i, 2) == str_fill(j, 2)[::-1]


def num_instances(diff, flag=False):
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff
        if are_reversed(daughter, mother) or are_reversed(daughter, mother + 1):
            count = count + 1
            if flag:
                print(daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count


def check_diffs():
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print(diff, n)
        diff = diff + 1


check_diffs()
num_instances(18, True)
