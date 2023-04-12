"""
    Variables are containers that hold data for use
"""

# Variables are assigned the minute they are given a value
# When declaring the 'type' does not need to be stated beforehand.
x = 2
name = 'Prince'

print(x)
print(name)

# Variables can be reassigned values with different types
x = 'Prince'
name = 2

# Casting
# But you might want to specify a particular 'type' for a variable

a = int(3)
b = float(3)

c = str(3)

print(a)
print(b)
print(c)

# To get the type of a variable you could use the 'type()' function
print(type(a))
print(type(name))
print(type(c))

# Other ways to assign variables

# Multiple vars can be assigned their values on a single line
x ,y, z = 1, 2, 3
print(x)
print(y)
print(z)

# Multiple vars can be assigned one value 