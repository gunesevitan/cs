# 2.19
 
# Assume the following register contents:
# $t0 = 0xAAAAAAAA, $t1 = 0x12345678

# 2.19.1

# For the register values shown above, what is the value of $t2 
# for the following sequence of instructions?

# sll $t2, $t0, 4
# or $t2, $t2, $t1

# 2.19.2

# For the register values shown above, what is the value of $t2
# for the following sequence of instructions?

# sll $t2, $t0, 4
# andi $t2, $t2, –1

# 2.19.3

# For the register values shown above, what is the value of $t2 
# for the following sequence of instructions?

# srl $t2, $t0, 3
# andi $t2, $t2, 0xFFEF

# Answer


# 2.19.1

# $t2 = 0xBABEFEFF

# 2.19.2

# $t2 = 0xAAAAAAA0

# 2.19.3

# $t2 = 0x00005545
