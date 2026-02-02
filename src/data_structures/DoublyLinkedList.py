from typing import Generic, TypeVar

from .Node import DoublyLinkedNode

T = TypeVar("T")


class DoublyLinkedList(Generic[T]):
    length: int
    head: DoublyLinkedNode[T] | None
    tail: DoublyLinkedNode[T] | None

    def __init__(self) -> None:
        self.length = 0
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"

    def __str__(self) -> str:
        return self.__repr__()

    def prepend(self, item: T) -> None:
        node = DoublyLinkedNode(item)

        self.length += 1

        if self.head is None:
            self.head = self.tail = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def insertAt(self, idx: int, item: T) -> None:

        if idx > self.length:
            raise IndexError("List index out of bounds")

        if idx == self.length:
            self.append(item)
            return

        if idx == 0:
            self.prepend(item)
            return

        # traverse list till index
        curr = self._getNode(idx)

        node = DoublyLinkedNode(item)
        node.next = curr
        node.prev = curr.prev
        curr.prev = node
        if node.prev:
            node.prev.next = node

        self.length += 1

    def append(self, item: T) -> None:
        node = DoublyLinkedNode(item)

        self.length += 1

        if self.tail is None:
            self.head = self.tail = node
            return

        self.tail.next = node
        node.prev = self.tail

        self.tail = node

    def remove(self) -> T | None:
        if self.length == 0:
            return None

        node = self._getNode(self.length - 1)

        if not node:
            return None

        return self._removeNode(node)

    def removeAt(self, idx: int) -> T | None:
        if idx >= self.length or idx < 0:
            raise IndexError("List index out of bounds")

        node = self._getNode(idx)

        if not node:
            return None

        return self._removeNode(node)

    def get(self, idx: int) -> T | None:
        if idx >= self.length or idx < 0:
            raise IndexError("List index out of bounds")

        node = self._getNode(idx)

        if node is None:
            return None

        return node.data

    def _removeNode(self, node: DoublyLinkedNode[T]) -> T | None:
        if self.length == 0:
            # self.head = self.tail = None
            return

        self.length -= 1
        out = node.data

        if node == self.head:
            self.head = node.next

        if node == self.tail:
            self.tail = node.prev

        if node.next:
            node.next.prev = node.prev

        if node.prev:
            node.prev.next = node.next

        return out

    def _getNode(self, idx: int) -> DoublyLinkedNode[T] | None:
        if idx >= self.length or idx < 0:
            raise IndexError("List index out of bounds")

        curr = self.head

        for _ in range(idx):
            if curr is None:
                break

            curr = curr.next

        return curr
