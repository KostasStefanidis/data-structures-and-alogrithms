class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next: Node = next
        
class Queue:
    length: int
    head: Node
    tail: Node
    
    def __init__(self, ) -> None:
        self.length = 0
        self.head = None
        self.tail = None
        
    def enqueue(self, item):
        node = Node(item)
        
        if self.tail is None:
            self.tail = self.head = node
        else:
            self.tail.next = node
            self.tail = node
        
        self.length += 1
        
    def deque(self):
        if self.head is None:
            return self.head
        
        self.length -= 1
        
        head = self.head
        self.head = self.head.next
        
        head.next = None
        
        return head.data
        
    def peek(self):
        return self.head.data or None