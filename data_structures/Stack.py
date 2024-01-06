class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next: Node = next

class Stack:
    length: int
    head: Node
    
    def __init__(self) -> None:
        self.length = 0
        self.head = None
        
    def push(self, item) -> None:
        node = Node(item)
        
        self.length += 1
        
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        
    def pop(self):       
        if self.head is None:
            return None
        
        self.length -= 1
        
        node = self.head
        self.head = self.head.next
        
        return node.data
        
    def peek(self):
        return self.head.data or None
    