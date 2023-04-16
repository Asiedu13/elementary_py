# Dictionaries are ordered and changeable but they do not allow duplicates

person = {
    'name': "Prince",
    'age':19,
    'weight': 24
}

print(person)

print(person['age'])
print(person.get('name'))

# Getting the keys of a dictionary
print(person.keys())
print(type(person.keys()))

# Adding to the dictionary
person['location'] = 'Accra'
print(person)

# Getting the values of a dictionary
print(person.values())

# Getting both keys and values
print(person.items()) # Returns a list of tuples

# print(isinstance(person.items()))

# check if a key is in the dictionary
if 'name' in person:
    print('Name is defined')
else:
    print('No user with this name')


# Changing values in dictionaries with update() method
person.update({'name': 'Prince Kofi Asiedu II'})
print(person)

# Removing values with pop()
# person.pop('age')
# person.pop('weight')
print(person)


# looping a dictionary
for x in person:
    print(x)
    
for x in person:
    print(person[x])
    
for x, y in person.items():
    print(x, y)
    
# Copying a dictionary
new_person = person.copy()
print(new_person)