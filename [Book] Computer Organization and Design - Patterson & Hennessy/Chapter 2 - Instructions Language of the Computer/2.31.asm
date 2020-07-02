# 2.31
 
# Implement the following C code in MIPS assembly. What is the
# total number of MIPS instructions needed to execute the function?

int fib(int n) {
   if (n==0)
      return 0;
   else if (n==1)
      return 1;
   else
      return fib(n-1) + fib(n-2);
}

	
# Answer


FIB:
	addi	$sp, $sp, -12
	sw  	$a0, 8($sp)
	sw  	$ra, 4($sp)
	sw  	$s0, 0($sp)
	slti	$t0, $a0, 2
	beq 	$t0, $0, ELSE
	add 	$v0, $a0, $0
	j   	EXIT
ELSE:
	addi 	$a0, $a0, -1
	jal 	FIB
	add 	$s0, $v0, $0
	addi	$a0, $a0, -1
	jal 	FIB
	add 	$v0, $v0, $s0
EXIT:
	lw  	$a0, 8($sp)
	lw  	$ra, 4($sp)
	lw  	$s0, 0($sp)
	addi	$sp, $sp, 12
	jr  	$ra