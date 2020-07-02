# 2.17
 
# Provide the type, assembly language instruction, and binary representation 
# of instruction described by the following MIPS fields:

# op=0x23, rs=1, rt=2, const=0x4


# Answer


# opcode | rs | rt | immediate
# 100011 00001 00010 0000 0000 0000 0100
	
lw  $v0, 4($at)	# I-type load instruction
