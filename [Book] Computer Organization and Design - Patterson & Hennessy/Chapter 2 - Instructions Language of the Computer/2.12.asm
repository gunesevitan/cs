# 2.12
 
# Assume that registers $s0 and $s1 hold the values 0x80000000 
# and 0xD0000000, respectively.

# 2.12.1

# What is the value of $t0 for the following assembly code?

add $t0, $s0, $s1

# 2.12.2

# Is the result in $t0 the desired result, or has there been 
# overflow?

# 2.12.3

# For the contents of registers $s0 and $s1 as specified above, 
# what is the value of $t0 for the following assembly code?

sub $t0, $s0, $s1

# 2.12.4

# Is the result in $t0 the desired result, or has there been overflow?

# 2.12.5

# For the contents of registers $s0 and $s1 as specified above, 
# what is the value of $t0 for the following assembly code?

add $t0, $s0, $s1
add $t0, $t0, $s0

# 2.12.6

# Is the result in $t0 the desired result, or has there been overflow?


# Answer


# $s0 -> 0x80000000
# $s1 -> 0xD0000000

# 2.12.1

# $t0 = $s0 + $s1 = 0x80000000 + 0xD0000000 = 0x150000000

# 2.12.2

# There has been overflow.

# 2.12.3

# $t0 = $s0 - $s1 = 0x80000000 - 0xD0000000 = -0x50000000

# 2.12.4

# It is the desired result.

# 2.12.5

# $t0 = $s0 + $s1 = 0x80000000 + 0xD0000000 = 0x150000000
# $t0 = $t0 + $s0 = 0x150000000 + 0x80000000 = 0x1D0000000

# 2.12.6

# There has been overflow.
