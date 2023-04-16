# Sets are immutable sequence data types in python.


# declaring a set
thisset = {'item', 'otheritem', 'banana'}

print(type(thisset))
print(thisset)
# Editing sets
# set are immutable so to edit a set, you'd need to convert it to a list then work with it

updated_set = list(thisset)
updated_set.extend(('from', 'the', 'list'))

thisset = set(updated_set)
print(thisset)

# Removing items with remove() method
thisset.remove('from')
print(thisset)

