import unittest

from max_depth import Tree, TreeNode


class TreeMaxDepthTests(unittest.TestCase):
    """Test Suite to test max depth of various binary trees"""

    def test_depth_of_a_null_binary_tree(self):
        self.assertEqual(Tree().get_max_depth(root=None), 0)

    def test_depth_of_a_single_node_binary_tree(self):
        node = TreeNode(1)
        self.assertEqual(Tree().get_max_depth(root=node), 1)

    def test_depth_of_a_small_binary_tree(self):
        node = TreeNode(
            3,
            left=TreeNode(9),
            right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)),
        )
        self.assertEqual(Tree().get_max_depth(root=node), 3)

    def test_depth_of_a_size_binary_tree(self):
        pass

    def test_depth_of_a_large_binary_tree(self):
        pass


if __name__ == "__main__":
    unittest.main()
