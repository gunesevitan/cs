# 2.4 
 
 
# For the MIPS assembly instructions below, what is the 
# corresponding C statement? Assume that the variables 
# f, g, h, i, and j are assigned to registers $s0, $s1,
# $s2, $s3, and $s4, respectively. Assume that the base
# address of the arrays A and B are in registers $s6 
# and $s7, respectively.
 
# sll	$t0, $s0, 2 	# $t0 = f * 4 
# add	$t0, $s6, $t0	# $t0 = &A[f] 
# sll	$t1, $s1, 2 	# $t1 = g * 4 
# add	$t1, $s7, $t1	# $t1 = &B[g] 
# lw	$s0, 0($t0) 	# f = A[f] 
# addi $t2, $t0, 4 
# lw	$t0, 0($t2) 
# add	$t0, $t0, $s0 
# sw	$t0, 0($t1)
 

# Answer


# f -> $s0
# g -> $s1
# h -> $s2
# i -> $s3
# j -> $s4
# A[0] -> $s6
# B[0] -> $s7

sll 	$t0, $s0, 2 	# $t0 = f * 4 
add 	$t0, $s6, $t0	# $t0 = &A[f] 
sll 	$t1, $s1, 2 	# $t1 = g * 4 
add 	$t1, $s7, $t1	# $t1 = &B[g] 
lw  	$s0, 0($t0) 	# f = A[f] 
addi	$t2, $t0, 4 	# A[f + 1]
lw  	$t0, 0($t2) 	# $t0 = A[f + 1]
add 	$t0, $t0, $s0	# $t0 = A[f + 1] + A[f]
sw  	$t0, 0($t1) 	# B[g] = $t0
 
# f = A[f]
# f = A[f + 1] + A[f]
# B[g] = f
