# Creating a list
thislist = ['apple', 'banana', 'cherry', 'orange', 'pineapple']
print(thislist)

otherlist = list(('books', 'eggs', 'vegetables'))
print(otherlist)
# The length of a list with the len() function
print(len(thislist))
print(len(otherlist))

# Access elements 
print(otherlist[1])

print(otherlist[2:])

print(thislist[:4])

if 'books' in otherlist:
    print('You already got that!')
else:
    print('Sam, go get it!')
    
# Editing list items
otherlist[1] = 'apples'
print(otherlist)

thislist[1:4] = ['Guava', 'melon', 'pear', 'apricot']
print(thislist)

# Adding to list items with insert() method
otherlist.insert(3, 'nice_fruit')
print(otherlist)

# Adding to list with append() method
otherlist.append('saucepan') # Produces an error when there is more than one argument.

otherlist.extend(('other saucepan', 'once')) # Takes just one argument
print(otherlist)

# You can add any iterable
thistuple = ('kiwi', 'orange')
otherlist.extend(thistuple)
print(otherlist)
print(type(otherlist))

# Removing items
# Removing with the remove() method
removable = 'other saucepan'
otherlist.remove('once')
otherlist.remove('{}'.format(removable))
print(otherlist)

# Removing using pop() method
thislist.pop(2)
print(thislist)


# Removing using del

del thislist[0]
print(thislist)

thislist.clear()
print()
# Looping through a list
thislist.extend(('Rangerover', 'Toyota', 'lamborghini', 'Mazda', 'Scion', 'Ferrari', 'Aston Martin'))

for x in thislist:
    print(x)
print()
for i in range(len(thislist)):
    print(thislist[i])
    
print()

[print(x) for x in thislist]

# List comprehension

# [expression for x in iterable if x = True]

# Create a new list with only values that have an 'a' in them
new_car_list = [x for x in thislist if 'a' in x]
print(new_car_list)
print('Thislist len {} but new_car_list has length {}'.format(len(thislist), len(new_car_list)))

# Sorting using the sort() method
fruits = ['orange', 'kiwi', 'mango', 'pineapple', 'banana']
fruits.sort()
print(fruits)

nums = [100, 50, 65, 82, 23]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

# Customizing the sort function
def reduce_by_ten(n):
    return n - 65

nums.sort(key = reduce_by_ten)
print(nums)



# Copying a list
new_list = thislist.copy()
print(new_list)