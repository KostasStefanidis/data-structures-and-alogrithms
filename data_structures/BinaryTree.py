from typing import TypeVar, Generic
from .ArrayList import ArrayList
from .Queue import Queue
from .Stack import Stack

T = TypeVar('T', int, float)

class BinaryNode(Generic[T]):
    def __init__(self, data: T, left = None, right = None) -> None:
        self.data = data
        self.left: BinaryNode = left
        self.right: BinaryNode = right
    
    def __str__(self) -> str:
        return str(self.data) if self.data else ''

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: {self.__str__()}'


class BinaryTree(Generic[T]):
    root: BinaryNode[T]
    
    def __init__(self, root: BinaryNode[T]) -> None:
        self.root = root
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: {self.__str__()}'
    
    def __str__(self) -> str:
        return f'Preorder: {self.preorder()}'
    
    def _walk_preorder(self, curr: BinaryNode[T], path: Stack[T]) -> Stack[T]:
        if curr is None:
            return path
        path.push(curr.data)
        self._walk_preorder(curr.left, path)
        self._walk_preorder(curr.right, path)
        return path
    
    def _walk_inorder(self, curr: BinaryNode[T], path: Stack[T]) -> Stack[T]:
        if curr is None:
            return path
        self._walk_inorder(curr.left, path)
        path.push(curr.data)
        self._walk_inorder(curr.right, path)
        return path
    
    def _walk_postorder(self, curr: BinaryNode[T], path: Stack[T]) -> Stack[T]:
        if curr is None:
            return path
        self._walk_postorder(curr.left, path)
        self._walk_postorder(curr.right, path)
        path.push(curr.data)
        return path
    
    def preorder(self) -> Stack[T]:
        return self._walk_preorder(self.root, Stack())
    
    # inorder traversal of a Binary Search Tree returns the elements in sorted order
    def inorder(self) -> Stack[T]:
        return self._walk_inorder(self.root, Stack())
    
    def postorder(self) -> Stack[T]:
        return self._walk_postorder(self.root, Stack())
    
    
    # def _walk_dfs(self, node: BinaryNode[T] | None, needle: T) -> bool:
    #     if node is None:
    #         return False
        
    #     if node.data == needle:
    #         return True
        
    #     self._walk_dfs(node.left, needle)
    #     self._walk_dfs(node.right, needle)
        
    #     return
    
    # def dfs(self, needle: T) -> bool:
    #     queue = ArrayList(self.root)
    #     print(f'Initial {queue=}')
    #     print(queue.capacity)
    #     print(queue.length)
        
    
    def bfs(self, needle: T) -> bool:
        queue = ArrayList(self.root)
        
        while len(queue):
            curr = queue.deque()
            if curr.data == needle:
                return True
            
            if curr.left is not None:    
                queue.enqueue(curr.left)
            if curr.right is not None:    
                queue.enqueue(curr.right)
        
        return False
    
    
    def _compare(self, nodeA: BinaryNode | None, nodeB: BinaryNode | None):
        # Depth-first Traversal preserves the shape of the traversal (Breadth-first does not)
        # so when comparing 2 Binary trees use Depth-first to traverse the nodes and check if 
        # they are equal
        
        # Structural check
        if nodeA is None and nodeB is None:
            return True
        
        # Structural check
        if (nodeA and not nodeB) or (nodeB and not nodeA):
            return False
        
        # Value equallity check
        if (nodeA.data != nodeB.data):
            return False
        
        # if the values of the 2 nodes are equal (nodeA.data = nodeB.data) 
        # simply letting the recursion continue, do not return True 
        # because that would interupt the recursion and end the traversal
        # prematurely without checking all the nodes of the trees
        return self._compare(nodeA.left, nodeB.left) and self._compare(nodeA.right, nodeB.right)
        
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, BinaryTree):
            raise TypeError(f"Cannot compare {self.__class__.__name__} object to {type(other)}")
        
        return self._compare(self.root, other.root)
    
    
    def _height_helper(self, node: BinaryNode[T]) -> int:
        if node is None:
            return 0
        return 1 + max(self._height_helper(node.left), self._height_helper(node.right))
    
    def height(self) -> int:
        if self.root is None:
            return 0
        return self._height_helper(self.root)
    
    
    def _size_helper(self, node: BinaryNode[T]) -> int:
        if node is None:
            return 0
        return 1 + self._size_helper(node.left) + self._size_helper(node.right)
        
    def size(self) -> int:
        if self.root is None:
            return 0
        return self._size_helper(self.root)
    
    
    def _is_balanced_helper(self, node: BinaryNode[T]) -> bool:
        if node is None:
            return True
        return abs(self._height_helper(node.left) - self._height_helper(node.right)) <= 1 and \
            self._is_balanced_helper(node.left) and self._is_balanced_helper(node.right)
    
    def is_balanced(self) -> bool:
        if self.root is None:
            return True
        return self._is_balanced_helper(self.root)
    
    
    def _is_mirror(self, left: BinaryNode[T], right: BinaryNode[T]) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.data == right.data and \
            self._is_mirror(left.left, right.right) and \
            self._is_mirror(left.right, right.left)
    
    def is_symmetric(self) -> bool:
        if self.root is None:
            return True
        return self._is_mirror(self.root.left, self.root.right)
    
    
    def _is_bst_helper(self, node: BinaryNode[T], min: T, max: T) -> bool:
        if node is None:
            return True
        if node.data <= min or node.data >= max:
            return False
        return self._is_bst_helper(node.left, min, node.data) and \
            self._is_bst_helper(node.right, node.data, max)
    
    def is_valid_bst(self) -> bool:
        if self.root is None:
            return True
        return self._is_bst_helper(self.root, float('-inf'), float('inf'))
    
    
    # runtime O(logn) - O(n) depending on how balanced is the tree
    def _find_helper(self, node: BinaryNode[T] , needle: T) -> bool:
        if not node:
            return False
        
        if node.data == needle:
            return True
        
        if node.data < needle:
            return self._find_helper(node.right, needle)
        
        return self._find_helper(node.left, needle)
    
    def find(self, needle: T) -> bool:
        if not self.is_valid_bst():
            raise ValueError('Cannot find item in invalid Binary Search Tree')
        
        if self.root is None:
            return False
        
        return self._find_helper(self.root, needle)
    
    
    def _insert_helper(self, node: BinaryNode[T], item: T) -> BinaryNode[T]:
        if not node:
            return BinaryNode(item)
        
        if node.data < item:
            node.right = self._insert_helper(node.right, item)
        else:
            node.left = self._insert_helper(node.left, item)
        
        return node
    
    def insert(self, item: T) -> None:
        if not self.is_valid_bst():
            raise ValueError('Cannot insert item in invalid Binary Search Tree')
        
        if self.root is None:
            self.root = BinaryNode(item)
            return
        
        self.root = self._insert_helper(self.root, item)
        
        
    def _delete_helper(self, node: BinaryNode[T], item: T) -> BinaryNode[T]:       
        return node
    
    def delete(self, item: T) -> BinaryNode[T]:
        if not self.is_valid_bst():
            raise ValueError('Cannot delete item in invalid Binary Search Tree')
        
        if self.root is None:
            return
        
        return self._delete_helper(self.root, item)