# Chapter Fourteen Exercises



# Exercise 14.1
# The os module provides a function called walk that is similar to this one but more
# versatile. Read the documentation and use it to print the names of the files in a given
# directory and its subdirectories.



import os

cwd = os.getcwd()
print(cwd)


def walk_dirs():
    for current_path, directories, files in os.walk(cwd):  # os.walk returns a tuple of path, directories and files
        print(type(current_path), type(directories), type(files))
        print (current_path, directories, files)



# Exercise 14.2
# Write a function called sed that takes as arguments a pattern string, a replacement string,
# and two filenames; it should read the first file and write the contents into the second file
# (creating it if necessary). If the pattern string appears anywhere in the file, it should be
# replaced with the replacement string.
# If an error occurs while opening, reading, writing or closing files, your program should
# catch the exception, print an error message, and exit.



def sed(pattern_string, replacement_string, source, destination):
    try:
        source_pointer = open(source, 'r')
        destination_pointer = open(destination, 'w')

        for line in source_pointer:
            line = line.replace(pattern_string, replacement_string)
            destination_pointer.write(line)

        source_pointer.close()
        destination_pointer.close()
    except IOError:
        print("Error")



# Exercise 14.3
# Write a module that imports anagram_sets and provides two new functions: store_anagrams
# should store the anagram dictionary in a "shelf;" read_anagrams should look
# up a word and return a list of its anagrams.


import shelve


def store_anagrams(filename, anagram_dict):
    shelf = shelve.open(filename, 'c')

    for word, anagrams in anagram_dict.items():
        shelf[word] =  anagrams  # Saving word as key and anagrams as list to shelf

    shelf.close()


def read_anagrams(filename, word):
    shelf = shelve.open(filename)
    sorted_string = sort_string(word)  # Sorting the letters of given word
    try:
        return shelf[sorted_string]  # Searching sorted string's anagrams' in the shelf
    except KeyError:
        return []


def sort_string(s):
    temp = list(s)
    temp.sort()
    temp = ''.join(temp)
    return temp



# Exercise 14.4
# In a large collection of MP3 files, there may be more than one copy of the same song,
# stored in different directories or with different file names. The goal of this exercise is to
# search for these duplicates.

# Write a program that searches a directory and all of its subdirectories, recursively,
# and returns a list of complete paths for all files with a given suffix (like .mp3).
# Hint: os.path provides several useful functions for manipulating file and path names.



def walk(dirname):

    files = []

    for filename in os.listdir(dirname):
        merged_path = os.path.join(dirname, filename)  # Merging the directory name with filename

        if os.path.isfile(merged_path):  # If the merged_path is a file, adding it to the files
            files.append(merged_path)
        else:
            files.extend(walk(merged_path))  # If it is not a file, calling the recursive call on that directory

    return files


def print_duplicates(dirname):

    file_list = walk(dirname)
    seen = []

    for file in file_list:
        if file in seen:
            print(file)
        else:
            seen.append(file)



# Exercise 14.5
# Type this example into a file named wc.py and run it as a script. Then run the Python
# interpreter and import wc. What is the value of __name__ when the module is being imported?



def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count


if __name__ == "__main__":
    print(linecount("asd.py"))

# This prints the line count of this file on script mode.
# When it is imported it doesn't print anything because
# it is not running as a script

# If the Python interpreter is running the source file as the main program,
# it sets the special __name__ variable to have a value "__main__".

# If this file is being imported from another module,
# __name__ will be set to the module's name.



# Exercise 14.6
# The following example downloads and prints a secret message
# from thinkpython.com:

import urllib.request

conn = urllib.request.urlopen("http://thinkpython.com/secret.html")
for line in conn:
    print(line.strip())


# Run this code and follow the instructions you see there.

# Write a program that prompts the user for a zip code and prints the
# name and population of the corresponding town.



zipcode = input(">>> Enter the zipcode: ")

url = 'http://uszip.com/zip/' + "02492"
conn = urllib.request.urlopen(url)

for line in conn:
    line = line.strip().decode()
    if line.startswith("<title>"):  # Prints the line that has the name of the town (Not parsed)
        print(line)

    if "Total population" in line:  # Prints the line that has the total population (Not parsed)
        print(line)