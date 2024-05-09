from abc import ABC, abstractmethod

from .ArrayList import ArrayList


class AbstractHeap(ABC):
    """
    Abstract base class for Heap data structure

    Heap is a complete binary tree

    Always balanced binary tree

    Heap is implemented using ArrayList

    Heap is used to implement Priority Queue
    """

    length: int
    data: ArrayList

    def __init__(self) -> None:
        self.length = 0
        self.data = ArrayList()

    def __len__(self) -> int:
        return self.length

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.data}"

    def __str__(self) -> str:
        return str(self.data)

    def _parent(self, idx: int) -> int:
        return (idx - 1) // 2

    def _left_child(self, idx: int) -> int:
        return 2 * idx + 1

    def _right_child(self, idx: int) -> int:
        return 2 * idx + 2

    def insert(self, item) -> None:
        """
        Insert item into heap
        Runtime: O(log n)
        """
        self.data.push(item)
        self._heapify_up(self.length)
        self.length += 1

    def delete(self):
        if self.length == 0:
            raise ValueError("Cannot delete item from empty Heap")

        out = self.data[0]
        self.data[0] = self.data.pop()
        self.length -= 1
        self._heapify_down(0)
        return out

    def _swap_values(self, parent_idx: int, child_idx: int) -> None:
        parent_value = self.data[parent_idx]
        child_value = self.data[child_idx]

        self.data[parent_idx] = child_value
        self.data[child_idx] = parent_value

    @abstractmethod
    def _heapify_up(self, idx: int):
        pass

    @abstractmethod
    def _heapify_down(self, idx: int):
        pass


class MinHeap(AbstractHeap):
    """
    Max Heap: parent node is always greater than child nodes
    """

    length: int
    data: ArrayList

    def _heapify_up(self, idx: int):
        parent_idx = self._parent(idx)

        child_value = self.data[idx]
        parent_value = self.data[parent_idx]

        if child_value < parent_value:
            self._swap_values(parent_idx, idx)
            self._heapify_up(parent_idx)

    def _heapify_down(self, idx: int):
        left_idx = self._left_child(idx)
        right_idx = self._right_child(idx)

        parent_value = self.data[idx]
        left_child_value = self.data[left_idx]
        right_child_value = self.data[right_idx]

        if left_child_value < right_child_value and left_child_value < parent_value:
            self._swap_values(idx, left_idx)
            self._heapify_down(left_idx)

        elif right_child_value < left_child_value and right_child_value < parent_value:
            self._swap_values(idx, right_idx)
            self._heapify_down(right_idx)


class MaxHeap(AbstractHeap):
    """
    Min Heap: parent node is always smaller than child nodes
    """

    length: int
    data: ArrayList

    def _heapify_up(self, idx: int):
        if idx == 0:
            return

        parent_idx = self._parent(idx)

        child_value = self.data[idx]
        parent_value = self.data[parent_idx]

        if child_value > parent_value:
            self._swap_values(parent_idx, idx)
            self._heapify_up(parent_idx)

    def _heapify_down(self, idx: int):
        left_idx = self._left_child(idx)
        right_idx = self._right_child(idx)

        # if the left child index is greater than the length of the heap,
        # then we have no more children
        if idx >= self.length or left_idx >= self.length:
            return

        parent_value = self.data[idx]
        left_child_value = self.data[left_idx]
        right_child_value = self.data[right_idx]

        if left_child_value > right_child_value and left_child_value > parent_value:
            self._swap_values(idx, left_idx)
            self._heapify_down(left_idx)

        elif right_child_value > left_child_value and right_child_value > parent_value:
            self._swap_values(idx, right_idx)
            self._heapify_down(right_idx)
