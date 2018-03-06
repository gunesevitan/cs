# 2.11
 
# For each MIPS instruction, show the value of the opcode (OP), 
# source register (RS), and target register (RT) fields. For the
# I-type instructions, show the value of the immediate field, 
# and for the R-type instructions, show the value of the 
# destination register (RD) field.


# Answer


addi	$t0, $s6, 4 	# I-Type, OP :  8, RS : 22, RT : 8, IM :  4
add 	$t1, $s6, $0	# R-Type, OP : 32, RS : 22, RT : 0, RD :  9
sw  	$t1, 0($t0) 	# I-Type, OP : 43, RS :  8, RT : 9, IM :  0
lw  	$t0, 0($t0) 	# I-Type, OP : 35, RS :  8, RT : 8, IM :  0
add 	$s0, $t1, $t0	# R-Type, OP : 32, RS :  9, RT : 8, RD : 16