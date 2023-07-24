# Homework 2

# TODO: clean code
# TODO: 2.  Given the list x = [2.0, 3.0, 5.0, 7.0, 9.0], create a list Y(x) for each float in x print list Y
# g = (x+y)**z
# Y(x) = ((3.0x)^2)/(99x-x^3) - (1)/(x)

# TODO: 3. general equation for quadratic equation is:
#                ax^2 + bx + c = 0
# where solution is x_0 = (-b + sqrt(b^2 - 4ac)) / (2a)
# and 
# x_1 = (-b - sqrt(b^2 - 4ac)) / (2a)
# create a function to solve the quadratic formula given a, b, c.
# Return x_0, x_1 with your function
# Use your function to print the solution when a = 3.3, b = 1.7, c = -9.4

# TODO: 4. Use a loop to find the largest integer that when squared is less than 2000
# print the integer

# TODO: 5. Create three separate functions
# one func should calculate the volume (v)
# another to calculate the surface area (A),
# and another to calculate the density (p) (rho) of a sphere.
# the input variable for these functions should be the radius r
# with the density function, allow the mass m to be an optional variable that defaults to m = 0.35.
# Print the volume of a sphere with:
# radius r = 0.69
# print the surface area of a sphere with radius r = 0.4.
# Print the density of a sphere with r = 0.3 and the default mass
# Print the density of a sphere with r = 0.25 and m = 2.0

# v = (4/3)*pi*r^3
# A = 4*pi*r^2
# p = m/v

# TODO: complete and push to github



# 1.
def fib_seq(n):
    '''returns fibonacci sequence to the nth term

    Args:
        n (int): the number of items to return from fibonacci sequence.
    '''
    # first three numbers of fib sequence
    f = [0, 1, 1]
    # generate next n numbers in sequence
    for i in range(len(f), n):
        f.append(f[i-1] + f[i-2])

    return f

n = 23  # number of sequence to generate
f = fib_seq(n)
# print the sequence
print(f)
# print the length of sequence
print(len(f))
