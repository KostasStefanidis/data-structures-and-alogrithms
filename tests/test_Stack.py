import pytest

from src.data_structures.Stack import Stack


class TestStack:
    """Test cases for Stack class."""

    def test_init(self):
        """Test Stack initialization."""
        stack = Stack()
        assert stack.length == 0
        assert stack.head is None

    def test_len_empty_stack(self):
        """Test __len__ on empty stack."""
        stack = Stack()
        assert len(stack) == 0

    def test_len_non_empty_stack(self):
        """Test __len__ on non-empty stack."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert len(stack) == 3

    def test_repr_empty_stack(self):
        """Test __repr__ on empty stack."""
        stack = Stack()
        assert repr(stack) == "Stack: []"

    def test_repr_non_empty_stack(self):
        """Test __repr__ on non-empty stack."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert repr(stack) == "Stack: [3, 2, 1]"

    def test_str_empty_stack(self):
        """Test __str__ on empty stack."""
        stack = Stack()
        assert str(stack) == "[]"

    def test_str_non_empty_stack(self):
        """Test __str__ on non-empty stack."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert str(stack) == "[3, 2, 1]"

    # Push tests
    def test_push_single_item(self):
        """Test pushing a single item."""
        stack = Stack()
        stack.push(5)
        assert stack.length == 1
        assert stack.head.data == 5
        assert stack.head.next is None

    def test_push_multiple_items(self):
        """Test pushing multiple items."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.length == 3
        assert stack.head.data == 3
        assert stack.head.next.data == 2
        assert stack.head.next.next.data == 1

    @pytest.mark.parametrize(
        "items, expected_top",
        [
            ([1], 1),
            ([1, 2, 3], 3),
            (["a", "b", "c"], "c"),
            ([10, 20, 30, 40], 40),
            ([True, False], False),
        ],
    )
    def test_push_various_types(self, items, expected_top):
        """Test pushing various data types."""
        stack = Stack()
        for item in items:
            stack.push(item)
        assert stack.head.data == expected_top
        assert len(stack) == len(items)

    def test_push_order_lifo(self):
        """Test that push maintains LIFO order."""
        stack = Stack()
        for i in range(5):
            stack.push(i)

        # Top should be the last pushed item
        assert stack.head.data == 4
        assert stack.head.next.data == 3
        assert stack.head.next.next.data == 2

    # Pop tests
    def test_pop_from_empty_stack(self):
        """Test popping from an empty stack."""
        stack = Stack()
        result = stack.pop()
        assert result is None
        assert stack.length == 0

    def test_pop_single_item(self):
        """Test popping a single item."""
        stack = Stack()
        stack.push(5)
        result = stack.pop()
        assert result == 5
        assert stack.length == 0
        assert stack.head is None

    def test_pop_multiple_items(self):
        """Test popping multiple items."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        assert stack.pop() == 3
        assert stack.length == 2
        assert stack.pop() == 2
        assert stack.length == 1
        assert stack.pop() == 1
        assert stack.length == 0
        assert stack.head is None

    def test_pop_lifo_order(self):
        """Test that pop maintains LIFO order."""
        stack = Stack()
        items = [10, 20, 30, 40, 50]
        for item in items:
            stack.push(item)

        # Pop should return items in reverse order
        for expected in reversed(items):
            assert stack.pop() == expected

    def test_pop_until_empty(self):
        """Test popping all items until stack is empty."""
        stack = Stack()
        for i in range(5):
            stack.push(i)

        for i in range(5):
            stack.pop()

        assert stack.length == 0
        assert stack.head is None
        assert stack.pop() is None

    def test_pop_updates_length(self):
        """Test that pop properly updates length."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        assert len(stack) == 3
        stack.pop()
        assert len(stack) == 2
        stack.pop()
        assert len(stack) == 1
        stack.pop()
        assert len(stack) == 0

    # Peek tests
    def test_peek_empty_stack(self):
        """Test peeking at an empty stack."""
        stack = Stack()
        with pytest.raises(AttributeError):
            stack.peek()

    def test_peek_single_item(self):
        """Test peeking at a stack with one item."""
        stack = Stack()
        stack.push(5)
        assert stack.peek() == 5
        assert stack.length == 1  # Length should not change

    def test_peek_multiple_items(self):
        """Test peeking at a stack with multiple items."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        assert stack.peek() == 3
        assert stack.length == 3  # Length should not change
        assert stack.peek() == 3  # Should still be 3

    def test_peek_does_not_modify_stack(self):
        """Test that peek does not modify the stack."""
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)

        initial_length = len(stack)
        peeked_value = stack.peek()

        assert peeked_value == 30
        assert len(stack) == initial_length
        assert stack.head.data == 30

    @pytest.mark.parametrize(
        "items, expected_peek",
        [
            ([1], 1),
            ([1, 2, 3], 3),
            (["a", "b"], "b"),
            ([True, False, True], True),
        ],
    )
    def test_peek_various_types(self, items, expected_peek):
        """Test peeking at various data types."""
        stack = Stack()
        for item in items:
            stack.push(item)
        assert stack.peek() == expected_peek

    # Iterator tests
    def test_iter_empty_stack(self):
        """Test iterating over an empty stack."""
        stack = Stack()
        items = list(stack)
        assert items == []

    def test_iter_single_item(self):
        """Test iterating over a stack with one item."""
        stack = Stack()
        stack.push(5)
        items = [node.data for node in stack]
        assert items == [5]

    def test_iter_multiple_items(self):
        """Test iterating over a stack with multiple items."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        items = [node.data for node in stack]
        assert items == [3, 2, 1]

    def test_iter_order(self):
        """Test that iteration follows LIFO order."""
        stack = Stack()
        expected = [10, 20, 30, 40, 50]
        for item in expected:
            stack.push(item)

        result = [node.data for node in stack]
        assert result == list(reversed(expected))

    def test_iter_does_not_modify_stack(self):
        """Test that iteration does not modify the stack."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        initial_length = len(stack)
        _ = [node.data for node in stack]

        assert len(stack) == initial_length
        assert stack.head.data == 3

    def test_multiple_iterations(self):
        """Test that stack can be iterated multiple times."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        first_iter = [node.data for node in stack]
        second_iter = [node.data for node in stack]

        assert first_iter == second_iter == [3, 2, 1]

    # Combined operations tests
    def test_push_pop_sequence(self):
        """Test a sequence of push and pop operations."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        stack.push(3)
        stack.push(4)
        assert stack.pop() == 4
        assert stack.pop() == 3
        assert stack.pop() == 1
        assert stack.pop() is None

    def test_push_peek_pop(self):
        """Test push, peek, and pop operations together."""
        stack = Stack()
        stack.push(10)
        assert stack.peek() == 10
        stack.push(20)
        assert stack.peek() == 20
        assert stack.pop() == 20
        assert stack.peek() == 10
        assert stack.pop() == 10

    def test_complex_operations(self):
        """Test complex sequence of stack operations."""
        stack = Stack()

        # Push some items
        for i in range(5):
            stack.push(i)
        assert len(stack) == 5

        # Pop a few
        stack.pop()
        stack.pop()
        assert len(stack) == 3

        # Push more
        stack.push(100)
        stack.push(200)
        assert len(stack) == 5
        assert stack.peek() == 200

        # Verify order
        assert stack.pop() == 200
        assert stack.pop() == 100
        assert stack.pop() == 2

    def test_stack_with_none_values(self):
        """Test stack operations with None values."""
        stack = Stack()
        stack.push(None)
        stack.push(1)
        stack.push(None)

        assert stack.length == 3
        assert stack.pop() is None
        assert stack.pop() == 1
        assert stack.pop() is None

    def test_stack_with_string_values(self):
        """Test stack with string values."""
        stack = Stack()
        words = ["hello", "world", "stack", "test"]

        for word in words:
            stack.push(word)

        assert str(stack) == "[test, stack, world, hello]"
        assert stack.pop() == "test"
        assert stack.peek() == "stack"

    def test_stack_with_mixed_types(self):
        """Test stack with mixed data types."""
        stack = Stack()
        stack.push(1)
        stack.push("two")
        stack.push(3.0)
        stack.push(True)

        assert stack.length == 4
        assert stack.pop() is True
        assert stack.pop() == 3.0
        assert stack.pop() == "two"
        assert stack.pop() == 1

    def test_large_stack(self):
        """Test stack with a large number of items."""
        stack = Stack()
        n = 1000

        for i in range(n):
            stack.push(i)

        assert len(stack) == n
        assert stack.peek() == n - 1

        for i in range(n):
            assert stack.pop() == n - 1 - i

        assert len(stack) == 0
        assert stack.head is None
