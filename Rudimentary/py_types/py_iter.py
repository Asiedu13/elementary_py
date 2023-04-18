# Iterations are like iterable objects
'''
This is so in the sense that with a list or any other iterable objects things are done at once and the state
of the iterable is not kept by the system. However, with iterators which have the lazy nature. You can call next() on an iterator and then later call next when you need it 
'''

# To create an iterator, you need an iterable object such as lists, tuple, sets
myNumbers = [1, 2,3 ,4 ,5, 6]
myiter = iter(myNumbers)
print(next(myiter))

print(next(myiter))

# https://www.datacamp.com/tutorial/python-iterators-generators-tutorial

