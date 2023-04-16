# Python has an extensive list of operators that are grouped into seven categories

# Arithmetic Operationsz
print('Arithmetic Operators')
print(3 + 3)
print(3 - 3)
print(3 / 3)
print(4 // 3)
print(4 ** 3)
print(4 % 2)

print()
# Assignment Operators
print('Assignment Operators')
x = 1
x += 2
print(x)

x -= 1
print(x)

x *= 3
print(x)

# basically all the arithmetic operations will work with the assignment operator

x >>= 2 # Left shift
x <<= 2 # Right Shift

print()
# Comparison operators
print('Comparison Operators')
print(10 < 6)
print(10 > 6)
print(10 == 5)
print(10 <= 5)
print(10 >= 5)
print(10 != 10)

if 5 != 10:
    print('5 and 10 are not equal')

print()

# Logical operators
print('Logical Operators')
print(10 and 4)
print(10 or 3)
print(not(10 and 4))

print()

# Identity Operators; These operators check if the operands are the same object with the same memory location
print('Identity operators')
y = 5
print(x is y )
print( x is not y)

print()

# Membership operators
print('Membership operators')
print('hi' in 'hiccup')
print('full' not in 'hiccup')

print()

print('Bitwise Operations')
print()