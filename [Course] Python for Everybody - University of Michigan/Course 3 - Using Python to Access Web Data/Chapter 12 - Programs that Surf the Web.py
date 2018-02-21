# Chapter 12 Quiz


# 1.
# Which of the following Python data structures is most similar to the
# value returned in this line of Python:

import urllib.request

x = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')


# file handle


# 2.
# In this Python code, which line actually reads the data?

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n'.encode())
while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print(data)
mysock.close()


# mysock.recv()


# 3.
# Which of the following regular expressions would extract the URL from this line of HTML:

# <p>Please click <a href="http://www.dr-chuck.com">here</a></p>


# href="(.+)"


# 4.
# In this Python code, which line is most like the open() call to read a file:

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print(data)
mysock.close()


# mysock.connect()


# 5.
# Which HTTP header tells the browser the kind of document that is being returned?


# Content-Type:


# 6.
# What should you check before scraping a web site?


# That the web site allows scraping


# 7.
# What is the purpose of the BeautifulSoup Python library?


# It repairs and parses HTML to make it easier for a program to understand


# 8.
# What ends up in the "x" variable in the following code:

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)
x = soup('a')


# A list of all the anchor tags (<a..) in the HTML from the URL


# 9.
# How are strings stored internally in Python 3?


# unicode


# 10.
# What word does the following sequence of numbers represent in ASCII:
# 108, 105, 110, 101


# line


# ----------------------------------------------------------------------------------------------------------------------


# Chapter 12 Assignments


# Scraping HTML Data with BeautifulSoup


from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen(input("Enter URL: "))
soup = BeautifulSoup(html, "html.parser")

span_tags = soup('span')

numbers = []

for span in span_tags:
    numbers.append(int(span.string))

print(sum(numbers))


# Following Links in HTML Using BeautifulSoup


import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen(input("Enter URL: "))
count = int(input('Enter count: '))
position = int(input('Enter position: '))

names = []

while count > 0:
    print("Retrieving: %s" % (html))
    page = urllib.request.urlopen(html)
    soup = BeautifulSoup(page,"html.parser")
    anchors = soup("a")

    name = anchors[position - 1].string
    names.append(name)
    html = anchors[position - 1]['href']
    count -= 1

print(names[-1])
