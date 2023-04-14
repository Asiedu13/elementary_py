print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33
if b > a :
    print('B is greater than a')
else:
    print('B is not greater than a')
    
# The bool() function lets you evaluate any value to either true or false
print(bool('H'))
print(bool('Hi There!'))
print(bool(0))
print(bool(15))

# functions that return true or false
def myFunction():
    return True

if myFunction():
    print('YES !')
else:
    print('No!')
    
print()  
# isinstance() function returns boolean

x = 200
print(isinstance(x, int))
print(isinstance(x, bool))