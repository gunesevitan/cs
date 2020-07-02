# 2.32
 
# Functions can often be implemented by compilers “in-line.” An in-line
# function is when the body of the function is copied into the program space, 
# allowing the overhead of the function call to be eliminated. Implement an 
# “in-line” version of the the C code in the table in MIPS assembly. What is the
# reduction in the total number of MIPS assembly instructions needed to complete
# the function? Assume that the C variable n is initialized to 5.

	
# Answer


# Due to recursive nature of the code, it's not possible for the 
# compiler to in-line the function call.