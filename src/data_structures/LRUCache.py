from typing import Generic, TypeVar

from .HashMap import HashMap
from .Node import DoublyLinkedNode

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")
DEFAULT_CAPACITY = 4


class LRUCache(Generic[K, V]):
    length: int
    head: DoublyLinkedNode[V] | None
    tail: DoublyLinkedNode[V] | None
    capacity: int
    lookup: HashMap[K, DoublyLinkedNode[V]]
    reverse_lookup: HashMap[DoublyLinkedNode[V], K]

    def __init__(self, capacity: int = DEFAULT_CAPACITY) -> None:
        self.capacity = capacity
        self.length = 0
        self.head = None
        self.tail = None
        self.lookup = HashMap()
        self.reverse_lookup = HashMap()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"

    def __str__(self) -> str:
        return self.__repr__()

    def update(self, key: K, value: V):
        # does it exist in the cache?
        node = self.lookup.get(key)

        # if no, insert at front & evict last if over capacity
        if not node:
            node = self.create_node(value)
            self.length += 1

        # if yes, update the value and move to front
        else:
            node.data = value
            self.detach(node)

        self.prepend(node)
        self.lookup[key] = node
        self.reverse_lookup[node] = key

        if self.length > self.capacity:
            self.evict_last()

    def get(self, key: K) -> V | None:
        # check the cache for existance of key
        node = self.lookup.get(key)

        if not node:
            return None

        self.detach(node)

        # udpate the value found and move to the front
        self.prepend(node)

        # return out the value found or None if not exist
        return node.data

    def detach(self, node: DoublyLinkedNode[V]):
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if node == self.head:
            self.head = self.head.next

        if node == self.tail:
            self.tail = self.tail.prev

        node.next = None
        node.prev = None

    def prepend(self, node: DoublyLinkedNode[V]):
        pass

    def create_node(self, value: V) -> DoublyLinkedNode[V]:
        pass

    def evict_last(self):
        if self.tail is not None:
            tail = self.tail
            self.detach(self.tail)
            key = self.reverse_lookup.get(tail)
            self.lookup.remove(key)
            self.reverse_lookup.remove(tail)

        self.length -= 1
