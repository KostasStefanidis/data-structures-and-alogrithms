import pytest

from src.data_structures.Node import BinaryNode, DoublyLinkedNode, Node


class TestNode:
    """Test cases for singly linked Node class."""

    @pytest.mark.parametrize(
        "data, next_node",
        [
            (5, None),
            ("hello", None),
            (3.14, None),
            ([1, 2, 3], None),
        ],
    )
    def test_init_without_next(self, data, next_node):
        """Test Node initialization without next node."""
        node = Node(data, next_node)
        assert node.data == data
        assert node.next is None

    def test_init_with_next(self):
        """Test Node initialization with next node."""
        next_node = Node(10)
        node = Node(5, next_node)
        assert node.data == 5
        assert node.next == next_node
        assert node.next.data == 10

    @pytest.mark.parametrize(
        "data, expected_str",
        [
            (5, "5"),
            ("hello", "hello"),
            (3.14, "3.14"),
            ([1, 2, 3], "[1, 2, 3]"),
            (True, "True"),
        ],
    )
    def test_str(self, data, expected_str):
        """Test Node string representation."""
        node = Node(data)
        assert str(node) == expected_str

    @pytest.mark.parametrize(
        "data, expected_repr",
        [
            (5, "Node: 5"),
            ("hello", "Node: hello"),
            (3.14, "Node: 3.14"),
        ],
    )
    def test_repr(self, data, expected_repr):
        """Test Node repr representation."""
        node = Node(data)
        assert repr(node) == expected_repr

    def test_eq_equal_nodes(self):
        """Test equality of nodes with same data."""
        node1 = Node(5)
        node2 = Node(5)
        assert node1 == node2

    def test_eq_different_nodes(self):
        """Test inequality of nodes with different data."""
        node1 = Node(5)
        node2 = Node(10)
        assert not (node1 == node2)

    def test_eq_with_different_type(self):
        """Test equality comparison with non-Node type raises TypeError."""
        node = Node(5)
        with pytest.raises(TypeError) as excinfo:
            node == 5
        assert "Cannot compare Node object to <class 'int'>" in str(
            excinfo.value)

    def test_eq_with_string(self):
        """Test equality comparison with string raises TypeError."""
        node = Node(5)
        with pytest.raises(TypeError) as excinfo:
            node == "5"
        assert "Cannot compare Node object to <class 'str'>" in str(
            excinfo.value)

    def test_linked_chain(self):
        """Test creating a chain of linked nodes."""
        node3 = Node(30)
        node2 = Node(20, node3)
        node1 = Node(10, node2)

        assert node1.data == 10
        assert node1.next.data == 20
        assert node1.next.next.data == 30
        assert node1.next.next.next is None


