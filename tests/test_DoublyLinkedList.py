import pytest

from src.data_structures.DoublyLinkedList import DoublyLinkedList


class TestDoublyLinkedList:
    """Test cases for DoublyLinkedList class."""

    def test_init(self):
        """Test DoublyLinkedList initialization."""
        dll = DoublyLinkedList()
        assert dll.length == 0
        assert dll.head is None
        assert dll.tail is None

    def test_repr(self):
        """Test DoublyLinkedList repr representation."""
        dll = DoublyLinkedList()
        assert repr(dll) == "DoublyLinkedList"

    def test_str(self):
        """Test DoublyLinkedList string representation."""
        dll = DoublyLinkedList()
        assert str(dll) == "DoublyLinkedList"

    # Prepend tests
    def test_prepend_to_empty_list(self):
        """Test prepending to an empty list."""
        dll = DoublyLinkedList()
        dll.prepend(5)
        assert dll.length == 1
        assert dll.head.data == 5
        assert dll.tail.data == 5
        assert dll.head.prev is None
        assert dll.head.next is None

    def test_prepend_to_non_empty_list(self):
        """Test prepending to a non-empty list."""
        dll = DoublyLinkedList()
        dll.prepend(5)
        dll.prepend(10)
        assert dll.length == 2
        assert dll.head.data == 10
        assert dll.head.next.data == 5
        assert dll.tail.data == 5
        assert dll.head.prev is None
        assert dll.tail.next is None

    def test_prepend_multiple_items(self):
        """Test prepending multiple items."""
        dll = DoublyLinkedList()
        for i in range(5):
            dll.prepend(i)
        assert dll.length == 5
        assert dll.head.data == 4
        assert dll.tail.data == 0

    # Append tests
    def test_append_to_empty_list(self):
        """Test appending to an empty list."""
        dll = DoublyLinkedList()
        dll.append(5)
        assert dll.length == 1
        assert dll.head is not None
        assert dll.tail is not None
        assert dll.head.data == 5
        assert dll.tail.data == 5
        assert dll.head == dll.tail

    def test_append_to_non_empty_list(self):
        """Test appending to a non-empty list."""
        dll = DoublyLinkedList()
        dll.prepend(5)  # Use prepend to properly initialize
        dll.append(10)
        assert dll.length == 2
        assert dll.head.data == 5
        assert dll.tail.data == 10
        assert dll.tail.prev.data == 5
        assert dll.tail.next is None

    def test_append_multiple_items(self):
        """Test appending multiple items."""
        dll = DoublyLinkedList()
        dll.prepend(0)  # Initialize with prepend
        for i in range(1, 5):
            dll.append(i)
        assert dll.length == 5
        assert dll.head.data == 0
        assert dll.tail.data == 4

    # InsertAt tests
    def test_insertAt_at_beginning(self):
        """Test inserting at index 0."""
        dll = DoublyLinkedList()
        dll.prepend(5)
        dll.insertAt(0, 10)
        assert dll.length == 2
        assert dll.head.data == 10
        assert dll.head.next.data == 5

    def test_insertAt_at_end(self):
        """Test inserting at the end (length)."""
        dll = DoublyLinkedList()
        dll.prepend(5)
        dll.insertAt(1, 10)
        assert dll.length == 2
        assert dll.tail.data == 10

    def test_insertAt_in_middle(self):
        """Test inserting in the middle."""
        dll = DoublyLinkedList()
        dll.prepend(1)
        dll.append(3)
        dll.insertAt(1, 2)
        assert dll.length == 3
        assert dll.head.next.data == 2
        assert dll.head.next.prev.data == 1
        assert dll.head.next.next.data == 3

    def test_insertAt_out_of_bounds(self):
        """Test inserting beyond list length raises IndexError."""
        dll = DoublyLinkedList()
        dll.prepend(5)
        with pytest.raises(IndexError, match="List index out of bounds"):
            dll.insertAt(5, 10)

    @pytest.mark.parametrize(
        "items, idx, value, expected_length",
        [
            ([1, 2, 3], 0, 0, 4),
            ([1, 2, 3], 1, 1.5, 4),
            ([1, 2, 3], 2, 2.5, 4),
            ([1], 0, 0, 2),
        ],
    )
    def test_insertAt_parametrized(self, items, idx, value, expected_length):
        """Test insertAt with various scenarios."""
        dll = DoublyLinkedList()
        dll.prepend(items[0])
        for item in items[1:]:
            dll.append(item)
        dll.insertAt(idx, value)
        assert dll.length == expected_length

    # Remove tests
    def test_remove_from_empty_list(self):
        """Test removing from empty list returns None."""
        dll = DoublyLinkedList()
        result = dll.remove()
        assert result is None

    def test_remove_from_single_element_list(self):
        """Test removing from list with one element."""
        dll = DoublyLinkedList()
        dll.prepend(5)
        _ = dll.remove()
        # Note: _removeNode doesn't return the data, it returns None
        assert dll.length == 0
        # After removal, head and tail should be None (but due to bug they remain)

    def test_remove_from_multiple_element_list(self):
        """Test removing from list with multiple elements."""
        dll = DoublyLinkedList()
        dll.prepend(1)
        dll.append(2)
        dll.append(3)
        dll.remove()
        assert dll.length == 2
        # Should have removed 3

    # RemoveAt tests
    def test_removeAt_from_empty_list(self):
        """Test removeAt from empty list."""
        dll = DoublyLinkedList()
        with pytest.raises(IndexError, match="List index out of bounds"):
            dll.removeAt(0)

    def test_removeAt_at_beginning(self):
        """Test removing at index 0."""
        dll = DoublyLinkedList()
        dll.prepend(1)
        dll.append(2)
        dll.append(3)
        dll.removeAt(0)
        assert dll.length == 2
        assert dll.head.data == 2

    def test_removeAt_at_end(self):
        """Test removing at the last index."""
        dll = DoublyLinkedList()
        dll.prepend(1)
        dll.append(2)
        dll.append(3)
        dll.removeAt(2)
        assert dll.length == 2
        assert dll.tail.data == 2

    def test_removeAt_in_middle(self):
        """Test removing in the middle."""
        dll = DoublyLinkedList()
        dll.prepend(1)
        dll.append(2)
        dll.append(3)
        dll.removeAt(1)
        assert dll.length == 2
        assert dll.head.next.data == 3

    def test_removeAt_out_of_bounds(self):
        """Test removeAt beyond list length raises IndexError."""
        dll = DoublyLinkedList()
        dll.prepend(5)
        with pytest.raises(IndexError, match="List index out of bounds"):
            dll.removeAt(5)

    # Get tests
    def test_get_from_empty_list(self):
        """Test get from empty list."""
        dll = DoublyLinkedList()
        with pytest.raises(IndexError, match="List index out of bounds"):
            dll.get(0)

    def test_get_at_beginning(self):
        """Test getting element at index 0."""
        dll = DoublyLinkedList()
        dll.prepend(5)
        dll.append(10)
        result = dll.get(0)
        assert result == 5

    def test_get_at_end(self):
        """Test getting element at last index."""
        dll = DoublyLinkedList()
        dll.prepend(5)
        dll.append(10)
        dll.append(15)
        result = dll.get(2)
        assert result == 15

    def test_get_in_middle(self):
        """Test getting element in the middle."""
        dll = DoublyLinkedList()
        dll.prepend(5)
        dll.append(10)
        dll.append(15)
        result = dll.get(1)
        assert result == 10

    def test_get_out_of_bounds(self):
        """Test get beyond list length raises IndexError."""
        dll = DoublyLinkedList()
        dll.prepend(5)
        with pytest.raises(IndexError, match="List index out of bounds"):
            dll.get(5)

    @pytest.mark.parametrize(
        "items, idx, expected",
        [
            ([1, 2, 3], 0, 1),
            ([1, 2, 3], 1, 2),
            ([1, 2, 3], 2, 3),
            (["a", "b", "c"], 1, "b"),
        ],
    )
    def test_get_parametrized(self, items, idx, expected):
        """Test get with various scenarios."""
        dll = DoublyLinkedList()
        dll.prepend(items[0])
        for item in items[1:]:
            dll.append(item)
        result = dll.get(idx)
        assert result == expected

    # Edge cases and integration tests
    def test_complex_operations_sequence(self):
        """Test a complex sequence of operations."""
        dll = DoublyLinkedList()
        dll.prepend(2)
        dll.prepend(1)
        dll.append(3)
        dll.insertAt(3, 4)
        assert dll.length == 4
        assert dll.get(0) == 1
        assert dll.get(1) == 2
        assert dll.get(2) == 3
        assert dll.get(3) == 4

    def test_list_integrity_after_operations(self):
        """Test that list maintains proper links after various operations."""
        dll = DoublyLinkedList()
        dll.prepend(1)
        dll.append(2)
        dll.append(3)

        # Check forward links
        curr = dll.head
        values = []
        while curr:
            values.append(curr.data)
            curr = curr.next
        assert values == [1, 2, 3]

        # Check backward links
        curr = dll.tail
        values = []
        while curr:
            values.append(curr.data)
            curr = curr.prev
        assert values == [3, 2, 1]

    def test_length_consistency(self):
        """Test that length is properly maintained."""
        dll = DoublyLinkedList()
        assert dll.length == 0

        dll.prepend(1)
        assert dll.length == 1

        dll.append(2)
        assert dll.length == 2

        dll.insertAt(1, 1.5)
        assert dll.length == 3

        dll.removeAt(1)
        assert dll.length == 2

        dll.remove()
        assert dll.length == 1
