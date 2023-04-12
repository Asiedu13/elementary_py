
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
b = 'This is the test string'
print(b[2:7])

# slice from the start
print(b[:6])

# Slice to the end
print(b[5:])

# Negative indexing
print(b[-5:-2])



# Modifying string
text = ' Gello, World! '
# upper method
print(text.upper())

# lower method
print(text.lower())

# strip method
print(text.strip())

# replace method
print(text.replace('G', 'H'))

# Python string methods always return a new value

# split() method
print(text.split(","))

# count method
print(text.count('l'))

string_methods_url = "https://www.w3schools.com/python/python_ref_string.asp"

