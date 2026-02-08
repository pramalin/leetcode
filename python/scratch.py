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

tb = TreeBuilder()
tree = tb.buildTree([4,2,7,1,3,6,9])

print(f"Original tree: {tb.toList(tree)}")

tb.printTree(tree)