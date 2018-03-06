# 2.10
 
# Translate the following MIPS code to C. Assume that the variables
# f, g, h, i, and j are assigned to registers ＄s0, ＄s1, ＄s2, ＄s3, 
# and ＄s4, respectively. Assume that the base address of the arrays 
# A and B are in registers ＄s6 and ＄s7, respectively.

addi	$t0, $s6, 4
add 	$t1, $s6, $0
sw  	$t1, 0($t0)
lw  	$t0, 0($t0)
add 	$s0, $t1, $t0


# Answer


# f -> $s0
# g -> $s1
# h -> $s2
# i -> $s3
# j -> $s4
# A[0] -> $s6
# B[0] -> $s7

# A[1] = A[0];
# f = A[0] + A[1];
