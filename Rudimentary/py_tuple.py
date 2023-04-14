thistuple = ('apple', 'banana', 'cherry')
print(type(thistuple))

# Creating a tuple with one item; this needs a comma for python
items = ('books')
print(type(items)) # this is considered a string

items = ('books', )
print(type(items)) # this is now considered a tuple

# Accessing elements in a tuple
print(thistuple[0])
print(thistuple[1])

print(thistuple[2:])

if 'apple' in thistuple:
    print('We have apples')
else:
    print('Go get us some apples')
    
# Editing a tuple
'''
Tuples cannot be edited in any way after being declared. To add, remove, insert values to a tuple, you'd need to convert the tuple into a list
'''

# Adding to a tuple
thistuple = list(thistuple)
thistuple.append('orange')

thistuple = tuple(thistuple)
print(thistuple)

# Unpacking a tuple
(green , *yellow, red) = thistuple
print(green , yellow, red)



