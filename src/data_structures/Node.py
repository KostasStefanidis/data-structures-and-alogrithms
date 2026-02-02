"""Node classes for various data structures."""
from typing import Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    """Singly linked node used by Queue and Stack."""

    def __init__(self, data: T, next=None) -> None:
        self.data = data
        self.next: Node[T] | None = next

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.__str__()}"

    def __str__(self) -> str:
        return str(self.data)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            raise TypeError(
                f"Cannot compare {self.__class__.__name__} object to {type(other)}")
        return self.data == other.data


class DoublyLinkedNode(Generic[T]):
    """Doubly linked node used by DoublyLinkedList and LRUCache."""

    def __init__(self, data, prev=None, next=None) -> None:
        self.data: T = data
        self.prev: DoublyLinkedNode[T] | None = prev
        self.next: DoublyLinkedNode[T] | None = next

    def __str__(self) -> str:
        return str(self.data) if self.data else ""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.__str__()}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DoublyLinkedNode):
            raise TypeError(
                f"Cannot compare {self.__class__.__name__} object to {type(other)}")
        return self.data == other.data


class BinaryNode(Generic[T]):
    """Binary tree node used by BinaryTree."""

    def __init__(self, data: T, left=None, right=None) -> None:
        self.data = data
        self.left: BinaryNode[T] | None = left
        self.right: BinaryNode[T] | None = right

    def __str__(self) -> str:
        return str(self.data) if self.data else ""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.__str__()}"
