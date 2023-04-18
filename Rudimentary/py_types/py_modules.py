import greeting_mod as gm
import platform
import datetime
gm.say_hello()

# Printing all the functions and variables in a module with dir() function
# print(dir(platform))
# print(dir(datetime))

print(dir(gm))

# Importing only 
# parts of a module
from greeting_mod import say_hello

say_hello()