# Homework 3

# 1.
import pyDOE
print(help(pyDOE))
print("\n\n\n")

# TODO: remove None print

# 2.
import os
hostname = "ufl.edu"
response = os.system("ping -c 2 " + hostname)
print()




# TODO: 2. Use the os library to print the current Python working directory
# import os
# run a system command to use the systems ping program
# if you are using linux ping -c 2 ufl.edu (command should be a string)
# windows ping -c -1? idk look up and also check the response 
# if response == 0:
#    print(f"{hostname} is up!")
# else:
#    print(f"{hostname} is down!")


# 3.
import math
import numpy as np
np_pi = np.pi
math_pi = math.pi
print("numpy pi and math pi are equivalent:")
if np_pi == math_pi:
    print(True)
else:
    print(False)



# TODO: 3. Compare math.pi to numpy.pi
# are these two representations of pi equal?
# print boolean statement true if they are otherwise false






print()
print()
print()
print()
print("sphere\n\n\n")







# 4.
class sphere:
    def __init__(self, radius=0.0, mass=0.0):
        self.radius = radius 
        self.mass = mass
    def v(self):
        return (4/3) * np.pi * self.radius**3
    def A(self):
        return 4 * np.pi * self.radius**2
    def p(self):
        return (self.mass / self.v())

red = sphere(1.7, 0.25)
print(dir(red))
print("\n\nSphere volume:")
print(red.v())
print("\n\nSphere surface area:")
print(red.A())
print("\n\nSphere density:")
print(red.p())
print("\n\n")


# 5.
x = [[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15]]
for num_list in x:
    print(num_list[0], num_list[1], num_list[2], num_list[3], sep = ' & ')


