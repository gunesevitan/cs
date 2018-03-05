/*

 * 2.6
 
 
 * The table below shows 32-bit values of an array stored in memory.
 
 * Address | Data
 *   24    |  2
 *   38    |  4
 *   32    |  3
 *   36    |  6
 *   40    |  1
 
 * 2.6.1
 
 
  
 */


# Answer


sll 	$t0, $s0, 2 	# $t0 = f * 4 
add 	$t0, $s6, $t0	# $t0 = &A[f] 
sll 	$t1, $s1, 2 	# $t1 = g * 4 
add 	$t1, $s7, $t1	# $t1 = &B[g] 
lw  	$s0, 0($t0) 	# f = A[f] 
lw  	$t0, 4($t2) 	# $t0 = A[f + 1]
add 	$t0, $t0, $s0	# $t0 = A[f + 1] + A[f]
sw  	$t0, 0($t1) 	# B[g] = $t0

# These lines are rewritten.
addi	$t2, $t0, 4 	# A[f + 1]
lw  	$t0, 0($t2) 	# $t0 = A[f + 1]