class TestDoublyLinkedNode:
    """Test cases for doubly linked DoublyLinkedNode class."""

    @pytest.mark.parametrize(
        "data",
        [
            5,
            "hello",
            3.14,
            [1, 2, 3],
            {"key": "value"},
        ],
    )
    def test_init_without_links(self, data):
        """Test DoublyLinkedNode initialization without prev/next."""
        node = DoublyLinkedNode(data)
        assert node.data == data
        assert node.prev is None
        assert node.next is None

    def test_init_with_prev(self):
        """Test DoublyLinkedNode initialization with prev node."""
        prev_node = DoublyLinkedNode(5)
        node = DoublyLinkedNode(10, prev=prev_node)
        assert node.data == 10
        assert node.prev == prev_node
        assert node.next is None

    def test_init_with_next(self):
        """Test DoublyLinkedNode initialization with next node."""
        next_node = DoublyLinkedNode(15)
        node = DoublyLinkedNode(10, next=next_node)
        assert node.data == 10
        assert node.prev is None
        assert node.next == next_node

    def test_init_with_both_links(self):
        """Test DoublyLinkedNode initialization with both prev and next."""
        prev_node = DoublyLinkedNode(5)
        next_node = DoublyLinkedNode(15)
        node = DoublyLinkedNode(10, prev=prev_node, next=next_node)
        assert node.data == 10
        assert node.prev == prev_node
        assert node.next == next_node

    @pytest.mark.parametrize(
        "data, expected_str",
        [
            (5, "5"),
            ("hello", "hello"),
            (3.14, "3.14"),
            ([1, 2, 3], "[1, 2, 3]"),
            (None, ""),
            ("", ""),
        ],
    )
    def test_str(self, data, expected_str):
        """Test DoublyLinkedNode string representation."""
        node = DoublyLinkedNode(data)
        assert str(node) == expected_str

    @pytest.mark.parametrize(
        "data, expected_repr",
        [
            (5, "DoublyLinkedNode: 5"),
            ("hello", "DoublyLinkedNode: hello"),
            (3.14, "DoublyLinkedNode: 3.14"),
            (None, "DoublyLinkedNode: "),
        ],
    )
    def test_repr(self, data, expected_repr):
        """Test DoublyLinkedNode repr representation."""
        node = DoublyLinkedNode(data)
        assert repr(node) == expected_repr

    def test_eq_equal_nodes(self):
        """Test equality of nodes with same data."""
        node1 = DoublyLinkedNode(5)
        node2 = DoublyLinkedNode(5)
        assert node1 == node2

    def test_eq_different_nodes(self):
        """Test inequality of nodes with different data."""
        node1 = DoublyLinkedNode(5)
        node2 = DoublyLinkedNode(10)
        assert not (node1 == node2)

    def test_eq_with_different_type(self):
        """Test equality comparison with non-DoublyLinkedNode type raises TypeError."""
        node = DoublyLinkedNode(5)
        with pytest.raises(TypeError) as excinfo:
            node == 5
        assert "Cannot compare DoublyLinkedNode object to <class 'int'>" in str(
            excinfo.value
        )

    def test_eq_with_list(self):
        """Test equality comparison with list raises TypeError."""
        node = DoublyLinkedNode([1, 2, 3])
        with pytest.raises(TypeError) as excinfo:
            node == [1, 2, 3]
        assert "Cannot compare DoublyLinkedNode object to <class 'list'>" in str(
            excinfo.value
        )

    def test_doubly_linked_chain(self):
        """Test creating a doubly linked chain."""
        node1 = DoublyLinkedNode(10)
        node2 = DoublyLinkedNode(20, prev=node1)
        node1.next = node2
        node3 = DoublyLinkedNode(30, prev=node2)
        node2.next = node3

        # Forward traversal
        assert node1.data == 10
        assert node1.next.data == 20
        assert node1.next.next.data == 30
        assert node1.next.next.next is None

        # Backward traversal
        assert node3.data == 30
        assert node3.prev.data == 20
        assert node3.prev.prev.data == 10
        assert node3.prev.prev.prev is None

    def test_bidirectional_links(self):
        """Test bidirectional linking between nodes."""
        node1 = DoublyLinkedNode(1)
        node2 = DoublyLinkedNode(2)

        node1.next = node2
        node2.prev = node1

        assert node1.next == node2
        assert node2.prev == node1
        assert node1.next.prev == node1
        assert node2.prev.next == node2


