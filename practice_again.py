def fib(n):
    if n == 0 or n == 1:
        return n
    
    return fib(n - 1) + fib(n - 2)

# Enhanced fib

# def e_fib(n:int, memo:dict):
#     # set the base case
#     if n == 0 or n == 1:
#         return n
    
#     # Check if the value has not already been cached
#     if not memo.get():
#         memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
#     return memo[n]
    
        
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
            
class LinkedList:
    def __init__(self, head):
        self.head = head
    
    def readAll(self):
        current_node = self.head
        
        while current_node.next != None:
            print(current_node.data)
            
            if current_node.next is not None:
                current_node = current_node.next
                
    def look_up(self, index):
        current_node = self.head
        current_index = 0
        
        while current_index < index:
            if current_node.next is not None:
                current_node = current_node.next
                current_index += 1
            else:
                return 'Does not exist'
        return current_node.data or None
    
    def find(self, search_value):
        current_node = self.head
        current_index = 0
        
        while current_node is not None:
            if current_node.data == search_value:
                return current_index
            else:
                current_index += 1
                current_node = current_node.next
                
    def insert_at_index(self, index, value):
        # create new node 
        new_node = Node(value)
        current_node = self.head
        current_index = 0
        
        # Move to index penultimate index
        while current_index < index - 1:
            current_node = current_node.next    
            current_index += 1
        # Link new node to the next node
        new_node.next = current_node.next
        
        # link previous node to new node
        current_node.next = new_node
        
        
            
    
node1 = Node(12)
node2 = Node(15)
node3 = Node(17)
node4 = Node('once')
node5 = Node('upon')

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

fNode = Node('beginning')
fNode.next =  node1


ll = LinkedList(fNode)
        
if __name__ == "__main__":
    # print(fib(10))\
    # print(node1.next)
    # print(node2)
    
    # ll.readAll()
    # print(ll.look_up(5))
    
    # print(ll.find(15))
    # print(ll.find('once'))
    ll.insert_at_index(3, 'this is the inserted')
    ll.readAll()
    