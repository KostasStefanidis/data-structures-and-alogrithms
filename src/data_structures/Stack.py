from typing import Generic, TypeVar

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, data: T, next = None) -> None:
        self.data = data
        self.next: Node[T] = next
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.__str__()}"
    
    def __str__(self) -> str:
        return str(self.data)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node[T]):
            raise TypeError(f"Cannot compare {self.__class__.__name__} object to {type(other)}")
        return self.data == other.data


class Stack(Generic[T]):
    length: int
    head: Node[T]
    curr: Node[T] # used for the iterator only
    
    def __init__(self) -> None:
        self.length = 0
        self.head = None
    
    def __len__(self) -> int:
        return self.length
    
    def __iter__(self):
        self.curr = self.head
        return self
    
    def __next__(self) -> Node[T]:
        if self.curr is None:
            raise StopIteration
        
        node = self.curr
        self.curr = self.curr.next
        return node
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.__str__()}"
    
    def __str__(self) -> str:
        return f"[{', '.join([str(node.data) for node in self])}]"
    
    def push(self, item: T) -> None:
        node = Node(item)
        
        self.length += 1
        
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def pop(self) -> T:       
        if self.head is None:
            return None
        
        self.length -= 1
        
        node = self.head
        self.head = self.head.next
        
        return node.data
        
    def peek(self) -> T:
        return self.head.data or None
    