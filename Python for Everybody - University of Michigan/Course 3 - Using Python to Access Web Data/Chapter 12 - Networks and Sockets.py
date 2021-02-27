# Chapter 12 - Networks and Sockets Quiz


# 1.
# What do we call it when a browser uses the HTTP protocol to load a file or page from a server and
# display it in the browser?


# The Request/Response Cycle


# 2.
# Which of the following is most similar to a TCP port number?


# A telephone extension


# 3.
# What must you do in Python before opening a socket?


# import socket


# 4.
# In a client-server application on the web using sockets, which must come up first?


# server


# 5.
# Which of the following is most like an open socket in an application?


# An "in-progress" phone conversation


# 6.
# What does the "H" of HTTP stand for?


# HyperText


# 7.
# What is an important aspect of an Application Layer protocol like HTTP?


# Which application talks first? The client or server?


# 8.
# What are the three parts of this URL (Uniform Resource Locator)?

# http://www.dr-chuck.com/page1.htm "


# Protocol, host, and document


# 9.
# When you click on an anchor tag in a web page like below, what HTTP request is sent to the server?

# <p>Please click <a href="page1.htm">here</a>.</p>


# GET


# 10.
# Which organization publishes Internet Protocol Standards?


# IETF


# ----------------------------------------------------------------------------------------------------------------------


# Chapter 12 - Networks and Sockets Assignments


# Understanding the Request/Response Cycle


import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('www.pythonlearn.com', 80))
my_socket.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n'.encode())

while True:
    data = my_socket.recv(512)
    if (len(data) < 1):
        break
    print(data.split())


my_socket.close()
