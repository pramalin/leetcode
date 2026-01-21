from typing import Optional
from utils.TreeBuilder import TreeNode
from utils.TreeBuilder import TreeBuilder

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

tb = TreeBuilder()
sol = Solution()
tree = tb.buildTree([4,2,7,1,3,6,9])

# note that the invertTree changes the tree in place
invTree = tb.buildTree([4,2,7,1,3,6,9])
sol.invertTree(invTree)

print(f"Original tree: {tb.toList(tree)}")
print(f"Inv tree: {tb.toList(invTree)}")
#inverted_tree = sol.invertTree(tree)
#print(f"Inverted tree: {tb.toList(inverted_tree)}")

tb.toAscii(tree)
tb.toAscii(invTree)