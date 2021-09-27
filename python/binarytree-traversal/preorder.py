"""Script to traverse a binary tree in preorder fashion"""

from typing import Optional, List


class TreeNode:
    """Represents a node of a tree"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    """Exposes methods to traverse a binary tree in preorder fashion"""

    def pre_order_recursive_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Traverses a binary tree in preorder fashion in a recursive manner.
        """

        res = []
        self.recursive_helper(root, res)
        return res

    def recursive_helper(self, node, res):
        """Helper method to traverse a binary tree recursively"""

        if not node:
            return

        res.append(node.val)
        self.recursive_helper(node.left, res)
        self.recursive_helper(node.right, res)

    def pre_order_iterative_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Traverses a binary tree in preorder fashion using iterative method.
        """

        stack = [root]
        res = []

        while stack:
            node = stack.pop()

            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return res


if __name__ == "__main__":
    tree = Tree()

    root_node = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
    assert tree.pre_order_recursive_traversal(root=root_node), [1, 2, 3]
    assert tree.pre_order_iterative_traversal(root=root_node), [1, 2, 3]
