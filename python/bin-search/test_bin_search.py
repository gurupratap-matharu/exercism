import unittest

from bin_search import Solution


class BinSearchTests(unittest.TestCase):
    """Test suite to check if binary search works properly"""

    def test_small_array_with_target(self):
        calculated = Solution().search([1, 2, 3, 4], 3)
        expected = 2
        self.assertEqual(calculated, expected)

    def test_small_array_with_no_target(self):
        calculated = Solution().search([1, 2, 3, 4], 0)
        expected = -1
        self.assertEqual(calculated, expected)

    def test_small_array_with_only_one_target_element(self):
        calculated = Solution().search([1], 1)
        expected = 0
        self.assertEqual(calculated, expected)

    def test_small_array_with_only_one_non_target_element(self):
        calculated = Solution().search([1], 5)
        expected = -1
        self.assertEqual(calculated, expected)

    def test_large_array_with_consecutive_elements_containing_target(self):
        calculated = Solution().search([x for x in range(1, 1000)], 750)
        expected = 749
        self.assertEqual(calculated, expected)

    def test_large_array_with_consecutive_elements_not_containing_target(self):
        calculated = Solution().search([x for x in range(1, 1000)], 1001)
        expected = -1
        self.assertEqual(calculated, expected)


if __name__ == "__main__":
    unittest.main()
