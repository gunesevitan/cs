/*

 * 2.5
 
 
 * For the MIPS assembly instructions in Exercise 2.4, rewrite the assembly code
 * to minimize the number  MIPS instructions (if possible) needed to carry out
 * the same function.
  
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
