""""Finds the maximum depth of a binary tree"""


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

        pass


if __name__ == "__main__":
    assert Tree().get_max_depth(TreeNode()), 0
    assert Tree().get_max_depth(TreeNode(1)), 1
