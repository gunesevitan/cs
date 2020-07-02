# 2.13
 
# Assume that $s0 holds the value 128ten

# 2.13.1

# For the instruction add $t0, $s0, $s1, what is the range(s) of 
# values for $s1 that would result in overflow?

# 2.13.2

# For the instruction sub $t0, $s0, $s1, what is the range(s) of
# values for $s1 that would result in overflow?

# 2.13.3

# For the instruction sub $t0, $s1, $s0, what is the range(s) of
# values for $s1 that would result in overflow?



# Answer


# $s0 -> 128

# 2.13.1

# From 2147483520 To 2147483647

# 2.13.2

# From -2147483648 To -2147483520

# 2.13.3

# From -2147483648 To -2147483521
