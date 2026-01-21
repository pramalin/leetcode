"""
003-longest-substring-without-repeating-characters.py
125-valid-palindrome.py

141-linked-list-cycle.py

34-find-first-and-last-position-of-element-in-sorted-array.py

153-find-minimum-in-rotated-sorted-array.py

33-search-in-rotated-sorted-array.py
215-kth-largest-element-in-an-array.py

226-invert-binary-tree.py
"""
from utils.TreeBuilder import TreeBuilder
from utils.TreeBuilder import TreeNode

# Example usage
if __name__ == "__main__":
    nodes = [1, 2, 3, None, 4, 5, 6]
    tb = TreeBuilder()
    root = tb.buildTree(nodes)

    print("\nTree as ASCII diagram:")
    tb.toAscii(root)
