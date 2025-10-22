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
        out = []
        def _in(n: Optional[Node]):
            if not n: return
            _in(n.left)
            out.append(n.key)
            _in(n.right)
        _in(self.root)
        return out

    def preorder(self) -> List[Any]:
        raise NotImplementedError

    def postorder(self) -> List[Any]:
        out = []
        def _post(n: Optional[Node]):
            if not n: return
            _post(n.left)
            _post(n.right)
            out.append(n.key)
        _post(self.root)
        return out

    def level_order(self) -> List[Any]:
        """Breadth-first traversal."""
        out = []
        if not self.root:
            return out
        q = [self.root]
        i = 0
        while i < len(q):
            n = q[i]; i += 1
            out.append(n.key)
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        return out

    def min(self) -> Optional[Any]:
        print("running")
        n = self.root
        if not n: return None
        while n.left:
            self.comparisons += 1
            n = n.left
        return n.key

    def max(self) -> Optional[Any]:
        n = self.root
        if not n: return None
        while n.right:
            self.comparisons += 1
            n = n.right
        return n.key

    def delete(self, key: Any) -> bool:
        """Delete key if present. Return True if deleted."""
        deleted = False

        def _delete(node: Optional[Node], key: Any) -> Optional[Node]:
            nonlocal deleted
            if node is None:
                return None
            self.comparisons += 1
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
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

    def is_valid_bst(self) -> bool:
        def _check(n: Optional[Node], low, high) -> bool:
            if not n: return True
            if (low is not None and n.key <= low) or (high is not None and n.key >= high):
                return False
            return _check(n.left, low, n.key) and _check(n.right, n.key, high)
        return _check(self.root, None, None)    