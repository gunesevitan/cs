/*

 * 2.1 
 
 
 * For the following C statement, what is the corresponding
 * MIPS assembly code? Assume that the variables f, g, h , 
 * and i are given and could be considered 32-bit integers 
 * as declared in a C program. Use a minimal number of MIPS
 * assembly instructions. 
 
 * f = g + (h – 5);
 
 */


# Answer


# h -> $t0
# g -> $t1
# s -> $s1

addi	$t0, $t0, -5	# h = h - 5
add 	$s1, $t1, $t0	# f = g + h
