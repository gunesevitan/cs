# 2.9
 
# Translate the following C code to MIPS. Assume that the variables 
# f, g, h, i, and j are assigned to registers ＄s0, ＄s1, ＄s2, ＄s3,
# and ＄s4, respectively. Assume that the base address of the arrays
# A and B are in registers ＄s6 and ＄s7, respectively. Assume that 
# the elements of the arrays A and B are 4-byte words:

# B[8] = A[i] + A[j];


# Answer


# f -> $s0
# g -> $s1
# h -> $s2
# i -> $s3
# j -> $s4
# A[0] -> $s6
# B[0] -> $s7

sll 	$t0, $s3, 2 	# $t0 = i * 4
add 	$t0, $t0, $s6	# $t0 = $t0 + $s6
lw  	$t0, 0($t0) 	# $t0 = A[i]
sll 	$t1, $s4, 2 	# $t1 = j * 4
add 	$t1, $t1, $s6	# $t1 = $t1 + $s6
lw  	$t1, 0($t1) 	# $t1 = A[j]
add 	$t2, $t0, $t1	# $t2 = $t0 + $t1
sw  	$t2, 32($s7) 	# B[8] = A[i] + A[j]
