class Stack():
    def __init__(self):
        self.arr = []
    
    def populate(self, word):
        self.arr = [i for i in word]
    
    
    def push(self, value):
        self.arr.append(value)
    
        
    def pop(self):
        return self.arr.pop()
    
    
    def read(self):
        print([i for i in self.arr])
    
    
    def reverse_content(self):
        reversed_content = ''
        arrCopy = self.arr.copy()
        
        for i in self.arr:
            reversed_content += arrCopy.pop()
            
        return str(reversed_content)
    
    
    def __str__(self):
        return "This is the Stack parent class"

parting_list = Stack()
print(type(parting_list))

parting_list.push('books')
parting_list.push('bread')
parting_list.read()

print(parting_list)


# Using a stack to reverse a string
word = Stack()
word.populate('abcde')
word.read()
print(word.reverse_content())