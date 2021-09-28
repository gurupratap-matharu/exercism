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
        tree_q = TreeNode(2)
        self.assertTrue(Tree().is_same_tree(tree_p, tree_q))

    def test_two_simple_and_different_binary_trees(self):
        self.fail()

    def test_two_medium_and_identical_binary_trees(self):
        self.fail()

    def test_two_medium_and_different_binary_trees(self):
        self.fail()

    def test_two_large_and_identical_binary_trees(self):
        self.fail()

    def test_two_large_and_slightly_different_binary_trees(self):
        self.fail()


if __name__ == "__main__":
    unittest.main()
