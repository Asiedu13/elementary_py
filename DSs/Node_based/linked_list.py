# Implementing a linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def printLinked(self):
        if self.head is None:
            print('Linked List is empty')
            return
        
        itr = self.head
        ll = ""
        while itr:
            ll += str(itr.data) + '--->'
            itr = itr.next
            
        print(ll)
            

        
if __name__ == '__main__':
    linked = LinkedList()
    linked.insert_at_beginning(1)
    linked.insert_at_beginning(56)
    linked.insert_at_beginning(12)
    linked.printLinked()
    