class TestBinaryNode:
    """Test cases for BinaryNode class."""

    @pytest.mark.parametrize(
        "data",
        [
            5,
            10,
            3.14,
            2.71,
        ],
    )
    def test_init_without_children(self, data):
        """Test BinaryNode initialization without children."""
        node = BinaryNode(data)
        assert node.data == data
        assert node.left is None
        assert node.right is None

    def test_init_with_left_child(self):
        """Test BinaryNode initialization with left child."""
        left_child = BinaryNode(5)
        node = BinaryNode(10, left=left_child)
        assert node.data == 10
        assert node.left == left_child
        assert node.right is None

    def test_init_with_right_child(self):
        """Test BinaryNode initialization with right child."""
        right_child = BinaryNode(15)
        node = BinaryNode(10, right=right_child)
        assert node.data == 10
        assert node.left is None
        assert node.right == right_child

    def test_init_with_both_children(self):
        """Test BinaryNode initialization with both children."""
        left_child = BinaryNode(5)
        right_child = BinaryNode(15)
        node = BinaryNode(10, left=left_child, right=right_child)
        assert node.data == 10
        assert node.left == left_child
        assert node.right == right_child

    @pytest.mark.parametrize(
        "data, expected_str",
        [
            (5, "5"),
            (10, "10"),
            (3.14, "3.14"),
            (0, ""),  # 0 is falsy, so returns empty string
            (None, ""),
        ],
    )
    def test_str(self, data, expected_str):
        """Test BinaryNode string representation."""
        node = BinaryNode(data)
        assert str(node) == expected_str

    @pytest.mark.parametrize(
        "data, expected_repr",
        [
            (5, "BinaryNode: 5"),
            (10, "BinaryNode: 10"),
            (3.14, "BinaryNode: 3.14"),
            (0, "BinaryNode: "),  # 0 is falsy, so returns empty string
            (None, "BinaryNode: "),
        ],
    )
    def test_repr(self, data, expected_repr):
        """Test BinaryNode repr representation."""
        node = BinaryNode(data)
        assert repr(node) == expected_repr

    def test_binary_tree_structure(self):
        """Test creating a simple binary tree structure."""
        #       10
        #      /  \\
        #     5    15
        left = BinaryNode(5)
        right = BinaryNode(15)
        root = BinaryNode(10, left=left, right=right)

        assert root.data == 10
        assert root.left.data == 5
        assert root.right.data == 15
        assert root.left.left is None
        assert root.left.right is None
        assert root.right.left is None
        assert root.right.right is None

    def test_complex_binary_tree_structure(self):
        """Test creating a more complex binary tree structure."""
        #         10
        #        /  \\
        #       5    15
        #      / \\   / \\
        #     3   7 12  20
        node3 = BinaryNode(3)
        node7 = BinaryNode(7)
        node12 = BinaryNode(12)
        node20 = BinaryNode(20)
        node5 = BinaryNode(5, left=node3, right=node7)
        node15 = BinaryNode(15, left=node12, right=node20)
        root = BinaryNode(10, left=node5, right=node15)

        assert root.data == 10
        assert root.left.data == 5
        assert root.right.data == 15
        assert root.left.left.data == 3
        assert root.left.right.data == 7
        assert root.right.left.data == 12
        assert root.right.right.data == 20

    def test_left_skewed_tree(self):
        """Test creating a left-skewed binary tree."""
        node3 = BinaryNode(30)
        node2 = BinaryNode(20, left=node3)
        node1 = BinaryNode(10, left=node2)

        assert node1.data == 10
        assert node1.left.data == 20
        assert node1.left.left.data == 30
        assert node1.right is None
        assert node1.left.right is None

    def test_right_skewed_tree(self):
        """Test creating a right-skewed binary tree."""
        node3 = BinaryNode(30)
        node2 = BinaryNode(20, right=node3)
        node1 = BinaryNode(10, right=node2)

        assert node1.data == 10
        assert node1.right.data == 20
        assert node1.right.right.data == 30
        assert node1.left is None
        assert node1.right.left is None

    def test_single_node_tree(self):
        """Test single node (leaf) tree."""
        node = BinaryNode(42)
        assert node.data == 42
        assert node.left is None
        assert node.right is None

    def test_float_values(self):
        """Test BinaryNode with float values."""
        left = BinaryNode(1.5)
        right = BinaryNode(3.7)
        root = BinaryNode(2.5, left=left, right=right)

        assert root.data == 2.5
        assert root.left.data == 1.5
        assert root.right.data == 3.7
