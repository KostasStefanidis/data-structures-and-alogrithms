from typing import Generic, TypeVar

T = TypeVar("T")
DEFAULT_CAPACITY = 4


class RingBuffer(Generic[T]):
    length: int
    capacity: int
    array: list[T]
    head: int = 0
    tail: int

    def __init__(self, item: list[T] | tuple[T] | T = None) -> None:
        if item is None:
            self.capacity = DEFAULT_CAPACITY
            self.length = 0
            self.array = [None for _ in range(self.capacity)]
            self.tail = self.capacity - 1
        elif isinstance(item, (list, tuple)):
            self.capacity = len(item)
            self.length = len(item)
            self.array = item
            self.tail = self.length - 1
        else:
            self.capacity = DEFAULT_CAPACITY
            self.length = 1
            self.array = [item] + [None for _ in range(self.capacity - 1)]
            self.tail = 0

    def __len__(self) -> int:
        return self.length

    def __repr__(self) -> str:
        output = ""
        pad = 8
        for i in range(self.capacity):
            if i == self.head == self.tail:
                output += "Head, Tail -> "
                pad = 14
            elif i == self.head:
                output += "Head -> "
            elif i == self.tail:
                output += "Tail -> "
            else:
                output += " " * pad
            output += str(self.array[i]) + ",\n"
        return output

    def __str__(self) -> str:
        return str(self.get_array())

    def _reallocate_array(self):
        self.capacity = self.capacity * 2
        print(f"Reallocating array with new capacity = {self.capacity}")

        # Create new array and copy the previous values into it
        new_array = [None] * self.capacity
        new_array[0 : self.length] = self.get_array()

        self.array = new_array
        self.head = 0
        self.tail = self.length - 1

    def get_array(self):
        if self.length != 0:
            if self.head < self.tail:
                return self.array[self.head : self.tail + 1]
            if self.head > self.tail:
                return self.array[self.head : self.capacity] + self.array[0 : self.tail + 1]
            else:
                return [self.array[self.head]]
        return []

    def push(self, item):
        if self.length + 1 > self.capacity:
            self._reallocate_array()

        self.tail = (self.tail + 1) % self.capacity
        self.array[self.tail] = item
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise IndexError("Cannot remove item from empty list")

        item = self.array[self.tail]
        self.array[self.tail] = None
        self.tail = (self.tail - 1) % self.capacity
        self.length -= 1

        return item

    def enqueue(self, item):
        if self.length + 1 > self.capacity:
            self._reallocate_array()

        self.length += 1
        self.head = (self.head - 1) % self.capacity

        self.array[self.head] = item

    def deque(self):
        if self.length == 0:
            raise IndexError("Cannot remove item from empty list")

        item = self.array[self.head]
        self.array[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.length -= 1

        return item
