# 2.23
 
# Assume $t0 holds the value 0x00101000. What is the value of $t2 
# after the following instructions?

		slt	$t2, $0, $t0
		bne	$t2, $0, ELSE
		j  DONE
ELSE:	addi  $t2, $t2, 2
DONE:


# Answer


# $t2 is 3