try:
    print(x)
except NameError:
    print('There variable does not exist!')
except:
    print("A problem occured")
    

try:
    print(y)
except SyntaxError:
    print('Syntax Error') # Specific exception handler
except:
    print('Another problem occured') # Exception handler
else:
    print('Successfull') # Executes when everything is successful
finally:
    print('Moving on to the next thing') # Executes with our without an error
    
# Raising exceptions
x = -1
if x < 0:
    raise Exception("Sorry, the number entered is less than 0")


# Setting your type of error to raise
x = '1'
if not type(x) is int:
    raise TypeError('Wrong data type identified')