# Homework 2

# TODO: clean code




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
print("Fibonacci sequence:")
print(f)
print()


# 2.
def y(x):
    return (((3.0 * x)**2) / (99 * x - (x**3))) - (1/x)


xs = [2.0, 3.0, 5.0, 7.0, 9.0]
ys = []
for x in xs:
    ys.append(y(x))

print("Y list:")
print(ys)
print()


# 3.
import math

def quad_solver(a, b, c):
    '''Solves the quadratic formula for given values a, b, and c.

    Args:
        a
        b
        c

    Returns:
	# TODO: add doc strings and clean them
    '''
    x0 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    x1 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)

    return x0, x1


# solve solution where a = 3.3, b = 1.7, c = -9.4
a = 3.3
b = 1.7
c = -9.4
x0, x1 = quad_solver(a, b, c)
print("x_0:")
print(x0)
print("x_1:")
print(x1)
print()


# 4.
limit = 2000
i = 1 # starting value for squaring
last_int = -1
while (i**2 < limit):
    # store current passible int
    last_int = i
    # increment integer for squaring
    i += 1

print("Largest integer ^2 less than 2000:")
print(last_int)
print(str(last_int) + "^2 = " + str(last_int**2))
print()


# 5.

# TODO: add doc strings and comments to explain whats happening or purpose
def v(r):
    return (4/3) * (22/7) * r**3


def A(r):
    return 4 * (22/7) * r**2


def p(v, m=0.35):
    return (m / v)


print("Volume of sphere with radius r=0.69:")
print(v(0.69))
print()
print("Surface area of sphere with radius r=0.4:")
print(A(0.4))
print()
print("Density of a sphere with radius r=0.3:")
v_1 = v(0.3)
print(p(v=v_1))
print()

print("Density of a sphere with radius r=0.25 and mass m=2.0:")
v_2 = v(0.25)
print(p(v=v_2, m=2.0))
print()

