from typing import Generic, TypeVar
T = TypeVar('T')
DEFAULT_CAPACITY = 4

class ArrayList(Generic[T]):
    length: int
    capacity: int
    array: list[T]
    
    def __init__(self, item: list[T] | tuple[T] | T = None) -> None:
        if item is None:
            self.capacity = DEFAULT_CAPACITY
            self.length = 0
            self.array = [None for _ in range(self.capacity)]
        elif isinstance(item, (list, tuple)):
            self.capacity = len(item)
            self.length = len(item)
            self.array = item
        else:
            self.capacity = DEFAULT_CAPACITY
            self.length = 1
            self.array = [item] + [None for _ in range(self.capacity - 1)]
    
    def __len__(self) -> int:
        return self.length
    
    def __getitem__(self, index: int):
        if index > self.length - 1:
            raise IndexError('ArrayList index out of bounds')
        
        return self.array[index]
    
    def __setitem__(self, index: int, value):
        if index > self.length - 1:
            raise IndexError('ArrayList index out of bounds')
        
        self.array[index] = value
        self.length += 1
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.array}"
    
    def __str__(self) -> str:
        return str([elem for elem in self.array if elem is not None])
    
    def __iter__(self):
        self.counter = 0
        return self
    
    def __next__(self) -> T:
        if self.length == 0 or self.counter >= self.length:
            raise StopIteration
        
        next_value = self.array[self.counter]
        self.counter += 1
        return next_value
    
    
    def _reallocate_array(self):
        print(f'Reallocating array with new capacity = {self.capacity}')
        
        # Create new array and copy the previous values into it
        new_array = [None] * self.capacity
        for i in range(self.length):
            new_array[i] = self.array[i]
        
        self.array = new_array
            
    
    def push(self, item) -> None:
        if self.length + 1 > self.capacity:
            self.capacity = self.capacity * 2
            self._reallocate_array()
        
        self.array[self.length] = item
        self.length += 1
    
    
    def pop(self) -> T | None:
        if self.length == 0:
            raise IndexError('Cannot pop from empty list')
        
        item = self.array[-1]
        self.array[-1] = None
        self.length -= 1
        return item
    
    
    def enqueue(self, item) -> None:
        if self.length + 1 > self.capacity:
            self.capacity = self.capacity * 2
            self._reallocate_array()
        
        self.length += 1
        
        for i in reversed(range(self.length)):
            self.array[i] = self.array[i-1]
        
        self.array[0] = item
    
    
    def deque(self) -> T | None:        
        item = self.array[self.length - 1] if self.length != 0 else None
        
        self.array[self.length - 1] = None
        
        self.length -= 1
        
        return item