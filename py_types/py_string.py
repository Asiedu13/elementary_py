
# Declaring strings
first_name = 'Prince'
last_name = "Asiedu"
other = 'Kofi'

print(first_name, last_name, other)

# Declaring string using the string literal
sentence = ''' Prince is in the university '''
print(sentence)

# Strings are an array of bytes representing unicode characters

test = "This is a string"

# Accessing string characters
print(test[5])

# Looping through a string
for x in test:
    print(x)

# finding substrings in a string using 'in' operator
print('is' in test)

if 'this' in test:
    print('yep')
else:
    print('nope')
    
# Using the 'not in' operator
print('ince' not in first_name)

if 'icne' not in first_name:
    print('correct spelling')

# String slicing
