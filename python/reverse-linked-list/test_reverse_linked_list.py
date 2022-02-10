import unittest

from node import Node
from reverse_linked_list import Solution
from traverse import Traverse


class ReverseListTests(unittest.TestCase):
    """Test Suite for Reversing Linked Lists"""

    def test_small_linked_list(self):
        head = Node(1, next=Node(2, next=Node(3)))
        nodes = Traverse().traverse_iteratively(head)

        reversed_head = Solution().reverse_list(head)
        reversed_nodes = Traverse().traverse_iteratively(reversed_head)

        self.assertEqual(nodes, reversed_nodes[::-1])

    def test_medium_linked_list(self):
        self.fail()

    def test_large_linked_list(self):
        self.fail()

    def test_null_linked_list(self):
        self.fail()

    def test_single_node_linked_list(self):
        self.fail()
