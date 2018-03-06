# 2.26
 
# Consider the following MIPS loop:

LOOP:	slt $t2, $0, $t1
		beq $t2, $0, DONE
		subi $t1, $t1, 1
		addi $s2, $s2, 2
		j LOOP
DONE:

# 2.26.1

# Assume that the register $t1 is initialized to the value 10. What 
# is the value in register $s2 assuming the $s2 is initially zero?

# 2.26.2

# For each of the loops above, write the equivalent C code routine. 
# Assume that the registers $s1, $s2, $t1, and $t2 are integers A,
# B, i, and temp, respectively.

# 2.26.3


# For the loops written in MIPS assembly above, assume that the register
# $t1 is initialized to the value N. How many MIPS instructions are executed?


# Answer


# 2.26.1

$s2 = 20

# 2.26.2

while(i > 0){
	i = i - 1
	B = B + 2

}

# 2.26.3

# 5N + 2