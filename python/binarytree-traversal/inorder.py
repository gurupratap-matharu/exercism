"""A script to traverse a binary tree in order either recursively or iteratively"""

from typing import List, Optional


class TreeNode:
    """Represents a single node of a binary tree"""

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Tree:
    """Represents a Binary Tree"""

    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """Traverses a binary tree in order using recursion"""

        res = []
        self.helper(node=root, res=res)
        return res

    def helper(self, node, res):
        """Helper recursive method to visit nodes"""

        if not node:
            return

        self.helper(node.left, res)
        res.append(node.val)
        self.helper(node.right, res)

    def inorder_iterative_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """Traverses a binary tree iteratively"""

        node = root
        res = []
        stack = []

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right

        return res


if __name__ == "__main__":
    tree = Tree()

    # recursive method
    assert tree.inorder_traversal(
        root=TreeNode(val=1, left=TreeNode(val=2), right=None)
    ), [2, 1]
    assert tree.inorder_traversal(
        root=TreeNode(
            val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3), right=None)
        )
    ), [1, 3, 2]

    # iterative method
    assert tree.inorder_iterative_traversal(
        root=TreeNode(val=1, left=TreeNode(val=2), right=None)
    ), [2, 1]
    assert tree.inorder_iterative_traversal(
        root=TreeNode(
            val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3), right=None)
        )
    ), [1, 3, 2]
