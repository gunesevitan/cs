# 2.20
 
# Find the shortest sequence of MIPS instructions that extracts bits 
# 16 down to 11 from register $t0 and uses the value of this field to
# replace bits 31 down to 26 in register $t1 without changing the other 
# 26 bits of register $t1.


# Answer


srl	$t2, $t0, 11
sll	$t2, $t2, 26
srl	$t1, $t1,  6
add	$t2, $t2, $t1
