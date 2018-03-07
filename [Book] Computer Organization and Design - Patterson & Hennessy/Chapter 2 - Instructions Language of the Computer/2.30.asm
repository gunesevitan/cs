# 2.30
 
# Rewrite the loop from Exercise 2.29 reduce the number of MIPS 
# instructions executed.

	
# Answer


# From
 
	addi $t1, $0, $0
LOOP: lw $s1, 0($s0)
	add $s2, $s2, $s1
	addi $s0, $s0, 4
	addi $t1, $t1, 1
	slti $t2, $t1, 100
	bne $t2, $0, LOOP

# To

	addi $t1, $s0, 400
LOOP:
	lw $s1, 0($s0)
	add $s2, $s2, $s1
	addi $s0, $s0, 4
	bne $s0, $t1, LOOP