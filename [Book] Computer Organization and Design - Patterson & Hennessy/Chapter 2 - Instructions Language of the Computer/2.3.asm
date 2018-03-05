/*

 * 2.3 
 
 
 * For the following C statement, what is the corresponding
 * MIPS assembly code? Assume that the variables f, g, h, i,
 * and j are assigned to registers $s0, $s1, $s2, $s3, and
 * $s4, respectively. Assume that the base address of the arrays
 * A and B are in registers $s6 and $s7, respectively.
 
 * B[8] = A[i-j];
 
 */


# Answer


# f -> $s0
# g -> $s1
# h -> $s2
# i -> $s3
# j -> $s4
# A[0] -> -> $s6
# B[0] -> -> $s7

sub 	$t0, $s3, $s4	# i = i - j 
add 	$t0, $s6, $t0	# A[0 + i]
lw  	$t1, 0($t0) 	# $t1 = A[0 + i] 
sw  	$t1, 32($s7)	# B[8] = $t1