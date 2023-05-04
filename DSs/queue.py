class Queue():
    def __init__(self):
        self.arr = []
    
    
    def enqueue(self, value):
        self.arr.append(value)
        
        
    def dequeue(self):
        self.arr.pop(0)
        
    
    def read_state(self):
        return self.arr
    
    
    def __str__(self):
        return "This is my first implementation of a queue"
    
ticket_stand = Queue()
ticket_stand.enqueue('Prince Asiedu')
ticket_stand.enqueue('Anifa Hardy')
print(ticket_stand.read_state())

ticket_stand.dequeue()
print(ticket_stand.read_state())
