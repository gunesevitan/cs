# Chapter 15 - Data Models and Relational SQL Quiz


# 1.
# What is the primary added value of relational databases over flat files?


# Ability to scan large amounts of data quickly


# 2.
# A primary key can be set to null.


# False


# 3.
# Which of the following is NOT a good rule to follow when developing a database model?


# Use a person's email address as their primary key


# 4.
# If our user interface (i.e., like iTunes) has repeated strings on one column
# of the user interface, how should we model this properly in a database?


# Make a table that maps the strings in the column to numbers and then use those numbers in the column


# 5.
# Which of the following is the label we give a column that
# the "outside world" uses to look up a particular row?


# Logical Key


# 6.
# What is the label we give to a column that is an integer and used
# to point to a row in a different table?


# Foreign Key


# 7.
# What SQLite keyword is added to primary keys in a CREATE TABLE statement
# to indicate that the database is to provide a value for the column when records are inserted?


# AUTOINCREMENT


# 8.
# What is the SQL keyword that reconnects rows that have foreign keys with
# the corresponding data in the table that the foreign key points to?


# JOIN


# 9.
# What happens when you JOIN two tables together without an ON clause?


# The number of rows you get is the number of rows in the
# first table times the number of rows in the second table


# 10.
# When you are doing a SELECT with a JOIN across multiple tables with
# identical column names, how do you distinguish the column names?


# tablename.columnname


# ----------------------------------------------------------------------------------------------------------------------


# Chapter 15 - Data Models and Relational SQL Assignments


# Multi-Table Database - Tracks


import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('Chapter 15 - TrackDB.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


filename = input('Enter file name: ')  # Enter Library.xml


def lookup(d, key):
    found = False
    for child in d:
        if found :
            return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(filename)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))

for entry in all:
    if ( lookup(entry, 'Track ID') is None ):
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry, 'Genre')

    if name is None or artist is None or album is None or genre is None:
        continue

    print(name, artist, album, count, rating, length, genre)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count, genre_id)
        VALUES ( ?, ?, ?, ?, ?, ? )''',
        ( name, album_id, length, rating, count, genre_id ) )

    conn.commit()
