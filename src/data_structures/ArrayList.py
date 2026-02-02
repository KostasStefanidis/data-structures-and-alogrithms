from typing import Generic, TypeVar

T = TypeVar("T")
DEFAULT_CAPACITY = 4


class ArrayList(Generic[T]):
    length: int
    capacity: int
    _array: list[T]
    counter: int

    def __init__(self, item: list[T] | tuple[T] | T = None) -> None:
        if item is None:
            self.capacity = DEFAULT_CAPACITY
            self.length = 0
            self._array = [None for _ in range(self.capacity)]

        elif isinstance(item, (list, tuple)):
            self.capacity = len(item)
            self.length = len(item)
            self._array = item

        else:
            self.capacity = DEFAULT_CAPACITY
            self.length = 1
            self._array = [item] + [None for _ in range(self.capacity - 1)]

    def __len__(self) -> int:
        return self.length

    def __getitem__(self, index: int) -> T:
        if self.length == 0 or index > self.length - 1 or -index > self.length:
            raise IndexError("ArrayList index out of bounds")

        return self._array[index]

    def __setitem__(self, index: int, value: T):
        if self.length == 0 or index > self.length - 1 or -index > self.length:
            raise IndexError("ArrayList index out of bounds")

        self._array[index] = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self._array}"

    def __str__(self) -> str:
        return str(self._get_array())

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self) -> T:
        if self.length == 0 or self.counter >= self.length:
            raise StopIteration

        next_value = self._array[self.counter]
        self.counter += 1
        return next_value

    def __eq__(self, other) -> bool:
        if not isinstance(other, ArrayList):
            raise TypeError(
                f"Cannot compare {self.__class__.__name__} object to {type(other)}")
        return self._get_array() == other._get_array()

    def _reallocate_array(self):
        self.capacity = self.capacity * 2
        print(f"Reallocating array with new capacity = {self.capacity}")

        # Create new array and copy the previous values into it
        new_array = [None] * self.capacity
        new_array[0: self.length] = self._get_array()

        self._array = new_array

    def shift_forward(self, idx):
        for i in reversed(range(idx, self.length)):
            self._array[i] = self._array[i - 1]

    def shift_backward(self, idx):
        for i in range(idx, self.length - 1):
            self._array[i] = self._array[i + 1]

    def _get_array(self):
        return self._array[0: self.length]

    def put(self, idx: int, item: T):
        if self.length + 1 > self.capacity:
            self._reallocate_array()

        self.length += 1
        self.shift_forward(idx)
        self._array[idx] = item

    def push(self, item) -> None:
        self.put(self.length, item)

    def enqueue(self, item) -> None:
        self.put(0, item)

    def remove(self, idx: int) -> T:
        if self.length == 0:
            raise IndexError("Cannot remove item from empty list")

        if idx > self.length - 1:
            raise IndexError("ArrayList index out of range")

        item = self._array[idx]
        self._array[idx] = None

        # In case an item is removed from the middle of the list,
        if idx < self.length - 1:
            self.shift_backward(idx)
            self._array[self.length - 1] = None

        self.length -= 1
        return item

    def pop(self) -> T:
        return self.remove(self.length - 1)

    def deque(self) -> T:
        return self.remove(0)
