# Chapter 15 - Basic Structured Query Language Quiz


# 1.
# Structured Query Language (SQL) is used to (check all that apply)


# Delete data, Create a table, Insert data


# 2.
# Which of these is the right syntax to make a new table?


# CREATE TABLE people;


# 3.
# Which SQL command is used to insert a new row into a table?


# INSERT INTO


# 4.
# Which command is used to retrieve all records from a table?


# SELECT * FROM Users


# 5.
# Which keyword will cause the results of the query to be displayed
# in sorted order?


# ORDER BY


# 6.
# In database terminology, another word for table is


# relation


# 7.
# In a typical online production environment, who has direct access
# to the production database?


# Database Administrator


# 8.
# Which of the following is the database software used in this class?


# SQLite


# 9.
# What happens if a DELETE command is run on a table without a WHERE clause?


# All the rows in the table are deleted


# 10.
# Which of the following commands would update a column named "name" in
# a table named "Users"?


# UPDATE Users SET name='new name' WHERE ...


# 11.
# What does this SQL command do?

# SELECT COUNT(*) FROM Users


# It counts the rows in the table Users


# ----------------------------------------------------------------------------------------------------------------------


# Chapter 15 - Basic Structured Query Language Assignments


# Counting Email in a Database


import sqlite3
import re

conn = sqlite3.connect('Chapter 15 - EmailDB.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

file_name = input('Enter file name: ')
file_pointer = open(file_name)

for line in file_pointer:
    if not line.startswith('From: '):
        continue

    matches = re.findall('[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,6})', line.rstrip())
    print(matches)

    if len(matches) > 0:
        domain = matches[0]
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
        row = cur.fetchone()

        if row is None:
            cur.execute('''INSERT INTO Counts (org, count)
                 VALUES ( ?, 1 )''', (domain,))
        else:
            cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', (domain,))
        conn.commit()

query = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(query):
    print(str(row[0]), row[1])

cur.close()
