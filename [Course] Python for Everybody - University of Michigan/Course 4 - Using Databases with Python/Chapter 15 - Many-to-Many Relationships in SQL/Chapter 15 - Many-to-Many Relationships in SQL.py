# Chapter 15 - Many-to-Many Relationships in SQL Quiz


# 1.
# How do we model a many-to-many relationship between two database tables?


# We add a table with two foreign keys


# 2.
# In Python, what is a database "cursor" most like?


# A file handle


# 3.
# What method do you call in an SQLIte cursor object in Python to run an SQL command?


# execute()


# 4.
# In the following SQL,

# cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))


# It is a placeholder for the contents of the "org" variable


# 5.
# In the following Python code sequence (assuming cur is a SQLite cursor object),

# cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
# row = cur.fetchone()

# What is the value in row if no rows match the WHERE clause?


# None


# 6.
# What does the LIMIT clause in the following SQL accomplish?

# SELECT org, count FROM Counts
# ORDER BY count DESC LIMIT 10


# It only retrieves the first 10 rows from the table


# 7.
# What does the executescript() method in the Python SQLite
# cursor object do that the normal execute() method does not do?


# It allows multiple SQL statements separated by semicolons


# 8.
# What is the purpose of "OR IGNORE" in the following SQL:

# INSERT OR IGNORE INTO Course (title) VALUES ( ? )


# It makes sure that if a particular title is already in the table,
# there are no duplicate rows inserted


# 9.
# For the following Python code to work, what must be added to
# the title column in the CREATE TABLE statement for the Course table:

# cur.execute('''INSERT OR IGNORE INTO Course (title)
#     VALUES ( ? )''', ( title, ) )
# cur.execute('SELECT id FROM Course WHERE title = ? ',
#     (title, ))
# course_id = cur.fetchone()[0]


# A UNIQUE constraint


# ----------------------------------------------------------------------------------------------------------------------


# Chapter 15 - Many-to-Many Relationships in SQL Assignments


# Many Students in Many Courses


import json
import sqlite3

conn = sqlite3.connect('Chapter 15 - RosterDB.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;
CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);
CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);
CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

filename  = input('Enter file name: ')  # Enter roster_data.json

text = open(filename).read()
data = json.loads(text)

for entry in data:

    name = entry[0]
    title = entry[1]
    role = entry[2]

    print(name, title, role)

    cur.execute('''INSERT OR IGNORE INTO User (name) 
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) 
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )

    conn.commit()
