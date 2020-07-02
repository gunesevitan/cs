# 2.33
 
# For each function call, show the contents of the stack after the 
# function call is made. Assume the stack pointer is originally at 
# address 0x7ffffffc, and follow the register conventions as specified
# in Figure 2.11.

	
# Answer


# 0x7ffffff0	$a0 address
# 0x7fffffe4	save return address of caller (n=3)
# 0x7fffffd8	$s0 address

# 0x7fffffcc	$a0 address
# 0x7fffffc0	save return address of 1st recursive call (n=2)
# 0x7fffffb4	$s0 address

# 0x7fffffa8	$a0 address
# 0x7fffff9c	save return address of 2nd recursive call (n=1)
# 0x7fffff90	$s0 address

# 0x7fffffa8	restore stack pointer of 2nd recursive call

# 0x7fffffa8	$a0 address
# 0x7fffff9c	save return address of 3rd recursive call (n=0)
# 0x7fffff90	$s0 address

# 0x7fffffa8	restore stack pointer of 3rd recursive call

# 0x7fffffcc	restore stack pointer of 1st recursive call

# 0x7fffffcc	$a0 address
# 0x7fffffc0	save return address of 4th recursive call (n=1)
# 0x7fffffb4	$s0 address

# 0x7fffffcc	restore stack pointer of 4th recursive call

# 0x7ffffff0	restore stack pointer of caller
