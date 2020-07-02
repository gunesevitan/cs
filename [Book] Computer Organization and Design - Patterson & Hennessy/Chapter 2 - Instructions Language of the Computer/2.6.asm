# 2.6
 
# The table below shows 32-bit values of an array stored in memory.
 
# Address | Data
#   24    |  2
#   38    |  4
#   32    |  3
#   36    |  6
#   40    |  1
 
# 2.6.1
 
# For the memory locations in the table above, write C code to sort
# the data from lowest to highest, placing the lowest value in the
# smallest memory location shown in the figure. Assume that the data
# shown represents the C variable called Array , which is an array of
# type int , and that the first number in the array shown is the first
# element in the array. Assume that this particular machine is a 
# byte-addressable machine and a word consists of four bytes.
 
# 2.6.2

# For the memory location in the table above, write MIPS code to sort
# the data from lowest to highest, placing the lowest value in the
# smallest memory location. Use a minimum number of MIPS instructions.
# Assume the base address of Array is stored in register $s6 . 



# Answer


# 2.6.1

temp = Array[0]
Array[0] = Array[16]
Array[16] = Array[12]
Array[12] = Array[4]
Array[4] = temp

# 2.6.2

lw	$t0, 0($s6) 	# temp = Array[0] 
lw	$t1, 16($s6)	# $t1 = 1 
sw	$t1, 0($s6) 	# Array[0] = $t1
lw	$t1, 12($s6)	# $t1 = 6
sw	$t1, 16($s6)	# Array[4] = $t1 
lw	$t1, 4($s6) 	# $t1 = 4
sw	$t1, 12($s6)	# Array[3] = $t1 
sw	$t0, 4($s6) 	# Array[1] = $t1 
