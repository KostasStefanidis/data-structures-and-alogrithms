# Data Structures and Algorithms

A Python implementation of fundamental data structures with comprehensive type hints and object-oriented design patterns.

**Python Version:** 3.12

This project is developed using Python 3.12 and is tested against Python 3.10, 3.11, and 3.12 in CI/CD pipelines.

## Project Structure

```
data-structures-and-alogrithms/
├── src/
│   ├── __init__.py
│   └── data_structures/         # Core data structure implementations
│       ├── ArrayList.py         # Dynamic array with automatic resizing
│       ├── BinaryTree.py        # Binary tree with traversal methods
│       ├── DoublyLinkedList.py  # Doubly linked list implementation
│       ├── HashMap.py           # Hash map with collision handling
│       ├── Heap.py              # Min and Max heap implementations
│       ├── LRUCache.py          # Least Recently Used cache
│       ├── Queue.py             # FIFO queue using linked list
│       ├── RingBuffer.py        # Circular buffer with fixed capacity
│       └── Stack.py             # LIFO stack using linked list
├── tests/                       # Unit tests
│   ├── __init__.py
│   ├── test_ArrayList.py
│   └── test_RingBuffer.py
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

## Data Structures

### ArrayList

A generic dynamic array implementation that automatically resizes when capacity is exceeded.

**Features:**
- Generic type support using Python's `TypeVar`
- Automatic capacity doubling when full
- Index-based access with bounds checking
- Support for iteration and common list operations
- Methods: `push()`, `pop()`, `put()`, `enqueue()`, `deque()`, `shift_forward()`, `shift_backward()`

**Time Complexity:**
- Access: $O(1)$
- Push (amortized): $O(1)$
- Insert at index: $O(n)$
- Remove: $O(n)$

---

### BinaryTree

A binary tree implementation with support for multiple traversal algorithms.

**Features:**
- Generic nodes with left and right children
- Preorder, inorder, and postorder depth-first traversals
- Breadth-first (level-order) traversal
- Inorder traversal returns sorted elements for BST

**Time Complexity:**
- Traversal: $O(n)$
- Space: $O(h)$ for recursive calls (h = height)

---

### DoublyLinkedList

A doubly linked list where each node maintains references to both previous and next nodes.

**Features:**
- Bidirectional traversal
- Generic type support
- Methods: `prepend()`, `append()`, `insertAt()`, `remove()`, `removeAt()`
- $O(1)$ insertion/deletion at head and tail

**Time Complexity:**
- Access: $O(n)$
- Insert at head/tail: $O(1)$
- Insert at index: $O(n)$
- Delete at head/tail: $O(1)$

---

### HashMap

A hash map implementation using separate chaining for collision resolution.

**Features:**
- Generic key-value pair storage
- Dynamic resizing based on load factor (default: 0.7)
- Collision handling via ArrayList buckets
- Dictionary-style access using `[]` operator
- Methods: `put()`, `get()`, `update()`

**Time Complexity:**
- Average case: $O(1)$ for insert, lookup, delete
- Worst case: $O(n)$ when many collisions occur

---

### Heap

Abstract base class with MinHeap and MaxHeap implementations using an ArrayList.

**Features:**
- Complete binary tree structure
- Array-based implementation for efficiency
- Automatic heapify operations
- Methods: `insert()`, `delete()`, `_heapify_up()`, `_heapify_down()`
- Used as foundation for priority queues

**Time Complexity:**
- Insert: $O(\log n)$
- Delete (extract min/max): $O(\log n)$
- Peek: $O(1)$

---

### LRUCache

Least Recently Used cache implementation combining a HashMap and doubly linked list.

**Features:**
- $O(1)$ lookup and eviction
- Automatic capacity management
- Most recently used items moved to front
- Evicts least recently used when capacity exceeded
- Methods: `get()`, `update()`

**Time Complexity:**
- Get: $O(1)$
- Update: $O(1)$

---

### Queue

A FIFO (First In, First Out) queue implemented using a singly linked list.

**Features:**
- Generic type support
- Linked list-based for dynamic sizing
- Iterable interface
- Methods: `enqueue()`, `deque()`, `peek()`

**Time Complexity:**
- Enqueue: $O(1)$
- Dequeue: $O(1)$
- Peek: $O(1)$

---

### RingBuffer

A circular buffer (ring buffer) with fixed capacity that wraps around when full.

**Features:**
- Fixed capacity with automatic wrapping
- Efficient for producer-consumer patterns
- Automatic resizing when needed
- Maintains head and tail pointers
- Methods: `push()`, `pop()`, `shift()`, `unshift()`

**Time Complexity:**
- Push/Pop: $O(1)$
- Random access: $O(1)$

---

### Stack

A LIFO (Last In, First Out) stack implemented using a singly linked list.

**Features:**
- Generic type support
- Linked list-based for dynamic sizing
- Iterable interface
- Methods: `push()`, `pop()`, `peek()`

**Time Complexity:**
- Push: $O(1)$
- Pop: $O(1)$
- Peek: $O(1)$

---

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from src.data_structures.ArrayList import ArrayList
from src.data_structures.Stack import Stack
from src.data_structures.HashMap import HashMap

# Create and use an ArrayList
arr = ArrayList([1, 2, 3, 4, 5])
arr.push(6)
print(arr[0])  # Output: 1

# Use a Stack
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20

# Use a HashMap
map = HashMap()
map.put("name", "Alice")
print(map.get("name"))  # Output: Alice
```

## Testing

Run the test suite:

```bash
python -m pytest tests/
```

## Continuous Integration

This project uses GitHub Actions for automated testing and code quality checks.

### Available GitHub Actions

#### Pytest Workflow
**File:** `.github/workflows/pytest.yaml`

Automatically runs the test suite on every push and pull request to the `main` branch.

- **Triggers:**
  - Push to `main` branch (when Python files or requirements change)
  - Pull requests to `main` branch (when Python files or requirements change)
  - Manual dispatch via GitHub UI

- **Test Matrix:**
  - Python 3.10
  - Python 3.11
  - Python 3.12
  - Python 3.13
  - Python 3.14

- **Purpose:** Ensures all unit tests pass across multiple Python versions before merging code.

#### Pylint Workflow
**File:** `.github/workflows/pylint.yaml`

Performs static code analysis using Pylint to maintain code quality standards.

- **Triggers:**
  - Push to `main` branch (when Python files or requirements change)
  - Pull requests to `main` branch (when Python files or requirements change)
  - Manual dispatch via GitHub UI

- **Test Matrix:**
  - Python 3.10
  - Python 3.11
  - Python 3.12
  - Python 3.13
  - Python 3.14

- **Purpose:** Enforces coding standards, identifies potential bugs, and maintains code quality across the project.

Both workflows use reusable workflows from [KostasStefanidis/github-workflows](https://github.com/KostasStefanidis/github-workflows) and require elevated permissions for security-events reporting.

## License

This project is for educational purposes.
