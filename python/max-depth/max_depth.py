""""Finds the maximum depth of a binary tree"""

from typing import Optional


class TreeNode:
    """Represents a node in a tree"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    """A Tree class which exposes utility functions for binary trees"""

    def get_max_depth(self, root: Optional[TreeNode]) -> int:
        """Returns the maximum depth of a binary tree"""

        node = root
        stack = []
        curr_depth = max_depth = 0

        while stack or node:

            if node:
                stack.append(node)
                node = node.left
                curr_depth += 1
                max_depth = max(curr_depth, max_depth)

            else:
                node = stack.pop()
                node = node.right
                curr_depth -= 1

        return max_depth


if __name__ == "__main__":
    assert Tree().get_max_depth(TreeNode()), 0
    assert Tree().get_max_depth(TreeNode(1)), 1
