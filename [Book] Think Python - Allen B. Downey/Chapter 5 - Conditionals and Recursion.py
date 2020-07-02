# Chapter Five Exercises



# Exercise 5.2
# Write a function called do_n that takes a function object and a number, n, as arguments,
# and calls that given function n times.



def do_n(f, n):
    if n <= 0:  # Base case to stop the function
        return
    f()
    do_n(f, n - 1)


	
# Exercise 5.3
# Fermat's Last Theorem says that there are no integers a,b, and c such that
# a^n + b^n = c^n
# for any values of n greater than 2.



# 1. Write a function named check_fermat that takes four parameters -a,b,c and n
#    and that checks to see if Fermat's theorem holds.
#    If n is greater than 2 and it turns out to be true that the program should print, "Holy smokes, Fermat was wrong!".
#    Otherwise the program should print, "No, that doesn't work."

def check_fermat(a, b, c, n):
    if c ** n == a ** n + b ** n and n > 2:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work")

# 2. Write a function that prompts the user to input values for a, b, c and n, converts them to integers,
#    and uses check_fermat to check whether they violate Fermat's theorem.

def check_fermat_prompt():
    a = input('Enter a')
    b = input('Enter b')
    c = input('Enter c')
    n = input('Enter n')

    check_fermat(int(a), int(b), int(c), int(n))
	

	
# Exercise 5.4
# If you are given three sticks, yo may or may not be able to arrange them in a triangle.
# For example, if one of the sticks is 12 inches long and the other two are one inch long,
# it is clear that you will not be able to get the short sticks to meet in the middle.
# For any three lengths, there is a simple test to see if it is possible to form a triangle.

# If any of the three lengths is greater than the sum of the other, then you cannot form a triangle.
# Otherwise, you can. (If the sum of two lengths equals the third, they form what is called a "degenerate" triangle.)



# 1. Write a function named is_triangle that takes three integers as arguments, and prints either "Yes" or "No",
#    depending on whether you can or cannot form a triangle from sticks with the given lengths.

def is_triangle(a, b, c):
    edges = [a, b, c]
    edges.sort()
    if edges[0] + edges[1] >= edges[2]:
        print("Yes")
    else:
        print("No")
		
# 2. Write a function that prompts the user to input three sticks lengths, converts them to integers,
#    and uses is_triangle to check whether sticks with the given lengths can form a triangle.

def is_triangle_prompt():
    a = input('Enter edge a')
    b = input('Enter edge b')
    c = input('Enter edge c')

    is_triangle(int(a), int(b), int(c))
