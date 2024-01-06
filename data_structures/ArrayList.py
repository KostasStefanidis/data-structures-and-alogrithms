class ArrayList():
    length: int
    capacity: int
    array: list
    
    def __init__(self) -> None:
        self.capacity = 4
        self.length = 0
        # Only way to "allocate" an array of specific size
        # Under the hood python may allocate a bigger array
        self.array = [None] * self.capacity        
    
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
        return self.__repr__()
    
    def __iter__(self):
        self.counter = 0
        return self
    
    def __next__(self):
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
        
        return new_array
    
    
    def push(self, item):
        if self.length + 1 > self.capacity:
            self.capacity = self.capacity * 2
            self.array = self._reallocate_array()
        
        self.array[self.length] = item
        self.length += 1
        
    
    def pop(self):
        if self.length > 0:
            self.array[-1] = None
            self.length -= 1

    
    def enqueue(self, item):
        if self.length + 1 > self.capacity:
            self.capacity = self.capacity * 2
            self.array = self._reallocate_array()
        
        for i in reversed(range(self.length+1)):
            self.array[i] = self.array[i-1]
        
        self.length += 1
        
        self.array[0] = item
    
    
    def deque(self):        
        item = self.array[0] if self.length != 0 else None
        
        for i in range(1, self.length):
            self.array[i-1] = self.array[i]
            
        self.length -= 1
            
        return item