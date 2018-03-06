# 2.18
 
# Assume that we would like to expand the MIPS register file to 128 registers
# and expand the instruction set to contain four times as many instructions.

# 2.18.1

# How would this affect the size of each of the bit fields in the 
# R-type instructions?

# 2.18.2

# How would this affect the size of each of the bit fields in the 
# I-type instructions?

# 2.18.3

# How could each of the two proposed changes decrease the size of an 
# MIPS assembly program? On the other hand, how could the proposed change 
# increase the size of an MIPS assembly program?


# Answer


# 2.18.1

# opcode (20) | rs (7) | rt (7) | rd (7) | shamt (3) | funct (20)

# 2.18.2

# opcode (20) | rs (7) | rt (7) | rd (7) | constant (23)

# 2.18.3

# I think the instructions would be decoded much slower but there would be fewer
# load/store instructions because there are 128 registers. The reallocation
# of the registers wouldn't be necessary in many cases.