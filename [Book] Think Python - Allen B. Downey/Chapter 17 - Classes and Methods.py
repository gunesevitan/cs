# Chapter Seventeen Exercises



# Exercise 17.1
# Rewrite time_to_int as a method. It is probably not appropriate to
# rewrite int_to_time as a method; what object you would invoke it on?



class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_int(self):
        # We create fractional portions of the "hour" attribute
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def __str__(self):
        return ':'.join([str(self.hour).zfill(2), str(self.minute).zfill(2), str(self.second).zfill(2)])

    def increment(self, seconds):
        self_seconds = self.time_to_int()
        ret_time_seconds = self_seconds + seconds
        return self.int_to_time(ret_time_seconds)

    def is_after(self, other):
        return self.time_to_int() < other.time_to_int()

    @staticmethod
    def int_to_time(seconds):  # Static methods doesn't need to invoke on instances, they can invoke on classes
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time


time_a = Time(15, 10, 45)
print(time_a)
time_a_int = time_a.time_to_int()
print(time_a_int)
print(Time.int_to_time(time_a_int))  # Invoked on the class



# Exercise 17.2
# Write an init method for the Point class that takes x and y as optional parameters and
# assigns them to the corresponding attributes.



class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return "x = %d and y = %d" % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        if isinstance(other, tuple):
            return Point(self.x + other[0], self.y + other[1])



# Exercise 17.3
# Write a str method for the Point class. Create a Point object and print it.



def __str__(self):
    return "x = %d and y = %d" % (self.x, self.y)



# Exercise 17.4
# Write an add method for the Point class.



def __add__(self, other):
    return self.x + other.x, self.y + other.y



# Exercise 17.5
# Write an add method for Points that works with either a Point object or a tuple:
# If the second operand is a Point, the method should return a new Point whose x
# coordinate is the sum of the x coordinates of the operands, and likewise for the y
# coordinates.
# If the second operand is a tuple, the method should add the first element of the tuple
# to the x coordinate and the second element to the y coordinate, and return a new
# Point with the result.



def __add__(self, other):
    if isinstance(other, Point):
        return Point(self.x + other.x, self.y + other.y)
    if isinstance(other, tuple):
        return Point(self.x + other[0], self.y + other[1])



# Exercise 17.6
# Change the attributes of Time to be a single integer representing seconds since midnight. Then
# modify the methods (and the function int_to_time) to work with the new implementation.
# You should not have to modify the test code in main. When you are done, the output
# should be the same as before.



class Time:
    def __init__(self, hour=0, minute=0, second=0):
        total_minutes = hour * 60 + minute
        self.total_seconds = total_minutes * 60 + second  # total_seconds is the only instance variable now

    def __str__(self):
        minutes, second = divmod(self.total_seconds, 60)
        hour, minute = divmod(minutes, 60)
        return '%.2d:%.2d:%.2d' % (hour, minute, second)

    def print_time(self):
        print(str(self))

    def time_to_int(self):
        return self.total_seconds

    def is_after(self, other):
        return self.total_seconds > other.total_seconds

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        assert self.is_valid() and other.is_valid()
        added_seconds = self.total_seconds + other.total_seconds
        return int_to_time(added_seconds)

    def increment(self, seconds):
        seconds += self.total_seconds
        return int_to_time(seconds)

    def is_valid(self):
        return self.total_seconds >= 0 and self.total_seconds < 24 * 60 * 60  # The min and max seconds


def int_to_time(seconds):
    return Time(0, 0, seconds)



# Exercise 17.7
# Write a definition for a class Kangaroo with the following methods:
# 1. An __init__ method that initializes an attribute named pouch_contents to an
#    empty list.
# 2. A method named put_in_pouch that takes an object of any type and adds it to
#    pouch contents
# 3. A __str__ method that returns a string representation of the Kangaroo object
#    and the contents of the pouch.
# Test your code by creating two Kangaroo objects, assigning them to variables named
# kanga and roo, and then adding roo to the contents of kanga's pouch.

# WARNING: this program contains a NASTY bug. I put
# it there on purpose as a debugging exercise, but
# you DO NOT want to emulate this example!

class Kangaroo:
    def __init__(self, contents=[]):  # The bug is here. The default argument value shouldn't be mutable
        self.pouch_contents = contents

    def __str__(self):
        t = [ object.__str__(self) + ' with pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """add a new item to the pouch contents"""
        self.pouch_contents.append(item)

kanga = Kangaroo()
roo = Kangaroo()

kanga.put_in_pouch(roo)

print(kanga)


# The default argument values are evaluated once at function definition time
# That means that when __init__ is defined, [] gets evaluated and contents
# gets a reference to an empty list.
# After that, every Kangaroo that gets the default value get a reference to
# the same list object. If any Kangaroo modifies this shared list,
# they all see the change.


def __init__(self, contents=[]):
    self.pouch_contents = contents


# In this version, the default value is None.  When __init__ runs,
# it checks the value of contents and, if necessary,
# creates a new empty list.  That way every Kangaroo
# that gets the default value get a reference to a different list.


def __init__(self, contents=None):  # Default value is not mutable now
    if contents == None:
        contents = []
    self.pouch_contents = contents