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
    def toAscii(root: Optional[TreeNode]) -> None:
        """
        Renders a binary tree as a simple ASCII diagram in a top-down layout.

        Args:
            root (TreeNode): Root of the binary tree.
        """
        def build_tree_lines(node, curr_index, include_index=False, delimiter=" "):
            if not node:
                return [], 0, 0, 0

            line1 = []
            line2 = []
            node_repr = f"{node.val}" if not include_index else f"{node.val}({curr_index})"

            new_root_width = gap_size = len(node_repr)

            # Get the left and right subtrees
            l_box, l_box_width, l_root_start, l_root_end = build_tree_lines(
                node.left, 2 * curr_index + 1, include_index, delimiter
            )
            r_box, r_box_width, r_root_start, r_root_end = build_tree_lines(
                node.right, 2 * curr_index + 2, include_index, delimiter
            )

            # Draw the branch connecting the current root to left and right subtrees
            if l_box_width > 0:
                l_root = (l_root_start + l_root_end) // 2 + 1
                line1.append(" " * (l_root + 1))
                line1.append(" " * (l_box_width - l_root))
                line2.append(" " * l_root + "/")
                line2.append(" " * (l_box_width - l_root))
                gap_size += 1
            else:
                gap_size += 1

            line1.append(node_repr)
            line2.append(" " * new_root_width)

            if r_box_width > 0:
                r_root = (r_root_start + r_root_end) // 2
                line1.append(" " * r_root)
                line1.append(" " * (r_box_width - r_root + 1))
                line2.append(" " * r_root + "\\")
                line2.append(" " * (r_box_width - r_root))
                gap_size += 1

            # Combine the left and right subtrees with the branches
            gap = delimiter * gap_size
            new_box = ["".join(line1), "".join(line2)]
            for i in range(max(len(l_box), len(r_box))):
                l_line = l_box[i] if i < len(l_box) else " " * l_box_width
                r_line = r_box[i] if i < len(r_box) else " " * r_box_width
                new_box.append(l_line + gap + r_line)

            return new_box, len(new_box[0]), l_box_width + gap_size // 2, l_box_width + gap_size // 2 + new_root_width

        if not root:
            print("Tree is empty.")
            return

        tree_lines, *_ = build_tree_lines(root, 0, include_index=False)
        for line in tree_lines:
            print(line)

# Example usage
if __name__ == "__main__":
    nodes = [1, 2, 3, None, 4, 5, 6]
    tb = TreeBuilder()
    root = tb.buildTree(nodes)

    print("Tree as list:", tb.toList(root))
    print("\nTree as ASCII diagram:")
    tb.toAscii(root)