from typing import List, Optional


class TreeNode:
    """Represents a single node of a binary tree"""

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(node=root, res=res)
        return res

    def helper(self, node, res):
        if not node:
            return

        self.helper(node.left, res)
        res.append(node.val)
        self.helper(node.right, res)


if __name__ == '__main__':
    tree = Tree()
    assert tree.inorder_traversal(root=TreeNode(val=1, left=TreeNode(val=2), right=None)), [2, 1]
    assert tree.inorder_traversal(root=TreeNode(val=1, left=None, right=TreeNode(
        val=2, left=TreeNode(val=3), right=None))), [1, 3, 2]
