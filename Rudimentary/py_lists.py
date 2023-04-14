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