# 2.14
 
# Provide the type and assembly language instruction for the following 
# binary value: 0000 0010 0001 0000 1000 0000 0010 0000


# Answer


# opcode	|	rs	|	rt	|	rd	|	shamt	|	funct
# 000000	  10000   10000   10000     00000		100000
	
add  $s0, $s0, $s0	# R-type add instruction
