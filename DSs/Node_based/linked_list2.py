# Creating the node class
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None
        


# Storing nodes
node_1 = Node(5)
node_2 = Node(7)
node_3 = Node('Once')
node_4 = Node('upon')

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4


# However we need an easier way to tell our program where the linked list begins, to do this we need the LinkedLIst class
class LinkedList:
    def __init__(self, firstNode):
        self.firstNode = firstNode
    # reading from a linked list takes O(n) time
    def read(self, index):
        current_node = self.firstNode
        current_index = 0
        
        while current_index < index:
            if current_node.next is not None:
                current_node = current_node.next
                current_index += 1
        return current_node.data
    
    # Searching a linked list also take O(n) time
    def indexOf(self, search_value):
        current_node = self.firstNode
        current_index = 0
        
        while current_node:
            if current_node.data == search_value:
                return current_index
            
            current_node = current_node.next
            current_index += 1
            
        return current_index
            
ll = LinkedList(node_1)

print(ll.read(3))
print(ll.indexOf(8))