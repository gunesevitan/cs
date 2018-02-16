# Chapter One Exercises



# Exercise 1.1
# Write a well-structured English sentence with invalid tokens in it.
# Then write another sentence with all valid tokens but with invalid structure.



Invalid_Tokens = 'Sh3 1s g01ng to sch00l.'
Invalid_Syntax = 'going is school She to.'



# Exercise 1.4
# Start the Python interpreter and use it as a calculator.
# Python’s syntax for math operations is almost the same as standard mathematical notation.
# For example, the symbols +, -, / and * denote addition, subtraction, division and multiplication.
# If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile?
# What is your average speed in miles per hour? (Hint: there are 1.61 kilometers in a mile).



# Average Time Per Mile

total_distance_km = 10
total_time_minutes = 43.5
total_distance_mile = total_distance_km / 1.61  # 6.2111 ( Distance is converted to mile from km)
minutes_per_mile = total_time_minutes / total_distance_mile  # 7.0035 ( Minutes spent on 1 mile)

# Average Speed in Miles Per Hour

total_distance_km = 10
total_time_minutes = 43.5
km_per_minute = total_distance_km / total_time_minutes  # 0.2298
km_per_hour = km_per_minute * 60  # 13.7931
miles_per_hour = km_per_hour / 1.61  # 8.5671
