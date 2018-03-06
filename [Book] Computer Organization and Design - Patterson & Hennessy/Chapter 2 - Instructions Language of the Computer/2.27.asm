# 2.27
 
# Translate the following C code to MIPS assembly code. Use a minimum 
# number of instructions. Assume that the values of a, b, i, and j are
# in registers $s0, $s1, $t0, and $t1, respectively. Also, assume that 
# register $s2 holds the base address of the array D.

for(i=0; i<a; i++)
 for(j=0; j<b; j++)
  D[4*j] = i + j;


# Answer


	add	$t0, $0, $0 	# i = 0
L1:	slt	$t2, $t0, $s0	# i < a
	beq	$t2, $0, EXIT	# $t2 == 0, go to EXIT
	add	$t1, $0, $0 	# j = 0
L2:	slt	$t2, $t1, $s1	# j < b
	beq	$t2, $0, L3 	# if $t2 == 0, go to L3
	add	$t2, $t0, $t1	# i+j
	sll	$t4, $t1, 2 	# $t4 = 4*j
	add	$t3, $t4, $s2	# $t3 = &D[4*j]
	sw	$t2, 0($t3) 	# D[4*j] = i+j
	addi	$t1, $t1, 1 # j = j+1
	j	L2
L3:	addi	$t0, $t0, 1 # i = i+1
	j	L1
EXIT
