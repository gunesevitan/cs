# Chapter Two Exercises



# Exercise 2.1
# Question:

# If you type an integer with a leading zero, you might get a confusing error:
# >>> zipcode = 02492
#                   ^
# SyntaxError: invalid token
# Other numbers seem to work, but the results are bizarre:

# >>> zipcode = 02132
# >>> zipcode
# 1114
# Can you figure out what is going on? Hint: display the values 01, 010, 0100 and 01000.

# Answer:

# Numbers start with 0 (0o in Python 3) are octal literals. Interpreter assumes that the number is base 8.
octal_num1 = 0o11  # 9
octal_num2 = 0o100  # 64



# Exercise 2.2
# Question:

# Type the following statements in the Python interpreter to see what they do:

# 5
# x = 5
# x + 1
# Now put the same statements into a script and run it.
# What is the output? Modify the script by transforming each expression into a print statement and then run it again.

# Answer:

# Interpreter

# >>> 5
# 5
# >>> x = 5
# >>> x + 1
# 6

# The values given to interpreter are printed, but the assignment statements are not.

# Script

# Script with only assignments and values shows no output. The script is processed by the interpreter and exits.

# Running the script after transforming each expression into a print statement yields TypeError.
# That's because x is not defined yet and it is tried to get printed.

# Exercise 2.3
# Question:

# Assume that we execute the following assignment statements:

width = 17
height = 12.0
delimiter = '.'

# For each of the following expressions, write the value of the expression and the type.

# width / 2
# width / 2.0
# height / 3
# 1 + 2 * 5
# delimiter * 5
# Use the Python interpreter to check your answers.

# Answer:

print(width / 2)  # 8, int (Python 2) / 8.5, float (Python 3)
print(width / 2.0)  # 8.5, float
print(height / 3)  # 4.0, float
print(1 + 2 * 5)  # 11, int
print(delimiter * 5)  # '.....', string



# Exercise 2.4
# Question:

# Practice using the Python interpreter as a calculator:

# Answer:

# 1. The volume of a sphere with radius r is 4/3 π r3.
#    What is the volume of a sphere with radius 5? Hint: 392.7 is wrong!

from math import pi

(4.0 / 3.0) * pi * 5 ** 3  # 523.5987755982989

# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
#    Shipping costs $3 for the first copy and 75 cents for each additional copy.
#    What is the total wholesale cost for 60 copies?

quantity = 60
cover_price = 24.95
discount = 0.40
cost = (cover_price * quantity) - (cover_price * quantity) * discount
shipping = 3 + (0.75 * quantity)
total_cost = cost + shipping  # 946.199999999

# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
#    then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

from datetime import datetime, timedelta

easy_pace_seconds = (8 * 60) + 15
tempo_pace_seconds = (7 * 60) + 12
total_seconds = (easy_pace_seconds * 2) + (tempo_pace_seconds * 3)

time_start = datetime(1, 1, 1, 6, 52)
time_passed = timedelta(seconds=total_seconds)
time_end = time_start + time_passed
time_end.time()  # 7:30:06

