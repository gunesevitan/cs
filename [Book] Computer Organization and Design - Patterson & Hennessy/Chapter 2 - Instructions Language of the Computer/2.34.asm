# 2.34
 
# Translate function f into MIPS assembly language. If you need to use registers 
# $t0 through $t7, use the lower-numbered registers first. Assume the function 
# declaration for func is “int func(int a, int b);”. 
# The code for function f is as follows:

# int f(int a, int b, int c, int d){
#	 return func(func(a,b),c+d);
# }

	
# Answer


addi	$sp, $sp, -4	# allocate stack frame of 4 bytes
sw  	$ra, 0($sp) 	# save return address
jal 	func			# call func(a,b)
add 	$a0, $v0, $0	# $a0 = result of func(a,b)
add 	$a1, $a2, $a3	# $a1 = c+d
jal 	func			# call func(func(a,b), c+d)
lw  	$ra, 0($sp) 	# restore return address
addi	$sp, $sp, 4 	# free stack frame
jr  	$ra 			# return to caller