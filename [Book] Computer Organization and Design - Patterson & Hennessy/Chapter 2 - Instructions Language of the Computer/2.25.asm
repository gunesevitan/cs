# 2.25
 
# The follow instruction is not included in the MIPS instruction set:
# rpt $t2, loop # if(R[rs]>0) R[rs]=R[rs]–1, PC=PC+4+BranchAddr

# 2.25.1

# If this instruction were to be implemented in the MIPS instruction set,
# what is the most appropriate instruction format?

# 2.25.2

# What is the shortest sequence of MIPS instructions that performs the
# same operation?


# Answer


# 2.25.1

# The most appropriate instruction format is I-type.

# 2.25.2

Loop:slt$t3, $0, $t2
	beq	$t3, $0, DONE
	sub	$t2, $t2, 1
	j	Loop
DONE: