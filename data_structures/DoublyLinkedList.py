from typing import Any, Generic
from typing import TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, data, prev = None, next = None) -> None:
        self.data: T = data
        self.prev: Node = prev
        self.next: Node = next

class DoublyLinkedList():
    length: int
    head: Node
    tail: Node
    
    def __init__(self) -> None:
        self.length = 0
        self.head = None
        self.tail = None
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}'
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def prepend(self, item):
        node = Node(item)
        
        self.length += 1
        
        if self.head is None:
            self.head = self.tail = node
            return
        
        node.next = self.head
        self.head.prev = node
        self.head = node
    
    def insertAt(self, idx: int, item: T):
        
        if idx > self.length:
            raise IndexError('List index out of bounds')
        elif idx == self.length:
            self.append(item)
            return
        elif idx == 0:
            self.prepend(item)
            return
        else:
            # traverse list till index
            curr = self._getNode(idx)
            
            node = Node(item)
            node.next = curr
            node.prev = curr.prev
            curr.prev = node
            node.prev.next = node
        
        self.length += 1
        
    def append(self, item: T):
        node = Node(item)
        
        if self.tail is None:
            self.head = self.tail = None
            return
        
        self.tail.next = node
        node.prev = self.tail
        
        self.tail = node
                
        self.length += 1
    
    
    def remove(self, item: T):
        node = self._getNode(self.length - 1)
        
        if not node:
            return None
        
        return self._removeNode()
    
    
    def removeAt(self, idx: int) -> T | None:
        node = self._getNode(idx)
        
        if not node:
            return None
        
        return self._removeNode(node)
    
    
    def get(self, idx: int) -> T | None:
        
        node = self._getNode(idx)
        
        if node is None:
            return None
        
        return node.data
    
    
    def _removeNode(self, node: Node) -> T | None:
        self.length -= 1
        
        if self.length == 0:
            self.head = self.tail = None
            return
        
        if node == self.head:
            self.head = node.next
        
        if node == self.tail:
            self.tail = node.prev
        
        if node.next:
            node.next.prev = node.prev
        
        if node.prev:
            node.prev.next = node.next
    
    
    def _getNode(self, idx: int) -> Node | None:
        if idx > self.length:
            raise IndexError('List index out of bounds')
        
        curr = self.head
        
        for i in range(1, idx):
            if curr is None:
                break
            
            curr = curr.next
            
        return curr
                