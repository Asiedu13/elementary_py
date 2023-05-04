class Stack():
    def __init__(self):
        self.arr = []
    
    def push(self, value):
        self.arr.append(value)
    def pop(self):
        return self.arr.pop()
    def read(self):
        print([i for i in self.arr])
    
    def __str__(self):
        return "This is the Stack parent class"

parting_list = Stack()
print(type(parting_list))

parting_list.push('books')
parting_list.push('bread')
parting_list.read()
