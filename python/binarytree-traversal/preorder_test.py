import unittest

from preorder import Tree, TreeNode


class TreeTests(unittest.TestCase):
    """Test suite for binary tree traversal using recursion and iteration method"""

    def test_preorder_recursive_traversal_for_null_binary_tree(self):
        root = TreeNode()
        self.assertEqual(Tree().preorder_recursive_traversal(root=root), [0])

    def test_preorder_recursive_traversal_for_single_node_binary_tree(self):
        root = TreeNode(val=5, left=None, right=None)
        self.assertEqual(Tree().preorder_recursive_traversal(root=root), [5])

    def test_preorder_recursive_traversal_for_simple_binary_tree(self):
        root = TreeNode(val=1, left=TreeNode(val=2))
        self.assertEqual(Tree().preorder_recursive_traversal(root=root), [1, 2])

    def test_preorder_recursive_traversal_for_medium_binary_tree(self):
        root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
        self.assertEqual(Tree().preorder_recursive_traversal(root=root), [1, 2, 3])

    def test_preorder_recursive_traversal_for_large_binary_tree(self):
        node_9 = TreeNode(9)
        node_11 = TreeNode(11)
        node_37 = TreeNode(37)
        node_21 = TreeNode(21, left=node_9)
        node_49 = TreeNode(49, right=node_11)
        node_17 = TreeNode(17, left=node_37)
        node_77 = TreeNode(77, left=node_49, right=node_17)
        node_7 = TreeNode(7, right=node_21)
        root = TreeNode(100, left=node_7, right=node_77)

        self.assertEqual(
            Tree().preorder_recursive_traversal(root=root),
            [100, 7, 21, 9, 77, 49, 11, 17, 37],
        )

    def test_preorder_iterative_traversal_for_null_binary_tree(self):
        root = TreeNode()
        self.assertEqual(Tree().preorder_iterative_traversal(root=root), [0])

    def test_preorder_iterative_traversal_for_single_node_binary_tree(self):
        root = TreeNode(val=5, left=None, right=None)
        self.assertEqual(Tree().preorder_iterative_traversal(root=root), [5])

    def test_preorder_iterative_traversal_for_simple_binary_tree(self):
        root = TreeNode(val=1, left=TreeNode(val=2))
        self.assertEqual(Tree().preorder_iterative_traversal(root=root), [1, 2])

    def test_preorder_iterative_traversal_for_medium_binary_tree(self):
        root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
        self.assertEqual(Tree().preorder_iterative_traversal(root=root), [1, 2, 3])

    def test_preorder_iterative_traversal_for_large_binary_tree(self):
        node_9 = TreeNode(9)
        node_11 = TreeNode(11)
        node_37 = TreeNode(37)
        node_21 = TreeNode(21, left=node_9)
        node_49 = TreeNode(49, right=node_11)
        node_17 = TreeNode(17, left=node_37)
        node_77 = TreeNode(77, left=node_49, right=node_17)
        node_7 = TreeNode(7, right=node_21)
        root = TreeNode(100, left=node_7, right=node_77)

        self.assertEqual(
            Tree().preorder_iterative_traversal(root=root),
            [100, 7, 21, 9, 77, 49, 11, 17, 37],
        )


if __name__ == "__main__":
    unittest.main()
