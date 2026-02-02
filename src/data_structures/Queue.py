from typing import Generic, TypeVar

from .Node import Node

T = TypeVar("T")


class Queue(Generic[T]):
    length: int
    head: Node[T] | None
    tail: Node[T] | None
    curr: Node[T]  # used for the iterator only

    def __init__(self) -> None:
        self.length = 0
        self.head = None
        self.tail = None

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

    def __str__(self) -> str:
        return f"[{', '.join([str(node.data) for node in self])}]"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.__str__()}"

    def enqueue(self, item: T) -> None:
        node = Node(item)

        if self.tail is None:
            self.tail = self.head = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def deque(self) -> T | None:
        if self.head is None:
            return self.head

        self.length -= 1

        head = self.head
        self.head = self.head.next

        head.next = None

        return head.data

    def peek(self) -> T | None:
        return self.head.data if self.head else None
