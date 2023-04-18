class Person():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def __str__(self):
        return "Using Person class"
    
    def printname(self):
        print(f'I am {self.firstname} {self.lastname}')
        return f'I am {self.firstname} {self.lastname}'
    

ama = Person('Ama', 'Asiedu')
print(ama.printname())

class Student(Person):
    def __init__(self, firstname, lastname, school):
        super().__init__(firstname, lastname)
        self.school = school
    
    def printschool(self):
        print(f'I am a student of {self.school}')

one_student = Student('Prince', 'Asiedu', 'KNUST')
one_student.printname()
one_student.printschool()