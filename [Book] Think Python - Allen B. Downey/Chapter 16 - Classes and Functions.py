# Chapter Sixteen Exercises



# Exercise 16.1
# Write a function called print_time that takes a Time object and prints it in the form
# hour:minute:second. Hint: the format sequence '%.2d' prints an integer using at least
# two digits, including a leading zero if necessary.



class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second


time_a = Time(23, 45, 12)
time_b = Time(12, 22, 56)

def print_time(time):
    hour, minute, second = time.hour, time.minute, time.second
    print("%.2d:%.2d:%.2d" % (hour, minute, second))


print_time(time_a)
print_time(time_b)



# Exercise 16.2
# Write a boolean function called is_after that takes two Time objects, t1 and t2, and
# returns True if t1 follows t2 chronologically and False otherwise. Challenge: don't use
# an if statement.



def convert_to_seconds(time):
    return time.hour * 3600 + time.minute * 60 + time.second


def is_after(time1, time2):
    return convert_to_seconds(time1) > convert_to_seconds(time2)

print(is_after(time_a, time_b))



# Exercise 16.3
# Write a correct version of increment that doesn't contain any loops.



def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        added_min, remaining_sec = divmod(time.second, 60)
        time.second = remaining_sec
        time.minute += added_min

    if time.minute >= 60:
        added_hour, remaining_min = divmod(time.minute, 60)
        time.minute = remaining_min
        time.hour += added_hour


print_time(time_b)
increment(time_b, 5467)
print_time(time_b)



# Exercise 16.4
# Write a "pure" version of increment that creates and returns a new Time object rather
# than modifying the parameter.



from copy import copy

def increment(time, seconds):
    new_time = copy(time)

    new_time.second += seconds

    if new_time.second >= 60:
        added_min, remaining_sec = divmod(new_time.second, 60)
        new_time.second = remaining_sec
        new_time.minute += added_min

    if new_time.minute >= 60:
        added_hour, remaining_min = divmod(new_time.minute, 60)
        new_time.minute = remaining_min
        new_time.hour += added_hour

    return new_time



# Exercise 16.5
# Rewrite increment using time_to_int and int_to_time.


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds  # Converting the time format into total seconds


def int_to_time(seconds):
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    return Time(hour, minute, second)  # Returning a new Time object from seconds


print_time(time_b)
print(time_to_int(time_b))


def increment_with_conversion(time, seconds):
    time_seconds = time_to_int(time)
    total_seconds = time_seconds + seconds
    return int_to_time(total_seconds)



# Exercise 16.6
# Write a function called mul_time that takes a Time object and a number and returns a
# new Time object that contains the product of the original Time and the number.

# Then use mul_time to write a function that takes a Time object that represents the
# finishing time in a race, and a number that represents the distance, and returns a Time
# object that represents the average pace(time per mile).



def mul_time(time, number):
    seconds = time_to_int(time) * number
    return int_to_time(seconds)



def time_per_mile(time, distance):
    seconds = time_to_int(time)
    secs_per_mile = seconds / distance
    return int_to_time(secs_per_mile)



# Exercise 16.7
# The datetime module provides date and time objects that are similar to the Date and
# Time objects in this chapter, but they provide a rich set of methods and operators.



# 1. Use the datetime module to write a program that gets the current date and prints
#    the day of the week.



from datetime import datetime

def find_day():
    today = datetime.today()
    print(today.weekday())  # Index of the week (Starts from 0)
    print(today.strftime('%A'))  # String representation of the day


find_day()



# 2. Write a program that takes a birthday as input and prints the user's age and the
#    number of days, hours, minutes and seconds until their next birthday.



def find_next_birthday(birthday):

    today = datetime.today()

    next_birthday = datetime(today.year, birthday.month, birthday.day)

    if today > next_birthday:
        next_birthday = datetime(today.year + 1, birthday.month, birthday.day)  # If birthday is passed adding 1 to year


    time_delta = next_birthday - today
    return time_delta.days

my_birthday = datetime(1992, 5, 15,)
print(find_next_birthday(my_birthday), "days remaining for next birthday.")



# 3. For two people born on different days, there is a day when one is twice as old as the
#    other. That's their Double Day. Write a program that takes two birthdays and computes
#    their Double Day.



def double_day(birthday1, birthday2):

    assert birthday1 > birthday2
    time_delta = birthday1 - birthday2
    double_day = birthday1 + time_delta
    return double_day


birthday_a = datetime(2015, 5, 2)
birthday_b = datetime(2008, 12, 22)
print(double_day(birthday_a, birthday_b))



# 4. For a little more challenge, write more general version that computes the day
#    when one person is n times older than the other.