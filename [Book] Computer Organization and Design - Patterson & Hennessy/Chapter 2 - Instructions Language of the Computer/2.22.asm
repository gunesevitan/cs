# 2.22
 
# For the following C statement, write a minimal sequence of MIPS assembly
# instructions that does the identical operation. Assume $t1 = A, $t2 = B, 
# and $s1 is the base address of C.

# A = C[0] << 4;


# Answer


lw	$t1, 0($s1)
sll	$t1, $t1, 4
