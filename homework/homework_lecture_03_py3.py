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


# TODO: 2. Use the os library to print the current Python working directory
# import os
# run a system command to use the systems ping program
# if you are using linux ping -c 2 ufl.edu (command should be a string)
# windows ping -c -1? idk look up and also check the response 
# if response == 0:
#    print(f"{hostname} is up!")
# else:
#    print(f"{hostname} is down!")

# TODO: 3. Compare math.pi to numpy.pi
# are these two representations of pi equal?
# print boolean statement true if they are otherwise false

# TODO: 4. Create a class called a sphere.
# the object sphere requires a radius and mass to initialize
# attributes of the sphere should include radius r, mass m, volume v, surface area A, and density p
# initiate a new sphere name red with r = 1.7, m = 0.25
# print dir(red)
# print the volume surface area and density of red

# TODO: 5. Print function adds functionality
# x = 1.0; y = 2.0;
# print(x, y, sep = '   & '?)
# will print 1.0 & 2.0
# given x = [[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15]]
# use a for loop to iterate through the four lists in x
# each item in list should be printed and separated by an &
# example output
# 0 & 1 & 2 & 3
# 4 & 5 & 6 & 7
