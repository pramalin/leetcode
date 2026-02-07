from traceback import print_tb
from typing import Optional, List, Union
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeBuilder:
    @staticmethod
    def buildTree(node_values: List[Optional[int]]) -> Optional[TreeNode]:
        """
        Builds a binary tree from a list of node values (level-order traversal).
        `None` represents a null node.

        Args:
            node_values (List[Optional[int]]): List of node values.

        Returns:
            TreeNode: Root of the constructed binary tree.
        """
        if not node_values:
            return None

        root = TreeNode(node_values[0])
        queue = [root]
        i = 1

        while queue and i < len(node_values):
            current = queue.pop(0)
            if node_values[i] is not None:
                current.left = TreeNode(node_values[i])
                queue.append(current.left)
            i += 1

            if i < len(node_values) and node_values[i] is not None:
                current.right = TreeNode(node_values[i])
                queue.append(current.right)
            i += 1

        return root

    @staticmethod
    def toList(root: Optional[TreeNode]) -> List[Union[int, None]]:
        """
        Converts a binary tree to a list (level-order traversal).

        Args:
            root (TreeNode): Root of the binary tree.

        Returns:
            List[Union[int, None]]: List representation of the tree.
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()

        return result

    @staticmethod
    def printTree(root, prefix="", is_left=True):
        if root is not None:
            TreeBuilder.printTree(root.right, prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + str(root.val))
            TreeBuilder.printTree(root.left, prefix + ("    " if is_left else "│   "), True)

# Example usage
if __name__ == "__main__":
    nodes = [1, 2, 3, None, 4, 5, 6]
    tb = TreeBuilder()
    root = tb.buildTree(nodes)

    print("Tree as list:", tb.toList(root))
    print("\nTree as ASCII diagram:")
    tb.printTree(root)