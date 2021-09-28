"""
Script to find if two binary trees are identical. 
Two trees are said to be identical if 
    1. They have the same structure
    2. They have the same node values
"""

from typing import Optional, List


class TreeNode:
    """Represents a single node of a binary tree."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    """Wrapper class that exposes an api to find if two binary trees are identical"""

    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Determines if two binary trees are identical"""

        tree_p = self.inorder_traverse(p)
        tree_q = self.inorder_traverse(q)

        return tree_p == tree_q

    def inorder_traverse(self, root: Optional[TreeNode]) -> List[int]:
        """Traverses a binary tree inorder fashion using iterative technique"""

        res = []
        stack = []
        node = root

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
    tree_1 = TreeNode(1, left=TreeNode(1))
    tree_2 = TreeNode(1, right=TreeNode(1))

    tree = Tree()
    res = tree.is_same_tree(p=tree_1, q=tree_2)
    print(res)
