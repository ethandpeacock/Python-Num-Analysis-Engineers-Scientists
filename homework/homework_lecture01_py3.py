# Homework 01


# 1.
print("Python2 is faster\n")

# 2.
x = [0, 1, 2, 3, 4, 5, 6]
print(x)
print(x[2])
print()

# 3.
y = []
index = len(x) - 1
for i in range(len(x)):
	y.append(x[index])
	index -= 1	
print(y)
print()

# 4.
z = []
z.append(x[1])
z.append(x[3])
z.append(x[5])
print(z)
print()

# 5.
se_code = "Incorrect syntax error code:\n \
		x = 99\n \
		if (x > 0) is True\n \
		print('x is positive')\n"
print(se_code)
x = 99
if (x > 0):
	print('x is positive')

