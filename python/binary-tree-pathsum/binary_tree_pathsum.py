"""
Script to find if sum of node values on any path from root to leaf
is equal to a predefined `target_sum`
"""


class TreeNode:
    """A node of a binary tree"""

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{(self.left.value)} <-- {(self.value)} --> {(self.right.value)}"


class BinaryTree:
    """A binary tree object with useful methods"""

    def has_path_sum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        """
        Finds out if sum of all node values along any root to leaf path is equal to target sum.
        """

        path_sums = []
        self.recursive_preorder_traversal(root, path_sums)

        return path_sums

    def recursive_preorder_traversal(self, node, path_sums) -> None:
        """
        Helper method to find path sums along all paths.
        """


