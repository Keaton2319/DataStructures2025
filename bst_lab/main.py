from bst import BST, Node

tree = BST([10, 5, 15, 2, 7, 18])
print("Search 7:", tree.search(7))    # True
print("Search 99:", tree.search(99))  # False
print("Comparisons so far:", tree.comparisons)
print("Inorder:", tree.inorder())
print("Preorder:", tree.preorder())
print("Postorder:", tree.postorder())
print("Level Order:", tree.level_order())
print("Minimum", tree.min())
print("Maximum", tree.max())
print("Delete", tree.delete(5))
print("Delete", tree.delete(18))
print("Delete", tree.delete(15))
print("Delete", tree.delete(13))
print("Inorder", tree.inorder())

def show_valid(name: str, t: BST) -> None:
    ok = t.is_valid_bst()
    print(f"{name}: is_valid_bst -> {ok}")
    print("  inorder:", t.inorder())
    assert ok, f"{name} should be valid"

print("----------------------------------------------------")
#Case A: standard valid BST
t1 = BST([10, 5, 15, 2, 7, 12, 18])
show_valid("Case A: standard", t1)

#Case B: empty tree is valid
t2 = BST([])
show_valid("Case B: empty", t2)

#Case C: single node is valid
t3 = BST([42])
show_valid("Case C: single", t3)

#Case D: "balanced-ish" insertion order (still valid)
t4 = BST([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])
show_valid("Case D: balanced-ish", t4)

#Case E: valid after a sequence of deletes and inserts
t5 = BST([10, 5, 15, 2, 7, 12, 18])
# deletes across different cases (leaf / one-child / two-children)
t5.delete(5)
t5.delete(12)
t5.delete(2)

#inserts should keep it valid
for x in (1, 6, 13, 19):
    t5.insert(x)
show_valid("Case E: after deletes/inserts", t5)

print("All true-positive validations passed")