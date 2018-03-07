# 2.29
 
# Translate the following loop into C. Assume that the C-level integer 
# i is held in register $t1, $s2 holds the C-level integer called result,
# and $s0 holds the base address of the integer MemArray.

	addi $t1, $0, $0
LOOP:lw $s1, 0($s0)
	add $s2, $s2, $s1
	addi $s0, $s0, 4
	addi $t1, $t1, 1
	slti $t2, $t1, 100
	bne $t2, $0, LOOP

	
# Answer

  
# while(i < 100){
#  result += MemArray[i];
#  i++;
# }
