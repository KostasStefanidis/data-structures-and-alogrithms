import pytest

from src.data_structures.Queue import Queue


class TestQueue:
    """Test cases for Queue class."""

    def test_init(self):
        """Test Queue initialization."""
        queue = Queue()
        assert queue.length == 0
        assert queue.head is None
        assert queue.tail is None

    def test_len_empty_queue(self):
        """Test __len__ on empty queue."""
        queue = Queue()
        assert len(queue) == 0

    def test_len_non_empty_queue(self):
        """Test __len__ on non-empty queue."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert len(queue) == 3

    def test_repr_empty_queue(self):
        """Test __repr__ on empty queue."""
        queue = Queue()
        assert repr(queue) == "Queue: []"

    def test_repr_non_empty_queue(self):
        """Test __repr__ on non-empty queue."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert repr(queue) == "Queue: [1, 2, 3]"

    def test_str_empty_queue(self):
        """Test __str__ on empty queue."""
        queue = Queue()
        assert str(queue) == "[]"

    def test_str_non_empty_queue(self):
        """Test __str__ on non-empty queue."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert str(queue) == "[1, 2, 3]"

    # Enqueue tests
    def test_enqueue_to_empty_queue(self):
        """Test enqueuing to an empty queue."""
        queue = Queue()
        queue.enqueue(5)
        assert queue.length == 1
        assert queue.head.data == 5
        assert queue.tail.data == 5
        assert queue.head.next is None

    def test_enqueue_to_non_empty_queue(self):
        """Test enqueuing to a non-empty queue."""
        queue = Queue()
        queue.enqueue(5)
        queue.enqueue(10)
        assert queue.length == 2
        assert queue.head.data == 5
        assert queue.tail.data == 10
        assert queue.head.next.data == 10

    def test_enqueue_multiple_items(self):
        """Test enqueuing multiple items."""
        queue = Queue()
        for i in range(5):
            queue.enqueue(i)
        assert queue.length == 5
        assert queue.head.data == 0
        assert queue.tail.data == 4

    @pytest.mark.parametrize(
        "items, expected_head, expected_tail, expected_length",
        [
            ([1], 1, 1, 1),
            ([1, 2], 1, 2, 2),
            ([1, 2, 3], 1, 3, 3),
            (["a", "b", "c"], "a", "c", 3),
            ([True, False], True, False, 2),
        ],
    )
    def test_enqueue_parametrized(self, items, expected_head, expected_tail, expected_length):
        """Test enqueuing various types of items."""
        queue = Queue()
        for item in items:
            queue.enqueue(item)
        assert queue.length == expected_length
        assert queue.head.data == expected_head
        assert queue.tail.data == expected_tail

    # Deque tests
    def test_deque_from_empty_queue(self):
        """Test dequeuing from an empty queue."""
        queue = Queue()
        result = queue.deque()
        assert result is None
        assert queue.length == 0

    def test_deque_single_item(self):
        """Test dequeuing single item from queue."""
        queue = Queue()
        queue.enqueue(5)
        result = queue.deque()
        assert result == 5
        assert queue.length == 0
        assert queue.head is None

    def test_deque_multiple_items(self):
        """Test dequeuing multiple items from queue."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        result1 = queue.deque()
        assert result1 == 1
        assert queue.length == 2
        assert queue.head.data == 2
        
        result2 = queue.deque()
        assert result2 == 2
        assert queue.length == 1
        assert queue.head.data == 3

    def test_deque_until_empty(self):
        """Test dequeuing until queue is empty."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        queue.deque()
        queue.deque()
        queue.deque()
        
        assert queue.length == 0
        assert queue.head is None

    def test_deque_fifo_order(self):
        """Test that deque follows FIFO order."""
        queue = Queue()
        items = [1, 2, 3, 4, 5]
        
        for item in items:
            queue.enqueue(item)
        
        dequeued = []
        while queue.length > 0:
            dequeued.append(queue.deque())
        
        assert dequeued == items

    @pytest.mark.parametrize(
        "items, deque_count, expected_result",
        [
            ([1, 2, 3], 1, 1),
            ([1, 2, 3], 2, 2),
            (["a", "b", "c"], 1, "a"),
            ([True, False, None], 1, True),
        ],
    )
    def test_deque_parametrized(self, items, deque_count, expected_result):
        """Test dequeuing various types of items."""
        queue = Queue()
        for item in items:
            queue.enqueue(item)
        
        result = None
        for _ in range(deque_count):
            result = queue.deque()
        
        assert result == expected_result

    # Peek tests
    def test_peek_empty_queue(self):
        """Test peeking at an empty queue."""
        queue = Queue()
        result = queue.peek()
        assert result is None

    def test_peek_single_item(self):
        """Test peeking at queue with single item."""
        queue = Queue()
        queue.enqueue(5)
        result = queue.peek()
        assert result == 5
        assert queue.length == 1  # Length should not change

    def test_peek_multiple_items(self):
        """Test peeking at queue with multiple items."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        result = queue.peek()
        assert result == 1
        assert queue.length == 3  # Length should not change

    def test_peek_does_not_modify_queue(self):
        """Test that peek does not modify the queue."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        
        peek1 = queue.peek()
        peek2 = queue.peek()
        
        assert peek1 == peek2 == 1
        assert queue.length == 2

    @pytest.mark.parametrize(
        "items, expected_peek",
        [
            ([1], 1),
            ([1, 2, 3], 1),
            (["first", "second"], "first"),
            ([True, False], True),
        ],
    )
    def test_peek_parametrized(self, items, expected_peek):
        """Test peeking at various types of items."""
        queue = Queue()
        for item in items:
            queue.enqueue(item)
        assert queue.peek() == expected_peek

    # Iterator tests
    def test_iterator_empty_queue(self):
        """Test iterating over an empty queue."""
        queue = Queue()
        items = [node.data for node in queue]
        assert items == []

    def test_iterator_single_item(self):
        """Test iterating over queue with single item."""
        queue = Queue()
        queue.enqueue(5)
        items = [node.data for node in queue]
        assert items == [5]

    def test_iterator_multiple_items(self):
        """Test iterating over queue with multiple items."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        items = [node.data for node in queue]
        assert items == [1, 2, 3]

    def test_iterator_does_not_modify_queue(self):
        """Test that iterating does not modify the queue."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        # First iteration
        items1 = [node.data for node in queue]
        # Second iteration
        items2 = [node.data for node in queue]
        
        assert items1 == items2 == [1, 2, 3]
        assert queue.length == 3

    def test_iterator_with_for_loop(self):
        """Test iterator using for loop."""
        queue = Queue()
        values = [10, 20, 30]
        for value in values:
            queue.enqueue(value)
        
        collected = []
        for node in queue:
            collected.append(node.data)
        
        assert collected == values

    # Integration tests
    def test_enqueue_deque_mixed_operations(self):
        """Test mixed enqueue and deque operations."""
        queue = Queue()
        
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.deque() == 1
        
        queue.enqueue(3)
        queue.enqueue(4)
        assert queue.deque() == 2
        assert queue.deque() == 3
        
        queue.enqueue(5)
        assert queue.length == 2
        assert queue.peek() == 4

    def test_queue_lifecycle(self):
        """Test complete queue lifecycle."""
        queue = Queue()
        
        # Empty state
        assert len(queue) == 0
        assert queue.peek() is None
        
        # Add items
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert len(queue) == 3
        assert queue.peek() == 1
        
        # Remove items
        assert queue.deque() == 1
        assert queue.deque() == 2
        assert len(queue) == 1
        
        # Add more items
        queue.enqueue(4)
        queue.enqueue(5)
        assert len(queue) == 3
        
        # Empty the queue
        queue.deque()
        queue.deque()
        queue.deque()
        assert len(queue) == 0
        assert queue.peek() is None

    def test_queue_with_different_types(self):
        """Test queue with different data types."""
        queue = Queue()
        
        queue.enqueue(1)
        queue.enqueue("string")
        queue.enqueue([1, 2, 3])
        queue.enqueue({"key": "value"})
        queue.enqueue(None)
        
        assert queue.deque() == 1
        assert queue.deque() == "string"
        assert queue.deque() == [1, 2, 3]
        assert queue.deque() == {"key": "value"}
        assert queue.deque() is None
        assert len(queue) == 0

    def test_queue_maintains_order(self):
        """Test that queue maintains FIFO order."""
        queue = Queue()
        items = list(range(100))
        
        for item in items:
            queue.enqueue(item)
        
        for expected in items:
            assert queue.deque() == expected
        
        assert len(queue) == 0

    def test_str_representation_updates(self):
        """Test that string representation updates correctly."""
        queue = Queue()
        assert str(queue) == "[]"
        
        queue.enqueue(1)
        assert str(queue) == "[1]"
        
        queue.enqueue(2)
        assert str(queue) == "[1, 2]"
        
        queue.deque()
        assert str(queue) == "[2]"
        
        queue.deque()
        assert str(queue) == "[]"

    def test_length_tracking_accuracy(self):
        """Test that length is tracked accurately."""
        queue = Queue()
        assert queue.length == 0
        
        for i in range(10):
            queue.enqueue(i)
            assert queue.length == i + 1
        
        for i in range(10):
            queue.deque()
            assert queue.length == 9 - i
        
        assert queue.length == 0
