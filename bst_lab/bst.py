from __future__ import annotations
from typing import Optional, Iterable, List, Tuple, Any

class Node:
    __slots__ = ("key", "left", "right")

    def __init__(self, key: Any):
        self.key = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

class BST:
    def __init__(self, values: Optional[Iterable[Any]] = None):
        self.root: Optional[Node] = None
        self.comparisons: int = 0  # for instrumentation
        if values:
            for v in values:
                self.insert(v)

    # ---- REQUIRED METHODS TO IMPLEMENT ----
    def insert(self, key: Any) -> None:
        """Insert key into BST. Ignore duplicates."""
        def _insert(node: Optional[Node], key: Any) -> Node:
            if node is None:
                return Node(key)
            self.comparisons += 1
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            # equal: do nothing (ignore duplicates)
            return node 
        self.root = _insert(self.root, key)

    def search(self, key: Any) -> bool:
        """Return True if key is in the BST, else False."""
        node = self.root
        while node:
            self.comparisons += 1
            if key == node.key:
                return True
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def inorder(self) -> List[Any]:
        """Return inorder traversal (sorted sequence)."""
        raise NotImplementedError

    def preorder(self) -> List[Any]:
        raise NotImplementedError

    def postorder(self) -> List[Any]:
        raise NotImplementedError

    def level_order(self) -> List[Any]:
        """Breadth-first traversal."""
        raise NotImplementedError

    def min(self) -> Optional[Any]:
        raise NotImplementedError

    def max(self) -> Optional[Any]:
        raise NotImplementedError

    def delete(self, key: Any) -> bool:
        """Delete key if present. Return True if deleted."""
        raise NotImplementedError