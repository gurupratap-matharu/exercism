"""Testing script to test if two binary trees are identical"""


import unittest

from same_tree import Tree, TreeNode


class SameTreeTests(unittest.TestCase):
    """Test Suite to identify if two binary trees are identical"""

    def test_two_null_tree(self):
        p = TreeNode(val=None)
        q = TreeNode(val=None)
        self.assertTrue(Tree().is_same_tree(p, q))

    def test_two_simple_and_identical_binary_trees(self):
        tree_p = TreeNode(1)
        tree_q = TreeNode(1)
        self.assertTrue(Tree().is_same_tree(tree_p, tree_q))

    def test_two_simple_and_different_binary_trees(self):
        tree_p = TreeNode(1, left=TreeNode(2))
        tree_q = TreeNode(1, right=TreeNode(2))
        self.assertFalse(Tree().is_same_tree(tree_p, tree_q))

    def test_two_medium_and_identical_binary_trees(self):
        tree_p = TreeNode(1, left=TreeNode(2, left=TreeNode(3)), right=TreeNode(4))
        tree_q = TreeNode(1, left=TreeNode(2, left=TreeNode(3)), right=TreeNode(4))
        self.assertTrue(Tree().is_same_tree(tree_p, tree_q))

    def test_two_medium_and_different_binary_trees(self):
        tree_p = TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(4))
        tree_q = TreeNode(1, left=TreeNode(2, left=TreeNode(3)), right=TreeNode(3))
        self.assertFalse(Tree().is_same_tree(tree_p, tree_q))


    def test_two_large_and_identical_binary_trees(self):
        tree_p = TreeNode(1, left=TreeNode(7), right=TreeNode(6, left=TreeNode(8), right=TreeNode(4, left=TreeNode(9))))
        tree_q = TreeNode(1, left=TreeNode(7), right=TreeNode(6, left=TreeNode(8), right=TreeNode(4, left=TreeNode(9))))
        self.assertTrue(Tree().is_same_tree(tree_p, tree_q))

    def test_two_large_and_slightly_different_binary_trees(self):
        tree_p = TreeNode(1, left=TreeNode(7), right=TreeNode(6, left=TreeNode(8), right=TreeNode(9, left=TreeNode(9))))
        tree_q = TreeNode(1, left=TreeNode(7), right=TreeNode(6, left=TreeNode(8), right=TreeNode(4, left=TreeNode(4))))
        self.assertFalse(Tree().is_same_tree(tree_p, tree_q))


if __name__ == "__main__":
    unittest.main()
