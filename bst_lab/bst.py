from __future__ import annotations
from typing import Optional, Iterable, List, Tuple, Any

# Generic node for BST containing key, left, and right pointers for traversal
class Node:
    __slots__ = ("key", "left", "right")

    def __init__(self, key: Any):
        self.key = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

# Binary Search Tree implementation with various operations to manage the tree
class BST:
    def __init__(self, values: Optional[Iterable[Any]] = None):
        self.root: Optional[Node] = None                                # root of the BST
        self.comparisons: int = 0  # for instrumentation
        if values:                                                      # if initial values provided for the tree
            for v in values:                                            # insert each value    
                self.insert(v)                                          # insert into the BST

    # ---- REQUIRED METHODS TO IMPLEMENT ----
    # Insert key into the BST, making sure to ignore any duplicates
    def insert(self, key: Any) -> None:
        """Insert key into BST. Ignore duplicates."""
        def _insert(node: Optional[Node], key: Any) -> Node:
            if node is None:                                            # If current node is None, create a new node
                return Node(key)
            self.comparisons += 1                                       # Increment comparison count    
            if key < node.key:                                          # Traverse left subtree
                node.left = _insert(node.left, key)
            elif key > node.key:                                        # Traverse right subtree
                node.right = _insert(node.right, key)
            # equal: do nothing (ignore duplicates)
            return node 
        self.root = _insert(self.root, key)                             # Start insertion from the root

    # Search key in the BST
    def search(self, key: Any) -> bool:
        """Return True if key is in the BST, else False."""
        node = self.root                                                # Start from the root
        while node:                                                     # Traverse until node is None
            self.comparisons += 1                                       # Increment comparison count
            if key == node.key:                                         # Key found
                return True
            elif key < node.key:                                        # Traverse left subtree
                node = node.left
            else:                                                       # Traverse right subtree
                node = node.right
        return False                                                    # Key not found

    # Inorder establishes the key values into a list based on value size
    def inorder(self) -> List[Any]:
        """Return inorder traversal (sorted sequence)."""
        out = []                                                        # Output list for inorder traversal
        def _in(n: Optional[Node]): 
            if not n: return                                            # If node is None, return
            _in(n.left)                                                 # Traverse left subtree
            out.append(n.key)
            _in(n.right)                                                # Traverse right subtree
        _in(self.root)                                                  # Start inorder traversal from root
        return out

    # Preorder establishes the key values into a list based on root-left-right traversal
    def preorder(self) -> List[Any]:
<<<<<<< HEAD
        out = []
        def _pre(n: Optional[Node]):
            if not n: return
            out.append(n.key)
            _pre(n.left)
            _pre(n.right)
        _pre(self.root)
        return out

    def postorder(self) -> List[Any]:
=======
>>>>>>> 1654428fc7e7778499eb34fbd9ab87e8a6ec31b8
        out = []
        def _pre(n: Optional[Node]):
            if not n: return
            out.append(n.key)
            _pre(n.left)
            _pre(n.right)
        _pre(self.root)
        return out

    # Postorder establishes the key values into list based on left-right-root traversal
    def postorder(self) -> List[Any]:
        out = []                                                        # Output list for inorder traversal
        def _post(n: Optional[Node]):
            if not n: return                                            # If node is None, return
            _post(n.left)                                               # Traverse left subtree
            _post(n.right)                                              # Traverse right subtree
            out.append(n.key)
        _post(self.root)                                                # Start inorder traversal from root
        return out

    # Level order establishes the key values into list based on breadth-first traversal
    def level_order(self) -> List[Any]:
        """Breadth-first traversal."""
        out = []                                                        # Output list for inorder traversal
        if not self.root:                                               # If tree is empty, return empty list
            return out
        q = [self.root]                                                 # Initialize queue with root node
        i = 0                                                           # Index for processing nodes in the queue
        while i < len(q):                                               # While there are nodes to process
            n = q[i]; i += 1                                            # Dequeue the next node
            out.append(n.key)                                           # Add the node's key to output
            if n.left: q.append(n.left)                                 # Enqueue left child if it exists
            if n.right: q.append(n.right)                               # Enqueue right child if it exists
        return out

    # Traverses the tree to locate the minimum value 
    def min(self) -> Optional[Any]:
        n = self.root                                                   # Start from the root
        if not n: return None                                           # If tree is empty, return None
        while n.left:                                                   # Traverse to the leftmost node
            self.comparisons += 1                                       # Increment comparison count
            n = n.left                                                  # Move to left child
        return n.key

    # Traverses the tree to locate the maximum value
    def max(self) -> Optional[Any]:
        n = self.root                                                   # Start from the root
        if not n: return None                                           # If tree is empty, return None
        while n.right:                                                  # Traverse to the rightmost node
            self.comparisons += 1                                       # Increment comparison count
            n = n.right                                                 # Move to right child
        return n.key
    
    # The delete function removes a key from the BST if it exists, if not then it does nothing
    def delete(self, key: Any) -> bool:
        """Delete key if present. Return True if deleted."""
        deleted = False                                                 # Set deleted to False

        # Helper function to take care of the recursive deletion process
        def _delete(node: Optional[Node], key: Any) -> Optional[Node]:
            nonlocal deleted                                            # Access the deleted variable from outer scope
            if node is None:                                            # If node is None, key not found
                return None
            self.comparisons += 1                                       # Increment comparison count
            if key < node.key:                                          # Traverse left subtree
                node.left = _delete(node.left, key)
            elif key > node.key:                                        # Traverse right subtree
                node.right = _delete(node.right, key)
            else:                                                       
                # Found node to delete
                deleted = True
                # Case 1: no children
                if node.left is None and node.right is None:
                    return None
                # Case 2: one child
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                # Case 3: two children -> successor
                succ_parent = node
                succ = node.right
                while succ.left:
                    succ_parent = succ
                    succ = succ.left
                node.key = succ.key  # copy successor's key
                # delete successor
                if succ_parent.left is succ:
                    succ_parent.left = succ.right
                else:
                    succ_parent.right = succ.right
            return node

        self.root = _delete(self.root, key)
        return deleted

    # Validate the BST properties across all of the nodes in the tree
    def is_valid_bst(self) -> bool:
        def _check(n: Optional[Node], low, high) -> bool:
            if not n: return True                                       # An empty node is valid    
            if (low is not None and n.key <= low) or (high is not None and n.key >= high):
                return False                                            
            return _check(n.left, low, n.key) and _check(n.right, n.key, high)
        return _check(self.root, None, None)    