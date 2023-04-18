class Person():
    def __init__(self, firstname):
        self.firstname = firstname
    def __str__(self):
        return f"The person class"


def say_hello():
    print('Hello!')