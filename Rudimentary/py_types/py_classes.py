# Classes are a great way to create objects in python
# A class is an object constructor

# Creating classes
class MyClass:
    x = 10

sunflower = MyClass()

print(type(sunflower))

class Person:
    # This function executes when the class is being created
    def __init__(self, name, age, home):
        self.name = name
        self.age = age
        self.home = home
    # This function controls what is seen when the function is being converted to a string
    def __str__(self):
        return f"Person: {self.name}"
    
    
    
    