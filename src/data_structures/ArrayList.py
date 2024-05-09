from typing import Generic, TypeVar
T = TypeVar('T')
DEFAULT_CAPACITY = 4

class ArrayList(Generic[T]):
    length: int
    capacity: int
    array: list[T]
    counter: int

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
        if self.length == 0 or index > self.length - 1 or -index > self.length:
            raise IndexError('ArrayList index out of bounds')

        return self.array[index]


    def __setitem__(self, index: int, value):
        if self.length == 0 or index > self.length - 1 or -index > self.length:
            raise IndexError('ArrayList index out of bounds')

        self.array[index] = value


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.array}"

    def __str__(self) -> str:
        # return str([elem for elem in self.array if elem is not None])
        return str(self.get_array())


    def __iter__(self):
        self.counter = 0
        return self


    def __next__(self) -> T:
        if self.length == 0 or self.counter >= self.length:
            raise StopIteration

        next_value = self.array[self.counter]
        self.counter += 1
        return next_value


    def __eq__(self, other) -> bool:
        if not isinstance(other, ArrayList):
            raise TypeError(f"Cannot compare {self.__class__.__name__} object to {type(other)}")
        return self.array == other.array


    def _reallocate_array(self):
        self.capacity = self.capacity * 2
        print(f'Reallocating array with new capacity = {self.capacity}')

        # Create new array and copy the previous values into it
        new_array = [None] * self.capacity
        for i in range(self.length):
            new_array[i] = self.array[i]

        self.array = new_array
        
    
    def get_array(self):
        return self.array[:self.length]


    def push(self, item) -> None:
        if self.length + 1 > self.capacity:
            self._reallocate_array()

        self.array[self.length] = item
        self.length += 1
    
    
    def enqueue(self, item) -> None:
        if self.length + 1 > self.capacity:
            self._reallocate_array()

        self.length += 1

        for i in reversed(range(self.length)):
            self.array[i] = self.array[i-1]

        self.array[0] = item


    def remove(self, idx: int = None) -> T | None:
        if self.length == 0:
            raise IndexError('Cannot remove item from empty list')

        # pop last item in the ArrayList (like poping from a stack).
        # No items need to be moved in this case
        if idx is None:
            idx = self.length - 1
        
        if idx > self.length - 1:
            raise IndexError('ArrayList index out of range')

        item = self.array[idx]
        self.array[idx] = None

        # In case an item is popped from the middle of the list, 
        if idx < self.length - 1:
            for i in range(idx, self.length - 1):
                self.array[i] = self.array[i + 1]

            self.array[self.length - 1] = None

        self.length -= 1
        return item
    
    
    def pop(self) -> T | None:
        return self.remove(self.length - 1)


    def deque(self) -> T | None:        
        return self.remove(0)
